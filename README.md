# diabetes-prediction-pima-indians

Webapp - https://diabetes-prediction-pima-indians.streamlit.app/

This repository contains a Jupyter Notebook for predicting diabetes using machine learning techniques. Below is an overview of the contents and steps involved:

Getting Started
To run the notebook, you can use Google Colab or any Jupyter Notebook environment. The notebook assumes you have basic knowledge of Python and machine learning concepts.

Prerequisites
Python 3.x
Jupyter Notebook or Google Colab

Contents
Setup: The notebook starts with importing necessary libraries and mounting Google Drive (if using Colab).

About Dataset: This section provides context about the dataset used for predicting diabetes, including its source, content, and acknowledgments.

Data Exploration and Preprocessing: Here, the dataset is loaded, and initial exploratory data analysis (EDA) is performed. It includes checking for missing values, duplicates, and zero values in the dataset. Features are visualized through histograms and boxplots. Data preprocessing steps such as handling missing values and feature selection are also conducted.

Model Building: The dataset is split into training and testing sets. Three models (Logistic Regression, Support Vector Machine, Random Forest) are trained and evaluated with varying numbers of features (k). Results are visualized and analyzed to determine the best model and optimal number of features.

Evaluation and Saving the Model: Model evaluation metrics such as accuracy, precision, recall, and F1-score are calculated using cross-validation. Additionally, a final model is trained using selected features, and the model is saved to a file using pickle.

Predictions: Finally, the saved model is loaded, and predictions are made on new data. A sample input is provided to demonstrate how to use the trained model for prediction.

Running the Notebook
You can run the notebook cell by cell to understand each step and its output. Make sure to install necessary packages if running locally (pip install -U scikit-learn).

Authors
Bamise Omolaso

Acknowledgments
Original dataset: National Institute of Diabetes and Digestive and Kidney Diseases
Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). "Using the ADAP learning algorithm to forecast the onset of diabetes mellitus."
License
This project is licensed under the MIT License.
