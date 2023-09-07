from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load dataset (replace with your actual dataset)
data = pd.read_csv('crop_data.csv')

# Features and target variable
X = data.drop('Crop', axis=1)
y = data['Crop']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier (replace with the appropriate model)
model = RandomForestClassifier()
model.fit(X_train, y_train)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nitrogen = int(request.form['nitrogen'])
        temperature = int(request.form['temperature'])
        rainfall = int(request.form['rainfall'])
        humidity = int(request.form['humidity'])
        ph = float(request.form['ph'])

        input_data = [[nitrogen, temperature, rainfall, humidity, ph]]
        crop_prediction = model.predict(input_data)[0]

        return render_template('index.html', crop_prediction=crop_prediction)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
