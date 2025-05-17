# Healthcare Diagnostics and Treatment

## Overview
An AI and IoT-enabled healthcare platform for real-time patient diagnosis and monitoring.

## Features
- AI-powered disease diagnosis (Diabetes, Hypertension)
- IoT-based health data ingestion (heart rate, temperature, SpO₂)
- Secure and unified health data platform
- Personalized treatment recommendations

## Tech Stack
- Python, Flask, Scikit-learn
- Simulated IoT inputs (CSV/JSON)
- RESTful APIs

## Endpoints
- `/diagnose` (POST): Returns diagnosis results.
- `/monitor` (POST): Accepts IoT data.
- `/get_patient_data/<id>` (GET): Fetches patient info.
- `/recommend_treatment` (POST): Suggests treatment.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run API: `python api/app.py`
