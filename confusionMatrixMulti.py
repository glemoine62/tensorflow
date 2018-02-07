import sys
import pandas as pd
import numpy as np

rootname = sys.argv[1] + '_{}_predictions.csv'

chunks = int(sys.argv[2])

for i in range(chunks):
	print rootname.format(i)
	df = pd.read_csv(rootname.format(i), low_memory = False)

	dim = len(df.columns)-2
	r_index = df.columns[2:]

	if i == 0:
		cm = np.zeros((dim, dim))

	for j in df.index:
		row = df.loc[j]
		n = np.array(row[r_index]).argmax()
		cm[row.klass][n] += 1 

np.set_printoptions(suppress=True, precision=0)
pd.set_option('expand_frame_repr', False)

print "Overall Accuracy: ", 100.0*cm.trace()/cm.sum()

# BEVL:
#crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'FBT']
#print pd.DataFrame(cm, index = crops, columns = crops)
# DK:

crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'WOR','SCE','WCE','VEG']
print pd.DataFrame(cm, index = crops, columns = crops)

