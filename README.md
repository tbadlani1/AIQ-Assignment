# AIQ-Assignment
Spotfire Assignment for AIQ
Objective
As part of this project, I built a Spotfire dashboard that integrates COVID-19 case data, U.S. Census demographics, and historical weather data. The objective was to analyze how population and environmental factors may have influenced COVID-19 trends over time and across different states. The dashboard allows users to interactively explore patterns and potential correlations across these datasets.

________________________________________
**Sources**
*COVID-19 Data
	-Collected from the CDC COVID Data Tracker via OData connector.
	-Includes daily figures on confirmed cases, deaths etc.
	-Available at both state and county levels, covering the years 2020 to 2023.

*U.S. Census Data
	-Covers demographic and socioeconomic indicators such as population size, median household income, unemployment, and age distribution.
	-Sourced from the U.S. Census Bureau, via API through Python Data Function.
	-Data is provided at the state and county levels, using the most recent available estimates.

*Weather Data
	-Contains information on temperature, rainfall, humidity, and instances of extreme weather.
	-Sourced from OpenWeather.
	-Aggregated at the state level on a monthly basis for the period 2020 to 2023.

________________________________________
**Data Transformation**
*Merging
	-Merged datasets using State and date as primary keys.
	-joined COVID-19 and Weather data via a left join.
	-joined the combined data with Census data via a left join.
	
*Aggregations
	-Aggregation of COVID-19 dataset from daily to monthly to match the aggregation in other sources.

*Calculated Columns
	-Deaths Per Capita = Deaths/Population.
	-COVID Case Rate = COVID_Cases/Population * 1000000

*Missing values imputation
	-Replaced missing values by filling them with mean or median wherever suitable.
	-Filtered outliers during model building.

________________________________________
**Data Functions in use**
Data Functions used in the form of Python scripts.
	-OpenWeather Data Integration: This Python script retrieves weather information using the OpenWeather API. It collects data points such as state, capital city, temperature, perceived temperature, minimum and maximum temperatures, atmospheric pressure, humidity, visibility, weather conditions, cloud coverage, wind speed and direction, along with geographic coordinates (latitude and longitude). The data is parsed into a DataFrame, which is then returned as an output table.
	-U.S. Census Data Retrieval: This Python script accesses demographic and economic statistics via the U.S. Census API. Key variables include state, total population, median household income, income inequality (Gini index), housing costs (median rent and home value), median age, unemployment rate, and population distribution by race and ethnicity. The retrieved data is structured into a DataFrame and output as a table.
	-Random Forest Model: This script implements an ensemble of Random Forest algorithm, Boosted Trees and Linear Regression to estimate COVID-19 case rates. The prediction model uses features such as population size, median household income, temperature, and humidity.
	-Clustering Algorithm: This script applies K-Means and hierarchical clustering techniques to group data based on indicators like population, age, unemployment rate, GDP, housing value and rent, and median income. It helps identify similar clusters across different regions.
	
	______________________________________
**Dashboard Features**
*Landing Page
	-Landing page describes the objective of the Dashboard.
*Census
	-Exploratory data analysis of the Census Data.
*Weather Impact
	-Analyze the impact of Weather on COVID-19 Cases and any correlations wrt to higher cases.
*COVID-19 Death Statistics
	-Statistics of Deaths vs Cases in the US States for 2020-2023.
*Forecast
	-Extension of the Death Statistics Tab, Along with correlations with Population and Death Forecast with a Timeseries model.
*Inbuilt Regression Model
	-Prediction of Deaths with the inbuilt Model (Decision Trees) wrt to the combined data and predictor columns.
*Covid Case Rate Prediction- Ensemble
	-Prediction of Covid Cases with an ensemble of Models.
*Clustering-Covid Cases
	-Creation of Clusters using K-Means and Hierarchial Clustering to view Demographics of COVID-19 Cases along with predictions.
