import numpy as np
import tensorflow
from tf.keras.layers import Dense
from tf.keras.models import Sequential

# Generate some synthetic data
X = np.random.rand(1000, 6)
y = np.zeros(1000)

# Assign labels to the data based on the size of the balls
for i in range(1000):
    if X[i, 0] > X[i, 1] > X[i, 2] > X[i, 3] > X[i, 4] > X[i, 5]:
        y[i] = 1

# Convert labels to categorical format
y = np.eye(2)[y.astype(int)]

# Define the model
model = Sequential()
model.add(Dense(64, input_dim=6, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model to the data
model.fit(X, y, epochs=10, batch_size=32)
