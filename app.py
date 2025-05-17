from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    symptoms = data.get("symptoms", [])
    diagnosis = random.choice(["Diabetes", "Hypertension", "Flu", "Normal"])
    return jsonify({"diagnosis": diagnosis})

@app.route('/monitor', methods=['POST'])
def monitor():
    data = request.json
    return jsonify({
        "status": "Data received",
        "heart_rate": data.get("heart_rate"),
        "temperature": data.get("temperature"),
        "spo2": data.get("spo2")
    })

@app.route('/get_patient_data/<patient_id>', methods=['GET'])
def get_patient_data(patient_id):
    # Placeholder patient data
    return jsonify({
        "id": patient_id,
        "name": "John Doe",
        "age": 45,
        "history": ["Diabetes", "Hypertension"]
    })

@app.route('/recommend_treatment', methods=['POST'])
def recommend_treatment():
    data = request.json
    condition = data.get("condition", "Unknown")
    recommendations = {
        "Diabetes": "Insulin therapy, low sugar diet, regular monitoring.",
        "Hypertension": "Low-sodium diet, beta-blockers, exercise.",
        "Flu": "Rest, fluids, antivirals.",
        "Normal": "Healthy lifestyle maintenance."
    }
    return jsonify({"recommendation": recommendations.get(condition, "Consult a doctor.")})

if __name__ == '__main__':
    app.run(debug=True)
