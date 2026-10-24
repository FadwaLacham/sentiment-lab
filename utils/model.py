
import os
import streamlit as st

LOCAL_MODEL = "./modele_sentiment"
REMOTE_MODEL = "cardiffnlp/twitter-xlm-roberta-base-sentiment"

MODEL_ID = (
    LOCAL_MODEL
    if os.path.isdir(LOCAL_MODEL)
    else REMOTE_MODEL
)

LABELS = ["negative", "neutral", "positive"]


@st.cache_resource
def load_model():
    from transformers import pipeline

    return pipeline(
        "sentiment-analysis",
        model=MODEL_ID,
        tokenizer=MODEL_ID,
        local_files_only=(MODEL_ID == LOCAL_MODEL),
        device=-1,
    )


def normalize_label(label: str) -> str:
    label = str(label).lower()

    if "negative" in label or label == "label_0":
        return "negative"
    if "neutral" in label or label == "label_1":
        return "neutral"
    if "positive" in label or label == "label_2":
        return "positive"

    return label


def analyze_comments(model, comments: list[str]) -> list[dict]:
    if not comments:
        return []

    predictions = model(
        comments,
        truncation=True,
        max_length=512,
        batch_size=8,
    )

    return [
        {
            "sentiment": normalize_label(result["label"]),
            "confiance": float(result["score"]),
        }
        for result in predictions
    ]
