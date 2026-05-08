// UI table component for extracted tools inventory
import React from "react";

export default function ToolsTable({ tools = [] }) {
  return (
    <section className="panel">
      <div className="table-wrap">
        <table className="data-table">
          <thead>
            <tr>
              <th>Stage</th>
              <th>Tools</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            {tools.map((item, index) => (
              <tr key={`${item.stage}-${index}`}>
                <td>{item.stage}</td>
                <td>
                  <div className="tag-list">
                    {item.tools.map((tool) => (
                      <span className="tag" key={tool}>{tool}</span>
                    ))}
                  </div>
                </td>
                <td>{item.notes}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
