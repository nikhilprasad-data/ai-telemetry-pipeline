# 🚀 AI Telemetry Data Pipeline & Feature Engineering

## 🚀 Overview
A robust data processing pipeline built with Python and Pandas to analyze, clean, and engineer features from raw AI API telemetry logs. 

Instead of working with clean Kaggle datasets, this project simulates a real-world LLM gateway backend. It takes messy, nested, and noisy JSON server logs and applies strict data type enforcements, statistical imputations, and feature engineering to create a high-quality, machine-learning-ready dataset.

## 🛠️ Tech Stack & Architecture
* **Language:** Python 3.x
* **Core Engine:** Pandas, NumPy
* **Environment:** Jupyter Notebook, Virtual Environment (venv)

## 📂 Pipeline Structure & Features

### 1. `scripts/generate_mock_logs.py` (Data Generation & Noise Injection)
Focuses on creating a realistic, messy telemetry dataset.
* Generates a synthetic dataset of 200 API request logs mimicking an AI gateway.
* Injects real-world data noise like missing confidence scores, `timeout_error` strings in numeric latency columns, and unstandardized URL traces.
* Exports raw data as structured JSON.

### 2. `01_pandas_data_cleaning.ipynb` (Data Cleaning & Imputation)
Focuses on standardizing and sanitizing the raw JSON logs.
* Performs strict type casting: standardizes timestamps to Pandas `datetime64[us]` and forces numeric conversions.
* Handles missing values using median imputation for latency (to prevent skewness) and mean imputation for confidence scores.
* Parses complex, concatenated strings in the `raw_system_prompt` column to extract isolated features (`device_type`, `http_status`, `user_query`).
* Cleans backend server traces to isolate core server node identifiers.

### 3. `02_feature_engineering.ipynb` (Feature Extraction & Encoding)
Focuses on transforming cleaned data into predictive, ML-ready features.
* Extracts `hour_of_day` from timestamps to enable time-series and traffic analysis.
* Engineers a binary `is_error` flag (0 for HTTP 200 OK, 1 for failures) for future classification models.
* Computes `query_length` to analyze prompt complexity and user behavior.
* Applies One-Hot Encoding (`pd.get_dummies`) to `device_type` to convert categorical text into numerical feature matrices.

## ⚙️ Local Setup & Installation

To run this data pipeline on your local machine, follow these steps:

**Step 1: Clone the repository**
    git clone https://github.com/nikhilprasad-data/ai-telemetry-pipeline.git

**Step 2: Set up the virtual environment**
    python -m venv venv
    source venv/bin/activate
    # On Windows use: venv\Scripts\activate

**Step 3: Install dependencies**
    pip install -r requirements.txt

**Step 4: Generate data & Run the notebooks**
    python scripts/generate_mock_logs.py
    
After generating the data, launch your Jupyter environment to execute the cleaning and feature engineering pipelines step-by-step.

## 🎯 Key Learning & Impact
This project acts as a complete end-to-end sandbox for understanding real-world Data Engineering and Exploratory Data Analysis (EDA). It proves core competency in tackling "Garbage In, Garbage Out" (GIGO) scenarios by converting messy, unstructured server logs into high-quality mathematical inputs for Machine Learning algorithms.