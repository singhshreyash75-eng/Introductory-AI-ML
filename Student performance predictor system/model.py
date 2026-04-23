import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([
    [2,70,6],[5,80,7],[7,90,8],
    [1,60,5],[4,75,6],[6,85,7]
])

y = np.array([50,65,80,40,60,75])

model = LinearRegression()
model.fit(X,y)

def predict(data):
    return model.predict([data])[0]