// DimensionAffectedView component for displaying affected DX dimensions
import React from "react";

export default function DimensionAffectedView({ friction_points, dimensions }) {
  // Group friction points by dimension
  const dimensionGroups = {};

  friction_points.forEach(point => {
    point.dimensions.forEach(dimKey => {
      if (!dimensionGroups[dimKey]) {
        dimensionGroups[dimKey] = [];
      }
      dimensionGroups[dimKey].push(point);
    });
  });

  // Filter to dimensions with friction points and sort by count descending
  const affectedDimensions = Object.entries(dimensionGroups)
    .filter(([_, points]) => points.length > 0)
    .sort((a, b) => b[1].length - a[1].length);

  const handleDimensionClick = (dimKey) => {
    const dim = dimensions[dimKey];
    if (dim) {
      alert(`${dim.name}\n\n${dim.definition}\n\n${dim.citation}`);
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 p-4">
      {affectedDimensions.map(([dimKey, points]) => {
        const dim = dimensions[dimKey];
        if (!dim) return null;

        return (
          <div key={dimKey} className="border rounded-lg p-4 bg-white shadow-sm">
            <div className="flex items-center justify-between mb-2">
              <h3
                className="font-bold text-lg cursor-pointer hover:text-blue-600"
                onClick={() => handleDimensionClick(dimKey)}
                title="Click for definition and citation"
              >
                {dim.name}
              </h3>
              <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-sm">
                {points.length}
              </span>
            </div>
            <div className="text-sm text-gray-600 mb-2">Affects:</div>
            <ul className="text-sm space-y-1">
              {points.map((point, idx) => (
                <li key={idx} className="flex items-start">
                  <span className="text-gray-400 mr-2">•</span>
                  <span>{point.stage} – {point.friction_label}</span>
                </li>
              ))}
            </ul>
          </div>
        );
      })}
    </div>
  );
}