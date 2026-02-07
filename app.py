from flask import Flask, request, jsonify
from quantum_model import quantum_drug_similarity, risk_assessment
from utils import load_drug_data, get_drug_features

app = Flask(__name__)

# Load dataset
drug_data = load_drug_data("drug_dataset.csv")


@app.route("/")
def home():
    return """
    <h1>Q Cure - Quantum Drug Interaction Analyzer</h1>
    <p>Enter two drug names in /analyze endpoint.</p>
    Example:
    /analyze?drug1=Paracetamol&drug2=Ibuprofen
    """


@app.route("/analyze", methods=["GET"])
def analyze():
    drug1 = request.args.get("drug1")
    drug2 = request.args.get("drug2")

    if not drug1 or not drug2:
        return jsonify({"error": "Please provide two drug names"}), 400

    # Extract molecular features
    features1 = get_drug_features(drug1, drug_data)
    features2 = get_drug_features(drug2, drug_data)

    if features1 is None or features2 is None:
        return jsonify({"error": "Drug not found in dataset"}), 404

    # Quantum similarity score
    similarity = quantum_drug_similarity(features1, features2)

    # Risk prediction
    risk = risk_assessment(similarity)

    # Output
    result = {
        "Drug 1": drug1,
        "Drug 2": drug2,
        "Molecular Info": {
            drug1: features1,
            drug2: features2
        },
        "Quantum Chemistry Analysis": {
            "Quantum Similarity Score": similarity
        },
        "Risk Assessment": risk,
        "Technical Details": {
            "Quantum Encoding": "Feature Map Encoding",
            "Quantum Metric": "State Fidelity Similarity",
            "Prediction Logic": "High similarity → Higher interaction risk"
        }
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
