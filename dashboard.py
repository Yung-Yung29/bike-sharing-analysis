
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bike Sharing Demand Dashboard",
    page_icon="🚲",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_csv("main_data.csv")

    # Convert date column to datetime
    df["dteday"] = pd.to_datetime(df["dteday"])

    return df


df = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("🚲 Bike Sharing Demand Dashboard")

st.markdown(
    """
    This dashboard provides an interactive overview of bike-sharing
    demand based on hourly patterns, day type, weather conditions,
    and seasons during 2011–2012.
    """
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Dashboard Filters")


# ------------------------------------------------------------
# DATE FILTER
# ------------------------------------------------------------

min_date = df["dteday"].min().date()
max_date = df["dteday"].max().date()

selected_date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_date_range) == 2:

    start_date = selected_date_range[0]
    end_date = selected_date_range[1]

else:

    start_date = min_date
    end_date = max_date


# ------------------------------------------------------------
# SEASON FILTER
# ------------------------------------------------------------

season_options = [
    "All Seasons"
] + sorted(
    df["season_name"].dropna().unique().tolist()
)

selected_season = st.sidebar.selectbox(
    "Select Season",
    options=season_options
)


# ------------------------------------------------------------
# WEATHER FILTER
# ------------------------------------------------------------

weather_options = [
    "All Weather Conditions"
] + sorted(
    df["weather_name"].dropna().unique().tolist()
)

selected_weather = st.sidebar.selectbox(
    "Select Weather Condition",
    options=weather_options
)


# ------------------------------------------------------------
# DAY TYPE FILTER
# ------------------------------------------------------------

day_type_options = [
    "All Day Types"
] + sorted(
    df["day_type"].dropna().unique().tolist()
)

selected_day_type = st.sidebar.selectbox(
    "Select Day Type",
    options=day_type_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["dteday"].dt.date >= start_date) &
    (df["dteday"].dt.date <= end_date)
].copy()


if selected_season != "All Seasons":

    filtered_df = filtered_df[
        filtered_df["season_name"] == selected_season
    ]


if selected_weather != "All Weather Conditions":

    filtered_df = filtered_df[
        filtered_df["weather_name"] == selected_weather
    ]


if selected_day_type != "All Day Types":

    filtered_df = filtered_df[
        filtered_df["day_type"] == selected_day_type
    ]


# ============================================================
# HANDLE EMPTY DATA
# ============================================================

if filtered_df.empty:

    st.warning(
        "No data is available for the selected filters. "
        "Please adjust your filter selections."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_rentals = filtered_df["cnt"].sum()

average_rentals = filtered_df["cnt"].mean()

peak_hour = (
    filtered_df
    .groupby("hr")["cnt"]
    .mean()
    .idxmax()
)

peak_hour_demand = (
    filtered_df
    .groupby("hr")["cnt"]
    .mean()
    .max()
)


# ============================================================
# KPI DISPLAY
# ============================================================

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Rentals",
        f"{total_rentals:,.0f}"
    )


with col2:

    st.metric(
        "Average Rentals / Hour",
        f"{average_rentals:,.2f}"
    )


with col3:

    st.metric(
        "Peak Hour",
        f"{int(peak_hour):02d}:00"
    )


with col4:

    st.metric(
        "Peak Average Demand",
        f"{peak_hour_demand:,.2f}"
    )


st.divider()


# ============================================================
# CHART 1 — HOURLY DEMAND
# ============================================================

st.subheader("1. Hourly Bike Rental Demand")


hourly_demand = (
    filtered_df
    .groupby(
        ["day_type", "hr"]
    )["cnt"]
    .mean()
    .reset_index()
)


fig1, ax1 = plt.subplots(
    figsize=(12, 5)
)


sns.lineplot(
    data=hourly_demand,
    x="hr",
    y="cnt",
    hue="day_type",
    marker="o",
    ax=ax1
)


ax1.set_title(
    "Average Bike Rental Demand by Hour and Day Type"
)

ax1.set_xlabel("Hour of Day")

ax1.set_ylabel(
    "Average Number of Rentals"
)

ax1.set_xticks(range(24))

