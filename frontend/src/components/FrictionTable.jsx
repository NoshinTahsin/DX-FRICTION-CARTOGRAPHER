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
              <th>Pain</th>
              <th>Affects</th>
              <th>Dimensions</th>
            </tr>
          </thead>
          <tbody>
            {frictionPoints.map((point, index) => (
              <tr key={`${point.stage}-${point.friction_label}-${index}`}>
                <td>{point.stage}</td>
                <td>{point.friction_label}</td>
                <td>{point.example}</td>
                <td>{point.how_often}</td>
                <td>{point.pain_level}/5</td>
                <td>{point.who_affects}</td>
                <td>
                  <div className="tag-list">
                    {point.dimensions.map((key) => (
                      <span className="tag" key={key}>{dimensions[key]?.name || key}</span>
                    ))}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
