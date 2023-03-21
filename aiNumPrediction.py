# Import necessary libraries
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load dataset
dataset = pd.read_csv('dataset.csv')

# Split dataset into input and output variables
X = dataset.iloc[:, :3].values
y = dataset.iloc[:, 3:].values

# Normalize input data
X = (X - X.min()) / (X.max() - X.min())

# Build neural network model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=3))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=10, activation='sigmoid'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=100, batch_size=32)

# Predict values
input_data = np.array([[12, 5, 2022]])
input_data = (input_data - X.min()) / (X.max() - X.min())
predicted_values = model.predict(input_data)

# Print predicted values
print(predicted_values)