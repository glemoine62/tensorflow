import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv', low_memory=False)

df = df[df.bufferedarea > 1000]

df.drop(['.geo', 'area', 'bufferedarea', 'AfgNavn', 'perimeter', 'random'], axis=1, inplace=True)

cropcode = 'AfgNr'
df[cropcode] = df[cropcode].astype(int)

#gra = df[cropcode].isin([265, 266])
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

#df.loc[gra, cropcode] = 0
df.loc[gra, cropcode] = 0
df.loc[mai, cropcode] = 1
df.loc[pot, cropcode] = 2
df.loc[wwh, cropcode] = 3
df.loc[sbt, cropcode] = 4
df.loc[wba, cropcode] = 5
df.loc[wor, cropcode] = 6
df.loc[sce, cropcode] = 7
df.loc[wce, cropcode] = 8
df.loc[veg, cropcode] = 9

subset = df.loc[df[cropcode].isin([0,1,2,3,4,5,6,7,8,9])]

subset.to_csv(sys.argv[1]+ '_cropselect.csv')

#subset.drop(['c_x', 'c_y'], axis=1, inplace=True)

#subset.to_csv(sys.argv[1]+ '_cropselect_nocrds.csv')
