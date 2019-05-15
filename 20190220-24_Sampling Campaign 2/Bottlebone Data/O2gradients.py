import pandas as pd
import matplotlib.pyplot as plt

station = 1
df = pd.read_csv('bottlebone_merged_stations.csv')
for i in range(1,14):
    df_plot = df.loc[df.station == i]
    plt.plot(df_plot.O2Concentration, df_plot.depth_m)
    plt.title(str(i))
    plt.gca().invert_yaxis()
    plt.show()

