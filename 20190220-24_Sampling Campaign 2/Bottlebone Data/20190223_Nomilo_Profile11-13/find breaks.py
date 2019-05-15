import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bottledeck1.kiwiprobe.csv')
plt.plot(df.ts)
plt.show()
