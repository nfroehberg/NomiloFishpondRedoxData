import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('20190422_CalibrationData.csv')
pretty_analytes = {'Fe': 'Fe', 'Mn':'Mn', 'O2':'O$_2$', 'HS':'H$_2$S'}
pretty_conc = {'Fe': 'C$_{Fe}$', 'Mn':'C$_{Mn}$', 'O2':'C$_{O_2}$', 'HS':'C$_{H_2S}$'}


# NF04 Mn
df_cal = df.loc[(df.electrode == 'NF04') & (df.analyte== 'Mn') & (df.scan_rate == 1500)]
concentrations = df_cal.concentration_round.unique()

fig = plt.figure(figsize=(6.3,3.8))

x = np.array(df_cal.current).reshape((-1, 1))
y = np.array(df_cal.concentration_calc)
model = LinearRegression().fit(x,y)

r_sq = model.score(x, y)
intercept = model.intercept_
coef = model.coef_[0]

df_cal['regr_value'] = (df_cal.current * coef) + intercept
function = r'{}[µM] ='.format(pretty_conc['Mn'])+'\n'+'{:.2f} + {:.2f}*I[nA]'.format(intercept, coef)+'\n\n'+r'R$^2$ = {:.3f}'.format(r_sq)

ax1 = fig.add_axes([.6, .12, .38, .85]) #[left, bottom, width, height]
ax1.scatter(df_cal.current, df_cal.concentration_calc, marker = 'x', s = 70, c = 'red')
ax1.plot(df_cal.current, df_cal.regr_value, c = 'black', linestyle = '--')
# these are matplotlib.patch.Patch properties

props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)
ax1.text(0.05, 0.78, function, transform=ax1.transAxes, bbox=props)
ax1.set_xlabel('Current I [nA]')
ax1.set_ylabel('Concentration [µmol/l]')

ax2 = fig.add_axes([.1, .12, .38, .85]) #[left, bottom, width, height]

concentration_colors_Mn = {'25': 'darkorange','50': 'green', '100': 'blue', '200':'purple'}
concentration_linestyles_Mn = {'25': ':', '50': '-.', '100': '--', '200': '-'}

for concentration in concentrations:
    files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
    if len(files)>1:
      file = files[0]
      df_scan = pd.read_csv(file+'.csv')
      df_scan = df_scan[1:df_scan.potential.idxmin()+1]
      ax2.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration,
               c=concentration_colors_Mn[str(concentration)],
               linestyle = concentration_linestyles_Mn[str(concentration)])
plt.gca().invert_xaxis()
ax2.set_ylim(top = 180, bottom = 0)
ax2.set_xlim(right = -1700)
ax2.set_xlabel('Potential [mV] vs Ag/AgCl')
ax2.set_ylabel('Current [nA]')
ax2.legend(title = 'Manganese\n[µM]')

fig.savefig('ExampleCalMn.png', dpi = 300)
fig.clf()







# NF07 Fe
df_cal = df.loc[(df.electrode == 'NF07') & (df.analyte== 'Fe') & (df.scan_rate == 1500)]
concentrations = df_cal.concentration_round.unique()

fig = plt.figure(figsize=(6.3,3.8))

x = np.array(df_cal.current).reshape((-1, 1))
y = np.array(df_cal.concentration_calc)
model = LinearRegression().fit(x,y)

r_sq = model.score(x, y)
intercept = model.intercept_
coef = model.coef_[0]

df_cal['regr_value'] = (df_cal.current * coef) + intercept
function = r'{}[µM] ='.format(pretty_conc['Fe'])+'\n'+'{:.2f} + {:.2f}*I[nA]'.format(intercept, coef)+'\n\n'+r'R$^2$ = {:.3f}'.format(r_sq)

ax1 = fig.add_axes([.6, .12, .38, .85]) #[left, bottom, width, height]
ax1.scatter(df_cal.current, df_cal.concentration_calc, marker = 'x', s = 70, c = 'red')
ax1.plot(df_cal.current, df_cal.regr_value, c = 'black', linestyle = '--')
# these are matplotlib.patch.Patch properties

props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)
ax1.text(0.05, 0.78, function, transform=ax1.transAxes, bbox=props)
ax1.set_xlabel('Current I [nA]')
ax1.set_ylabel('Concentration [µmol/l]')

ax2 = fig.add_axes([.1, .12, .38, .85]) #[left, bottom, width, height]

concentration_colors_Fe = {'25': 'darkorange','50': 'green', '100': 'blue', '200':'purple', '300': 'cyan'}
concentration_linestyles_Fe = {'25': ':', '50': '-.', '100': '--', '200': '-', '300': (0, (10, 1,1,1,1,1,1,1))}

for concentration in concentrations:
    files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
    if len(files)>=1:
      file = files[0]
      df_scan = pd.read_csv(file+'.csv')
      df_scan = df_scan[1:df_scan.potential.idxmin()+1]
      ax2.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration,
               c=concentration_colors_Fe[str(concentration)],
               linestyle = concentration_linestyles_Fe[str(concentration)])
