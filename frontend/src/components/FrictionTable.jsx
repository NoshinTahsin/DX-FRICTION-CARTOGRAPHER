// UI table component for friction points in DX Friction Cartographer
import React from "react";

export default function FrictionTable({ frictionPoints = [], dimensions = {} }) {
  return (
    <section className="panel">
      <div className="table-wrap">
        <table className="data-table">
          <thead>
            <tr>
              <th>Stage</th>
              <th>Friction</th>
              <th>Example</th>
              <th>Frequency</th>
              <th>Pain (1-5)</th>
              <th>Affects</th>
              <th>Dimensions</th>
            </tr>
          </thead>
          <tbody>
            {frictionPoints.length ? (
              frictionPoints.map((point, index) => (
                <tr key={`${point.stage}-${point.friction_label}-${index}`}>
                  <td>{point.stage}</td>
                  <td>{point.friction_label}</td>
                  <td>{point.example}</td>
                  <td>{point.how_often}</td>
                  <td>{point.pain_level}</td>
                  <td>
                    <div className="affects-cell">
                      <span>{point.who_affects}</span>
                      {point.justification ? (
                        <button
                          className="info-button"
                          title={point.justification}
                          aria-label={`Why ${point.who_affects}`}
                        >
                          i
                        </button>
                      ) : null}
                    </div>
                  </td>
                  <td>
                    <div className="tag-list">
                      {point.dimensions.map((key) => (
                        <span className="tag" key={key}>{dimensions[key]?.name || key}</span>
                      ))}
                    </div>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td className="empty-row" colSpan="7">No friction points match the selected filters.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}
