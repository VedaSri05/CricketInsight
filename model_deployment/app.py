from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("C:/vedasri/Projects/Sports Data Analysis/model_deployment/final_model.pkl")

# Define route for homepage
@app.route('/')
def home():
    return render_template('index.html')  # Correct relative path # Optional UI

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract values correctly
        features = np.array([
            data['total_matches'], data['innings'], 
            data['average_score'], data['strike_rate'], 
            data['highest_score'], data['fours'], 
            data['sixes'], data['fifties'], data['hundreds']
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        # Return result
        return jsonify({'predicted_total_runs': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
