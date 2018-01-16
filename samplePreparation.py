import sys
import pandas as pd 

df = pd.read_csv(sys.argv[1] + '.csv')

df = df[df.bufferedarea > 3000]

df.drop(['.geo', 'area', 'bufferedarea', 'gws_gewas', 'id', 'perimeter'], axis=1, inplace=True)

df["gws_gewasc"] = df.gws_gewasc.astype(int)

#gra = df['gws_gewasc'].isin([265, 266])
mai = df['gws_gewasc'].isin([259, 316, 317])
pot = df['gws_gewasc'].isin([2014, 2015, 2016, 2017])
wwh = df['gws_gewasc'].isin([233])
sbt = df['gws_gewasc'].isin([256])
oni = df['gws_gewasc'].isin([262, 1931])
sba = df['gws_gewasc'].isin([236])


#df.loc[gra, 'gws_gewasc'] = 0
df.loc[sba, 'gws_gewasc'] = 0
df.loc[mai, 'gws_gewasc'] = 1
df.loc[pot, 'gws_gewasc'] = 2
df.loc[wwh, 'gws_gewasc'] = 3
df.loc[sbt, 'gws_gewasc'] = 4
df.loc[oni, 'gws_gewasc'] = 5

subset = df.loc[df['gws_gewasc'].isin([0,1,2,3,4,5])]

subset.to_csv(sys.argv[1]+ '_cropselect.csv')

subset.drop(['c_x', 'c_y'], axis=1, inplace=True)

subset.to_csv(sys.argv[1]+ '_cropselect_nocrds.csv')
