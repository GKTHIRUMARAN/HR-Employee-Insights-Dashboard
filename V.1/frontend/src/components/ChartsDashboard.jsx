import React from "react";
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { Bar, Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, Tooltip, Legend);

function CardChart({ title, children }) {
  return (
    <Card variant="outlined">
      <CardContent>
        <Typography variant="subtitle1" gutterBottom>{title}</Typography>
        {children}
      </CardContent>
    </Card>
  );
}

export default function ChartsDashboard({ charts }) {
  // charts expected: salary_buckets, cat_<col>
  const salaryBuckets = charts.salary_buckets ?? null;
  const categoryCharts = Object.keys(charts).filter(k => k.startsWith('cat_'));

  return (
    <Grid container spacing={2}>
      {salaryBuckets && (
        <Grid item xs={12} md={6}>
          <CardChart title="Salary Distribution">
            <Bar data={{
              labels: salaryBuckets.map(b => b.label),
              datasets: [{ label: 'Count', data: salaryBuckets.map(b => b.value) }]
            }} />
          </CardChart>
        </Grid>
      )}

      {categoryCharts.map((key, idx) => (
        <Grid item xs={12} md={6} key={key}>
          <CardChart title={key.replace('cat_', '')}>
            <Pie data={{
              labels: charts[key].map(x => x.label),
              datasets: [{ data: charts[key].map(x => x.value) }]
            }} />
          </CardChart>
        </Grid>
      ))}
    </Grid>
  );
}
