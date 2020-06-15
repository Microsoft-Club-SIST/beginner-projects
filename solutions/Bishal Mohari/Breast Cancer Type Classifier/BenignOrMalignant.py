# Machine Learning Model on the Breast Cancer Dataset.
# To Predict the features most significant for predicting the type of cancer.
# Our goal to create the optimum model for predicting Benign(B) or Malignant(M) cancer.

# importing the libraries
import numpy as np
import matplotlib.pyplot # Note : The visualisation of the training and test set results will be updated ater
import pandas as pd 

# importing the dataset
dataset1 = pd.read_csv("data.csv")

# Splitting the independent and dependent variables into X and y respectively
y = dataset1.diagnosis
list = ['Unnamed: 32', 'id', 'diagnosis']
X = dataset1.drop(list, axis = 1)
X.head()

# Label Encoding the categorical data values -> Benign(B) and Malignant(M) into 0 and 1
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling for bringing the different features if X into the continoues range
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# In the independent variable we observe their being two sets of values (B and M)  so we consider this to be a classification problem
# Now we apply the  different types of Classification Algorithms on our training and testing sets 
# Then we analyse their accuracy and take the model with the highest accuracy to be the best fit for our problem

# Fitting the Logistic Regression Algorithm to the Training Set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)
# 95.8 Acuracy

# Fitting K-NN Algorithm to the Training Set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)
# 95.1 Acuracy

# Fitting SVM to the Training Set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train) 
# 97.2 Acuracy

# Fitting K-SVM to the Training Set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)
# 96.5 Acuracy

# Fitting Naive_Bayes to the Training Set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
# 91.6 Acuracy

# Fitting Decision Tree Algorithm to the Training Set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
# 95.8 Accuracy

# Fitting RandomForestClassifier Algorithm for the Training Set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)
# 98.6% Accuracy

# The RFC model provides 98.6% Accuracy and is the highest among all other
# classification models

# Predicting the test set results 
y_pred = classifier.predict(X_test)

# Creating the confusion matrix
# This is  created inorder to look at the total number of correct and incorrect predictions
# The total number of predictions is divided by the number of correct predictions
# to find the accuracy of our model in the given problem
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm[0,0]+cm[1,1])
