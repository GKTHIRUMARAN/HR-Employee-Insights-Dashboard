import React from "react";
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import PersonIcon from '@mui/icons-material/Person';
import ShowChartIcon from '@mui/icons-material/ShowChart';
import BusinessIcon from '@mui/icons-material/Business';
import MonetizationOnIcon from '@mui/icons-material/MonetizationOn';

function KPICard({ title, value, icon }) {
  return (
    <Card variant="outlined">
      <CardContent>
        <Grid container alignItems="center" spacing={2}>
          <Grid item>
            {icon}
          </Grid>
          <Grid item>
            <Typography variant="subtitle2">{title}</Typography>
            <Typography variant="h6">{value}</Typography>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
}

export default function KPIDashboard({ kpis }) {
  const total = kpis.total_rows ?? kpis.rows ?? "-";
  const unique = kpis.unique_employees ?? "-";
  const avgSalary = kpis.numeric_mean ? (kpis.numeric_mean.Salary ?? kpis.numeric_mean.salary ?? "-") : "-";
  const attrRate = kpis.attrition_rate ? (Math.round(kpis.attrition_rate*10000)/100) + '%' : '-';

  return (
    <Grid container spacing={2} mb={3}>
      <Grid item xs={12} md={3}>
        <KPICard title="Total Rows" value={total} icon={<PersonIcon fontSize="large" />} />
      </Grid>
      <Grid item xs={12} md={3}>
        <KPICard title="Unique Employees" value={unique} icon={<BusinessIcon fontSize="large" />} />
      </Grid>
      <Grid item xs={12} md={3}>
        <KPICard title="Avg Salary" value={avgSalary} icon={<MonetizationOnIcon fontSize="large" />} />
      </Grid>
      <Grid item xs={12} md={3}>
        <KPICard title="Attrition Rate" value={attrRate} icon={<ShowChartIcon fontSize="large" />} />
      </Grid>
    </Grid>
  );
}
