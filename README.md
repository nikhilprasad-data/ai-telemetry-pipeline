# 🚀 AI Telemetry Data Pipeline & Feature Engineering

## 🚀 Overview

A data processing pipeline built with Python and Pandas to analyze, clean, and engineer features from raw AI API telemetry logs.

Rather than working with clean datasets, this project simulates a real-world AI gateway backend environment. The pipeline starts with noisy, semi-structured JSON logs and transforms them into a structured dataset suitable for analysis and machine learning workflows.

---

## 🛠️ Tech Stack

* Python 3.x
* Pandas
* NumPy
* Jupyter Notebook
* Virtual Environment (venv)

---

## 📁 Project Structure

```text
ai-telemetry-pipeline/
│
├── data/
│   ├── processed/
│   │   ├── api_logs_v1_cleaned_2026-05-19.csv
│   │   └── api_logs_v1_features_added_2026-05-19.csv
│   │
│   └── raw/
│       └── api_logs_v1_2026-05-19.json
│
├── notebooks/
│   ├── 01_pandas_data_cleaning.ipynb
│   └── 02_feature_engineering.ipynb
│
├── scripts/
│   └── generate_mock_logs.py
│
├── src/
│   └── __init__.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📂 Pipeline Structure & Features

### 1️⃣ `scripts/generate_mock_logs.py`

### Data Generation & Noise Injection

This script generates a synthetic telemetry dataset that mimics logs produced by an AI API gateway.

#### Features

* Generates 200 synthetic API request logs
* Injects missing confidence scores
* Simulates `timeout_error` values in latency fields
* Creates inconsistent backend traces and URL patterns
* Exports structured JSON data for downstream processing

---

### 2️⃣ `01_pandas_data_cleaning.ipynb`

### Data Cleaning & Imputation

This notebook focuses on cleaning and standardizing raw telemetry logs.

#### Features

* Converts timestamps into Pandas datetime format
* Performs numeric type conversions
* Handles missing values through statistical imputation
* Extracts structured information from raw prompt strings
* Cleans backend server traces
* Standardizes inconsistent and noisy values

---

### 3️⃣ `02_feature_engineering.ipynb`

### Feature Extraction & Encoding

This notebook transforms cleaned data into machine-learning-ready features.

#### Features

* Extracts `hour_of_day` from timestamps
* Creates a binary `is_error` feature
* Calculates `query_length`
* Applies One-Hot Encoding using:

```python
pd.get_dummies()
```

* Prepares categorical variables for machine learning workflows

---

## ⚙️ Local Setup & Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/nikhilprasad-data/ai-telemetry-pipeline.git
cd ai-telemetry-pipeline
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Environment

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Generate Mock Data

```bash
python scripts/generate_mock_logs.py
```

### Step 6: Launch Jupyter Notebook

```bash
jupyter notebook
```

Run the notebooks in the following order:

1. `01_pandas_data_cleaning.ipynb`
2. `02_feature_engineering.ipynb`

---

## 🎯 What I Learned From This Project

This project was created to move beyond basic Pandas exercises and work with data that resembles real-world application telemetry.

While building this pipeline, I gained hands-on experience in:

* Processing nested JSON datasets
* Performing data type enforcement and validation
* Handling missing values using statistical imputation techniques
* Cleaning inconsistent and noisy records
* Parsing semi-structured log data into meaningful features
* Engineering new features from raw telemetry information
* Working with datetime operations and time-based analysis
* Converting categorical variables into machine-learning-ready features using One-Hot Encoding
* Building a structured data preprocessing workflow using Pandas

One of the most valuable lessons from this project was understanding that feature engineering and data cleaning often require more effort than model building itself. Real-world datasets frequently contain inconsistencies, missing information, invalid data types, and formatting issues that must be resolved before any meaningful analysis can begin.

Through this project, I strengthened my understanding of Pandas, data preprocessing, feature engineering, and the practical workflow required to transform raw operational data into structured analytical datasets.
