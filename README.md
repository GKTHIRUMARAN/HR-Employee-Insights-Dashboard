# ⚡ HR-Employee-Insights-Dashboard

> **HR Insight System — Intelligent HR Analytics Platform powered by Streamlit, FastAPI & Machine Learning**  

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/HR-Employee-Insights-Dashboard?color=brightgreen&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/HR-Employee-Insights-Dashboard?color=blue&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/HR-Employee-Insights-Dashboard?color=yellow&style=for-the-badge)

---

## 🧠 Overview

**HR-Employee-Insights-Dashboard** is an intelligent analytics platform that transforms static HR data into **predictive insights**.  
It unifies data ingestion, cleaning, machine learning, and interactive dashboards into one seamless environment.  

The system currently features the **V.0 prototype build** using **Streamlit + Scikit-learn**, with **V.1 (FastAPI + React + MLflow)** nearly completed.  

Built for HR leaders and data scientists alike, it enables organizations to **visualize**, **analyze**, and **predict** employee trends — from attrition and satisfaction to performance forecasting.

---

## 🎯 Project Summary

| Version | Description | Key Tech |
| :------ | :----------- | :-------- |
| [V.0 — Prototype Build](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.0) | Streamlit dashboard for HR data visualization and predictive insights. | Streamlit, Python, Scikit-learn |
| V.1 — Full Build *(Nearly Completed)* | FastAPI backend + React frontend + MLflow integration for scalable analytics. | FastAPI, React, MLflow |

---

## 🧩 Core Features

- 📊 **Interactive HR Dashboard:** Track KPIs like attrition rate, satisfaction score, and performance levels.  
- ⚙️ **Automated ETL Pipeline:** End-to-end ingestion, cleaning, and transformation scripts.  
- 🤖 **Predictive Modeling:** Machine learning models forecast employee attrition and performance.  
- 🧠 **Insight Engine:** Data-driven suggestions for HR strategy and retention planning.  
- 🧾 **Logging & Monitoring:** Comprehensive log files for all key operations.  
- ☁️ **Scalable Architecture (V.1):** Designed with FastAPI + React + MLflow for cloud-ready analytics.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[Raw HR Data / CSV or Database] -->|Ingestion| B[ETL Scripts]
    B -->|Cleaned Dataset| C[Model Training Engine]
    C -->|Trained Models - PKL Files| D[Streamlit / React Dashboard]
    D -->|Predictions and Visuals| E[End User]
    C -->|Logs and Metrics| F[Monitoring & Logs]
    E -->|Input or Refresh| D
````

---

## 🔍 Technical Stack

| Layer                | Technology                      | Purpose                                |
| :------------------- | :------------------------------ | :------------------------------------- |
| **Frontend**         | Streamlit / React               | Interactive dashboard & analytics UI   |
| **Backend**          | FastAPI                         | Model serving and API integration      |
| **Data Layer**       | Pandas, NumPy, SQLite           | Data management and transformation     |
| **ML Engine**        | Scikit-learn                    | Predictive model training              |
| **Model Management** | MLflow                          | Model tracking, versioning, deployment |
| **Visualization**    | Matplotlib, Seaborn             | Visual analytics and charts            |
| **Deployment**       | GCP Cloud Run / Streamlit Cloud | Cloud-ready scalability                |

---

## 📁 Repository Modules

| Folder                                                                                 | Purpose                                                            |
| :------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| [`/V.0`](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.0) | Prototype HR dashboard using Streamlit and ML models.              |
| `/V.1` *(Nearly Completed)*                                                            | Full FastAPI + React + MLflow backend for real-time analytics.     |
| `/models`                                                                              | Stores trained ML models for attrition and performance prediction. |
| `/data`                                                                                | Contains raw and cleaned HR datasets.                              |
| `/scripts`                                                                             | ETL, preprocessing, and modeling logic.                            |
| `/pipeline`                                                                            | Centralized execution of the data workflow.                        |
| `/logs`                                                                                | Tracks ingestion, cleaning, and prediction processes.              |

---

## 🧮 Workflow Overview

1. **Data Ingestion:** Loads HR data from CSV/API sources.
2. **Data Preprocessing:** Cleans missing values, encodes features, and prepares for ML.
3. **Model Training:** Builds models for attrition and performance prediction.
4. **Prediction Layer:** Generates insights in real time on the dashboard.
5. **Visualization:** Displays HR trends, metrics, and distributions interactively.

---

## 💬 Example Dashboard Snapshot

<p align="center">
  <img src="https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/blob/main/V.0/Demo/Streamlit.png" alt="HR Dashboard Demo" width="800">
</p>

---

## 🧠 Evolution Path

| Stage | Goal                                          | Status               |
| :---- | :-------------------------------------------- | :------------------- |
| V.0   | Streamlit-based prototype with ML predictions | ✅ Completed          |
| V.1   | FastAPI + React + MLflow backend integration  | 🏗️ Nearly Completed |

---

## 🧩 Future Roadmap

* 🔹 Finalize V.1 build with real-time analytics
* 🔹 Integrate advanced explainability (SHAP) for model insights
* 🔹 Enable cloud-hosted, scalable dashboards
* 🔹 Add dynamic HR metric alerts and notifications

---

## 📘 Architecture Philosophy

This project is built on **data democratization** — transforming HR data from static reports into predictive, actionable intelligence.
Each phase emphasizes **automation**, **scalability**, and **real-time decision support** for HR teams.

---

## 🪐 Project Ecosystem

| Module                       | Description                                                  | Link                                                                                       |
| :--------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| 🧩 **Prototype Build (V.0)** | Streamlit-based HR analytics prototype.                      | [Open → V.0](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/tree/main/V.0) |
| ⚡ **Full Build (V.1)**       | FastAPI + React + MLflow backend with scalable architecture. | *Nearly Completed*                                                                         |

---

## 📜 License

Licensed under the [MIT License](https://github.com/GKTHIRUMARAN/HR-Employee-Insights-Dashboard/blob/main/LICENSE).

---

## 👤 Author
**GK Thirumaran**  
🎓 *B.Tech Artificial Intelligence and Data Science*  
🌍 *Coimbatore, Tamil Nadu, India*  
💼 *Aspiring Data Scientist & Analyst | AIML Developer*  
🔗 [Linkedin](https://www.linkedin.com/in/thirumarangk-ai) | [Porfolio](https://maranthiru180.wixsite.com/my-site)
