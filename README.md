# 💊 Q Cure — Quantum Drug Interaction Risk Analyzer  
### Hackathon Submission: Quantum Similarity-Based Drug Interaction Prediction  

Q Cure is a quantum-inspired healthcare application that predicts potential **drug–drug interaction risks** by comparing molecular properties using **real quantum circuit encoding and fidelity similarity**.

This project demonstrates how **quantum computing concepts** can support safer medicine and next-generation drug analysis.

---

## 🏆 Hackathon Innovation Highlights  

### 🎯 Problem Statement  

Drug–drug interactions are a major healthcare challenge:

- Unsafe drug combinations can cause serious side effects  
- Adverse drug reactions increase hospitalization risk  
- Classical tools often lack deeper molecular similarity modeling  

Healthcare needs faster and smarter methods to assess interaction risks.

---

## ⚛️ Quantum Solution  

Q Cure introduces a **Quantum Fidelity-Based Interaction Predictor** that:

✅ Encodes molecular drug descriptors into quantum states  
✅ Computes similarity using quantum fidelity overlap  
✅ Provides real-time interaction risk classification  
✅ Gives transparent technical explanations for users and judges  

---

## 🔬 Technical Architecture  

### 🧬 Molecular Feature Extraction  

Each drug is represented using key molecular descriptors from a dataset:

- Molecular Weight  
- Polarity  
- Hydrogen Bond Donors  
- Hydrogen Bond Acceptors  

These features are normalized before quantum encoding.

---

### ⚛️ Quantum Feature Map Encoding (Qiskit)

Q Cure uses a quantum feature map circuit:

```python
from qiskit.circuit.library import ZZFeatureMap

feature_map = ZZFeatureMap(feature_dimension=4, reps=2)

🚀 Core Features
✅ Quantum Similarity Analysis
Real Qiskit quantum circuit encoding
Fidelity-based similarity measurement
Quantum-inspired drug comparison

✅ Risk Assessment System
Fidelity Score Range	Risk Level
> 0.8	🔴 High Risk
0.5 – 0.8	🟠 Moderate Risk
< 0.5	🟢 Low Risk
✅ Web Application Interface
Flask-based interactive UI
Drug name input form
Instant quantum analysis output

📊 Example Output
Q Cure provides:
Drug Molecular Information
Quantum Similarity Score
Interaction Risk Assessment
Technical Quantum Explanation

🛠 Tech Stack
Python
Flask Web Framework
Qiskit Quantum Simulator
NumPy + Pandas
HTML + CSS Frontend

🌍 Impact
Q Cure can support:
Safer prescriptions
Faster drug screening
Quantum-powered healthcare research
Educational demonstration of quantum similarity

🔮 Future Scope
Integration with PubChem live drug database
Larger FDA-approved drug datasets
Hybrid Quantum + AI interaction prediction
Deployment as a clinical decision support tool
