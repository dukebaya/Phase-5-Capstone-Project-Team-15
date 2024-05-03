Leveraging Machine Learning to Combat Bushmeat Poaching and Illegal Logging in Arabuko-Sokoke Forest Reserve, Kenya

Welcome to the Forecasting Illegal Activities in Arabuko-Sokoke Forest repository! This project aims to provide actionable insights to guide conservation interventions and law enforcement strategies by forecasting future illegal activities in the Arabuko-Sokoke Forest (ASF).

Repository Contents

1.	Jupyter Notebook (Illegal_Activities_Analysis.ipynb):
•	This notebook contains a comprehensive analysis of illegal activities data in ASF, including data preprocessing, exploratory data analysis, time series analysis and modelling, and evaluation.
2.	README.md:
•	This file provides an overview of the repository and instructions for running the code. It also includes information about the project structure, usage guide, references, and contributors.

Introduction

The Arabuko-Sokoke Forest (ASF), a UNESCO Man and Biosphere Reserve and a crucial biodiversity hotspot, faces persistent threats from illegal poaching and logging. These activities are primarily driven by the high demand for forest products from nearby urban centers such as Malindi, Watamu, Kilifi, and Mombasa, as well as the presence of over 200,000 people living at the forest boundary. These threats endanger the integrity of the forest ecosystem, its biodiversity, and the livelihoods of local communities dependent on its resources. Effective strategies are needed to combat illegal utilization of forest resources and safeguard the ecological and socio-economic value of ASF.

General Objectives

•	To provide actionable insights to guide conservation interventions and law enforcement strategies with historical law-enforcement and biodiversity monitoring data.

•	To develop forecasting models to forecast future illegal activities in the forest reserve and support proactive conservation efforts.

 
Business and Data Understanding

Business Problem: Providing actionable insights to guide conservation interventions and law enforcement strategies by forecasting future illegal activities in the Arabuko-Sokoke Forest (ASF).

Implementation Overview:

1.	Data Preparation:
•	We used a dataset from a survey carried out by Arabuko-Sokoke Forest (ASF).
•	We parsed waypoint dates, dropped unnecessary columns and rows, created a function which categorized entries into poaching and logging, and renamed this new entry as illegal activities. We also filled missing values, took care of duplicates, and reset waypoint date as the index.

2.	Exploratory Data Analysis (EDA):
•	The dataset was explored visualizing illegal activities over time. Temporal and seasonal analysis was carried out identifying trends and seasonality. Augmented Dickey-Fuller Test was employed which confirmed non-stationarity, differencing technique was applied before modeling.

3.	Time Series Modeling:
•	Time series component was decomposed, auto-correlation, and partial auto-correlation function were analyzed.
•	Three Models were used: ARIMA, VAR, and XGBoost which were fitted and also used for forecasting.

4.	Feature Engineering and Modeling:
•	Time series features were created, visualizing relationships between features and illegal activities, combining logging and poaching into a single target variable, training XGBoost regressor models, feature importance was also analyzed.

5.	Forecasting and Testing:
•	Illegal activities were forecasted using trained models, forecasted values were against actual data, and model performance was evaluated using RMSE scores.
 

Future Directions
1.	Refinement of Machine Learning Models: Further tuning of hyperparameters and exploration of additional algorithms to improve model performance.
2.	Integration of External Data: Incorporation of external datasets (e.g., weather data, socio-economic indicators) to enhance predictive capabilities.
3.	Real-Time Monitoring System: Development of a real-time monitoring system for early detection and prevention of illegal activities in ASF.
4.	Stakeholder Engagement: Collaboration with conservation organizations, law enforcement agencies, and local communities to implement and validate predictive models in practice.

Instructions
1.	Clone the repository to your local machine.
2.	Open the Jupyter Notebook (Illegal_Activities_Analysis.ipynb) using Jupyter Notebook or JupyterLab.
3.	Ensure that the necessary libraries (e.g., pandas, numpy, seaborn, statsmodels, xgboost) are installed.
4.	Run each cell in the notebook sequentially to reproduce the analysis and results.


Recommendations

Based on the analysis of historical data from 2018 to 2024, it is evident that illegal activities in the Arabuko-Sokoke Forest have shown a positive trend, with an increasing number of incidents over time. To address this concerning trend, it is recommended to focus on enhancing the predictive models developed using time series analysis techniques.

Given the positive trend observed in illegal activities, it becomes imperative to refine and optimize the predictive models to better forecast future occurrences of illegal logging and poaching. This can be achieved by incorporating more granular data, such as seasonal variations, spatial dynamics, and socio-economic factors influencing illegal activities.

Additionally, the use of ensemble techniques, which combine the strengths of multiple algorithms such as ARIMA, VAR, and XGBoost, could further improve the accuracy and robustness of the predictive models. Ensemble methods can effectively mitigate the weaknesses of individual algorithms and provide more reliable forecasts.

Furthermore, continuous monitoring and evaluation of the predictive models' performance, using metrics such as Root Mean Squared Error (RMSE), should be undertaken to ensure their effectiveness in guiding conservation interventions and law enforcement strategies.

By refining the predictive models and enhancing their accuracy in forecasting illegal activities, stakeholders can proactively implement targeted conservation strategies and allocate resources more efficiently to mitigate the threats posed to the Arabuko-Sokoke Forest ecosystem and support the livelihoods of local communities

Conclusions

The integration of machine learning techniques into conservation planning and management offers a promising approach to combat illegal activities threatening the Arabuko-Sokoke Forest. By harnessing the power of predictive analytics, stakeholders can work towards a sustainable future for ASF, preserving its biodiversity and ecosystem services for generations to come