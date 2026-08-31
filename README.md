# 🚲 Bike Sharing Demand Analysis

## 📌 Project Overview

This project analyzes bike-sharing rental demand using the Bike Sharing Dataset.

The analysis focuses on identifying patterns in bike rental demand based on:

- Hour of the day
- Day type
- Weather conditions
- Seasons
- Demand levels

The project consists of a Jupyter Notebook for data analysis and an interactive Streamlit dashboard for presenting the analysis results.

---

## 📊 Dataset

The dataset used in this project is the **Bike Sharing Dataset**.

The dataset contains hourly bike rental information from 2011 to 2012, including:

- Date and time
- Season
- Weather condition
- Temperature
- Humidity
- Wind speed
- Casual users
- Registered users
- Total bike rentals

The dataset was obtained from Kaggle.

---

## 🎯 Business Questions

This project addresses the following business questions:

### 1. How does bike rental demand vary by hour between working days and weekends/holidays during 2011–2012?

This question aims to identify peak rental periods for different day types and support operational planning.

### 2. How does bike rental demand vary across different weather conditions and seasons during 2011–2012?

This question aims to identify environmental conditions associated with higher or lower rental demand and support resource allocation.

---

## 📁 Project Structure

```text
bike-sharing-analysis/
│
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── data/
│   └── hour.csv
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
