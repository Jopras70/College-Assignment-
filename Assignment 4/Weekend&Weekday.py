import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

"""
1.	Create a new factor variable in the dataset with two levels 
"weekday" and "weekend" indicating whether a given date is a weekday or weekend day.
2.	Make a plot containing a time series plot of the 5-minute interval (x-axis)
and the average number of steps taken, averaged across all weekdays or weekend days (y-axis).
"""

data = pd.read_csv("newActivity.csv")
data["steps"] = data["steps"].fillna(0) 
data["date"] = pd.to_datetime(data["date"])
data["number"] = data["date"].dt.dayofweek
data["type"] = np.where(data["number"] > 5, "Weekends", "Weekdays")
grp = data.groupby(['interval', 'type'])['steps'].mean()

pd.pivot_table(data.reset_index(), index='interval', columns='type', values='steps').plot(subplots=True)
plt.show()


