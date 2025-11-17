# ⚡ **HR-Employee-Insights-Dashboard — V.1 Full Build**

> **Intelligent HR Data Analysis System (FastAPI + React + Material UI)**
> The evolution of the lightweight *HR Dashboard Prototype (V.0)* into a **complete analytics engine** with automated ETL, KPI extraction, chart generation, and a modern React dashboard.

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/HR-Employee-Insights-Dashboard?color=brightgreen&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/HR-Employee-Insights-Dashboard?color=blue&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/HR-Employee-Insights-Dashboard?color=yellow&style=for-the-badge)

---

## 🧠 Overview

**HR Employee Insights Dashboard (V.1)** is the **first fully functional build** of an intelligent HR analytics system capable of transforming raw HR datasets (CSV/XLSX) into **cleaned data**, **KPIs**, and **interactive charts**.

Powered by **FastAPI**, **React + Material UI**, and an **auto-schema ETL engine**, this full-stack system delivers:

* Automatic ETL (cleaning, processing, schema detection)
* KPI extraction (rows, employees, salary patterns, attrition, etc.)
* Categorical & numeric summaries
* Departmental visual insights
* Interactive dashboards with charts
* A modular backend + responsive frontend

This version expands the simple [V.0](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.0) prototype into a **scalable HR analytics platform**.

---

## 🎯 Core Vision

Build a **clean, automated HR analytics framework** that can:

* Accept HR datasets via frontend upload  
* Clean and preprocess data automatically  
* Generate numeric/categorical summaries  
* Produce interactive visualizations  
* Render a modern MUI-based HR dashboard  
* Enable smooth extension into ML models (Attrition Prediction V.2)  

---

## ⚙️ System Architecture

```mermaid
flowchart TD
    A[User Upload] --> B[React MUI Dashboard]
    B -->|POST /etl/run| C[FastAPI Backend]
    C --> D[ETL Engine]
    D -->|Clean & Process| E[Processed Data Store]
    C --> F[KPI Engine]
    C --> G[Chart Generator]
    F -->|Return JSON| B
    G -->|Return Chart JSON| B
````

---

## 🧩 Key Components

| Layer        | Technology     | Role                                                 |
| ------------ | -------------- | ---------------------------------------------------- |
| **Frontend** | React + MUI    | Dashboard UI, KPI cards, chart rendering             |
| **Backend**  | FastAPI        | ETL pipeline, KPI engine, chart data API             |
| **ETL**      | Pandas         | Auto-schema detection, cleaning, feature engineering |
| **Charts**   | Chart.js       | Salary distribution + categorical visualizations     |
| **Storage**  | Local FS       | Raw + processed datasets                             |
| **Logs**     | Logging Module | Tracks ETL, analytics, processing events             |

---

## 🧱 Folder Structure

```
backend/
│  main.py
│  requirements.txt
│
├── api/
│     ├── etl.py
│     └── analytics.py
│
├── pipeline/
│     ├── etl_process.py
│     └── analytics_engine.py
│
├── core/
│     ├── file_handler.py
│     └── utils.py
│
├── data/
│     ├── raw/
│     └── processed/
└── logs/

frontend/
│  package.json
│  vite.config.js
│  index.html
│
└── src/
     ├── App.jsx
     ├── api.js
     ├── index.jsx
     └── components/
          ├── FileUpload.jsx
          ├── KPIDashboard.jsx
          └── ChartsDashboard.jsx
```

---

## 📸 Demo Snapshot

<p align="center">
  <img src="https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/blob/main/V.1/demo.png" alt="HR Dashboard Demo" width="600">
</p>

---

## ⚡ Backend — FastAPI Core

The backend is the **engine** powering ETL, KPI extraction, summary generation, and visualization APIs.

### 🔧 Main Components

| File / Module         | Description                                    |
| --------------------- | ---------------------------------------------- |
| `main.py`             | Initializes FastAPI and routes                 |
| `etl.py`              | File upload → ETL trigger                      |
| `analytics.py`        | Generates KPIs + chart JSON                    |
| `etl_process.py`      | Cleaning, missing value handling, feature gen. |
| `analytics_engine.py` | Numeric + categorical summaries                |
| `file_handler.py`     | Saves/uploads raw & processed files            |
| `utils.py`            | Column detection, schema inference             |
| `raw/`, `processed/`  | File storage directories                       |
| `logs/`               | ETL + analytics event tracking                 |

### ✅ Backend Highlights

* Auto-schema ETL processing
* Full KPI engine
* Chart-ready JSON for frontend
* Processed data versioning
* Robust error logging

---

## 💻 Frontend — React + Material UI

A clean, responsive dashboard enabling users to upload HR datasets and view insights instantly.

### ✨ UI Features

* File upload UI
* KPI cards (total rows, employees, salary stats...)
* Salary distribution charts
* Pie charts for departments, gender, etc.
* Auto-fetch after upload
* Fully responsive MUI layout

### 🧩 Directory Snapshot

```
frontend/src/
├── App.jsx
├── api.js
└── components/
    ├── FileUpload.jsx
    ├── KPIDashboard.jsx
    └── ChartsDashboard.jsx
