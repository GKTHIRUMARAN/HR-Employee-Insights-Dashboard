import React from "react";
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { uploadFile } from "../api";
import UploadFileIcon from '@mui/icons-material/UploadFile';

export default function FileUpload({ onDone }) {
  const [file, setFile] = React.useState(null);
  const [loading, setLoading] = React.useState(false);
  const [msg, setMsg] = React.useState("");

  async function handleUpload(e) {
    e.preventDefault();
    if (!file) return setMsg("Choose a file first");

    setLoading(true);
    setMsg("");
    try {
      const res = await uploadFile(file);
      setMsg("Upload complete");
      onDone && onDone(res);
    } catch (err) {
      console.error(err);
      setMsg("Upload failed: " + (err?.message || ""));
    } finally {
      setLoading(false);
    }
  }

  return (
    <Box component="form" onSubmit={handleUpload} display="flex" alignItems="center" gap={2}>
      <input
        id="file-input"
        type="file"
        accept=".csv,.xls,.xlsx"
        onChange={(e) => setFile(e.target.files[0])}
        style={{ display: 'inline-block' }}
      />
      <Button type="submit" variant="contained" startIcon={<UploadFileIcon />} disabled={loading}>
        {loading ? "Uploading..." : "Upload & Run ETL"}
      </Button>
      <div>{msg}</div>
    </Box>
  );
}
