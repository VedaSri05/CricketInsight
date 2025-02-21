# Player Runs Prediction

## 📌 Project Overview
This project predicts a cricket player's total runs based on their past performance using Machine Learning. A **Flask API** is deployed with a **modern web UI** to allow users to input player statistics and get instant predictions.

## 🚀 Features
- **Web Scraping**: Data collected from cricket stats websites
- **Machine Learning Model**: Random Forest-based prediction
- **Flask API**: Exposes an endpoint for real-time predictions
- **Interactive Web UI**: Users can input stats and get predictions
- **Power BI Dashboards**: For deeper insights & trends

## 🛠️ Installation & Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo.git
   cd project
   ```
2. **Create a virtual environment**:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run Flask app**:
   ```sh
   python model_deployment/app.py
   ```
5. **Open browser & test**:
   - Visit `http://127.0.0.1:5000/` for the UI
   - Use Postman or Python script to test API

## 🏆 Results & Insights
- **Model Accuracy:** Achieved high precision with **RandomForestRegressor**
- **Power BI Dashboard:** Trends in cricket player performances
