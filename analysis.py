import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn import datasets, linear_model

# Returns a classifier that analyzes the correlation between data.
def trainOnData(data):
    X = [pair[0] for pair in data]
    Y = [pair[1] for pair in data]

    print("X: " + str(X))
    print("Y: " + str(Y))
    
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
    clf.fit(X, Y)
    
    """
    MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
                beta_1=0.9, beta_2=0.999, early_stopping=False,
                epsilon=1e-08, hidden_layer_sizes=(15,), learning_rate='constant',
                learning_rate_init=0.001, max_iter=200, momentum=0.9,
                nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
                solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
                warm_start=False)
    """

    return clf



clf = trainOnData([
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
])

