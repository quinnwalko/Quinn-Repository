%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

file = "city_data.csv"
file2 = "ride_data.csv"

city_data_df = pd.read_csv(file)
city_data_df = city_data_df.drop_duplicates("city", keep = "first")
ride_data_df = pd.read_csv(file2)
merged_df = city_data_df.merge(ride_data_df, on = "city")
