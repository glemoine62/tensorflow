import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv', low_memory=False)

#df = df[df.bufferedarea > 1000]

df.drop(['.geo', 'area', 'perimeter', 'Crop_Name_', 'APPL_ID', 'FARMER_ID'], axis=1, inplace=True)

df.dropna(inplace=True)

cropcode = 'Cod_ISAC'
df['cropcode'] = df[cropcode].astype(int)

df.drop([cropcode], axis=1, inplace=True)

cropcode = 'cropcode'

wwh = df[cropcode].isin([111011])
sfl = df[cropcode].isin([122010])
mai = df[cropcode].isin([111050])
wor = df[cropcode].isin([122031])
wba = df[cropcode].isin([111061])
alf = df[cropcode].isin([132021])
gra = df[cropcode].isin([314000])

# Make sure the new codes are not overlapping with existing codes
df.loc[wwh, cropcode] = 0
df.loc[sfl, cropcode] = 1
df.loc[mai, cropcode] = 2
df.loc[wor, cropcode] = 3
df.loc[wba, cropcode] = 4
df.loc[alf, cropcode] = 5
df.loc[gra, cropcode] = 6

subset = df.loc[df[cropcode].isin([0,1,2,3,4,5,6])]

subset.to_csv(sys.argv[1]+ '_cropselect.csv')
