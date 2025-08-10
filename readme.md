# 📊 Flask Loan Prediction API

## 🛠 Tech Stack
- **Python 3.x**
- **Flask** (for API creation)
- **Pickle** (for loading trained ML model)
- **Postman** (for API testing)
- **scikit-learn** (for training the model)

---

## 📌 Features
- `/ping` endpoint for health check.
- `/predict` endpoint to send loan application details and receive prediction.
- Encodes categorical values (`Gender`, `Married`) into numeric form for the ML model.
- Returns `"Loan accepted"` or `"Loan rejected"`.

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
pip install flask scikit-learn

# 4. Ensure 'model.pkl' is present in the project directory

# 5. Run the Flask app
python app.py


Open Postman.

Set request method to PUT.

Use the URL:

arduino
Copy
Edit
http://127.0.0.1:5000/predict
In the Body tab → Select raw → Choose JSON.

Paste this JSON:

json
Copy
Edit
{
  "Gender": "Female",
  "Married": "Yes",
  "ApplicantIncome": 15000,
  "LoanAmount": 15000,
  "Credit_History": 0
}