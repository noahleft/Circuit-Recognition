#!/usr/local/bin/python3

import tensorflow as tf
from tensorflow.keras import layers

print(tf.VERSION)
print(tf.keras.__version__)

model = tf.keras.Sequential([
# Adds a densely-connected layer with 64 units to the model:
layers.Dense(43, activation='relu'),
# Adds a densely-connected layer with 64 units to the model:
layers.Dense(20, activation='relu'),
# Add another:
layers.Dense(1, activation='relu')])

# Configure a model for categorical classification.
#model.compile(optimizer=tf.train.RMSPropOptimizer(0.01),
#              loss=tf.keras.losses.binary_crossentropy,
#              metrics=[tf.keras.metrics.binary_accuracy])
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=[tf.keras.metrics.binary_accuracy])
import numpy as np


with open('train.data') as infile:
    train = [line.rstrip().split(' ') for line in infile.readlines()]
with open('test.data') as infile:
    test = [line.rstrip().split(' ') for line in infile.readlines()]
with open('train_converted.data') as infile:
    train_conv = [line.rstrip().split(' ') for line in infile.readlines()]
with open('test_converted.data') as infile:
    test_conv = [line.rstrip().split(' ') for line in infile.readlines()]

X = [[int(c) for c in d[0]] for d in train]
X_test = [[int(c) for c in d[0]] for d in test]
X_conv = [[int(c) for c in d[0]] for d in train_conv]
X_conv_test = [[int(c) for c in d[0]] for d in test_conv]
y = [int(d[1]) for d in train]
y_test = [int(d[1]) for d in test]
y_conv = [int(d[1]) for d in train_conv]
y_conv_test = [int(d[1]) for d in test_conv]

Xtrain = X + X_conv
Ytrain = y + y_conv

data = np.array(Xtrain)
labels = np.array(Ytrain)

model.fit(data, labels, validation_split = 0.2 , epochs=10, batch_size=32)

data = np.array(X)
labels = np.array(y)
result = model.evaluate(data, labels, batch_size=32)
print('train data precision:',result[1])

data = np.array(X_test)
labels = np.array(y_test)
result = model.evaluate(data, labels, batch_size=32)
print('test data precision:',result[1])

data = np.array(X_conv)
labels = np.array(y_conv)
result = model.evaluate(data, labels, batch_size=32)
print('train data precision (conv):',result[1])

data = np.array(X_conv_test)
labels = np.array(y_conv_test)
result = model.evaluate(data, labels, batch_size=32)
print('test data precision (conv):',result[1])

