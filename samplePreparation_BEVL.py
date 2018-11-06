import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv', low_memory=False)

df = df[df['area']> 3000]

df.drop(['.geo', 'area', 'GWSNAM_H', 'perimeter', 'random'], axis=1, inplace=True)

df.dropna(inplace=True)

cropcode = 'GWSCOD_H'
# Make sure crop label is added as the last column
df['croplabel'] = df[cropcode].astype(int)
df.drop([cropcode], axis=1, inplace=True)

cropcode = 'croplabel'

gra = df[cropcode].isin([60,700,3432])
mai = df[cropcode].isin([201,202])
pot = df[cropcode].isin([901,904])
wwh = df[cropcode].isin([311,36])
sbt = df[cropcode].isin([91])
wba = df[cropcode].isin([321])
fbt = df[cropcode].isin([71])

#df.loc[gra, cropcode] = 0
df.loc[gra, cropcode] = 0
df.loc[mai, cropcode] = 1
df.loc[pot, cropcode] = 2
df.loc[wwh, cropcode] = 3
df.loc[sbt, cropcode] = 4
df.loc[wba, cropcode] = 5
df.loc[fbt, cropcode] = 6

subset = df.loc[df[cropcode].isin([0,1,2,3,4,5,6])]

subset.to_csv(sys.argv[1]+ '_cropselect.csv')