plt.gca().invert_xaxis()
ax2.set_ylim(top = 260, bottom = 10)
ax2.set_xlim(right = -1700)
ax2.set_xlabel('Potential [mV] vs Ag/AgCl')
ax2.set_ylabel('Current [nA]')
ax2.legend(title = 'Iron µM]')

fig.savefig('ExampleCalFe.png', dpi = 300)

fig.clf()









# NF07 H2S
df_cal = df.loc[(df.electrode == 'NF07') & (df.analyte== 'HS') & (df.scan_rate == 500)]
concentrations = df_cal.concentration_round.unique()

fig = plt.figure(figsize=(6.3,3.8))

x = np.array(df_cal.current).reshape((-1, 1))
y = np.array(df_cal.concentration_calc)
model = LinearRegression().fit(x,y)

r_sq = model.score(x, y)
intercept = model.intercept_
coef = model.coef_[0]

df_cal['regr_value'] = (df_cal.current * coef) + intercept
function = r'{}[µM] ='.format(pretty_conc['HS'])+'\n'+'{:.2f} + {:.2f}*I[nA]'.format(intercept, coef)+'\n\n'+r'R$^2$ = {:.3f}'.format(r_sq)

ax1 = fig.add_axes([.6, .12, .38, .85]) #[left, bottom, width, height]
ax1.scatter(df_cal.current, df_cal.concentration_calc, marker = 'x', s = 70, c = 'red')
ax1.plot(df_cal.current, df_cal.regr_value, c = 'black', linestyle = '--')
# these are matplotlib.patch.Patch properties

props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)
ax1.text(0.05, 0.78, function, transform=ax1.transAxes, bbox=props)
ax1.set_xlabel('Current I [nA]')
ax1.set_ylabel('Concentration [µmol/l]')

ax2 = fig.add_axes([.1, .12, .38, .85]) #[left, bottom, width, height]

concentration_colors_HS = {'10': 'darkorange','25': 'green', '50': 'blue', '100':'purple'}
concentration_linestyles_HS = {'10': ':', '25': '-.', '50': '--', '100': '-'}

for concentration in concentrations:
    files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
    if len(files)>=1:
      file = files[0]
      df_scan = pd.read_csv(file+'.csv')
      df_scan = df_scan[1:df_scan.potential.idxmin()+1]
      ax2.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration,
               c=concentration_colors_HS[str(concentration)],
               linestyle = concentration_linestyles_HS[str(concentration)])
plt.gca().invert_xaxis()
ax2.set_ylim(top = 290, bottom = -20)
ax2.set_xlim(right = -1700)

ax2.set_xlabel('Potential [mV] vs Ag/AgCl')
ax2.set_ylabel('Current [nA]')
ax2.legend(title = 'Sulphide\n[µM]')

fig.savefig('ExampleCalH2S.png', dpi = 300)

fig.clf()










# NF09 O2
df_cal = df.loc[(df.electrode == 'NF09') & (df.analyte== 'O2') & (df.scan_rate == 1500)]
concentrations = df_cal.concentration_round.unique()

fig = plt.figure(figsize=(6.3,3.8))

x = np.array(df_cal.current).reshape((-1, 1))
y = np.array(df_cal.concentration_calc)
model = LinearRegression().fit(x,y)

r_sq = model.score(x, y)
intercept = model.intercept_
coef = model.coef_[0]

df_cal['regr_value'] = (df_cal.current * coef) + intercept
function = r'{}[µM] ='.format(pretty_conc['O2'])+'\n'+'{:.2f} + {:.2f}*I[nA]'.format(intercept, coef)+'\n\n'+r'R$^2$ = {:.3f}'.format(r_sq)

ax1 = fig.add_axes([.6, .12, .38, .85]) #[left, bottom, width, height]
ax1.scatter(df_cal.current, df_cal.concentration_calc, marker = 'x', s = 70, c = 'red')
ax1.plot(df_cal.current, df_cal.regr_value, c = 'black', linestyle = '--')
# these are matplotlib.patch.Patch properties

props = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)
ax1.text(0.05, 0.78, function, transform=ax1.transAxes, bbox=props)
ax1.set_xlabel('Current I [nA]')
ax1.set_ylabel('Concentration [µmol/l]')

ax2 = fig.add_axes([.1, .12, .38, .85]) #[left, bottom, width, height]

concentration_colors_O2 = {'0': 'darkorange', '100':'purple'}
concentration_linestyles_O2 = {'0': '--', '100': '-'}
concentration_labels = {'0': 0, '100': 232.8}

for concentration in concentrations:
    files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
    if len(files)>=1:
      file = files[0]
      df_scan = pd.read_csv(file+'.csv')
      df_scan = df_scan[1:df_scan.potential.idxmin()+1]
      ax2.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration_labels[str(concentration)],
               c=concentration_colors_O2[str(concentration)],
               linestyle = concentration_linestyles_O2[str(concentration)])
plt.gca().invert_xaxis()
ax2.set_ylim(top = 178, bottom = 0)
ax2.set_xlim(right = -1800)

ax2.set_xlabel('Potential [mV] vs Ag/AgCl')
ax2.set_ylabel('Current [nA]')
ax2.legend(title = 'Oxygen\n[µM]')

fig.savefig('ExampleCalO2.png', dpi = 300)
fig.clf()
