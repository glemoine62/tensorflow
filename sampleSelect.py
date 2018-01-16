import sys
import pandas as pd
import numpy as np 

df = pd.read_csv(sys.argv[1])

samplesize = int(sys.argv[2])

training = df.take(np.random.permutation(len(df))[:samplesize])
testing = df.drop(training.index)

training.to_csv(sys.argv[1].replace('.csv', '_train_{}.csv').format(samplesize))
testing.to_csv(sys.argv[1].replace('.csv', '_test_{}.csv').format(len(testing)))