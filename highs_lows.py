import csv
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt


# Get dates and high temperatures from file.
filename = 'data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # if current_date.day == 1:
            #     xticks_months.append(current_date)
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot data.
fig = plt.figure(dpi=100, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # prevent overlapping
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#plt.xticks(xticks_months)
plt.margins(0) #matplotlib adds a 5% margin on all sides of the axes. To get rid of that margin we set it to 0.
plt.show()