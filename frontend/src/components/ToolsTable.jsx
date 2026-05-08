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
            {tools.length ? tools.map((item, index) => {
              const itemTools = item.tools.filter(Boolean);
              return (
                <tr key={`${item.stage}-${index}`}>
                  <td>{item.stage || <span className="muted-value">No stage mentioned</span>}</td>
                  <td>
                    {itemTools.length ? (
                      <div className="tag-list">
                        {itemTools.map((tool) => (
                          <span className="tag" key={tool}>{tool}</span>
                        ))}
                      </div>
                    ) : (
                      <span className="muted-value">No tool mentioned</span>
                    )}
                  </td>
                  <td>{item.notes || <span className="muted-value">No notes mentioned</span>}</td>
                </tr>
              );
            }) : (
              <tr>
                <td className="empty-row" colSpan="3">No tools mentioned in this transcript.</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}
