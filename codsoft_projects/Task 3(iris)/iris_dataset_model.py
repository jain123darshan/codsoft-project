# -*- coding: utf-8 -*-
"""iris_dataset_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HYYn_6L38_oaobn1OB2wFEIZZUVa1yGe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Load the Iris dataset
file_path = '/content/drive/MyDrive/iris.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
df.head()

# Check for missing values
df.isnull().sum()

# Check the data types
df.dtypes

# Separate features (sepal length, sepal width, petal length, petal width) and target (species)
X = df.drop('species', axis=1)
y = df['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features (optional but recommended for KNN and other distance-based algorithms)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))

import seaborn as sns
import matplotlib.pyplot as plt


sns.pairplot(df, hue='species')
plt.show()

df

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from IPython.display import display
import ipywidgets as widgets


from google.colab import drive
drive.mount('/content/drive')


file_path = '/content/drive/MyDrive/iris.csv'
df = pd.read_csv(file_path)


def preprocess_and_train(file_path):
    df = pd.read_csv(file_path)


    X = df.drop('species', axis=1)
    y = df['species']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train KNN classifier
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    # Make predictions
    y_pred = knn.predict(X_test)

    # Calculate metrics
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)

    # Display results
    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(cr)
    print("\nAccuracy Score:", acc)

    # Plot pairplot
    sns.pairplot(df, hue='species')
    plt.show()

# Create widgets for user interface
file_path_widget = widgets.Text(
    value='/content/drive/MyDrive/iris.csv',
    placeholder='Enter file path',
    description='File Path:',
    disabled=False
)

button = widgets.Button(description="Load and Analyze Data")

# Define function to handle button click event
def on_button_clicked(b):
    file_path = file_path_widget.value
    preprocess_and_train(file_path)

# Attach function to button click event
button.on_click(on_button_clicked)

# Display widgets
display(file_path_widget)
display(button)