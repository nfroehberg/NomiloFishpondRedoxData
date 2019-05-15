# Plot of solid phase iron by dithionite extraction at Nomilo fihspond and Wai Kai lagoon

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Nomilo_Haseko_Sediment_Fe_Dithionite.csv', skiprows =  [1])

fig = plt.figure(1, figsize=(2.5,5))
ax = fig.add_axes([0.28, 0.1, 0.7, 0.85]) #[left, bottom, width, height]
profiles = ['N-A','N-B','WK-1']
colors = {'N-A': 'navy','N-B': 'royalblue','WK-1': 'darkviolet'}
markers = {'N-A': 'v','N-B': 'o','WK-1': 's'}
linestyles = {'N-A': '-','N-B': '--','WK-1': ':'}
labels = {'N-A': 'Nomilo 5 m','N-B': 'Nomilo\n3.5 m','WK-1': 'Wai Kai\nSite 1'}
for profile in profiles:
    df_profile = df.loc[df.Core == profile]
    ax.plot(df_profile.Fe, df_profile['core depth']*-1, c = colors[profile],
            marker = markers[profile], linestyle = linestyles[profile],
            label = labels[profile])

ax.set_ylabel('Distance from Sediment Water Interface [mm]')
ax.set_xlabel('Solid Phase Fe [µmol/g]')
ax.legend(handlelength = 3)
fig.savefig('Nomilo_Haseko_Sediment_Fe_Dithionite.png', dpi=300)
plt.show()
