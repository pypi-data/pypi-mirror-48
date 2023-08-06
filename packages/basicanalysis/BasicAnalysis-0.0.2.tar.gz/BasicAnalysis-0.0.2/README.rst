Performance Overview of Supervised Learning methods 
====================================================

A small task of creating and uploading a pip-installable Python package, and by no means
a substitute for `reading the documentation <https://packaging.python.org/tutorials/distributing-packages>`_, even
if you are in a rush and your cat is on fire.

This small package of merely few bytes and code written in less than 100 lines, provide you the overview of all fundamental metrics measured for almost all supervised learning method.

-------------------------------------------------------
|	Models evaluated:	|	Metrics considered:	|
-------------------------------------------------------
|					|					|
|	Decision Trees		|	Accuracy			|
|	Logistic Regression	|	Precision			|
|	Naive Bayes		|	Jaccard Score		|
|	SVM				|	F1_Score			|
|	Neural Networks		|	R (Corr Coeff)		|
|	K-NN				|	ROC AUC			|
|	Random Forest		|	MSE				|
|	Adaboost			|	Log Loss			|
-------------------------------------------------------

Mandatory inputs required:
A Pandas DataFrame

Optional inputs in the given order:

Column numbers for the predictors in the form of a LIST 
Default: It will take all columns except the last one.

Column number for the response in the form of a LIST
Default: It will take the last column.

Test size in Float Ex. 0.3 for 30% Test Size. Default: 0.25


----

README file for the task

Written in reStructuredText or .rst file, and used to generate the project page on PyPI.