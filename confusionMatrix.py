import sys
import pandas as pd
import numpy as np

df = pd.read_csv(sys.argv[1], low_memory = False)

threshold = 0.50

dim = len(df.columns)-2
r_index = df.columns[2:]

cm = np.zeros((dim, dim))

for i in df.index:
	row = df.loc[i]
	n = np.array(row[r_index]).argmax()
	cm[row.klass][n] += 1 

np.set_printoptions(suppress=True, precision=0)
pd.set_option('expand_frame_repr', False)

print "OA: ", 100.0*cm.trace()/cm.sum()

# BEVL:
#crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'FBT']
#print pd.DataFrame(cm, index = crops, columns = crops)
# DK:

crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'WOR','SCE','WCE','VEG']
print pd.DataFrame(cm, index = crops, columns = crops)

