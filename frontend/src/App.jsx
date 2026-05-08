import React, { useEffect, useMemo, useState } from "react";
import DimensionAffectedView from "./components/DimensionAffectedView.jsx";
import FrictionTable from "./components/FrictionTable.jsx";
import ToolsTable from "./components/ToolsTable.jsx";
import { DIMENSIONS } from "./data/dimensions.js";

const SAMPLE_TRANSCRIPT = `We use Jira for planning but tickets are always vague. Requirements change mid-sprint constantly. For coding we use VS Code and GitHub. Our CI pipeline takes 25 minutes. Flaky tests fail randomly and nobody trusts them. Deployment is manual with a 15 step checklist in Notion.`;
const PROGRESS_STAGES = ["Extracting tools", "Classifying friction", "Synthesizing summary"];

function getStageImpactStats(frictionPoints = []) {
  const stageStats = Object.values(
    frictionPoints.reduce((acc, point) => {
      if (!acc[point.stage]) {
        acc[point.stage] = { stage: point.stage, total: 0, count: 0 };
      }
      acc[point.stage].total += point.pain_level;
      acc[point.stage].count += 1;
      return acc;
    }, {})
  ).map((item) => {
    const average = item.total / item.count;
    return {
      ...item,
      average,
      impact: average * Math.log2(item.count + 1),
    };
  });

  return stageStats.sort((a, b) => b.impact - a.impact || b.average - a.average || b.count - a.count);
}

