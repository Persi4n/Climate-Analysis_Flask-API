# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

# Create an engine to connect to your SQLite database.
engine = create_engine('sqlite:///hawaii.sqlite')

# Use automap_base to reflect the database tables into classes.
Base = automap_base()

# Reflect the tables into classes.
Base.prepare(engine, reflect=True)

# Save references to each table.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the DB.
session = Session(engine)

@app.route("/")
def home():
    return (
        "Welcome to the Climate App API!<br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start_date<br/>"
        "/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2017-08-23').all()
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').filter(Measurement.station == 'USC00519281').all()
    tobs_data = {date: tobs for date, tobs in results}
    return jsonify(tobs_data)

@app.route("/api/v1.0/<start>")
def start_date(start):
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    start_date_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(start_date_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    start_end_date_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(start_end_date_data)

if __name__ == "__main__":
    app.run(debug=True)
