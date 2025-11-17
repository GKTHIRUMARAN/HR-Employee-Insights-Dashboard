import axios from "axios";
const API_BASE = "http://127.0.0.1:8000";

export const uploadFile = (file) => {
  const fd = new FormData();
  fd.append("file", file);
  return axios.post(`${API_BASE}/etl/run`, fd, {
    headers: { "Content-Type": "multipart/form-data" },
  }).then(r => r.data);
};

export const getKPIs = () => axios.get(`${API_BASE}/analytics/kpis`).then(r => r.data);
export const getCharts = () => axios.get(`${API_BASE}/analytics/charts`).then(r => r.data);
