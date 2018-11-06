import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv')

df = df[df.area > 1000]

#df.drop(['.geo', 'area', 'bufferedarea', 'gws_gewas', 'id', 'perimeter'], axis=1, inplace=True)
df.drop(['.geo', 'area', 'gws_gewas', 'id', 'perimeter'], axis=1, inplace=True)

df["gws_gewasc"] = df.gws_gewasc.astype(int)

gra = df['gws_gewasc'].isin([265, 266, 331, 336])
mai = df['gws_gewasc'].isin([259])
pot = df['gws_gewasc'].isin([2014])
sba = df['gws_gewasc'].isin([236])
sbt = df['gws_gewasc'].isin([256])


df.loc[gra, 'gws_gewasc'] = 0
df.loc[mai, 'gws_gewasc'] = 1
df.loc[pot, 'gws_gewasc'] = 2
df.loc[sba, 'gws_gewasc'] = 3
df.loc[sbt, 'gws_gewasc'] = 4

subset = df.loc[df['gws_gewasc'].isin([0,1,2,3,4])]

subset.to_csv(sys.argv[1] + '_cropselect.csv')

