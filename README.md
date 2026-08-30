````markdown
# Bike Sharing Demand Analysis

## Project Overview

This project analyzes the Bike Sharing Dataset to identify patterns and factors associated with bike rental demand.

The analysis focuses on hourly rental patterns, differences between working days and weekends/holidays, weather conditions, and seasonal patterns.

An interactive Streamlit dashboard is also provided to allow users to explore the analysis using different filters.

## Dataset

The dataset used in this project is the **Bike Sharing Dataset**, which contains hourly bike rental information together with information about time, season, weather conditions, and other environmental variables.

The dataset covers the period from **2011 to 2012**.

## Business Questions

The analysis addresses the following business questions:

1. **When does bike rental demand reach its peak on working days compared with weekends and holidays?**

2. **How do weather conditions and seasons relate to bike rental demand?**

These questions are intended to support operational planning, particularly bike availability and resource allocation.

## Data Analysis Process

The analysis follows these main stages:

1. Data Gathering
2. Data Assessing
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Data Visualization
6. Explanatory Analysis
7. Conclusion and Recommendations

## Key Findings

### Hourly Demand

Bike rental demand varies throughout the day and differs between working days and weekends/holidays.

On working days, the highest average rental demand occurs around the commuting period, with the peak occurring at **17:00**.

On weekends and holidays, demand is more concentrated during the afternoon, with the highest average occurring at approximately **13:00**.

### Weather Conditions

Weather conditions are associated with differences in bike rental demand.

Clear weather has the highest average rental demand at approximately **204.87 rentals per hour**, while Light Rain / Snow has a lower average of approximately **111.58 rentals per hour**.

Heavy Rain / Snow has the lowest observed average at approximately **74.33 rentals per hour**. However, this category contains only three observations, so the result should be interpreted cautiously.

### Seasonal Patterns

Rental demand also varies by season.

Fall has the highest average rental demand at approximately **236.02 rentals per hour**, while Spring has the lowest average at approximately **111.11 rentals per hour**.

## Recommendations

Based on the analysis, several operational actions are recommended:

1. Prioritize bike availability during peak working-day hours, particularly around commuting periods.

2. Increase operational readiness during high-demand seasons, especially Fall.

3. Consider weather conditions when planning bike redistribution and operational resources.

4. Use historical demand patterns to adjust operational capacity during periods of expected high or low demand.

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

The dashboard provides:

- Year filtering
- Season filtering
- Weather-condition filtering
- Day-type filtering
- Total rental KPI
- Average rental KPI
- Peak-hour KPI
- Hourly demand visualization
- Weather-demand visualization
- Seasonal-demand visualization
- Demand-level distribution
- Filtered dataset preview

## Project Structure

```text
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── data/
│   └── hour.csv
│
├── notebook.ipynb
├── README.md
└── requirements.txt
````

## How to Run the Dashboard Locally

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install the Required Libraries

Open Terminal or Command Prompt and navigate to the project folder.

Run:

```bash
pip install -r requirements.txt
```

### 3. Navigate to the Dashboard Folder

Run:

```bash
cd dashboard
```

### 4. Run Streamlit

Run:

```bash
streamlit run dashboard.py
```

The dashboard will then be available through the local Streamlit address shown in the terminal, usually:

```text
http://localhost:8501
```

## Author

Bike Sharing Demand Analysis Project

```
```
