import sys
import pandas as pd
import numpy as np

df = pd.read_csv(sys.argv[1])

threshold = 0.50

dim = len(df.columns)-2
r_index = df.columns[2:]

cm = np.zeros((dim, dim))

for i in df.index:
	row = df.loc[i]
	n = np.array(row[r_index]).argmax()
	cm[row.klass][n] += 1 

np.set_printoptions(suppress=True, precision=0)

print "OA: ", 100.0*cm.trace()/cm.sum()

print pd.DataFrame(cm, index = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'ONI'], columns = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'ONI'])
