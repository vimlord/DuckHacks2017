# Emotion analysis module
from emotion import *
from analysis import *

# Song player module
from youtube import *
from camera import *

# The list of currently supported genres
genres = ['pop', 'edm', 'rock']

clf = loadClassifier('./classifier.pkl')

def runCycle(prevState):
    
    # Takes a selfie.
    picture()
    
    # Gets the emotion data for the selfie.
    data = imageRequest('./selfie.jpg')

    # Gets the emotion vector from the image.
    vec = parseEmotion(data)

    # Computes the prediction.
    pred = makePrediction(clf, vec)

    # Choose the dimension with the highest value.
    choice = 0
    for i in range(1, len(genres)):
        if vec[i] > vec[choice]:
            choice = i
    
    # Play the requested genre
    if prevState != genres[choice]:
        print("Will play " + genres[choice])
        search(genres[choice])

    return genres[choice]






