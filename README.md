# **AI-Powered Enterprise Data Quality Auditor**

A multi-agent system that automatically evaluates, scores, and explains the quality of structured datasets using a **Planner → Worker → Evaluator** workflow.  
Designed for enterprise data engineering teams, deployed on Hugging Face Spaces, and fully open-source.

---

## 🚀 Live Demo

**Hugging Face Space:** *(Add your HF URL here)*  
**GitHub Repository:** https://github.com/ItzMilitia/AI-Powered-Enterprise-Data-Quality-Auditor

---

## 🎯 Project Overview

Data quality is one of the biggest hidden bottlenecks in enterprise analytics and machine learning.  
Teams spend enormous time detecting and fixing issues such as:

- Missing values  
- Duplicates  
- Schema mismatches  
- Outliers  
- Incorrect data types  
- Inconsistent distributions  

This project automates that entire process through a structured **multi-agent** architecture.  
The system audits datasets, generates a **Global Data Quality Score**, and provides human-readable insights.

---

## 🧠 Why Agents?

Traditional scripts run checks sequentially. Data quality auditing, however, is inherently **multi-step** and **modular**, making it perfect for agent-based design:

### **Planner Agent**
Decides which checks should run based on dataset metadata.

### **Worker Agents**
Each Worker is responsible for one type of quality check:
- Missing value detection  
- Outlier detection  
- Duplicate identification  
- Schema & dtype validation  
- Basic statistical profiling  

### **Evaluator Agent**
Aggregates Worker outputs and computes:
- Severity levels  
- Recommendations  
- A final **Data Quality Score (0–100)**  

Agent-based design gives:
- ✔ Modularity  
- ✔ Scalability  
- ✔ Fault isolation  
- ✔ Better explainability  
- ✔ Easier future expansion  

---

## 🏗 Architecture

User Input
│
▼
Main Agent
│
Decides: Audit Mode or Conversation Mode
│
├──────────────────────────────┐
│ │
▼ ▼
Planner Agent Conversational Response
│
▼
Audit Plan
│
▼
Worker Agents (parallel checks)
│
▼
Collected Results
│
▼
Evaluator Agent
│
▼
Final JSON Report + Score + Summary

yaml
Copy code

---

## 🧪 Features

### 🔍 Automated Data Quality Checks
- Missing values  
- Schema / type drift  
- Duplicates  
- Outliers  
- Dataset completeness  
- Column statistics  

### 📊 Global Score
A weighted scoring model produces a final **0–100 quality score**.

### 📝 Reporting
- JSON structured findings  
- Human-readable summaries  
- Session logs  
- Full audit history  

### 🧠 Memory Support
- Stores previous runs  
- Multi-turn conversations  
- Repeated queries inside same session  

### 🌐 Deployed App
- Gradio UI  
- Live Log panel  
- Hugging Face Space hosting  

---

## 💻 Tech Stack

- Python  
- Pandas  
- Gradio  
- Loguru  
- Hugging Face Spaces  
- Custom Multi-Agent Planner → Worker → Evaluator pipeline  
- JSON-based A2A protocol  
- Session memory store  

---

## 🔎 Usage Examples

### **1. Ask general questions**
What can you do?

shell
Copy code

### **2. Run a default audit**
audit my dataset

shell
Copy code

### **3. Audit a specific CSV**
Place the file at:
/content/project/test.csv

arduino
Copy code

Then run:
audit test.csv

shell
Copy code

### **4. Ask about the system**
Run a quick self-check and describe your internal workflow.

yaml
Copy code

---

## 🧩 Folder Structure

project/
│
├── agents/
│ ├── planner.py
│ ├── worker.py
│ └── evaluator.py
│
├── core/
│ ├── context_engineering.py
│ ├── a2a_protocol.py
│ └── observability.py
│
├── memory/
│ └── session_memory.py
│
├── tools/
│ └── tools.py
│
├── main_agent.py
└── app.py

yaml
Copy code

---

## 🛠 How It Works

### **Step 1 — Planner**
Extracts metadata → generates a detailed audit plan.

### **Step 2 — Workers**
Each Worker executes one check independently and returns structured JSON findings.

### **Step 3 — Evaluator**
Aggregates Worker results → assigns severity → calculates overall Data Quality Score.

### **Step 4 — Final Output**
- Summary text  
- JSON report  
- Logged process  
- Session memory updated  

---

## 📦 Installation (Local)

```bash
git clone https://github.com/ItzMilitia/AI-Powered-Enterprise-Data-Quality-Auditor
cd AI-Powered-Enterprise-Data-Quality-Auditor
pip install -r requirements.txt
python project/run_demo.py

🌟 If I Had More Time…
1. LLM-Powered Insight Generator

Explain findings + propose solutions.

2. Advanced Checks

Schema drift

Data drift

Domain-based validations

Correlation & anomaly detection

3. Dashboard

Interactive visualization using Streamlit / Plotly.

4. Auto-Fix Mode

Automatically correct missing values + outliers.

5. Package Release

Publish as:

pip install dq-auditor-agent
dq-audit mydata.csv

🏁 Final Notes

This project demonstrates:
✔ Multi-agent design
✔ Enterprise-grade auditing
✔ Real-time deployment
✔ Clean architecture
✔ Data engineering + AI workflow automation
