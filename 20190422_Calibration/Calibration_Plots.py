import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv('20190422_CalibrationData.csv')

electrodes = df.electrode.unique()
analytes = df.analyte.unique()
scan_rates = df.scan_rate.unique()
pretty_analytes = {'Fe': 'Fe', 'Mn':'Mn', 'O2':'O$_2$', 'HS':'H$_2$S'}
pretty_conc = {'Fe': 'C$_{Fe}$', 'Mn':'C$_{Mn}$', 'O2':'C$_{O_2}$', 'HS':'C$_{H_2S}$'}

output_electrode = []
output_analyte = []
output_scan_rate = []
output_intercept = []
output_slope = []
output_r_sq = []

fig = plt.figure(figsize=(8,8.2))
for electrode in electrodes:
  for analyte in analytes:
    for scan_rate in scan_rates:
      name = electrode + '_' + analyte + '_' + str(scan_rate)

      title = r'Electrode: {}, Analyte: {}, Scan Rate: {} mV/s'.format(electrode, pretty_analytes[analyte], scan_rate)
      print(title)
      fig.suptitle(title)
      
      df_cal = df.loc[(df.electrode == electrode) & (df.analyte== analyte) & (df.scan_rate == scan_rate)]
      concentrations = df_cal.concentration_round.unique()
      
      x = np.array(df_cal.current).reshape((-1, 1))
      y = np.array(df_cal.concentration_calc)
      model = LinearRegression().fit(x,y)

      r_sq = model.score(x, y)
      intercept = model.intercept_
      coef = model.coef_[0]

      output_electrode.append(electrode)
      output_analyte.append(analyte)
      output_scan_rate.append(scan_rate)
      output_intercept.append(intercept)
      output_slope.append(coef)
      output_r_sq.append(r_sq)
      
      df_cal['regr_value'] = (df_cal.current * coef) + intercept
      function = r'{}[µM] = {:.2f} + {:.2f}*I[nA]'.format(pretty_conc[analyte], intercept, coef)+'\n'+r'R$^2$ = {:.3f}'.format(r_sq)

      
      ax1 = fig.add_axes([.58, .55, .4, .39]) #[left, bottom, width, height]

      ax1.scatter(df_cal.current, df_cal.concentration_calc)
      ax1.plot(df_cal.current, df_cal.regr_value)
      ax1.text(0.05, 0.85, function, transform=ax1.transAxes)
      ax1.set_xlabel('Current [nA]')
      ax1.set_ylabel('Concentration [µmol/l]')


      ax2 = fig.add_axes([.08, .55, .4, .39]) #[left, bottom, width, height]
      
      for concentration in concentrations:
        files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
        file = files[0]
        df_scan = pd.read_csv(file+'.csv')
        df_scan = df_scan[1:df_scan.potential.idxmin()+1]
        ax2.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration)
      plt.gca().invert_xaxis()
      ax2.set_xlabel('Potential [mV]')
      ax2.set_ylabel('Current [nA]')
      ax2.legend()

      ax3 = fig.add_axes([.08, .05, .4, .39]) #[left, bottom, width, height]
      for concentration in concentrations:
        files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
        if len(files)>1:
          file = files[1]
          df_scan = pd.read_csv(file+'.csv')
          df_scan = df_scan[1:df_scan.potential.idxmin()+1]
          ax3.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration)
      plt.gca().invert_xaxis()
      ax3.set_xlabel('Potential [mV]')
      ax3.set_ylabel('Current [nA]')
      ax3.legend()

      ax4 = fig.add_axes([.58, .05, .4, .39]) #[left, bottom, width, height]
      for concentration in concentrations:
        files = df_cal.loc[df_cal.concentration_round == concentration].reset_index()['file']
        if len(files)>2:
          file = files[2]
          df_scan = pd.read_csv(file+'.csv')
          df_scan = df_scan[1:df_scan.potential.idxmin()+1]
          ax4.plot(df_scan.potential, df_scan.current_filtered*-1000000000, label = concentration)
      plt.gca().invert_xaxis()
      ax4.legend()
      ax4.set_xlabel('Potential [mV]')
      ax4.set_ylabel('Current [nA]')
    
      name = 'calibration_plots/' + name + '.png'
      fig.savefig(name, dpi = 300)
      fig.clf()
      
d = {'electrode': output_electrode, 'analyte': output_analyte, 'scan_rate': output_scan_rate,
     'intercept': output_intercept, 'slope': output_slope, 'r_sq':output_r_sq}
df = pd.DataFrame(d)
df.to_csv('CalibrationRegressions.csv', index = False)
