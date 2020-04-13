# Breast Cancer Type Classifier [ Chunin Projects ]
We are given a [dataset on Breast Cancer](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data) with various features that determine whether a cancer(tumor) is  Benign and Malignant.
Our goal is to make a Machine Learning Model to predict the features that are most significant for determining the type of cancer.(No visualisation)

## Motivation
Inorder to check my understanding of the ML-classification models and determining an optimum model from among them for this dataset. 

## Tech/framework used
<b>Built with</b>
- [Spyder](https://www.spyder-ide.org)
- [Python](https://electron.atom.io)

## Features of the project

The early diagnosis of BC can improve the prognosis and chance of survival significantly, as it can promote timely clinical treatment to patients. Further accurate classification of benign tumors can prevent patients undergoing unnecessary treatments. Thus, the correct diagnosis of BC and classification of patients into malignant or benign groups is the subject of much research. Because of its unique advantages in critical features detection from complex BC datasets, machine learning (ML) is widely recognized as the methodology of choice in BC pattern classification.

The features of the dataset ->

Attribute Information:

1) ID number

2) Diagnosis (M = malignant, B = benign)
3-32) (The dependent variable vector)

Ten real-valued features are computed for each cell nucleus (Independent matrix of features to determine the optimum features from) :

a) radius (mean of distances from center to points on the perimeter)

b) texture (standard deviation of gray-scale values)

c) perimeter

d) area

e) smoothness (local variation in radius lengths)

f) compactness (perimeter^2 / area - 1.0)

g) concavity (severity of concave portions of the contour)

h) concave points (number of concave portions of the contour)

i) symmetry

j) fractal dimension ("coastline approximation" - 1)

The mean, standard error and "worst" or largest (mean of the three
largest values) of these features were computed for each image,
resulting in 30 features. 

All feature values are recoded with four significant digits.

Missing attribute values: none

Class distribution: 357 benign, 212 malignant

## Tests
Inorder to find the accuracy of the model we take the number of correct predictions from the confussion matrix and divide it with the total number of predictions for each classification algorithm and find the follwing values :

1. Logistic Regression — 95.8%

2. Nearest Neighbor — 95.1%

3. Support Vector Machines — 97.2%

4. Kernel SVM — 96.5%

5. Naive Bayes — 91.6%

6. Decision Tree Algorithm — 95.8%

7. Random Forest Classification — 98.6%

## Credits
The dataset has beem taken from [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+%28diagnostic%29).
Learning materials from [Machine Learning Udemy Course](https://www.udemy.com/machine-learning) and [Towards Data Science](https://towardsdatascience.com)
