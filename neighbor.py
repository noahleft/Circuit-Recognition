#!/usr/local/bin/python3

from sklearn.neighbors import KNeighborsClassifier

with open('train.data') as infile:
    train = [line.rstrip().split(' ') for line in infile.readlines()]
with open('test.data') as infile:
    test = [line.rstrip().split(' ') for line in infile.readlines()]

X = [[int(c) for c in d[0]] for d in train]
X_test = [[int(c) for c in d[0]] for d in test]
y = [int(d[1]) for d in train]
y_test = [int(d[1]) for d in test]

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X, y)

from sklearn.metrics import precision_score

print('nearest neighbor method:')
y_predict = clf.predict(X)
precision = precision_score(y, y_predict)
print('train data precision:',precision)

y_predict = clf.predict(X_test)
precision = precision_score(y_test, y_predict)
print('test data precision:',precision)


