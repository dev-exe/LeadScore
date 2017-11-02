import pickle
import sys

from preprocess import feature_format,targetFeatureSplit

data_dict = pickle.load(open("data_files/formated_data1.pkl","r"))
print data_dict
feature_list = ["GTM", "filing_status"]

data = feature_format(data_dict,feature_list)


labels, features = targetFeatureSplit(data)

from sklearn import  model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn import grid_search
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size= 0.30, random_state = 42)

dt = DecisionTreeClassifier(random_state= 0)
#svr = svm.SVC()
#params = {'kernel': ('linear', 'rbf'), 'C':[1, 10]}
#clf = model_selection.GridSearchCV(svr, params)
#clf.fit(features_train, labels_train)
#pred1 = clf.predict(features_test)
#print "The SVM optimized params are"
#acc1 = accuracy_score(labels_test,pred1)
#print acc1

dt.fit(features_train,labels_train)
pred = dt.predict(features_test)
print dt.score(features, labels)
print len(labels_train)
acc = accuracy_score(labels_test, pred)
print pred
print labels_test
