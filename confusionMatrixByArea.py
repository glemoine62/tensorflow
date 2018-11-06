import sys
import pandas as pd
import numpy as np

root = sys.argv[1]

areath = float(sys.argv[2])
# Join original input with classes results
df0 = pd.read_csv('{}.csv'.format(root), index_col = 0, low_memory=False)
df1 = pd.read_csv('{}_cropselect_classes.csv'.format(root), index_col = 0, low_memory=False)

# Create the join and retain 'klass' label as 'klass_1'
df = df0.join(df1, how="outer", rsuffix= '_1')

df.drop(['.geo'], axis=1, inplace=True)
df.dropna(inplace=True)
#print df[0:10]
df['klass'] = df['klass'].astype(int)
df['majclass'] = df['majclass'].astype(int)

df = df[df.area<areath]

# BEVL:
#crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'FBT']
# DK:
#crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'WOR','SCE','WCE','VEG']
# NL Vallei:
#crops = ['GRA', 'MAI', 'POT', 'SBA', 'SBT']
# BG:
crops = ['WWH', 'SFL', 'MAI', 'WOR', 'WBA', 'ALF','GRA']

dim = len(crops)

cm_cnt = np.zeros((dim, dim)).astype(float)
cm_area = np.zeros((dim, dim)).astype(float)

for j in df.index:
	row = df.loc[j]
	#n = np.array(row[r_index]).argmax()
	cm_cnt[row.klass][row.majclass] += 1
	cm_area[row.klass][row.majclass] += row.area/10000.0

pd.set_option('expand_frame_repr', False)
pd.set_option('precision', 1)

print "Overall Accuracy (by parcel count): ", 100.0*cm_cnt.trace()/cm_cnt.sum()

print pd.DataFrame(cm_cnt, index = crops, columns = crops)

print "\n\nOverall Accuracy (by parcel area): ", 100.0*cm_area.trace()/cm_area.sum()

print pd.DataFrame(cm_area, index = crops, columns = crops)
