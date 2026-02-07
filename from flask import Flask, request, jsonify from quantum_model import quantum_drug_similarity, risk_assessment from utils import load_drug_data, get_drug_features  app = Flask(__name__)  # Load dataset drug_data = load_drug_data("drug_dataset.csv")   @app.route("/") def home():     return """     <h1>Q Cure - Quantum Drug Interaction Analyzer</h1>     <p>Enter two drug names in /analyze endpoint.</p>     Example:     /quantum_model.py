import numpy as np


def quantum_drug_similarity(features1, features2):
    """
    Quantum-inspired similarity calculation.

    We simulate how quantum circuits compare drug molecules
    by converting features into normalized quantum states.
    """

    v1 = np.array(list(features1.values()))
    v2 = np.array(list(features2.values()))

    # Normalize vectors (like quantum state normalization)
    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)

    # Fidelity similarity (dot product squared)
    fidelity = np.dot(v1, v2) ** 2

    return round(float(fidelity), 4)


def risk_assessment(similarity_score):
    """
    Convert similarity score into interaction risk levels.
    """

    if similarity_score > 0.8:
        return "High Interaction Risk"
    elif similarity_score > 0.5:
        return "Moderate Interaction Risk"
    else:
        return "Low Interaction Risk"
