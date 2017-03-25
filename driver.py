# Emotion analysis module
import emotion
import analysis

# Song player module
import youtube

# Takes the photograph.
def takePicture():
    print("TODO: Take pictures")

# The list of currently supported genres
genres = ['pop', 'edm', 'rock']

clf = loadClassifier('./classifier.pkl')

def runCycle(prevState):
    
    # Takes a selfie.
    takePicture()
    
    # Gets the emotion data for the selfie.
    data = imageRequest('./selfie.jpg')

    # Gets the emotion vector from the image.
    vec = parseEmotion(data)

    # Computes the prediction.
    pred = makePrediction(clf, pred)

    # Choose the dimension with the highest value.
    choice = 0
    for i in range(1, len(genres)):
        if vec[i] > vec[choice]:
            choice = i

    # Play the requested genre
    search(genres[choice])






