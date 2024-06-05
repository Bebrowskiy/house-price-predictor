import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def load_data():
    from sklearn.datasets import fetch_california_housing
    data = fetch_california_housing()
    df = pd.DataFrame(data=data.data, columns=data.feature_names)
    df['MedHouseVal'] = data.target
    return df

def preprocess_data(df):
    x = df.drop('MedHouseVal', axis=1)
    y = df['MedHouseVal']
    return train_test_split(x, y, test_size=0.2, random_state=42)

def train_model():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df=df)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    
    joblib.dump(model, 'models/model.pkl')
    print("Model saved!")
    
if __name__ == "__main__":
    train_model()