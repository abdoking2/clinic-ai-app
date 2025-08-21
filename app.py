import os
from flask import Flask, request, jsonify, render_template

# إنشاء تطبيق Flask
app = Flask(__name__)

# الصفحة الرئيسية (واجهة الويب)
@app.route('/')
def home():
    return render_template("index.html")

# API للتجربة (مثال بسيط للتشخيص)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = data.get("symptoms", "").lower()

    if "fever" in symptoms and "cough" in symptoms:
        diagnosis = "Flu"
        recommendation = "Rest + Flu Medication"
    elif "headache" in symptoms:
        diagnosis = "Migraine"
        recommendation = "Painkiller + Rest"
    else:
        diagnosis = "Unknown"
        recommendation = "Consult a doctor"

    return jsonify({
        "diagnosis": diagnosis,
        "recommendation": recommendation
    })

# تشغيل محلي
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
