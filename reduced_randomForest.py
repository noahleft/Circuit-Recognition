#!/usr/local/bin/python3

from sklearn.ensemble import RandomForestClassifier

with open('train.data') as infile:
    train = [line.rstrip().split(' ') for line in infile.readlines()]
with open('test.data') as infile:
    test = [line.rstrip().split(' ') for line in infile.readlines()]
with open('train_converted.data') as infile:
    train_conv = [line.rstrip().split(' ') for line in infile.readlines()]
with open('test_converted.data') as infile:
    test_conv = [line.rstrip().split(' ') for line in infile.readlines()]

X = [[int(c) for c in d[0][:40]] for d in train]
X_test = [[int(c) for c in d[0][:40]] for d in test]
X_conv = [[int(c) for c in d[0][:40]] for d in train_conv]
X_conv_test = [[int(c) for c in d[0][:40]] for d in test_conv]
y = [int(d[1]) for d in train]
y_test = [int(d[1]) for d in test]
y_conv = [int(d[1]) for d in train_conv]
y_conv_test = [int(d[1]) for d in test_conv]

clf = RandomForestClassifier(n_estimators=100)
Xtrain = X + X_conv
Ytrain = y + y_conv
clf.fit(Xtrain, Ytrain)

from sklearn.metrics import precision_score

print('random forest:')
y_predict = clf.predict(X)
precision = precision_score(y, y_predict)
print('train data precision:',precision)

y_predict = clf.predict(X_test)
precision = precision_score(y_test, y_predict)
print('test data precision:',precision)

y_predict = clf.predict(X_conv)
precision = precision_score(y_conv, y_predict)
print('train data precision (conv):',precision)

y_predict = clf.predict(X_conv_test)
precision = precision_score(y_conv_test, y_predict)
print('test data precision (conv):',precision)


