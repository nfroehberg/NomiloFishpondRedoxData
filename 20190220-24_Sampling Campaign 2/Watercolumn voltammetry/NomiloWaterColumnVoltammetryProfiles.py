import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from scipy.signal import savgol_filter

# data import
df_volt_1 = pd.read_csv('20190222_watercolumn-voltammetry_NF18-2-data.csv')
df_volt_1 = df_volt_1.dropna(subset=['h2s_conc'])
df_volt_2 = pd.read_csv('20190223_watercolumn-voltammetry_NF07-data.csv')
df_volt_2 = df_volt_2.dropna(subset=['h2s_conc'])
df_volt_2_FeS = pd.read_csv('20190223_watercolumn-voltammetry_NF07-data.csv')
df_volt_2_FeS = df_volt_2_FeS.dropna(subset=['FeS_current'])
df_volt_o2_1 = pd.read_csv('20190222_watercolumn-voltammetry_NF18-2-data_O2binned.csv')
df_volt_o2_1 = df_volt_o2_1.dropna(subset=['mean_oxygen_conc'])
df_volt_o2_2 = pd.read_csv('20190223_watercolumn-voltammetry_NF07-data_O2binned.csv')
df_volt_o2_2 = df_volt_o2_2.dropna(subset=['mean_oxygen_conc'])
df_bottlebone = pd.read_csv('bottlebone_merged_stations.csv')

station_1 = 11
station_2 = 12
df_station_1 = df_bottlebone.loc[df_bottlebone.station == station_1]
df_station_2 = df_bottlebone.loc[df_bottlebone.station == station_2]

###########################################################################
# Bottlebone Plots
# Plotting all standard biogeochemical parameters to accompany voltammetric data

parameters = ['Temperature', 'Salinity', 'Chlorophyll_calibrated', 'Turbidity_calibrated']
labels = {'Temperature':'Temperature [°C]', 'Salinity':'Salinity [psu]',
          'Chlorophyll_calibrated':'Chlorophyll a [µg/l]', 'Turbidity_calibrated':'Turbidity [ntu]'}
colors = {'Temperature':('red','orange'), 'Salinity':('purple','magenta'),
          'Chlorophyll_calibrated':('green','lime'), 'Turbidity_calibrated':('maroon','chocolate')}

for parameter in parameters:
    fig = plt.figure(figsize=(2.8,4.3))
    ax = fig.add_axes([.2, .12, .75, .85])  #[left, bottom, width, height]

    # two stations:
    plt.plot(savgol_filter(df_station_1[parameter], 99, 3), df_station_1.depth_m, color = colors[parameter][0],
             label = 'Station {}'.format(station_1))
    plt.plot(savgol_filter(df_station_2[parameter], 99, 3), df_station_2.depth_m, color = colors[parameter][1],
             label = 'Station {}'.format(station_2), linestyle = '--')
    plt.gca().invert_yaxis()
    plt.xlabel(labels[parameter])
    plt.ylabel('Depth [m]')
    plt.legend()
    plt.savefig('Nomilo_WatercolumnVoltammetry_{}.png'.format(parameter), dpi = 300)

###########################################################################
# Oxygen (Voltammetric and Optode) plot plus inset for sulphide in bottom water
# First Station


from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
h2s_color = 'darkorange'

fig = plt.figure(figsize=(6,4.3))

# host axis for oxygen plot
host = HostAxes(fig, [.06, .12, .375, .75])  #[left, bottom, width, height]

# parasite axis for sulphide plot
par1 = ParasiteAxes(host, sharey=host)
host.parasites.append(par1)
fig.add_axes(host)

host.axis["top"].set_visible(False)
par1.axis["top"].set_visible(True)
par1.set_xlabel(r"H$_2$S [µmol/l]")
par1.axis["top"].major_ticklabels.set_visible(True)
par1.axis["top"].label.set_visible(True)
par1.axis["top"].label.set_color(h2s_color)
par1.axis["top"].major_ticklabels.set_color(h2s_color)
par1.axis["top"].major_ticks.set_color(h2s_color)

# oxygen plots
host.plot(savgol_filter(df_station_1['O2Concentration'], 99, 3), df_station_1.depth_m,
         color = 'midnightblue', label = 'Oxygen (Optode)')
host.errorbar(df_volt_o2_1.mean_oxygen_conc, df_volt_o2_1.mean_depth, marker = '.', capsize = 5,
             xerr = (2*df_volt_o2_1.sd_oxygen_conc), color = 'turquoise', linestyle = ':', fmt = '.-',
             label = 'Oxygen (Voltammetry)')
plt.ylabel('Depth [m]')
plt.xlabel(r"O$_2$ [µmol/l]")

# sulphide plot (invisible, plotted again later to be above the inset marker box)
par1.scatter(df_volt_1.h2s_conc, df_volt_1.depth, visible = False, label = '_nolegend_')
par1.set_xlim(-60,880)

plt.gca().invert_yaxis()

# coordinates of area to zoom for inset
x1, x2, y1, y2 = -40, 840, 6.1, 6.92
# inset size defined relative to plot size, in top right of canvas
axins = inset_axes(par1, width = 2.5, height = 2.4, bbox_to_anchor = (1.15, -.02),
                   bbox_transform = par1.transAxes, loc = 'lower left')
axins.axis([x1, x2, y1, y2])
axins.scatter(df_volt_1.h2s_conc, df_volt_1.depth, color = h2s_color, 
             label = 'Sulphide (Voltammetry)', marker = 'D')
# previously defined limits for zoomed area
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

