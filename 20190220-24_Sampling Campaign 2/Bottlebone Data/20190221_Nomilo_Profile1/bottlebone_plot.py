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

variables = list(df.columns)
variables.remove('depth_m')
for i in range(len(variables)):
    p = (ggplot(df, aes(x=variables[i], y='depth_m', color='factor(station)')) +
         geom_path() +
         scale_y_reverse() +
         labs(color='Station'))
    p.save(filename = '{}/{}.png'.format(plot_dir, variables[i]), width = 3, height = 6, dpi = 300, units = 'in')



