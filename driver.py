# Emotion analysis module
from emotion import *
from analysis import *

# Song player module
from youtube import *
from picture import *

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


clf = loadClassifier('./classifier.pkl')

def runCycle(prevState):
    print("Beginning procedure...") 

    # Takes a selfie.
    picture()
    print("Snap!")
    
    # Gets the emotion data for the selfie.
    data = imageRequest('./selfie.jpg')
    print("Scanned image.")
    print(data)

    # Gets the emotion vector from the image.
    vec = parseEmotion(data)
    print("Acquired sentiment.")
    for i in range(len(vec)):
        print(emotions[i] + ": " + str(vec[i]))

    print('')

    # Computes the prediction.
    pred = makePrediction(clf, vec)
    print("Choice vector computed.")
    for i in range(len(pred)):
        print(genres[i] + ": " + str(pred[i]))

    # Choose the dimension with the highest value.
    choice = 0
    for i in range(1, len(genres)):
        if pred[i] > pred[choice]:
            choice = i
    
    # Play the requested genre
    if prevState != genres[choice]:
        print("Will play " + genres[choice])
        search(genres[choice])

    return genres[choice]

if __name__ == '__main__':
    runCycle('hi')