ax1.legend(
    title="Day Type"
)

plt.tight_layout()

st.pyplot(fig1)


st.markdown(
    """
    **Business insight:** Working days tend to show stronger demand
    around commuting periods, while weekends and holidays tend to
    show higher demand during the afternoon.
    """
)


# ============================================================
# CHART 2 — WEATHER
# ============================================================

st.subheader(
    "2. Bike Rental Demand by Weather Condition"
)


weather_summary = (
    filtered_df
    .groupby("weather_name")["cnt"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)


fig2, ax2 = plt.subplots(
    figsize=(10, 5)
)


sns.barplot(
    data=weather_summary,
    x="weather_name",
    y="cnt",
    ax=ax2
)


ax2.set_title(
    "Average Bike Rental Demand by Weather Condition"
)

ax2.set_xlabel(
    "Weather Condition"
)

ax2.set_ylabel(
    "Average Number of Rentals"
)

ax2.tick_params(
    axis="x",
    rotation=20
)

plt.tight_layout()

st.pyplot(fig2)


st.markdown(
    """
    **Business insight:** Rental demand is generally higher under
    favorable weather conditions and decreases under less favorable
    weather conditions.
    """
)


# ============================================================
# CHART 3 — SEASON
# ============================================================

st.subheader(
    "3. Bike Rental Demand by Season"
)


season_summary = (
    filtered_df
    .groupby("season_name")["cnt"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)


fig3, ax3 = plt.subplots(
    figsize=(10, 5)
)


sns.barplot(
    data=season_summary,
    x="season_name",
    y="cnt",
    ax=ax3
)


ax3.set_title(
    "Average Bike Rental Demand by Season"
)

ax3.set_xlabel("Season")

ax3.set_ylabel(
    "Average Number of Rentals"
)

plt.tight_layout()

st.pyplot(fig3)


st.markdown(
    """
    **Business insight:** Seasonal demand varies substantially.
    Historical seasonal patterns can therefore be used when planning
    bike availability and operational capacity.
    """
)


# ============================================================
# CHART 4 — DEMAND LEVEL
# ============================================================

st.subheader(
    "4. Demand Level Distribution"
)


filtered_df["demand_level"] = pd.qcut(
    filtered_df["cnt"],
    q=3,
    labels=[
        "Low Demand",
        "Medium Demand",
        "High Demand"
    ],
    duplicates="drop"
)


demand_distribution = (
    filtered_df["demand_level"]
    .value_counts()
    .sort_index()
    .reset_index()
)


demand_distribution.columns = [
    "Demand Level",
    "Number of Observations"
]


fig4, ax4 = plt.subplots(
    figsize=(10, 5)
)


sns.barplot(
    data=demand_distribution,
    x="Demand Level",
    y="Number of Observations",
    ax=ax4
)


ax4.set_title(
    "Distribution of Bike Rental Demand Levels"
)

ax4.set_xlabel(
    "Demand Level"
)

ax4.set_ylabel(
    "Number of Observations"
)

plt.tight_layout()

st.pyplot(fig4)


# ============================================================
# OPERATIONAL RECOMMENDATIONS
# ============================================================

st.divider()

st.subheader(
    "Operational Recommendations"
)


st.markdown(
    """
    Based on the analysis, the following operational actions are
    recommended:

    1. **Prioritize bike availability during peak working-day hours.**
       Additional operational capacity should be prepared around
       morning and afternoon commuting periods.

    2. **Increase operational readiness during high-demand seasons.**
       Historical seasonal demand should be considered when allocating
       bikes and operational resources.

    3. **Consider weather conditions in operational planning.**
       Favorable weather is associated with higher rental demand,
       while unfavorable weather tends to correspond with lower demand.

    4. **Use demand-level segmentation for operational monitoring.**
       Low, Medium, and High Demand categories can provide a simple
       framework for identifying periods requiring different levels
       of operational attention.
    """
)


# ============================================================
# DATA SUMMARY
# ============================================================

with st.expander("View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        width="stretch"
    )


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "Bike Sharing Dataset | Analysis period: 2011–2012"
)
