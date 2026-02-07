import pandas as pd


def load_drug_data(filename):
    return pd.read_csv(filename)


def get_drug_features(drug_name, dataset):
    """
    Returns molecular features from dataset.
    """

    row = dataset[dataset["Drug"] == drug_name]

    if row.empty:
        return None

    return {
        "MolecularWeight": float(row["MolecularWeight"].values[0]),
        "Polarity": float(row["Polarity"].values[0]),
        "H_Bond_Donors": float(row["H_Bond_Donors"].values[0]),
        "H_Bond_Acceptors": float(row["H_Bond_Acceptors"].values[0])
    }
