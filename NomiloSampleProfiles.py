# Script by Nico Fröhberg (2019)
# nfroeh@hawaii.edu/nico.froehberg@gmx.de
# Plotting Carbonate Chemistry (Alkalinity/DIC), Inorganic Nutrient Concentrations, pH
# in samples from Nomilo Fishpond, Kaua'i

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

# data import
df = pd.read_csv('NomiloSamples.csv')

# Same aesthetics for all plots
stations = ['A22.1', 'A22.5', 'B12', 'B13', '0-1']
station_labels = ['2018\nAfternoon', '2018\nMorning', '2019\nMorning',
                  '2019\nAfternoon', 'Glazer\n2018']
station_colors = ['red', 'orange', 'blue', 'cyan', 'purple']
station_markers = ['o', '<', 'D', 'X', 's']
station_linestyles = [':', '-.', '--', '-', (0, (3,1,1,1,1,1,1,1))]

#########################################################################################
# Total N plot with legend and inset

# figure size defined to roughly the final size in the document
fig = plt.figure(figsize=(3.9,3.9))

# decreased width to make room for legend
ax = fig.add_axes([.12, .12, .48, .8]) #[left, bottom, width, height]

# adding a plot for every station
for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.plot(df_station['Total N'], df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
# inverted y-axis for water depth   
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')

ax.set_xlabel(r'N$_T$ [µmmol/l]')
plt.title('Total Nitrogen')

# legend located on the right side of plot vertically centered
# handlelength is longer to show different linestyles
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), handlelength = 4)

# defining what area should be zoomed for the inset by x and y (data coordinate) limits
x1, x2, y1, y2 = 25, 65, 0.1, 5.8
# inset size defined relative to plot size, in top right of canvas
axins = inset_axes(ax, width='50%', height='60%', loc=1)
axins.axis([x1, x2, y1, y2])

# adding same plot to inset
for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    axins.plot(df_station['Total N'], df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
# previously defined limits for zoomed area
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_yaxis()

# draw a box that shows the area that is shown in the inset on the main plot
# which corners are being connected needs to be defined manually because of the inverted y-axis
patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'green', fill = False)
# connect the left bottom and top corners
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

plt.savefig('Nomilo_TotalN.png', dpi = 300)
#plt.show()

#
# following plots are the same but some without inset/legend and accordingly adjusted size
#

#########################################################################################
# Ammonium plot without legend with inset

