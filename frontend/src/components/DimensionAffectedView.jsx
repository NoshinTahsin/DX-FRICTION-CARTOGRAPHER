import React from "react";

export default function DimensionAffectedView({ frictionPoints = [], dimensions = {} }) {
  const dimensionGroups = {};

  frictionPoints.forEach((point) => {
    point.dimensions.forEach((dimKey) => {
      if (!dimensionGroups[dimKey]) {
        dimensionGroups[dimKey] = [];
      }
      dimensionGroups[dimKey].push(point);
    });
  });

  const affectedDimensions = Object.entries(dimensionGroups)
    .filter(([, points]) => points.length > 0)
    .sort((a, b) => b[1].length - a[1].length);

  if (!affectedDimensions.length) {
    return <section className="panel metric empty">No affected DX dimensions identified.</section>;
  }

  return (
    <section className="dimension-grid">
      {affectedDimensions.map(([dimKey, points]) => {
        const dim = dimensions[dimKey];
        if (!dim) return null;

        return (
          <article key={dimKey} className="panel dimension-card">
            <div className="card-header">
              <div className="dimension-title">
                <h3>{dim.name}</h3>
                <span className="reference-popover">
                  <button
                    className="info-button"
                    aria-label={`${dim.name} literature reference`}
                    type="button"
                  >
                    i
                  </button>
                  <span className="reference-content" role="tooltip">
                    <strong>Framework:</strong> {dim.framework}
                    <br />
                    <strong>Reference:</strong> {dim.citation}
                  </span>
                </span>
              </div>
              <span className="count">{points.length}</span>
            </div>
            <p>{dim.definition}</p>
            <div className="stack">
              {points.map((point, index) => (
                <span className="tag" key={`${point.stage}-${point.friction_label}-${index}`}>
                  {point.stage}: {point.friction_label}
                </span>
              ))}
            </div>
          </article>
        );
      })}
    </section>
  );
}
