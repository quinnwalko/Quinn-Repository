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
  
  
