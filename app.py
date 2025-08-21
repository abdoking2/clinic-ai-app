import os
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# الصفحة الرئيسية: تعرض index.html الموجود بجانب app.py
@app.route("/")
def home():
    return send_file("index.html")

# مثال API للتجربة
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    symptoms = data.get("symptoms", "").lower()

    if "fever" in symptoms and "cough" in symptoms:
        diagnosis = "Flu"
        recommendation = "Rest + Flu Medication"
    elif "headache" in symptoms:
        diagnosis = "Migraine"
        recommendation = "Painkillers + Rest"
    else:
        diagnosis = "Unknown"
        recommendation = "Consult a doctor"

    return jsonify({
        "diagnosis": diagnosis,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
