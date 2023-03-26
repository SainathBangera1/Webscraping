# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Load dataset
dataset = pd.read_csv('superPERCENT_HORIZONTAL.csv')

# Convert date columns to datetime objects
dataset['date'] = pd.to_datetime(dataset[['year', 'month', 'day']])
dataset.drop(['day', 'month', 'year'], axis=1, inplace=True)

# Split dataset into training and testing sets
X = dataset.drop('output', axis=1)
y = dataset['output']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to predict outputs for a given date
def predict_output(day, month, year):
    date = datetime(year, month, day)
    input_data = pd.DataFrame({'date': [date]})
    input_data['year'] = input_data['date'].dt.year
    input_data['month'] = input_data['date'].dt.month
    input_data['day'] = input_data['date'].dt.day
    input_data.drop(['date'], axis=1, inplace=True)
    output = model.predict(input_data)
    return output

# Example usage
day = 16
month = 3
year = 2023
predicted_output = predict_output(day, month, year)
print(predicted_output)
#######################333###################################################################################################################################################################################################################################

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv('dataset.csv')

# Separate features and target variable
X = data.iloc[:, :-6] # Day, month, year
y = data.iloc[:, -6:] # Six numbers

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model architecture
model = keras.Sequential([
    keras.layers.Dense(64, input_shape=(3,), activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(6, activation='linear')
])

# Compile the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32)

# Take input for prediction
day = input("Enter day: ")
month = input("Enter month: ")
year = input("Enter year: ")

# Convert input to numpy array format
new_data = np.array([[day, month, year]])

# Make prediction
prediction = model.predict(new_data)

# Output prediction
print("Predicted six numbers are: ", prediction)