# aesthetics of inset axes
axins.axis["bottom"].major_ticklabels.set_visible(False)
axins.axis["bottom"].major_ticks.set_visible(False)
axins.axis["left"].major_ticklabels.set_visible(False)
axins.axis["left"].major_ticks.set_visible(False)
axins.axis["top"].set_visible(True)
axins.axis["right"].set_visible(True)
axins.axis["top"].major_ticklabels.set_color(h2s_color)
axins.axis["top"].major_ticks.set_color(h2s_color)

plt.gca().invert_yaxis()

# draw a box that shows the area that is shown in the inset on the main plot
# which corners are being connected needs to be defined manually because of the inverted y-axis
patch, pp1,pp2 = mark_inset(par1, axins, loc1=1,loc2=1, color = 'green', fill = False)
# connect the left bottom and top corners
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

# sulphide plot above inset marker box
par1.scatter(df_volt_1.h2s_conc, df_volt_1.depth, color = h2s_color,
             label = '_nolegend_', marker = 'D', s = 8)

fig.legend(handlelength = 3, title = 'Station {}'.format(station_1), loc = 'lower left',
           bbox_to_anchor = (.53, .75))
fig.savefig('Nomilo_WatercolumnVoltammetry_Oxygen1.png', dpi = 300)
#plt.show()

###########################################################################
# Oxygen (Voltammetric and Optode) plot plus inset for sulphide and FeS in bottom water
# Second Station

from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
h2s_color = 'darkorange'

fig = plt.figure(figsize=(6,4.3))

# host axis for oxygen plot
host = HostAxes(fig, [.06, .12, .375, .75])  #[left, bottom, width, height]

# parasite axis for sulphide plot
par1 = ParasiteAxes(host, sharey=host)
host.parasites.append(par1)
fig.add_axes(host)

host.axis["top"].set_visible(False)
par1.axis["top"].set_visible(True)
par1.set_xlabel(r"H$_2$S [µmol/l]")
par1.axis["top"].major_ticklabels.set_visible(True)
par1.axis["top"].label.set_visible(True)
par1.axis["top"].label.set_color(h2s_color)
par1.axis["top"].major_ticklabels.set_color(h2s_color)
par1.axis["top"].major_ticks.set_color(h2s_color)

# oxygen plots
host.plot(savgol_filter(df_station_2['O2Concentration'], 99, 3), df_station_2.depth_m,
         color = 'midnightblue', label = 'Oxygen (Optode)')
host.errorbar(df_volt_o2_2.mean_oxygen_conc, df_volt_o2_2.mean_depth, marker = '.', capsize = 5,
             xerr = (2*df_volt_o2_2.sd_oxygen_conc), color = 'turquoise', linestyle = ':', fmt = '.-',
             label = 'Oxygen (Voltammetry)')
plt.ylabel('Depth [m]')
plt.xlabel(r"O$_2$ [µmol/l]")

# sulphide plot (invisible, plotted again later to be above the inset marker box)
par1.scatter(df_volt_2.h2s_conc, df_volt_2.depth, visible = False, label = '_nolegend_')
par1.set_xlim(-30,350)

plt.gca().invert_yaxis()

# coordinates of area to zoom for inset
x1, x2, y1, y2 = -20, 340, 6.42, 6.68
# inset size defined relative to plot size, in top right of canvas
axins = inset_axes(par1, width = 2.5, height = 2.15, bbox_to_anchor = (1.15, -.02),
                   bbox_transform = par1.transAxes, loc = 'lower left')
axins.axis([x1, x2, y1, y2])
axins.scatter(df_volt_2.h2s_conc, df_volt_2.depth, color = h2s_color, 
             label = 'Sulphide (Voltammetry)', marker = 'D')

# previously defined limits for zoomed area
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

# aesthetics of inset axes
axins.axis["bottom"].major_ticklabels.set_visible(False)
axins.axis["bottom"].major_ticks.set_visible(False)
axins.axis["left"].major_ticklabels.set_visible(False)
axins.axis["left"].major_ticks.set_visible(False)
axins.axis["top"].set_visible(True)
axins.axis["right"].set_visible(True)
axins.axis["top"].major_ticklabels.set_color(h2s_color)
axins.axis["top"].major_ticks.set_color(h2s_color)

plt.gca().invert_yaxis()

# adding FeS plot to inset, can't easily parasitize the inset axis so manually tweaked
# another axis to cover the same area with transparent background
FeS_color = 'indigo'
axFeS = fig.add_axes((.503, 0.12, .4166666666666666666666667, .5),sharey = axins)
axFeS.set_facecolor("None")
axFeS.yaxis.set_visible(False)
axFeS.tick_params(axis='x', colors=FeS_color)
axFeS.xaxis.label.set_color(FeS_color)
axFeS.scatter(df_volt_2_FeS.FeS_current, df_volt_2_FeS.depth, color = FeS_color,
              label = 'FeS (Voltammetry)', marker = '^')
axFeS.set_xlabel('FeS current [nA]')
axFeS.set_xlim(-.5,7)

# draw a box that shows the area that is shown in the inset on the main plot
# which corners are being connected needs to be defined manually because of the inverted y-axis
patch, pp1,pp2 = mark_inset(par1, axins, loc1=1,loc2=1, color = 'green', fill = False)
# connect the left bottom and top corners
pp1.loc1 = 2
pp1.loc2 = 3
pp2.loc1 = 3
pp2.loc2 = 2

# sulphide plot above inset marker box
par1.scatter(df_volt_2.h2s_conc, df_volt_2.depth, color = h2s_color,
             label = '_nolegend_', marker = 'D', s = 8)

fig.legend(handlelength = 3, title = 'Station {}'.format(station_2), loc = 'lower left',
           bbox_to_anchor = (.53, .7))
fig.savefig('Nomilo_WatercolumnVoltammetry_Oxygen2.png', dpi = 300)
#plt.show()
