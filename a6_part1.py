"""
Assignment 6 Part 1: Student Performance Prediction
Name: Frank McCrudden
Date: 11/21/2025

This assignment predicts student test scores based on hours studied.
Complete all the functions below following the in-class ice cream example.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def load_and_explore_data(filename):
    # TODO: Load the CSV file using pandas
    data = pd.read_csv(filename)
    # TODO: Print the first 5 rows
    print("=== Student Scores Data ===")
    print(f"\nFirst 5 rows:")
    print(data.head())
    # TODO: Print the shape of the dataset (number of rows and columns)
    print(f"\nDataset shape: {data.shape[0]} rows, {data.shape[1]} columns")
    # TODO: Print basic statistics (mean, min, max, etc.)
    print(f"\nBasic statistics:")
    print(data.describe())
    # TODO: Return the dataframe
    return data


def create_scatter_plot(data):
    # TODO: Create a figure with size (10, 6)
    plt.figure(figsize=(10, 6))
    # TODO: Create a scatter plot with Hours on x-axis and Scores on y-axis
    #       Use color='purple' and alpha=0.6
    plt.scatter(data['Hours'], data['Scores'], color='purple', alpha=0.6)
    # TODO: Add x-axis label: 'Hours Studied'
    plt.xlabel('Hours Studied', fontsize=12)
    # TODO: Add y-axis label: 'Test Score'
    plt.ylabel('Test Scores', fontsize=12)
    # TODO: Add title: 'Student Test Scores vs Hours Studied'
    plt.title('Student Test Scores vs Hours Studied', fontsize=14, fontweight='bold')
    # TODO: Add a grid with alpha=0.3
    plt.grid(True, alpha=0.3)
    # TODO: Save the figure as 'scatter_plot.png' with dpi=300
    plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
    # TODO: Show the plot
    plt.show()


def split_data(data):
    # TODO: Create X with the 'Hours' column (use double brackets to keep as DataFrame)
    
    # TODO: Create y with the 'Scores' column
    
    # TODO: Split the data using train_test_split with test_size=0.2 and random_state=42
    
    # TODO: Print how many samples are in training and testing sets
    
    # TODO: Return X_train, X_test, y_train, y_test
    pass


def train_model(X_train, y_train):
    # TODO: Create a LinearRegression model
    
    # TODO: Train the model using .fit()
    
    # TODO: Print the coefficient (slope) and intercept
    
    # TODO: Return the trained model
    pass


def evaluate_model(model, X_test, y_test):
    # TODO: Make predictions using the model
    
    # TODO: Calculate R² score using r2_score()
    
    # TODO: Calculate Mean Squared Error using mean_squared_error()
    
    # TODO: Calculate Root Mean Squared Error (square root of MSE)
    
    # TODO: Print all three metrics with clear labels
    
    # TODO: Return the predictions
    pass


def visualize_results(X_train, y_train, X_test, y_test, predictions, model):
    # TODO: Create a figure with size (12, 6)
    
    # TODO: Plot training data as blue scatter points with label 'Training Data'
    
    # TODO: Plot test data (actual) as green scatter points with label 'Test Data (Actual)'
    
    # TODO: Plot predictions as red X markers with label 'Predictions'
    
    # TODO: Create and plot the line of best fit
    #       Hint: Create a range of X values, predict Y values, then plot as a black line
    
    # TODO: Add x-axis label, y-axis label, and title
    
    # TODO: Add legend
    
    # TODO: Add grid with alpha=0.3
    
    # TODO: Save the figure as 'predictions_plot.png' with dpi=300
    
    # TODO: Show the plot
    pass


def make_prediction(model, hours):
    # TODO: Reshape hours into the format the model expects: np.array([[hours]])
    
    # TODO: Make a prediction
    
    # TODO: Print the prediction with a clear message
    
    # TODO: Return the predicted score
    pass


if __name__ == "__main__":
    print("=" * 70)
    print("STUDENT PERFORMANCE PREDICTION - YOUR ASSIGNMENT")
    print("=" * 70)
    
    # Step 1: Load and explore the data
    # TODO: Call load_and_explore_data() with 'student_scores.csv'
    data = load_and_explore_data('student_scores.csv')

    # Step 2: Visualize the relationship
    # TODO: Call create_scatter_plot() with the data
    create_scatter_plot(data)
    # Step 3: Split the data
    # TODO: Call split_data() and store the returned values
    
    # Step 4: Train the model
    # TODO: Call train_model() with training data
    
    # Step 5: Evaluate the model
    # TODO: Call evaluate_model() with the model and test data
    
    # Step 6: Visualize results
    # TODO: Call visualize_results() with all the necessary arguments
    
    # Step 7: Make a new prediction
    # TODO: Call make_prediction() for a student who studied 7 hours
    
    print("\n" + "=" * 70)
    print("✓ Assignment complete! Check your saved plots.")
    print("Don't forget to complete a6_part1_writeup.md!")
    print("=" * 70) 