export default function App() {
  const [transcript, setTranscript] = useState(SAMPLE_TRANSCRIPT);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [progressStage, setProgressStage] = useState(0);
  const [stageFilter, setStageFilter] = useState("all");
  const [dimensionFilter, setDimensionFilter] = useState("all");
  const [accessCode, setAccessCode] = useState("");
  const [isUnlocked, setIsUnlocked] = useState(false);
  const [authError, setAuthError] = useState("");
  const [isCheckingAccess, setIsCheckingAccess] = useState(false);

  useEffect(() => {
    if (!isLoading) return undefined;

    setProgressStage(0);
    const timer = window.setInterval(() => {
      setProgressStage((current) => Math.min(current + 1, PROGRESS_STAGES.length - 1));
    }, 2500);

    return () => window.clearInterval(timer);
  }, [isLoading]);

  async function validateAccessCode() {
    const normalizedAccessCode = accessCode.trim();
    setAuthError("");
    setIsCheckingAccess(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/validate", {
        method: "POST",
        headers: normalizedAccessCode ? { "X-App-Access-Code": normalizedAccessCode } : {},
      });
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || "Invalid access code");
      }

      setIsUnlocked(true);
    } catch (err) {
      setAuthError(err.message);
      setIsUnlocked(false);
    } finally {
      setIsCheckingAccess(false);
    }
  }

  const stageOptions = useMemo(() => {
    if (!result) return [];
    return [...new Set(result.friction_points.map((point) => point.stage))].sort();
  }, [result]);

  const dimensionOptions = useMemo(() => {
    if (!result) return [];
    const keys = new Set();
    result.friction_points.forEach((point) => {
      point.dimensions.forEach((key) => keys.add(key));
    });
    return [...keys].sort((a, b) => (DIMENSIONS[a]?.name || a).localeCompare(DIMENSIONS[b]?.name || b));
  }, [result]);

  const filteredFrictionPoints = useMemo(() => {
    if (!result) return [];
    return result.friction_points.filter((point) => {
      const matchesStage = stageFilter === "all" || point.stage === stageFilter;
      const matchesDimension = dimensionFilter === "all" || point.dimensions.includes(dimensionFilter);
      return matchesStage && matchesDimension;
    });
  }, [dimensionFilter, result, stageFilter]);

  const summaryDetails = useMemo(() => {
    if (!result) {
      return {
      dimensionCount: 0,
      frictionText: "Total number of friction points extracted from the transcript.",
      painText: "Highest impact stage combines pain severity and number of friction points.",
      dimensionText: "Number of distinct DX dimensions tagged across all friction points.",
      };
    }

    const dimensionKeys = new Set();
    result.friction_points.forEach((point) => {
      point.dimensions.forEach((key) => dimensionKeys.add(key));
    });

    const highestStage = getStageImpactStats(result.friction_points)[0];

    const topDimensions = [...dimensionKeys]
      .map((key) => DIMENSIONS[key]?.name || key)
      .sort()
      .join(", ");

    return {
      dimensionCount: dimensionKeys.size,
      frictionText: `${result.friction_points.length} friction point${result.friction_points.length === 1 ? "" : "s"} extracted from the transcript. Click to jump to the friction table.`,
      painText: highestStage
        ? `Formula: impact = average pain x log2(friction count + 1). Calculation: ${highestStage.stage} = ${highestStage.average.toFixed(1)} x log2(${highestStage.count} + 1) = ${highestStage.impact.toFixed(1)}. This is a relative score for comparing stages, not a percentage or score out of 10. Click to jump to the friction table.`
        : "No friction identified, so no highest pain stage was calculated.",
      dimensionText: topDimensions
        ? `${dimensionKeys.size} distinct DX dimension${dimensionKeys.size === 1 ? "" : "s"} identified: ${topDimensions}. Click to jump to the dimension cards.`
        : "No DX dimensions were identified.",
    };
  }, [result]);

  const stagePainStats = useMemo(() => {
    if (!result) return [];
    return getStageImpactStats(result.friction_points);
  }, [result]);

  const maxStageImpact = stagePainStats[0]?.impact || 1;

  function jumpToSection(id) {
    document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  async function analyzeTranscript() {
    const normalizedAccessCode = accessCode.trim();
    if (!isUnlocked) {
      setError("Enter a valid access code first.");
      return;
    }

    setIsLoading(true);
    setError("");
    setResult(null);
    setStageFilter("all");
    setDimensionFilter("all");
    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(normalizedAccessCode ? { "X-App-Access-Code": normalizedAccessCode } : {}),
        },
        body: JSON.stringify({ transcript }),
      });

      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || "Analysis failed");
      }

      setResult(payload);
      setProgressStage(PROGRESS_STAGES.length);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="app">
      {!isUnlocked ? (
        <section className="access-overlay">
          <div className="access-card">
            <h1>DX Friction Cartographer</h1>
            <p>Enter the shared access code to use the analyzer.</p>
            <label className="field-label" htmlFor="gate-access-code">Access code</label>
            <input
              className="text-input"
              id="gate-access-code"
              value={accessCode}
              onChange={(event) => setAccessCode(event.target.value)}
              onKeyDown={(event) => {
                if (event.key === "Enter") validateAccessCode();
              }}
              placeholder="Paste your access code here"
              type="password"
            />
            <button
              className="primary-button"
              disabled={isCheckingAccess || !accessCode.trim()}
              onClick={validateAccessCode}
            >
              {isCheckingAccess ? "Checking..." : "Unlock App"}
            </button>
            {authError ? <div className="error">{authError}</div> : null}
          </div>
        </section>
      ) : null}

      <div className={!isUnlocked ? "locked-shell" : ""} aria-hidden={!isUnlocked}>
        <header className="topbar">
          <div className="brand">DX Friction Cartographer</div>
        </header>

        <section className="workspace">
        <aside className="panel input-panel">
          <h1 className="panel-title">Transcript</h1>
          <textarea
            className="transcript-input"
            value={transcript}
            onChange={(event) => setTranscript(event.target.value)}
          />
          <button
            className="primary-button"
            disabled={isLoading || !transcript.trim()}
            onClick={analyzeTranscript}
          >
            {isLoading ? "Analyzing..." : "Analyze Transcript"}
          </button>
          {error ? <div className="error">{error}</div> : null}
          {isLoading ? (
            <div className="progress-panel">
              {PROGRESS_STAGES.map((stage, index) => {
                const isActive = index === progressStage;
                const isComplete = index < progressStage;
                return (
                  <div className="progress-step" key={stage}>
                    <div className="progress-row">
                      <span className={isActive ? "active" : isComplete ? "complete" : ""}>{stage}</span>
                      <span>{isComplete ? "Done" : isActive ? "Running" : "Queued"}</span>
                    </div>
                    <div className="progress-track">
                      <div
                        className={`progress-fill ${isComplete ? "complete" : ""}`}
                        style={{ width: isComplete ? "100%" : isActive ? "62%" : "0%" }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          ) : null}
        </aside>

        <section className="results">
          {result ? (
            <>
              <section className="summary-grid">
                <button className="panel metric metric-button" onClick={() => jumpToSection("friction-section")}>
                  <div className="metric-header">
                    <div className="metric-label">Friction Points</div>
                    <span className="reference-popover">
                      <span className="info-button" tabIndex="0">i</span>
                      <span className="reference-content" role="tooltip">{summaryDetails.frictionText}</span>
                    </span>
                  </div>
                  <div className="metric-value">{result.devex_summary.total_friction_points}</div>
                </button>
                <button
                  className="panel metric metric-button"
                  onClick={() => jumpToSection("friction-section")}
                >
                  <div className="metric-header">
                    <div className="metric-label">Highest Impact Stage</div>
                    <span className="reference-popover">
                      <span className="info-button" tabIndex="0">i</span>
                      <span className="reference-content" role="tooltip">{summaryDetails.painText}</span>
                    </span>
                  </div>
                  <div className="metric-value">{stagePainStats[0]?.stage || result.devex_summary.highest_pain_stage}</div>
                  <div className="mini-stage-bars">
                    {stagePainStats.map((item) => (
                      <div className="mini-stage-row" key={item.stage}>
                        <div className="mini-stage-label">
                          <span>{item.stage}</span>
                          <span>{item.impact.toFixed(1)}</span>
                        </div>
                        <div className="mini-stage-track">
                          <div className="mini-stage-fill" style={{ width: `${(item.impact / maxStageImpact) * 100}%` }} />
                        </div>
                      </div>
                    ))}
                  </div>
                </button>
                <button className="panel metric metric-button" onClick={() => jumpToSection("dimensions-section")}>
                  <div className="metric-header">
                    <div className="metric-label">DX Dimensions</div>
                    <span className="reference-popover">
                      <span className="info-button" tabIndex="0">i</span>
                      <span className="reference-content" role="tooltip">{summaryDetails.dimensionText}</span>
                    </span>
                  </div>
                  <div className="metric-value">{summaryDetails.dimensionCount}</div>
                </button>
              </section>

              <ToolsTable tools={result.tools_inventory} />
              <section className="panel filters-panel" id="friction-section">
                <div>
                  <label className="filter-label" htmlFor="stage-filter">Stage</label>
                  <select
                    className="filter-select"
                    id="stage-filter"
                    value={stageFilter}
                    onChange={(event) => setStageFilter(event.target.value)}
                  >
                    <option value="all">All stages</option>
                    {stageOptions.map((stage) => (
                      <option key={stage} value={stage}>{stage}</option>
                    ))}
                  </select>
                </div>
                <div>
                  <label className="filter-label" htmlFor="dimension-filter">DX dimension</label>
                  <select
                    className="filter-select"
                    id="dimension-filter"
                    value={dimensionFilter}
                    onChange={(event) => setDimensionFilter(event.target.value)}
                  >
                    <option value="all">All dimensions</option>
                    {dimensionOptions.map((key) => (
                      <option key={key} value={key}>{DIMENSIONS[key]?.name || key}</option>
                    ))}
                  </select>
                </div>
                <div className="filter-count">
                  Showing {filteredFrictionPoints.length} of {result.friction_points.length}
                </div>
              </section>
              <FrictionTable frictionPoints={filteredFrictionPoints} dimensions={DIMENSIONS} />
              <section id="dimensions-section">
                <DimensionAffectedView frictionPoints={filteredFrictionPoints} dimensions={DIMENSIONS} />
              </section>
            </>
          ) : (
            <div className="panel metric empty">
              Run an analysis to map tools, friction points, and affected DX dimensions.
            </div>
          )}
        </section>
        <footer className="site-footer">
          Copyright (c) 2026 Noshin Tahsin. All rights reserved.
        </footer>
      </section>
      </div>
    </main>
  );
}
