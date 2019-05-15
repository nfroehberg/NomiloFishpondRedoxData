# Plots of carbonate speciation at Nomilo fishpond

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Data
df_raw = pd.read_csv('Carbonate.csv')

stations = ['2018 Afternoon','2018 Morning']
labels = [r'HCO$_3^-$', r'CO$_3^=$', r'CO$_2$']
hatches = ['//','\\\\','||']


for station in stations:
    fig = plt.figure(figsize=(2.2,3.9))
    ax = fig.add_axes([.24, .12, .7, .81]) #[left, bottom, width, height]
    df = df_raw.loc[df_raw.profile == station]
    depth = df.depth
    df = df[['HCO3rel','CO3rel','CO2rel']]
    data = np.cumsum(df.values, axis=1)
    for i, col in enumerate(df.columns):
        ax.fill_betweenx(depth, data[:,i], label=labels[i], zorder=-i, hatch = hatches[i])
    ax.set_xlim(70,100)
    ax.set_ylabel('Depth [m]')
    ax.set_xlabel('Relative Contr. [%]')
    plt.gca().invert_yaxis()
    fig.suptitle(station)
    ax.margins(y=0)
    ax.set_axisbelow(False)

    ax.legend(loc='upper left')

    fig.savefig('Carbonate_Relative_{}.png'.format(station), dpi = 300)


