import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers

# Example training data

data = pd.read_csv('Superena.csv')

data = np.array(data[["Day","Month","Year","Digit1","Digit2","Digit3","Digit4","Digit5","Digit6"]]
    # more training data here...
)

# Scale the random numbers to range between 0 and 1
data[:, 3:] = data[:, 3:] / 90.0

# Split the data into input (date) and output (random numbers) arrays
input_data = data[:, :3]  # day, month, year
output_data = data[:, 3:]  # random numbers

# Define the neural network architecture
model = keras.Sequential([
    layers.Dense(16, activation='relu', input_shape=(3,)),
    layers.Dense(16, activation='relu'),
    layers.Dense(6, activation='sigmoid')  # output between 0 and 1
])

# Compile the model with mean squared error loss and Adam optimizer
model.compile(loss='mse', optimizer='adam')

# Train the model
model.fit(input_data, output_data, epochs=100)

# Example usage to predict the random numbers for a given date
day=int(input("Please enter the day: "))
month=int(input("Please enter the month: "))
year=int(input("Please enter the year: "))

date = [day, month, year]  # day, month, year
predicted_numbers = model.predict(np.array([date])) * 90.0  # scale back to 1-90 range
print(predicted_numbers)
