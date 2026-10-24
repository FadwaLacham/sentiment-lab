
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report,
)

LABELS = ["negative", "neutral", "positive"]


def normalize_reference_labels(series: pd.Series) -> pd.Series:
    """Uniformise les sentiments de référence en français ou anglais."""
    return (
        series.astype(str)
        .str.strip()
        .str.lower()
        .replace({
            "positif": "positive",
            "négatif": "negative",
            "negatif": "negative",
            "neutre": "neutral",
        })
    )


def calculate_metrics(y_true, y_pred) -> dict:
    """Calcule les principales métriques de classification."""
    accuracy = accuracy_score(y_true, y_pred)

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=LABELS,
        average="macro",
        zero_division=0,
    )

    matrix = confusion_matrix(y_true, y_pred, labels=LABELS)

    report = classification_report(
        y_true,
        y_pred,
        labels=LABELS,
        output_dict=True,
        zero_division=0,
    )

    return {
        "accuracy": accuracy,
        "precision_macro": precision,
        "recall_macro": recall,
        "f1_macro": f1,
        "confusion_matrix": pd.DataFrame(
            matrix,
            index=LABELS,
            columns=LABELS,
        ),
        "classification_report": pd.DataFrame(report).transpose(),
    }
