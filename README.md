# Agentic Data Pipeline Reliability Platform

## Overview

The Agentic Data Pipeline Reliability Platform is a multi-agent AI system designed to automate ETL and data pipeline incident management.

Modern data platforms generate thousands of pipeline failures caused by schema drift, data quality issues, infrastructure failures, Spark job failures, Airflow task failures, and database connectivity problems.

Traditionally, engineers manually investigate logs, search troubleshooting documentation, determine root causes, recommend fixes, and create incident reports.

This project automates that workflow using CrewAI, Gemini, ChromaDB, FastAPI, and Streamlit.

---

# High-Level Architecture

```text
┌─────────────────────┐
│     Streamlit UI    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      FastAPI        │
└──────────┬──────────┘
           │
           ▼
┌──────────────────────────────────────┐
│        CrewAI Orchestration          │
└──────────────────────────────────────┘
           │
           ▼

┌──────────────────────────────────────┐
│ Agent 1: Failure Classification      │
└──────────────────────────────────────┘
           │
           ▼

┌──────────────────────────────────────┐
│ Agent 2: Root Cause Analysis         │
└──────────────────────────────────────┘
           │
           ▼

┌──────────────────────────────────────┐
│ ChromaDB Retrieval Layer             │
└──────────────────────────────────────┘
           │
           ▼

┌──────────────────────────────────────┐
│ Agent 3: Documentation Analysis      │
└──────────────────────────────────────┘
           │
           ▼

┌──────────────────────────────────────┐
│ Agent 4: Fix Recommendation          │
└──────────────────────────────────────┘
           │
           ▼

┌──────────────────────────────────────┐
│ Agent 5: Incident Report Generation  │
└──────────────────────────────────────┘
           │
           ▼

┌─────────────────────┐
│ Incident Repository │
└─────────────────────┘
```

---

# Problem Solved

Data Engineering teams spend significant time manually investigating pipeline failures.

Typical workflow:

1. Read ETL logs
2. Identify failure category
3. Determine root cause
4. Search troubleshooting guides
5. Recommend corrective actions
6. Create incident reports

This process is repetitive, time-consuming, and difficult to scale.

The Agentic Data Pipeline Reliability Platform automates these tasks and reduces incident triage effort through AI-driven workflow orchestration.

---

# Key Features

### Multi-Agent Incident Analysis

Specialized AI agents collaborate to investigate pipeline failures.

### Automated Root Cause Analysis

Identifies likely causes of failures using log context.

### Retrieval-Augmented Generation (RAG)

Retrieves relevant troubleshooting documentation using ChromaDB vector search.

### Remediation Recommendations

Generates actionable recommendations for incident resolution.

### Incident Report Generation

Creates structured enterprise-style incident reports.

### REST API Support

FastAPI endpoints enable integration with external systems.

### Interactive Dashboard

Streamlit interface for real-time analysis.

### Incident Persistence

Stores generated incident reports for future reference.

---

# Agent Responsibilities

## Agent 1 — Failure Classification Agent

Responsibilities:

* Categorize pipeline failures
* Determine severity
* Classify incident type

Outputs:

* Failure category
* Severity level

---

## Agent 2 — Root Cause Analysis Agent

Responsibilities:

* Analyze logs
* Identify likely root cause
* Explain reasoning

Outputs:

* Root cause analysis

---

## Agent 3 — Documentation Analysis Agent

Responsibilities:

* Analyze retrieved documentation
* Summarize supporting evidence
* Provide operational guidance

Outputs:

* Knowledge summary

---

## Agent 4 — Fix Recommendation Agent

Responsibilities:

* Generate remediation plans
* Recommend corrective actions
* Suggest preventive measures

Outputs:

* Actionable fixes

---

## Agent 5 — Incident Report Agent

Responsibilities:

* Generate enterprise incident reports
* Consolidate findings
* Provide final incident summary

Outputs:

* Incident report

---

# Tech Stack

## AI & Agent Framework

* CrewAI
* Google Gemini 2.5 Flash

## Retrieval-Augmented Generation

* ChromaDB
* Local Embeddings

## Backend

* FastAPI

## Frontend

* Streamlit

## Storage

* JSON Incident Repository

## Containerization

* Docker
* Docker Compose

## Language

* Python

---

# Example Workflow

Input:

```text
ETL Job Failed

Column customer_age missing

Schema Validation Failed

Pipeline Terminated
```

Pipeline Execution:

```text
Failure Classification
      ↓
Root Cause Analysis
      ↓
Document Retrieval
      ↓
Documentation Analysis
      ↓
Fix Recommendation
      ↓
Incident Report Generation
```

Output:

```text
Severity: Critical

Root Cause:
Schema Drift

Impact:
Customer records not loaded

Recommended Actions:
- Validate source schema
- Update ETL mappings
- Implement schema contracts
```

---

# Project Structure

```text
AgenticDataPipelineReliabilityPlatform/

agents/
crew/
rag/
api/
ui/
storage/
evaluation/
monitoring/
logs/
docs/
incidents/

Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

# Running Locally

### Clone Repository

```bash
git clone <repository_url>

cd AgenticDataPipelineReliabilityPlatform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Start FastAPI

```bash
uvicorn api.main:app --reload
```

### Start Streamlit

```bash
streamlit run ui/app.py
```

---

# API Endpoints

### Health Check

```http
GET /
```

### Analyze Pipeline Failure

```http
POST /analyze
```

Request:

```json
{
  "log_text": "Pipeline Failure Log"
}
```

Response:

```json
{
  "incident_id": "INC-12345",
  "report": "Generated Incident Report"
}
```

---

# Future Enhancements

### LangGraph Migration

Replace linear workflows with graph-based agent orchestration.

### Model Context Protocol (MCP)

Enable secure integration with enterprise systems such as Jira, GitHub, Databases, BigQuery, and Airflow.

### Agent Memory

Support long-running investigations and historical context.

### Human-in-the-Loop Approval

Require engineer approval before executing critical recommendations.

### Automated Remediation

Enable automatic corrective actions for recurring incidents.

### Real-Time Monitoring

Integrate with Prometheus and Grafana for observability.

### Kubernetes Deployment

Support large-scale production deployment.

### Enterprise Authentication

OAuth2, SSO, and Role-Based Access Control (RBAC).

### Evaluation Framework

Measure:

* Classification Accuracy
* Root Cause Accuracy
* Retrieval Quality
* Recommendation Quality

---

# Skills Demonstrated

* Multi-Agent Systems
* CrewAI
* Agent Orchestration
* Retrieval-Augmented Generation (RAG)
* ChromaDB
* FastAPI
* Streamlit
* Docker
* REST APIs
* ETL Reliability Engineering
* Root Cause Analysis
* Incident Management
* AI System Design
* Production AI Workflows

---

# Author

Veneel Kumar A

Aspiring AI Engineer | Data Scientist | MLOps Enthusiast

Focused on building production-grade AI systems that solve real-world operational problems.
