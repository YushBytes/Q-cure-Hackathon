from quantum_model import quantum_drug_similarity

def test_similarity_score():
    """
    Basic test to ensure quantum similarity returns valid value.
    """

    drug1 = {
        "MolecularWeight": 150,
        "Polarity": 1.2,
        "H_Bond_Donors": 1,
        "H_Bond_Acceptors": 2
    }

    drug2 = {
        "MolecularWeight": 200,
        "Polarity": 0.9,
        "H_Bond_Donors": 1,
        "H_Bond_Acceptors": 1
    }

    score = quantum_drug_similarity(drug1, drug2)

    print("Quantum Similarity Score:", score)

    assert 0 <= score <= 1
