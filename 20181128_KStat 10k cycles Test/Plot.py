# Script for plotting data of KStat stability test (10k cycles over dummy cell)
# with colorbar for showing scan number and inset to show extent of vertical variability
# Nico Fröhberg 2019
# nfroeh@hawaii.edu/nico.froehberg@gmx.de

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

# reduce n_lines for testing purposes to decrease computing time, 10000 for full data set
n_lines = 10000

# generating colormap for number of lines
c = np.arange(1, n_lines + 1)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.viridis_r)
cmap.set_array([])

# read data and set up figure
df = pd.read_csv('KStat_10kTest.csv')
fig = plt.figure(figsize=(6.3,3.15))
ax = fig.add_axes([.1, .14, .4, .85]) #[left, bottom, width, height]

# add one line for every scan
for i in range(n_lines):
    df_scan=df.loc[df.scan==i]
    lines = ax.plot(df_scan.potential, df_scan.current*-1000000000, c=cmap.to_rgba(i + 1))
    if i % 100 == 0:
        print(i)
plt.gca().invert_xaxis()
ax.set_xlabel('Potential vs Ag/AgCl [mV]')
ax.set_ylabel('Current [nA]')

#define bounds of inset
x1, x2, y1, y2 = -1424.45, -1423.05, 140.001, 140.149
axins = inset_axes(ax, width=2, height=2, bbox_to_anchor = (1.15, -.02),
                   bbox_transform = ax.transAxes, loc = 'lower left')
axins.axis([x1, x2, y1, y2])

#add lines to inset
for i in range(n_lines):
    df_scan=df.loc[df.scan==i]
    lines = axins.plot(df_scan.potential, df_scan.current*-1000000000, c=cmap.to_rgba(i + 1))
    if i % 100 == 0:
        print(i)

# inset y-axis on the right instead of the left
axins.axis["left"].major_ticklabels.set_visible(False)
axins.axis["left"].major_ticks.set_visible(False)
axins.axis['right'].set_visible(True) 
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_xaxis()

# draw a box that shows the area that is shown in the inset on the main plot
# which corners are being connected needs to be defined manually because of the inverted y-axis
patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'red', fill = False)
# connect the left bottom and top corners
pp1.loc1 = 3
pp1.loc2 = 1
pp2.loc1 = 1
pp2.loc2 = 1

# create separate axes to control position and add colorbar
cbaxes = fig.add_axes([0.55, 0.85, 0.4, 0.08]) 
cb = plt.colorbar(cmap, cax = cbaxes, orientation = 'horizontal')
cb.ax.set_title('Scan Number')

# save file
fig.savefig('KStat_10kTest.png', dpi = 300)
plt.show()
