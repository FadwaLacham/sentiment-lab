
import pandas as pd


def read_file(uploaded_file) -> pd.DataFrame:
    """Lit un fichier CSV ou Excel et retourne un DataFrame."""
    filename = uploaded_file.name.lower()

    if filename.endswith(".csv"):
        return pd.read_csv(uploaded_file, sep=None, engine="python")

    if filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(uploaded_file)

    raise ValueError(
        "Format non pris en charge. Utilise un fichier CSV ou Excel."
    )