fig = plt.figure(figsize=(3.04,3.9))
ax = fig.add_axes([.15, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.plot(df_station.Ammonium, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel(r'NH$_4$$^+$ [µmmol/l]')
plt.title('Ammonium')

x1, x2, y1, y2 = -1, 22, 0.1, 5.8
axins = inset_axes(ax, width='50%', height='60%', loc=1)
axins.axis([x1, x2, y1, y2])

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    axins.plot(df_station.Ammonium, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)

axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_yaxis()

patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'green', fill = False)
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

plt.savefig('Nomilo_Ammonium.png', dpi = 300)
#plt.show()

#########################################################################################
#Phosphate plot without legend with inset

fig = plt.figure(figsize=(3.04,3.9))
ax = fig.add_axes([.15, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.plot(df_station.Phosphate, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel(r'PO$_4$$^3$$^-$ [µmol/l]')
plt.title('Phosphate')

x1, x2, y1, y2 = .1, .55, 0.1, 5.8
axins = inset_axes(ax, width='50%', height='60%', loc=1)
axins.axis([x1, x2, y1, y2])

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    axins.plot(df_station.Phosphate, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)

axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_yaxis()

patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'green', fill = False)
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

plt.savefig('Nomilo_Phosphate.png', dpi = 300)
#plt.show()

#########################################################################################
# Nitrate + Nitrite plot without legend without inset
fig = plt.figure(figsize=(1.7,3.9))
ax = fig.add_axes([.22, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station['N+N'], df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel(r'NO$_3$$^-$ + N0$_2$$^-$ [µmol/l]', fontsize = 8.5)
plt.title('Nitrate + Nitrite')
plt.tight_layout()
plt.savefig('Nomilo_N+N.png', dpi = 300)
#plt.show()

#########################################################################################
# pH plot without legend without inset
fig = plt.figure(figsize=(1.7,3.9))
ax = fig.add_axes([.22, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station['pH'], df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel(r'pH')
plt.title('pH')
plt.tight_layout()
plt.savefig('Nomilo_pH.png', dpi = 300)
#plt.show()

#########################################################################################
# Silicate plot without legend without inset
fig = plt.figure(figsize=(1.7,3.9))
ax = fig.add_axes([.22, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station.Silicate, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel(r'SiO$_4$$^2$$^-$ [µmol/l]')
plt.title('Silicate')
plt.tight_layout()
plt.savefig('Nomilo_Silicate.png', dpi = 300)
#plt.show()


#########################################################################################
# pH plot without legend without inset
fig = plt.figure(figsize=(2.2,3.9))
ax = fig.add_axes([.24, .12, .74, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station.pH, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel('pH')
plt.title('Acidity')
plt.tight_layout()
plt.savefig('Nomilo_pH.png', dpi = 300)
#plt.show()

#########################################################################################
# alkalinity plot without legend with inset

fig = plt.figure(figsize=(3.04,3.9))
ax = fig.add_axes([.15, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station.TA, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label, xerr = df_station.TAsd*2, capsize=5)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel(r'A$_T$ [µmmol/kg]')
plt.title('Total Alkalinity')

x1, x2, y1, y2 = 2600, 3350, 0.1, 5.8
axins = inset_axes(ax, width='50%', height='60%', loc=1)
axins.axis([x1, x2, y1, y2])

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    axins.errorbar(df_station.TA, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label, xerr = df_station.TAsd*2, capsize=5)

axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_yaxis()

patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'green', fill = False)
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

plt.savefig('Nomilo_Alkalinity.png', dpi = 300)
#plt.show()

#########################################################################################
# DIC plot with inset and legend

fig = plt.figure(figsize=(3.9,3.9))
ax = fig.add_axes([.12, .12, .48, .8]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    if station == '0-1':
        station_label = '_nolegend_'
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station.DIC, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label, xerr = df_station.DICsd*2, capsize=5)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel('DIC [µmmol/kg]')
plt.title('Dissolved Inorganic Carbon')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), handlelength = 4, ncol=2)

x1, x2, y1, y2 = 2300, 2920, 0.1, 5.8
axins = inset_axes(ax, width='50%', height='60%', loc=1)
axins.axis([x1, x2, y1, y2])

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    axins.errorbar(df_station.DIC, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label, xerr = df_station.DICsd*2, capsize=5)

axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_yaxis()

patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'green', fill = False)
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

plt.savefig('Nomilo_DIC.png', dpi = 300)
#plt.show()


#########################################################################################
# DIC plot with inset without legend

fig = plt.figure(figsize=(3.04,3.9))
ax = fig.add_axes([.15, .12, .76, .81]) #[left, bottom, width, height]

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    if station == '0-1':
        station_label = '_nolegend_'
    df_station = df.loc[df.Station == station]
    ax.errorbar(df_station.DIC, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label, xerr = df_station.DICsd*2, capsize=5)
ax.set_ylim(bottom=0)
plt.gca().invert_yaxis()
ax.set_ylabel('Depth [m]')
ax.set_xlabel('DIC [µmmol/kg]')
plt.title('Dissolved Inorganic Carbon')
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), handlelength = 4)

x1, x2, y1, y2 = 2300, 2920, 0.1, 5.8
axins = inset_axes(ax, width='50%', height='60%', loc=1)
axins.axis([x1, x2, y1, y2])

for j in range(len(stations)):
    station = stations[j]
    station_label = station_labels[j]
    df_station = df.loc[df.Station == station]
    axins.errorbar(df_station.DIC, df_station.Depth, marker = station_markers[j],
                color = station_colors[j], linestyle = station_linestyles[j],
                label = station_label, xerr = df_station.DICsd*2, capsize=5)

axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.gca().invert_yaxis()

patch, pp1,pp2 = mark_inset(ax, axins, loc1=1,loc2=1, color = 'green', fill = False)
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

plt.savefig('Nomilo_DIC_noLegend.png', dpi = 300)
#plt.show()
