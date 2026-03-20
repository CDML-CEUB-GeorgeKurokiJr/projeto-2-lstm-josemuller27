from sklearn.preprocessing import MinMaxScaler
import numpy as np

def preprocess(data, window=60):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data.values.reshape(-1,1))

    X, y = [], []
    for i in range(window, len(scaled)):
        X.append(scaled[i-window:i])
        y.append(scaled[i])

    return np.array(X), np.array(y), scaler
