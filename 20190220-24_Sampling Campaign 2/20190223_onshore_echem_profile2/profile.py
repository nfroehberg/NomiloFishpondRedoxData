#https://matplotlib.org/gallery/axisartist/demo_parasite_axes.html

from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import matplotlib.pyplot as plt
import pandas as pd

o2_color = 'blue'
o2_color_bottle = 'cyan'
t_color = 'red'
h2s_color = 'green'

fig = plt.figure(1, figsize=(2.5,5))
host = HostAxes(fig, [0.23, 0.08, 0.7, 0.83]) #[left, bottom, width, height]
par1 = ParasiteAxes(host, sharey=host)

host.parasites.append(par1)



host.axis["top"].set_visible(True)
host.axis["bottom"].set_visible(False)
par1.axis["top"].set_visible(False)
par1.axis["bottom"].set_visible(True)

par1.axis["bottom"].major_ticklabels.set_visible(True)
par1.axis["bottom"].label.set_visible(True)
host.axis["top"].major_ticklabels.set_visible(True)
host.axis["top"].label.set_visible(True)

fig.add_axes(host)

host.set_ylabel("Distance from Sediment Water Interface [mm]")
host.set_xlabel("O$_2$ [µmol/l]")
par1.set_xlabel("H$_2$S [µmol/l]")

df = pd.read_csv('profile_data.csv')

p1, = host.plot(df['oxygen_conc'], df['location'], '.-', color = o2_color,
                label = 'Oxygen', marker = 'o')
p2, = par1.plot(df['h2s_conc'], df['location'],'.-', label='Sulphide',
                color = h2s_color, marker = '>', linestyle = ':')
host.axhline(color = 'black', linestyle = '--')

host.legend(loc='upper center', bbox_to_anchor=(0.5, 0.9))
#host.legend()

host.axis["top"].label.set_color(o2_color)
host.axis["top"].major_ticklabels.set_color(o2_color)
host.axis["top"].major_ticks.set_color(o2_color)
host.axis["top"].line.set_color(o2_color)
par1.axis["bottom"].label.set_color(h2s_color)
par1.axis["bottom"].major_ticklabels.set_color(h2s_color)
par1.axis["bottom"].major_ticks.set_color(h2s_color)
par1.axis["bottom"].line.set_color(h2s_color)

#plt.title('20190223_Nomilo_On-Shore_Profile 2', y=1.1)
fig.savefig('20190223_Nomilo_On-Shore_Profile 2.png', dpi = 300)

plt.show()
