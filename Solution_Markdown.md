# **Solution**: COVID-19, US Census, Weather Data Analytics for US States

## **Objective**

As part of this project, I built a Spotfire dashboard that integrates COVID-19 case data, U.S. Census demographics, and historical weather data.  
The objective was to analyze how population and environmental factors may have influenced COVID-19 trends over time and across different states.  
The dashboard allows users to interactively explore patterns and potential correlations across these datasets.

---

## **Sources**

### **COVID-19 Data**
- Collected from the CDC COVID Data Tracker via OData connector.
- Includes daily figures on confirmed cases, deaths, etc.
- Available at both state and county levels, covering the years 2020 to 2023.

### **U.S. Census Data**
- Covers demographic and socioeconomic indicators such as population size, median household income, unemployment, and age distribution.
- Sourced from the U.S. Census Bureau, via API through Python Data Function.
- Data is provided at the state and county levels, using the most recent available estimates.

### **Weather Data**
- Contains information on temperature, rainfall, humidity, and instances of extreme weather.
- Sourced from OpenWeather.
- Aggregated at the state level on a monthly basis for the period 2020 to 2023.

---

## **Data Transformation**

### **Merging**
- Merged datasets using state and date as primary keys.
- Joined COVID-19 and weather data via a left join.
- Joined the combined data with census data via a left join.

### **Aggregations**
- Aggregation of COVID-19 dataset from daily to monthly to match the aggregation in other sources.

### **Calculated Columns**
- `Deaths Per Capita = Deaths / Population`
- `COVID Case Rate = COVID_Cases / Population * 1,000,000`

### **Missing Values Imputation**
- Replaced missing values by filling them with mean or median wherever suitable.
- Filtered outliers during model building.

---

## **Data Functions in Use**

Python scripts were used for the following data functions:

- **OpenWeather Data Integration**  
  Retrieves weather data via the OpenWeather API, including metrics like temperature, humidity, wind speed, and location coordinates. Data is structured into a DataFrame and passed to a Spotfire table.

- **U.S. Census Data Retrieval**  
  Fetches demographic and economic variables such as population, median income, age, and racial composition from the U.S. Census API. The data is returned as a structured DataFrame.

- **Random Forest Model**  
  Implements an ensemble model combining Random Forest, Boosted Trees, and Linear Regression to predict COVID-19 case rates based on population, income, temperature, and humidity.

- **Clustering Algorithm**  
  Applies K-Means and Hierarchical clustering to group states based on features like population, age, unemployment, GDP, home value, rent, and income.

---

## **Dashboard Features**

- **Landing Page**  
  Describes the objective of the dashboard.

- **Census**  
  Exploratory data analysis of the census data.

- **Weather Impact**  
  Analyzes the relationship between weather conditions and COVID-19 case patterns.

- **COVID-19 Death Statistics**  
  Visualizes death vs case rates across U.S. states from 2020–2023.

- **Forecast**  
  Time series modeling and forecasting of COVID-related deaths, including correlations with population.

- **Inbuilt Regression Model**  
  Uses Spotfire's built-in decision tree model to predict deaths using combined datasets.

- **Covid Case Rate Prediction – Ensemble**  
  Predicts COVID-19 cases using a combination of multiple models.

- **Clustering – COVID Cases**  
  Identifies clusters of states using demographic and case data for deeper insights.

---

## **External Data Source Links**

1. [CDC COVID-19 Data Tracker](https://covid.cdc.gov/)
2. [US Census Bureau](https://www.census.gov/)
3. [OpenWeather](https://openweathermap.org/)
