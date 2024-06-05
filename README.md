<p align="center"><img alt="image" src="pictures/image.png" /></p>

# House Price Predictor Project

This project is a web application for predicting house prices in California using machine learning (I use a sklearn dataset *fetch_california_housing*). Users can input various characteristics of a house, and based on this data, the model predicts the price of the house.

## Project Structure

```
house_price_predictor/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── forms.py
│ └── templates/
│ ├── base.html
│ ├── index.html
├── models/
│ ├── train_model.py
│ └── model.pkl
├── run.py
└── requirements.txt
```

- `app/`: Directory containing the code for the web application.
  - `routes.py`: Application routes.
  - `forms.py`: Form definition for data input.
  - `templates/`: HTML templates for displaying the user interface.
- `models/`: Directory containing files for model training and the saved trained model.
  - `model.pkl`: Trained model
  - `train_model.py`: Model training file
- `run.py`: File to run the web application.
- `requirements.txt`: Project dependencies file.

## Input Data

Users can input the following house characteristics for price prediction:

1. **Median Income (Median Income)**: Median household income in the area (in tens of thousands of dollars).
2. **House Age (House Age)**: Average house age in the area (in years).
3. **Average Number of Rooms (Average Rooms)**: Average number of rooms in the house.
4. **Average Number of Bedrooms (Average Bedrooms)**: Average number of bedrooms in the house.
5. **Population (Population)**: Population of the area.
6. **Average Occupancy (Average Occupancy)**: Average house occupancy.
7. **Latitude (Latitude)**: Geographic latitude of the area.
8. **Longitude (Longitude)**: Geographic longitude of the area.

## Output Data

1. **Predicted House Price**: Predicted house price based on the entered data
2. **Rounded Prediction**: Rounded house price

## Usage example

If you want to predict the value of a house with the following characteristics:

- Median Income: 60 000$
- House Age: 25 years
- Average Rooms: 7
- Average Bedrooms: 3
- Population: 2500 people
- Average Occupancy: 3.5 people
- Latitude: 34.05
- Longitude: -118.25

Then the form will be filled out as follows:
- Median Income: 6.0
- House Age: 25.0
- Average Number of Rooms: 7.0
- Average Number of Bedrooms: 3.0
- Population: 2500.0
- Average Occupancy: 3.5
- Latitude: 34.05
- Longitude: -118.25

## Running the Application

1. Install the repository

```sh
git clone https://github.com/Bebrowskiy/house-price-predictor.git
```

2. Install dependencies

```sh
pip install -r requirements.txt
```

3. Train the model

```sh
python models/train_model.py
```

4. Run the web application

```sh
python run.py
```

Then, open a web browser and go to `http://127.0.0.1:5000/` to start using the application.
