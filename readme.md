# Flask Loan Prediction API

A simple Flask-based REST API for predicting loan approval status using a trained machine learning model (`model.pkl`).

## 📌 Features
- `/ping` endpoint for health check
- `/predict` endpoint to send loan application details and receive prediction
- Encodes categorical values for `Gender` and `Married`
- Returns `"Loan accepted"` or `"Loan rejected"`

---

## 🚀 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install flask

# 4. Ensure 'model.pkl' is present in the project directory

# 5. Run the Flask app
python app.py
