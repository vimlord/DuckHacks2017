import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import datasets, linear_model

import cPickle

from emotion import *

# Returns a classifier that analyzes the correlation between data.
def trainOnData(data):
    X = [pair[0] for pair in data]
    Y = [pair[1] for pair in data]

    #clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
    clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
    clf.fit(X, Y)
    
    return clf

# Parses emotion from the return value of the Microsoft Emotion API.
def parseEmotion(data):
    return [data[0]['scores'][em] for em in emotions]

# Makes a prediction about a vector based on a classifier.
def makePrediction(clf, vec):
    return clf.predict([vec])[0]

def saveClassifier(filename, clf):
    with open(filename, 'wb') as fid:
        cPickle.dump(clf, fid)

def loadClassifier(filename):
    with open(filename, 'rb') as fid:
        return cPickle.load(fid)

def rebuildClassifier():
    # Input is [sad, happy, disgust, anger, surprise, fear, neutral, contempt]
    # Output is [rap, hardrock, metal, classical, jazz, pop, classrock, edm, country]
    X = [
        [1, 0, 0, 0, 0, 0, 0, 0], # Sad
        [0, 1, 0, 0, 0, 0, 0, 0], # Happy
        [0, 0, 0, 1, 0, 0, 0, 0], # Angry
        [0, 0, 0, 0, 0, 0, 1, 0]  # Neutral
    ]

    Y = [
        [0, 0, 0, 1, 1, 0, 0, 0, 1], # Sad
        [0, 0, 0, 0, 0, 1, 1, 1, 0], # Happy
        [1, 1, 1, 0, 0, 0, 0, 0, 0], # Angry
        [0, 0, 0, 0, 0, 0, 1, 1, 1]
        
    ]
    
    clf = trainOnData([(X[i], Y[i]) for i in range(len(Y))])
    saveClassifier('./classifier.pkl', clf)

