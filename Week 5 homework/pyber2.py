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

city_group = merged_df.groupby(["city"])
average_fare = city_group["fare"].mean()
rides_per_city = city_group["ride_id"].count()
drivers_per_city = city_group["driver_count"].mean()
city_data = city_data_df.set_index('city')['type']

summary_table_pyber = pd.DataFrame({"Number of Rides": rides_per_city,
                                    "Average Fare": average_fare,
                                    "Number of Drivers": drivers_per_city,
                                    "Type of City": city_data})
summary_table_pyber.head()

rural_df = summary_table_pyber[summary_table_pyber["Type of City"] == "Rural"]
suburban_df = summary_table_pyber[summary_table_pyber["Type of City"] == "Suburban"]
urban_df = summary_table_pyber[summary_table_pyber["Type of City"] == "Urban"]
citycolor = {"Urban":"lightcoral", "Suburban":"gold", "Rural":"lightblue" }

plt.grid()
plt.scatter(rural_df["Number of Rides"], rural_df["Average Fare"], s = rural_df["Number of Drivers"] * 15, color = citycolor["Rural"], edgecolor = "black")
plt.scatter(suburban_df["Number of Rides"], suburban_df["Average Fare"], s = suburban_df["Number of Drivers"] * 15, color = citycolor["Suburban"], edgecolor = "black")
plt.scatter(urban_df["Number of Rides"], urban_df["Average Fare"], s = urban_df["Number of Drivers"] * 15, color = citycolor["Urban"], edgecolor = "black")

plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (per city)")
plt.ylabel("Average Fare ($)")

legend = plt.legend(frameon = True)
legend.legendHandles[0]
legend.legendHandles[1]
legend.legendHandles[2]


plt.show()

city_pie = merged_df.groupby(["type"])
fares = city_pie["fare"].sum()
labels = fares.index
colors = [citycolor[n] for n in labels]
explode = [0, 0, .2]

plt.pie(fares, startangle = 90, colors = colors, labels = labels, explode = explode,  autopct="%1.1f%%", shadow = True)
plt.title("% of Total Fares by City Type")
plt.axis("equal")
plt.show()

rides = city_pie["ride_id"].count()
labels2 = rides.index
colors2 = [citycolor[n] for n in labels]
explode = [0, 0, .2]

plt.pie(rides, startangle = 90, colors = colors2, labels = labels2, explode = explode,  autopct="%1.1f%%", shadow = True)
plt.title("% of Total Rides by City Type")
plt.axis("equal")
plt.show()

drivers = city_pie["driver_count"].sum()
labels3 = drivers.index
colors3 = [citycolor[n] for n in labels]
explode = [0, 0, .4]

plt.pie(drivers, startangle = 90, colors = colors3, labels = labels3, explode = explode,  autopct="%1.1f%%", shadow = True)
plt.title("% of Drivers by City Type")
plt.axis("equal")
plt.show()
