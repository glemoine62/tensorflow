from __future__ import print_function

import numpy as np
import tflearn
import sys

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv

fname = sys.argv[1]
nclass = int(sys.argv[2])

data, labels = load_csv(fname, target_column=-1,
                        categorical_labels=True, n_classes=nclass)

print(labels)

org_data, org_labels = load_csv(fname, target_column=-1,
                        categorical_labels=True, n_classes=nclass)

# Preprocessing function
def preprocess(profiles, columns_to_delete):
    # Sort by descending id and delete columns
    for column_to_delete in sorted(columns_to_delete, reverse=True):
        [profile.pop(column_to_delete) for profile in profiles]
    return np.array(profiles, dtype=np.float32)

# Ignore 'id' 
to_ignore=[0,1]

# Preprocess data
data = preprocess(data, to_ignore)

# Build neural network
net = tflearn.input_data(shape=[None, len(data[0])])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, nclass, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data[0:1000], labels[0:1000], n_epoch=100, batch_size=32, show_metric=True)

# Check predictions for the samples not used in training
for i in range(1000,len(data)):
  sample = data[i]
  slabel = labels[i].tolist().index(1)
  #print(labels[i])
  pred = model.predict([sample])
  print("{:s},{:1.0f},{:6.2f},{:6.2f},{:6.2f},{:6.2f},{:6.2f},{:6.2f}".format(org_data[i][1], slabel, 100*pred[0][0], 100*pred[0][1], 100*pred[0][2], 100*pred[0][3], 100*pred[0][4], 100*pred[0][5]))