```

---

## 🧰 Environment Setup

### **Backend Setup**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### **Frontend Setup**

```bash
cd frontend
npm install
npm run start
```

### **Access App**

```
http://localhost:5173
```

---

## 🧨 Core Endpoints

### **POST `/etl/run`**

Uploads file → triggers ETL → returns ETL summary.

### **GET `/analytics/kpis`**

Returns:

* Total rows
* Unique employees
* Salary statistics
* Department distributions
* Attrition rate (if present)

### **GET `/analytics/charts`**

Returns salary & categorical chart JSON.

---

## 🧾 KPIs Calculated

| KPI                     | Description                 |
| ----------------------- | --------------------------- |
| Total Rows              | Dataset length              |
| Unique Employees        | ID-like column detection    |
| Avg/Min/Max Salary      | Salary column auto-detected |
| Attrition Rate          | Yes/No detection            |
| Department Distribution | Frequency counts            |

---

## 📊 Charts Rendered

✔ Salary distribution (Bar)
✔ Department distribution (Pie)
✔ Gender distribution (Pie)
✔ Top categories (Pie)

---

## ✅ Current Capabilities (V.1)

| Feature              | Status     |
| -------------------- | ---------- |
| Auto ETL             | ✅ Complete |
| KPI Engine           | ✅ Complete |
| Charts               | ✅ Complete |
| React MUI Dashboard  | ✅ Complete |
| Data Versioning      | ✅ Working  |
| Logging System       | ✅ Enabled  |
| Error Handling       | ✅ Stable   |
| Frontend Integration | ✅ Synced   |

---

## 🔮 Future Roadmap (V.2)

| Goal                      | Description                      |
| ------------------------- | -------------------------------- |
| **ML Attrition Model**    | Predict employee turnover        |
| **Postgres Integration**  | Persistent HR database           |
| **User History Tracking** | Store prior uploads + insights   |
| **Authentication**        | Multi-user access                |
| **Advanced Visuals**      | Heatmaps, Boxplots, Correlations |
| **Docker Deployment**     | Containerized production build   |
| **Cloud Hosting**         | Render / Railway / Vercel        |

---

## 🧠 Lessons Learned

* A clean ETL pipeline dramatically improves stability
* Auto-schema detection makes the system dataset-agnostic
* Separating KPIs + charts yields cleaner frontend logic
* React + MUI is excellent for analytics dashboards
* This architecture scales smoothly for ML + DB integrations

---

## 📜 Project Links

| Resource          | Link                                                                                                                                                                 |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🏠 **Main Repo**  | [https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard)                                     |
| 📂 **V.0 Folder** | [https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.0](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.0)         |
| ⚡ **V.1 Folder**  | [https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.1](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.1)         |
| 📜 **License**    | [https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/blob/main/LICENSE](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/blob/main/LICENSE) |

---

## 🧩 How It Fits in the Whole Project

**V.1** transforms the simple prototype from [V.0](../V.0/README.md) into a **production-style analytics engine**.
This version lays the foundation for:

* ML-driven attrition prediction
* Database integration
* Historical analytics
* Enterprise-ready HR intelligence

> 🌱 The architecture is complete — now V.2 adds real intelligence.

[⬅ Back to Main README](../README.md)

---

## 👤 Author

**GK Thirumaran**  
🎓 *B.Tech Artificial Intelligence and Data Science*  
🌍 *Coimbatore, Tamil Nadu, India*  
💼 *Aspiring Data Scientist & Analyst | AIML Developer*  
🔗 [LinkedIn](https://www.linkedin.com/in/thirumarangk-ai) | [Portfolio](https://maranthiru180.wixsite.com/my-site)

```
```
