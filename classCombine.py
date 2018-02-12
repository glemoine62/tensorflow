import pandas as pd
import numpy as np
import sys

from collections import Counter

# The join of the first and second run will include ALL parcels,
# because the outer join of df0 and df1 introduce the 20% subset of
# training parcels that were used in run 0 and not in run 1
root = sys.argv[1]

nchunks = int(sys.argv[2])

df0 = pd.read_csv('{}_cropselect_0_class.csv'.format(root), index_col = 0, low_memory=False)
df1 = pd.read_csv('{}_cropselect_1_class.csv'.format(root), index_col = 0, low_memory=False)

# Create the join and retain 'klass' label as 'klass_1'
df = df0.join(df1, how="outer", rsuffix= '_1')
# Records that were not yet in df0 have 'klass' label missing (NA)
# so, overwrite with those of 'klass_1'
df['klass'].loc[df['klass'].isnull()] = df['klass_1'].loc[df['klass'].isnull()]
# and drop the now redundant 'klass_1' label
df.drop('klass_1', axis=1, inplace=True)

for i in range(2,nchunks):
  # Load the other runs
  print i
  dfN = pd.read_csv('{}_cropselect_{}_class.csv'.format(root, i), index_col = 0, low_memory=False)
  dfN.drop('klass', axis=1, inplace=True)
  df = df.join(dfN, how="outer")  

# Join the latter, overwrite NA values and save as int

df.fillna(-1, inplace=True)

r_index = df.columns[1:]

# def majority(args):
# 	(values, counts) = np.unique(np.array(args[r_index]), return_counts =True)
# 	ind =np.argmax(counts)
# 	return pd.Series({'majclass': ind, 'majcount': np.max(counts)})


df['majclass'] = df.apply(lambda x: Counter(x[r_index]).most_common(1)[0][0], axis=1)
df['majcount'] = df.apply(lambda x: Counter(x[r_index]).most_common(1)[0][1], axis=1)

df.astype(int).to_csv('{}_cropselect_classes.csv'.format(root))