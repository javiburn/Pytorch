# Sentiment Analysis on Movie Reviews

## Introduction

In this project, you'll build a sentiment analysis model using PyTorch and process a dataset of movie reviews with Apache Spark. The goal is to classify reviews as positive or negative. This project will help you understand the basics of data preprocessing with Spark and building and training neural networks with PyTorch.

## Mandatory Part

### 1. Setting Up the Environment

Install necessary packages:
- PySpark
- PyTorch
- TorchText (for text processing)

### 2. Data Preprocessing with Spark

- Load the dataset (e.g., CSV file with movie reviews and their corresponding sentiments) into a Spark DataFrame.
- Clean the text data (remove punctuation, lowercasing, etc.).
- Split the data into training and testing sets.

### 3. Building the Model with PyTorch

- Create a simple neural network with an embedding layer, LSTM, and a linear layer.
- Define loss function and optimizer.

### 4. Training the Model

- Train the model using the training data.
- Evaluate the model using the testing data.

### 5. Submission and Evaluation

Submit the project on your Git repository.