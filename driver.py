# Emotion analysis module
from emotion import *
from analysis import *

# Song player module
from youtube import *
from picture import *

import os
import os.path
import time
import random

# The list of currently supported genres
genres = [
    'rap',
    'hard rock',
    'metal',
    'classical',
    'jazz',
    'pop',
    'classic rock',
    'edm',
    'country'
]

subemo = [
    'happiness',
    'sadness',
    'anger',
    'neutral'
]


clf = loadClassifier('./classifier.pkl')

def runCycle(prevEmo, prevState):
    print("Beginning procedure...") 

    # Takes a selfie.
    picture()
    print("Snap!")
    
    # Gets the emotion data for the selfie.
    data = imageRequest('./selfie.jpg')
    print("Scanned image.")
    print(data)
    
    #if os.path.isfile('./selfie.jpg'):
    #    os.remove('./selfie.jpg') # Remove the old picture

    # Return if no faces
    if len(data) == 0:
        print('No faces detected')
        return (prevEmo, prevState)

    # Gets the emotion vector from the image.
    vec = parseEmotion(data)
    print("Acquired sentiment.")

    for i in range(len(subemo)):
        print(subemo[i] + ": " + str(vec[emotions.index(subemo[i])]))

    print('')
    
    # Figure out if the dominant emotion changed
    domEmo = subemo[0]
    for i in range(1, len(subemo)):
        if vec[emotions.index(domEmo)] < vec[emotions.index(subemo[i])]:
            domEmo = subemo[i]

    if prevEmo == domEmo:
        print("Dominant mood unchanged")
        return (prevEmo, prevState)
    else:
        print("Current dominant emotion is " + domEmo)

    # Computes the prediction.
    pred = makePrediction(clf, vec)
    print("Choice vector computed.")
    for i in range(len(pred)):
        print(genres[i] + ": " + str(pred[i]))
    
    # Introduce a small random variability to each value.
    # Remove if bad results are received.
    for i in range(len(genres)):
        pred[i] += random.random() * 0.03

    # Choose the dimension with the highest value.
    choice = 0
    for i in range(1, len(genres)):
        if pred[i] > pred[choice]:
            choice = i

    return (domEmo, genres[choice])
    
    # Play the requested genre
    if prevState != genres[choice]:
        print("Will play " + genres[choice])
        search(genres[choice])

    return (domEmo, genres[choice])

if __name__ == '__main__':
    prevType = ''
    prevEmo = ''
    while True:
        pair = runCycle(prevEmo, prevType)
        prevEmo = pair[0]
        prevType = pair[1]
        time.sleep(15)
else:
    rebuildClassifier()



