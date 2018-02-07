import sys
import pandas as pd
import numpy as np 

df = pd.read_csv(sys.argv[1], low_memory=False)

chunks = int(sys.argv[2])

df_test = df.copy(deep=True)

samplesize = len(df)/chunks

for i in range(chunks-1):
	print i, len(df)
	training = df.take(np.random.permutation(len(df))[:samplesize])

	training.to_csv(sys.argv[1].replace('.csv', '_train_{}.csv').format(i))

	df.drop(training.index, inplace=True)

	df_test.loc[~df_test.index.isin(training.index)].to_csv(sys.argv[1].replace('.csv', '_test_{}.csv').format(i))


print "Remainder", len(df)
df.to_csv(sys.argv[1].replace('.csv', '_train_{}.csv').format(chunks-1))
df_test.loc[~df_test.index.isin(df.index)].to_csv(sys.argv[1].replace('.csv', '_test_{}.csv').format(chunks-1))
