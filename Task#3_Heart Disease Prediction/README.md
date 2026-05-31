# Task 3: Heart Disease Prediction

## Objective
The objective of this project is to predict whether a person is at risk of heart disease based on medical and health-related attributes using machine learning techniques.

## Dataset
This project uses the Heart Disease Dataset obtained from Kaggle.

## Features
The dataset contains several health indicators, including:
- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope
- HeartDisease


## Tools and Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

## Project Workflow

### 1. Data Cleaning
- Loaded the dataset.
- Checked for missing values.
- Cleaned and prepared the data for analysis.

### 2. Exploratory Data Analysis (EDA)
- Analyzed feature distributions.
- Examined relationships between variables.
- Visualized trends using charts and graphs.

### 3. Model Training
- Split the dataset into training and testing sets.
- Trained a classification model:
  - Logistic Regression
    
### 4. Model Evaluation
The model was evaluated using:
- Accuracy Score
- Classification Report
- F1 score
- Confusion Matrix

### 5. Streamlit Web Application
A user-friendly Streamlit interface was developed to:
- Enter patient health information.
- Predict heart disease.
- Display prediction results interactively.

## Results
The trained model successfully predicts the likelihood of heart disease based on patient health data and provides predictions through an interactive web interface.

## How to Run

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### Run the Streamlit App

```bash
streamlit run app.py
```

## Project Structure

```text
Task3/
├── heart_app.py
├── scaler.pkl
├── heart.csv
├── heart_risk.ipynb
├── LG_heart.txt
└── columns.pkl
```

## Author
Shanzay Mahmood
