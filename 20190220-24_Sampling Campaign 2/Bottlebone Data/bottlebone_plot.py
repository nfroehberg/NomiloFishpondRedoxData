from plotnine import *
from plotnine.data import *
import pandas as pd
import os
file = "bottlebone_merged_stations.csv"
df = pd.read_csv(file)
df = df.dropna()
df.station = df.station.astype(int)

plot_dir = 'profile-plots'
if not os.path.isdir(plot_dir):
    os.mkdir(plot_dir)

labels = {'AirSaturation':'Oxygen [% air sat.]', 'Chlorophyll':'Chlorophyll [µg/l]',
          'Conductivity':'Conductivity [mS/cm]', 'Density':'Density [kg/m^3]',
          'O2Concentration': 'Oxygen [µmol/l]', 'Salinity': 'Salinity [psu]',
          'Temperature':'Temperature [°C]', 'Turbidity':'Turbidity [ntu]'}

variables = list(df.columns)
dump = ['depth_m', 'SN', 'SN_bottlebone.optode', 'station', 'Thermistor','dt',
        'date', 'time']
for element in dump:
    variables.remove(element)
for i in range(len(variables)):
    if variables[i] in labels.keys():
        label = labels[variables[i]]
    else:
        label = variables[i]
    p = (ggplot(df, aes(x=variables[i], y='depth_m', color='factor(station)')) +
         geom_path() +
         scale_y_reverse() +
         labs(color='Station', x = label, y = 'Depth [m]'))
    p.save(filename = '{}/{}.png'.format(plot_dir, variables[i]), width = 3, height = 6, dpi = 300, units = 'in')



