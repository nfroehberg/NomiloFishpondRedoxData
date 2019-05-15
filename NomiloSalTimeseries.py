# TIme series of surface salinity at Nomilo fishpond south shore

import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
import datetime as dt

df = pd.read_csv('nomilo,node-105,sal.csv')
df = df.loc[df.sal>20]
dates=[dt.datetime.fromtimestamp(ts) for ts in df.ReceptionTime]
datenums=md.date2num(dates)

fig, ax = plt.subplots(1, figsize = (6.3, 3.15))
plt.xticks( rotation=25 )
plt.subplots_adjust(bottom=0.2)
ax.plot(datenums, df.sal.rolling(window=200).mean(), c = 'midnightblue')
xfmt = md.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(xfmt)
ax.set_ylabel('Salinity [psu]')
fig.savefig('NomiloSalTimeseries.png', dpi = 300)
plt.show()
