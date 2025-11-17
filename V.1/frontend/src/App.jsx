import React from "react";
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import FileUpload from "./components/FileUpload";
import KPIDashboard from "./components/KPIDashboard";
import ChartsDashboard from "./components/ChartsDashboard";
import { getKPIs, getCharts } from "./api";

export default function App() {
  const [summary, setSummary] = React.useState(null);
  const [kpis, setKpis] = React.useState(null);
  const [charts, setCharts] = React.useState(null);

  async function handleDone(res) {
    setSummary(res.etl_summary);
    // fetch KPIs and charts after processing
    try {
      const kp = await getKPIs();
      setKpis(kp);
      const ch = await getCharts();
      setCharts(ch);
    } catch (e) {
      console.error("Failed to fetch kpis/charts", e);
    }
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box display="flex" justifyContent="space-between" alignItems="center" mb={3}>
        <Typography variant="h4" component="h1">HR Data v1 — MUI Dashboard</Typography>
      </Box>

      <Box mb={3}>
        <FileUpload onDone={handleDone} />
      </Box>

      {kpis && <KPIDashboard kpis={kpis} />}

      {charts && <ChartsDashboard charts={charts} />}

      {!kpis && summary && (
        <Box mt={4}>
          <Typography variant="h6">ETL Summary</Typography>
          <pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(summary, null, 2)}</pre>
        </Box>
      )}
    </Container>
  );
}
