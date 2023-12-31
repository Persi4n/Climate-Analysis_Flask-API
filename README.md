# Honolulu Climate Analysis

## Overview

The Honolulu Climate Analysis project is a data-driven exploration of the climate in Honolulu, Hawaii. It leverages Python, SQLAlchemy, and Flask to analyze historical weather data, provide insights, and offer access to the analysis results through a web API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Exploratory Analysis](#exploratory-analysis)
- [Flask API](#flask-api)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Located in the tropical paradise of Hawaii, Honolulu experiences diverse weather patterns throughout the year. This project dives into the climate data to answer questions about precipitation, temperature trends, and station information. Whether you're planning a vacation or conducting climate research, this project provides valuable insights.

## Features

### 1. Precipitation Analysis

- Find the most recent date in the dataset.
- Calculate the previous 12 months of precipitation data.
- View summary statistics for precipitation.
- Visualize precipitation data over time.

### 2. Station Analysis

- Determine the total number of weather stations.
- Identify the most active weather stations.
- Retrieve temperature statistics for the most active station.
- Access the last 12 months of temperature observations for the most active station.

### 3. Flask API

- Explore climate data through API endpoints.
- Retrieve JSON data for precipitation, stations, temperature, and statistics.
- Query temperature statistics for specific date ranges.

## Requirements

To run this project, you will need the following:

- Python 3.x
- Jupyter Notebook
- SQLAlchemy
- Flask
- Matplotlib
- pandas
- datetime

## Installation

1. Clone the project repository:
git clone <repository-url>


2. Install the required Python packages:
pip install -r requirements.txt


3. Ensure you have the SQLite database file (`hawaii.sqlite`) and the CSV data files (`hawaii_measurements.csv` and `hawaii_stations.csv`) in the correct locations.

## Usage

### Exploratory Analysis

1. Open the Jupyter Notebook file `climate_starter.ipynb`.
2. Run each cell in the notebook to perform the exploratory analysis of climate data, including precipitation analysis, station analysis, and temperature analysis.

### Flask API

1. Open the `app.py` file.
2. Run the Flask application to start the API server:
3. Access the API routes as described in the [API Routes](#api-routes) section.

## API Routes

- `/api/v1.0/precipitation`: Returns JSON representation of precipitation data for the last 12 months.
- `/api/v1.0/stations`: Returns JSON representation of all weather stations.
- `/api/v1.0/tobs`: Returns JSON representation of temperature observations for the most active station for the last 12 months.
- `/api/v1.0/<start>`: Returns JSON representation of temperature statistics for a specified start date.
- `/api/v1.0/<start>/<end>`: Returns JSON representation of temperature statistics for a specified date range.


