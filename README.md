# Honolulu Climate Analysis

This project performs a climate analysis of Honolulu, Hawaii, using Python, SQLAlchemy, and Flask. It includes an exploratory analysis of climate data and the creation of a Flask API to access the analysis results.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Exploratory Analysis](#exploratory-analysis)
- [Flask API](#flask-api)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Honolulu Climate Analysis is a project that aims to provide insights into the climate data of Honolulu, Hawaii. It includes both data exploration and the creation of a Flask API to access the analysis results.

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


