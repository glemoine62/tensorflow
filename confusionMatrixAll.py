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

