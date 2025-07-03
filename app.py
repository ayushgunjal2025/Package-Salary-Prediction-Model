from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Load both models
simple_model = joblib.load("model_simple.joblib")
multi_model = joblib.load("model_multi.joblib")

@app.route("/")
def home():
    return "API is live!"

@app.route("/predict/package")
def predict_package():
    try:
        cgpa = float(request.args.get("cgpa", 0))
        result = simple_model.predict([[cgpa]])[0]
        return jsonify(package=round(result, 2))
    except:
        return jsonify(error="Invalid CGPA")

@app.route("/predict/salary")
def predict_salary():
    try:
        age = float(request.args.get("age"))
        exp = float(request.args.get("exp"))
        result = multi_model.predict([[age, exp]])[0]
        return jsonify(salary=round(result, 2))
    except:
        return jsonify(error="Invalid age or experience")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
