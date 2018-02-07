import numpy as np
import tensorflow as tf
import tflearn
import sys
import glob

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv

# tflearn.init_graph(gpu_memory_fraction=0.0)

rootname = sys.argv[1]
nclass = int(sys.argv[2])
nepoch = int(sys.argv[3])
nrun = int(sys.argv[4])

flist = glob.glob(rootname + '_train_{}.csv'.format(nrun))
print flist

if len(flist) > 1:
  print "FATAL: Only single training set allowed for {}, found {}".format(rootname, len(flist))
  sys.exit(1)
elif len(flist) == 0:
  print "FATAL: No training set found for {}".format(rootname)
  sys.exit(1)
 
glist = glob.glob(rootname + '_test_{}.csv'.format(nrun))

if len(glist) > 1:
  print "FATAL: Only single test set allowed for {}, found {}".format(rootname, len(flist))
  sys.exit(1)
elif len(glist) == 0:
  print "FATAL: No test set found for {}".format(rootname)
  sys.exit(1)
 
fname = flist[0]
gname = glist[0]

data, labels = load_csv(fname, target_column=3,
                        categorical_labels=True, n_classes=nclass)

test_data, test_labels = load_csv(gname, target_column=3,
                        categorical_labels=True, n_classes=nclass)

# Preprocessing function
def preprocess(profiles, columns_to_delete):
    # Sort by descending id and delete columns
    for column_to_delete in sorted(columns_to_delete, reverse=True):
        [profile.pop(column_to_delete) for profile in profiles]
    return np.array(profiles, dtype=np.float32)

# Ignore 'id' 
to_ignore=[0,1,2]

# Preprocess data
data = preprocess(data, to_ignore)

# Build neural network
net = tflearn.input_data(shape=[None, len(data[0])])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
#net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, nclass, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=nepoch, batch_size=32, show_metric=True)

fw = open('{}_{}_predictions.csv'.format(rootname, nrun), 'w')
fw.write("id,klass")
for i in range(nclass):
  fw.write(",prob{}".format(i))
fw.write('\n')

# Check predictions for the samples not used in training
for i in range(len(test_data)):
  sample = test_data[i][3:]
  slabel = test_labels[i].tolist().index(1)
  #print(labels[i])
  pred = model.predict([sample])
  fw.write("{},{}".format(test_data[i][2], str(slabel)))
  for i in range(nclass):
    fw.write(",{:6.2f}".format(100*pred[0][i]))
  fw.write('\n')

