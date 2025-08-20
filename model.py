import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Clinic AI App is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data or "symptoms" not in data:
            return jsonify({"error": "Please provide symptoms in JSON format"}), 400

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

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # مهم في Render: لازم نحدد host="0.0.0.0"
    app.run(host="0.0.0.0", port=5000, debug=True)

