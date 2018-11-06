import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv', low_memory=False)

df = df[df.bufferedarea > 1000]

df.drop(['.geo', 'area', 'bufferedarea', 'AfgNavn', 'perimeter', 'random'], axis=1, inplace=True)

cropcode = 'AfgNr'
df['cropcode'] = df[cropcode].astype(int)

cropcode = 'cropcode'
df.drop(['AfgNr'], axis=1, inplace=True)


gra = df[cropcode].isin([260, 252, 108, 254, 276, 263, 247, 101, 251, 111, 106, 250, 268, 257, 113, 255, 264])
mai = df[cropcode].isin([216,5])
pot = df[cropcode].isin([151, 152])
wwh = df[cropcode].isin([11,13])
sbt = df[cropcode].isin([160])
wba = df[cropcode].isin([10])
wor = df[cropcode].isin([22])
sce = df[cropcode].isin([1,2])
wce = df[cropcode].isin([15,3,14])
veg = df[cropcode].isin([30,424,31,124])

# Make sure the new codes are not overlapping with existing codes
df.loc[gra, cropcode] = 1000
df.loc[mai, cropcode] = 1001
df.loc[pot, cropcode] = 1002
df.loc[wwh, cropcode] = 1003
df.loc[sbt, cropcode] = 1004
df.loc[wba, cropcode] = 1005
df.loc[wor, cropcode] = 1006
df.loc[sce, cropcode] = 1007
df.loc[wce, cropcode] = 1008
df.loc[veg, cropcode] = 1009

subset = df.loc[df[cropcode].isin([1000,1001,1002,1003,1004,1005,1006,1007,1008,1009])]

subset[cropcode] = subset[cropcode].map(lambda x: x - 1000)

subset.to_csv(sys.argv[1]+ '_cropselect.csv')
