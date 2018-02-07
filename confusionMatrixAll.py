import sys
import pandas as pd
import numpy as np

rootname = sys.argv[1] + '_{}_predictions.csv'

chunks = int(sys.argv[2])

for i in range(chunks):
	print rootname.format(i)
	df = pd.read_csv(rootname.format(i), index_col=0, low_memory = False)

	r_index = df.columns[1:]

	df['pred{}'.format(i)] = df.apply(lambda x: np.array(x[r_index]).argmax(), axis=1)

	df.drop(r_index, axis=1, inplace=True)

	df.to_csv(sys.argv[1]+ '_{}_class.csv'.format(i))


# for i in df.index:
# 	row = df.loc[i]
# 	n = np.array(row[r_index]).argmax()

# for i in range(1,chunks):
# 	print rootname.format(i)
# 	df_new = pd.read_csv(rootname.format(i), low_memory = False)

	

# 	for j in df_new.index:
# 		if j in df.index:

# 		row = df_new.loc[j]
# 		n = np.array(row[r_index]).argmax()
# 		cm[row.klass][n] += 1 

# np.set_printoptions(suppress=True, precision=0)
# pd.set_option('expand_frame_repr', False)

# print "Overall Accuracy: ", 100.0*cm.trace()/cm.sum()

# # BEVL:
# #crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'FBT']
# #print pd.DataFrame(cm, index = crops, columns = crops)
# # DK:

# crops = ['GRA', 'MAI', 'POT', 'WWH', 'SBT', 'WBA', 'WOR','SCE','WCE','VEG']
# print pd.DataFrame(cm, index = crops, columns = crops)

