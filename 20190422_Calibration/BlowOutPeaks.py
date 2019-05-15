import pandas as pd

#read data file and extract info on electrode, analyte, and concentration from scan names
df = pd.read_csv('peaks.csv')
df['electrode'] = df.file.str.slice(0,4,1)
df['analyte'] = df.file.str.slice(5,7,1)
df['concentration_round'] = pd.to_numeric(df.file.str.slice(8,11,1))

# map true, calculated calibration concentrations to rounded values
Fe_Conc = {'25':25.23, '50':50.41, '100': 100.63, '200': 200.47, '300':299.53}
Mn_Conc = {'25':25.02, '50':49.99, '100': 99.79, '200': 198.8}
HS_Conc = {'10':9.93, '25':24.81, '50': 49.57, '100': 98.95}
O2_Conc = {'0':0, '100':232.832}

df_Fe = df.loc[df.analyte == 'Fe']
df_Fe['concentration_calc'] = df_Fe.concentration_round.astype(str).map(Fe_Conc)
df_Mn = df.loc[df.analyte == 'Mn']
df_Mn['concentration_calc'] = df_Mn.concentration_round.astype(str).map(Mn_Conc)
df_HS = df.loc[df.analyte == 'HS']
df_HS['concentration_calc'] = df_HS.concentration_round.astype(str).map(HS_Conc)
df_O2 = df.loc[df.analyte == 'O2']
df_O2['concentration_calc'] = df_O2.concentration_round.astype(str).map(O2_Conc)
df = df_Fe.append(df_Mn)
df = df.append(df_HS)
df = df.append(df_O2)

#write file
df.to_csv('20190422_CalibrationData.csv', index = False)
