import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import datasets, linear_model

from emotion import imageRequest

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
    return data[0]['scores'].values()

# Makes a prediction about a vector based on a classifier.
def makePrediction(clf, vec):
    return clf.predict([vec])[0]

def __christest():
    X = [[0,1,0,0,0,0,0,0]] * 6 + [[0,0,0,1,0,0,0,0]] * 6 + [[0,0,0,0,0,0,1,0]] * 6
    Y = [
        [0,0,1],
        [0,0,1],
        [0,0,1],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [0,1,1],
        [0,1,0],
        [0,1,0],
        [0,1,1],
        [0,1,0],
        [0,1,0],
        [0,0,1],
        [0,0,1],
        [0,0,1],
        [0,1,0],
        [1,0,0],
        [1,0,0]
    ]

    print(str(len(X)) + " inputs")
    print(str(len(Y)) + " outputs")
    clf = trainOnData([(X[i], Y[i]) for i in range(len(Y))])

    emote = imageRequest('/home/chrishittner/Desktop/sample.jpg')
    print(emote)
    print(makePrediction(clf, parseEmotion(emote)))

