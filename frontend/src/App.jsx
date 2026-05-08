import React, { useState } from "react";
import DimensionAffectedView from "./components/DimensionAffectedView.jsx";
import FrictionTable from "./components/FrictionTable.jsx";
import ToolsTable from "./components/ToolsTable.jsx";
import { DIMENSIONS } from "./data/dimensions.js";

const SAMPLE_TRANSCRIPT = `We use Jira for planning but tickets are always vague. Requirements change mid-sprint constantly. For coding we use VS Code and GitHub. Our CI pipeline takes 25 minutes. Flaky tests fail randomly and nobody trusts them. Deployment is manual with a 15 step checklist in Notion.`;

export default function App() {
  const [transcript, setTranscript] = useState(SAMPLE_TRANSCRIPT);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function analyzeTranscript() {
    setIsLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ transcript }),
      });

      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.detail || "Analysis failed");
      }

      setResult(payload);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <main className="app">
      <header className="topbar">
        <div className="brand">DX Friction Cartographer</div>
        <div className="status-pill">API: http://127.0.0.1:8000/analyze</div>
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
        </aside>

        <section className="results">
          {result ? (
            <>
              <section className="summary-grid">
                <div className="panel metric">
                  <div className="metric-label">Friction Points</div>
                  <div className="metric-value">{result.devex_summary.total_friction_points}</div>
                </div>
                <div className="panel metric">
                  <div className="metric-label">Highest Pain Stage</div>
                  <div className="metric-value">{result.devex_summary.highest_pain_stage}</div>
                </div>
                <div className="panel metric">
                  <div className="metric-label">Top Dimensions</div>
                  <div className="metric-value">{result.devex_summary.most_affected_dimensions.length}</div>
                </div>
              </section>

              <ToolsTable tools={result.tools_inventory} />
              <FrictionTable frictionPoints={result.friction_points} dimensions={DIMENSIONS} />
              <DimensionAffectedView frictionPoints={result.friction_points} dimensions={DIMENSIONS} />
            </>
          ) : (
            <div className="panel metric empty">
              Run an analysis to map tools, friction points, and affected DX dimensions.
            </div>
          )}
        </section>
      </section>
    </main>
  );
}
