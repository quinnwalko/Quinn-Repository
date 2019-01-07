from flask import Flask
app = Flask(__name__)

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

import pandas as pd
import numpy as np
import datetime

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

@app.route("/")
def home():
    print("Server received request for 'Home' page")
    return "Welcome to Your Friendly Neighborhood Weather API!"
  
@app.route("/welcome")
def welcome():
    return(
        f"Welcome to Your Friendly Neighborhood Weather API<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0<start>/<end><br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "08-23-2017").all()
    year_prcp = list(np.ravel(results))
    year_prcp = []
    for result in results:
        row = {}
        row[Measurement.date] = row[Measurement.prcp]
        year_prcp.append(row)
        
    return jsonify(year_prcp)

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    every_station = list(np.ravel(results))
    
    return jsonify(every_station)

@app.route("/api/v1.0/tobs")
def temperature():
    year_tobs = list(np.ravel(results))
    year_tobs = []
    results = session.query(Measurement.tobs).filter(Measurement.date >= "08-23-2017").all()
    
    return jsonify(year_tobs)
    
@app.route("/api/v1.0/<start>")
def start_trip_day(start_date):
    start_trip = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date == start_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date == start_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date == start_date).all()

    start_trip = list(np.ravel(results_min,results_max, results_avg))

    return jsonify(start_trip)

def temperature_start_date(start_date):

    start_trip_date_temperature = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    start_trip_date_temperature = list(np.ravel(results_min,results_max, results_avg))

    return jsonify(start_trip_date_temperature)

@app.route("/api/v1.0/<start>/<end>")

def start_finish_trip(start_date, end_date):

    start_end_trip_temperature = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date == start_date, Measurement.date == end_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date == start_date, Measurement.date == end_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date == start_date, Measurement.date == end_date).all()

    start_end_trip_temperature = list(np.ravel(results_min,results_max, results_avg))

    return jsonify(start_end_trip_temperature)

def start_finish_trip(start_date, end_date):

    round_trip_temperature = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date >= end_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date >= end_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date >= end_date).all()

    round_trip_temperature = list(np.ravel(results_min,results_max, results_avg))

    return jsonify(round_trip_temperature)

if __name__ == '__main__':
        app.run(debug=True)
  
  
