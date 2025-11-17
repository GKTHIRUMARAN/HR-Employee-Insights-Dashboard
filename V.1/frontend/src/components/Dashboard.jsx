import React from "react";

export default function Dashboard({ summary }) {
  const s = summary;
  return (
    <div>
      <h3>ETL Summary</h3>
      <p>Rows: {s.row_count}</p>
      <p>Columns: {s.col_count}</p>

      <h4>Numeric Stats</h4>
      <pre>{JSON.stringify(s.numeric_stats, null, 2)}</pre>

      <h4>Top Categorical</h4>
      <pre>{JSON.stringify(s.categorical_top, null, 2)}</pre>
    </div>
  );
}
