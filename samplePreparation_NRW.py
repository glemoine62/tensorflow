import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv', low_memory=False)

df.drop(['.geo', 'area', 'gtype', 'id', 'MON10_CR_2', 'perimeter'], axis=1, inplace=True)

cropcode = 'MON10_CR_1'
df['cropcode'] = df[cropcode].astype(int)

cropcode = 'cropcode'
df.drop(['MON10_CR_1'], axis=1, inplace=True)


gra = df[cropcode].isin([459, 424, 422])
mai = df[cropcode].isin([411, 171])
pot = df[cropcode].isin([602])
wwh = df[cropcode].isin([115])
sbt = df[cropcode].isin([603])
wba = df[cropcode].isin([131])
wor = df[cropcode].isin([311])
wce = df[cropcode].isin([156,121,112])
sce = df[cropcode].isin([132, 116, 143])
veg = df[cropcode].isin([220])

# Make sure the new codes are not overlapping with existing codes
df.loc[gra, cropcode] = 1000
df.loc[mai, cropcode] = 1001
df.loc[pot, cropcode] = 1002
df.loc[wwh, cropcode] = 1003
df.loc[sbt, cropcode] = 1004
df.loc[wba, cropcode] = 1005
df.loc[wor, cropcode] = 1006
df.loc[wce, cropcode] = 1007
df.loc[sce, cropcode] = 1008
df.loc[veg, cropcode] = 1009

subset = df.loc[df[cropcode].isin([1000,1001,1002,1003,1004,1005,1006,1007,1008,1009])]

subset[cropcode] = subset[cropcode].map(lambda x: x - 1000)

subset.to_csv(sys.argv[1]+ '_cropselect.csv')
