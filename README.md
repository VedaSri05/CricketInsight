# 🏏 CricketInsight

A machine learning-powered web application that predicts a cricket player's total career runs based on their stats such as average, strike rate, and innings data.

## 🔗 Data Source
Player statistics were scraped from the official BCCI website:  
👉 [BCCI Test Stats - International Men](https://www.bcci.tv/international/men/stats/test)

## 🧠 Tech Stack

- **Backend**: Python, Flask, Scikit-Learn
- **Scraping**: BeautifulSoup, Selenium
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Power BI
- **Frontend**: HTML, CSS, JavaScript


## ⚙️ How to Run the Model Locally

### 1. Clone the Repository
git clone https://github.com/VedaSri05/CricketInsight.git
cd CricketInsight
### 2. Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
### 3. Install Dependencies
pip install -r requirements.txt
If requirements.txt is not available, install manually:
pip install flask pandas numpy scikit-learn matplotlib seaborn selenium beautifulsoup4
### 4. Run the Application
python app.py
Then open your browser and navigate to:
http://127.0.0.1:5000/

## 📊 Visualization
Comprehensive insights into player performance trends are visualized using Power BI. These dashboards help interpret model predictions and underlying patterns effectively.
![image](https://github.com/user-attachments/assets/efd7ccd6-c1f9-498b-bb2a-69fa9dd21b4d)

