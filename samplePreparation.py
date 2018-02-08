import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv')

#df = df[df.bufferedarea > 3000]

#df.drop(['.geo', 'area', 'bufferedarea', 'gws_gewas', 'id', 'perimeter'], axis=1, inplace=True)
df.drop(['.geo', 'area', 'gws_gewas', 'id', 'perimeter'], axis=1, inplace=True)

df["gws_gewasc"] = df.gws_gewasc.astype(int)

gra = df['gws_gewasc'].isin([265, 266, 331, 336, 383])
mai = df['gws_gewasc'].isin([259, 316, 317])
pot = df['gws_gewasc'].isin([2014, 2015, 2016, 2017])
wwh = df['gws_gewasc'].isin([233])
sbt = df['gws_gewasc'].isin([256])
oni = df['gws_gewasc'].isin([262, 1931])
sba = df['gws_gewasc'].isin([236])
flo = df['gws_gewasc'].isin([1004, 1002])


df.loc[gra, 'gws_gewasc'] = 0
df.loc[mai, 'gws_gewasc'] = 1
df.loc[pot, 'gws_gewasc'] = 2
df.loc[wwh, 'gws_gewasc'] = 3
df.loc[sbt, 'gws_gewasc'] = 4
df.loc[oni, 'gws_gewasc'] = 5
df.loc[sba, 'gws_gewasc'] = 6
df.loc[flo, 'gws_gewasc'] = 7

subset = df.loc[df['gws_gewasc'].isin([0,1,2,3,4,5,6,7])]

subset.to_csv(sys.argv[1] + '_cropselect.csv')

