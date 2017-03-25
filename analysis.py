import sklearn
from sklearn import datasets, linear_model

# Returns a classifier that analyzes the correlation between data.
def trainOnData(data):
    X = [[pair[0]] for pair in data]
    Y = [pair[1] for pair in data]
    
    # Build a model and train it
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)

    print('Coefficients: \n', regr.coef_)
    return regr



regr = trainOnData([
(0, 0), (1, 1), (2, 2)
])

print(regr.predict([[1], [2], [3]]))
