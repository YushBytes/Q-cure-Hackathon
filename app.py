from flask import Flask, request, render_template
from quantum_model import quantum_drug_similarity, risk_assessment
from utils import load_drug_data, get_drug_features

app = Flask(__name__)

drug_data = load_drug_data("drug_dataset.csv")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    drug1 = request.form.get("drug1")
    drug2 = request.form.get("drug2")

    features1 = get_drug_features(drug1, drug_data)
    features2 = get_drug_features(drug2, drug_data)

    if features1 is None or features2 is None:
        return render_template("index.html", result={
            "Drug 1": drug1,
            "Drug 2": drug2,
            "Quantum Chemistry Analysis": {
                "Quantum Similarity Score": "N/A"
            },
            "Risk Assessment": "Drug not found in dataset!",
            "Technical Details": {
                "Quantum Metric": "Dataset Matching Failed"
            }
        })

    similarity = quantum_drug_similarity(features1, features2)
    risk = risk_assessment(similarity)

    result = {
        "Drug 1": drug1,
        "Drug 2": drug2,
        "Quantum Chemistry Analysis": {
            "Quantum Similarity Score": similarity
        },
        "Risk Assessment": risk,
        "Technical Details": {
            "Quantum Metric": "Fidelity Similarity using Qiskit Feature Map"
        }
    }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
