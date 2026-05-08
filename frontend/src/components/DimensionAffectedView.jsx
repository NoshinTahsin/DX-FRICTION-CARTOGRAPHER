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

  return (
    <section className="dimension-grid">
      {affectedDimensions.map(([dimKey, points]) => {
        const dim = dimensions[dimKey];
        if (!dim) return null;

        return (
          <article key={dimKey} className="panel dimension-card">
            <div className="card-header">
              <h3>{dim.name}</h3>
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
