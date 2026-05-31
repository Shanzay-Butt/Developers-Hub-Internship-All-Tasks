# Task 2: Predict Future Stock Prices (Short-Term)

## Objective
The objective of this task is to use historical stock market data to predict the next day's closing price using machine learning techniques.

## Dataset
Historical stock data was retrieved from Yahoo Finance using the `yfinance` library.

### Features Used
- Open Price
- High Price
- Low Price
- Volume

### Target Variable
- Next Day Closing Price

## Tools and Libraries
- Python
- Pandas
- NumPy
- yfinance
- Scikit-learn
- Matplotlib
- Seaborn

## Methodology

### Data Collection
- Downloaded historical stock data using the `yfinance` library.
- Selected a stock (e.g., Apple - AAPL).

### Data Preprocessing
- Cleaned and prepared the dataset.
- Created the target variable by shifting the closing price by one day.

### Model Training
- Split the dataset into training and testing sets.
- Trained a machine learning model:
  - Linear Regression / Random Forest Regressor

### Evaluation
- Predicted closing prices on the test set.
- Compared actual and predicted values.

### Visualization
- Created a line plot showing:
  - Actual Closing Prices
  - Predicted Closing Prices

## Results
The model was able to learn patterns from historical stock data and generate short-term price predictions. Performance was evaluated by comparing predicted values with actual closing prices.

## How to Run

1. Install required libraries:

```bash
pip install pandas numpy yfinance scikit-learn matplotlib seaborn
```

2. Run the Python script:

```bash
python task2.py
```

## Author
Shanzay Mahmood
