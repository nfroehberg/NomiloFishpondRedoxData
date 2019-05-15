import pandas as pd
from glob import glob
# change .txt to .csv files
# highest resolution series was EC, select as reference for timestamps:
ref_csv = 'bottlebone.ec.csv'
ref_df = pd.read_csv(ref_csv)

# read names of all remaining csv files
files = glob('*.csv')
files.remove(ref_csv)

# merge dataseries to closest timestamp (gaps in the lower resolution series are filled by duplication of closest datapoint)
output_df = ref_df
for merge_csv in files:
    merge_df = pd.read_csv(merge_csv)
    #print(merge_df)
    print(merge_csv)
    output_df = pd.merge_asof(left = output_df, right = merge_df.sort_values('ts'), on = 'ts',
                              direction = 'nearest',
                              suffixes = ('','_{}'.format(merge_csv.replace('.csv',''))))
    #print(output_df)
# write to csv
output_df.to_csv('bottlebone_merged.csv', index = False)
    
# timestamps for beginning, end, and ID of each station
starts = [1550793769.79469]
ends = [1550796197.99393]
stations = [2]

# get profiles from merged dataset by station
output_stations = pd.DataFrame(columns = output_df.columns)
output_stations['station'] = 0
for i in range(len(stations)):
    station_df = output_df.loc[(output_df.ts >= starts[i]) & (output_df.ts <= ends[i])]
    station_df['station'] = stations[i]
    output_stations = output_stations.append(station_df)
# write to csv
output_stations.to_csv('bottlebone_merged_stations.csv', index = False)
