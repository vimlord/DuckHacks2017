# Emotion analysis module
from emotion import *
from analysis import *

# Song player module
from youtube import *
from picture import *

# The list of currently supported genres
genres = ['pop', 'edm', 'rock']

clf = loadClassifier('./classifier.pkl')

def runCycle(prevState):
    print("Beginning procedure...") 

    # Takes a selfie.
    picture()
    print("Snap!")
    
    # Gets the emotion data for the selfie.
    data = imageRequest('./selfie.jpg')
    print("Scanned image.")

    # Gets the emotion vector from the image.
    vec = parseEmotion(data)
    print("Acquired sentiment.")

    # Computes the prediction.
    pred = makePrediction(clf, vec)
    print("Choice vector computed.")

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

runCycle('hi')




