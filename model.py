import os
from flask import Flask, request, jsonify

# إنشاء تطبيق Flask
app = Flask(__name__)

# مسار رئيسي للتأكد أن السيرفر شغال
@app.route('/')
def home():
    return "Clinic AI App is running successfully on Render!"

# مثال: API للتشخيص حسب الأعراض
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = data.get("symptoms", "").lower()

    if "fever" in symptoms and "cough" in symptoms:
        diagnosis = "Flu"
        recommendation = "Rest + Flu Medication"
    elif "headache" in symptoms:
        diagnosis = "Migraine"
        recommendation = "Painkillers and rest"
    else:
        diagnosis = "Unknown"
        recommendation = "Consult a doctor"

    return jsonify({
        "diagnosis": diagnosis,
        "recommendation": recommendation
    })

# تشغيل التطبيق
if __name__ == "__main__":
    # Render يحدد البورت في متغير بيئة اسمه PORT
    port = int(os.environ.get("PORT", 5000))
    # لازم نخلي السيرفر يسمع على كل الشبكة مش localhost
    app.run(host="0.0.0.0", port=port)
