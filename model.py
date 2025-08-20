from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
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

    # لازم نرجع JSON
    return jsonify({
        "diagnosis": diagnosis,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run()
