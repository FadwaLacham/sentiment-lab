
import pandas as pd
import streamlit as st

from utils.model import load_model, analyze_comments
from utils.data_loader import read_file
from utils.metrics import normalize_reference_labels, calculate_metrics


st.set_page_config(
    page_title="Évaluation du modèle | Sentiment Lab",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Évaluation du modèle")
st.write(
    "Compare les prédictions du modèle avec des sentiments de référence "
    "annotés manuellement."
)

uploaded_file = st.file_uploader(
    "Importer le fichier de référence",
    type=["csv", "xlsx", "xls"],
    key="evaluation_file",
)

if uploaded_file:
    try:
        df = read_file(uploaded_file)

        if len(df.columns) < 2:
            st.error("Le fichier doit contenir au moins deux colonnes.")
        else:
            st.subheader("Aperçu du fichier")
            st.dataframe(df.head(10), width="stretch")

            text_column = st.selectbox(
                "Colonne des commentaires",
                df.columns.tolist(),
                key="eval_text",
            )

            label_column = st.selectbox(
                "Colonne des sentiments attendus",
                df.columns.tolist(),
                key="eval_label",
            )

            if text_column == label_column:
                st.warning("Choisis deux colonnes différentes.")

            elif st.button("Calculer les métriques", type="primary"):
                subset = df[[text_column, label_column]].dropna().copy()

                subset["reference"] = normalize_reference_labels(
                    subset[label_column]
                )

                subset = subset[
                    subset["reference"].isin(
                        ["negative", "neutral", "positive"]
                    )
                    & subset[text_column].astype(str).str.strip().ne("")
                ].copy()

                if subset.empty:
                    st.error(
                        "Aucune ligne exploitable. Utilise positive, "
                        "neutral, negative, positif, négatif ou neutre."
                    )
                else:
                    with st.spinner(
                        f"Évaluation de {len(subset)} commentaires..."
                    ):
                        model = load_model()
                        predictions = analyze_comments(
                            model,
                            subset[text_column].astype(str).tolist(),
                        )

                    subset["prediction"] = [
                        item["sentiment"] for item in predictions
                    ]
                    subset["confiance"] = [
                        item["confiance"] for item in predictions
                    ]

                    y_true = subset["reference"]
                    y_pred = subset["prediction"]

                    metrics = calculate_metrics(y_true, y_pred)

                    st.subheader("Indicateurs de performance")

                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Accuracy", f"{metrics['accuracy']:.1%}")
                    c2.metric(
                        "Précision macro",
                        f"{metrics['precision_macro']:.1%}",
                    )
                    c3.metric(
                        "Rappel macro",
                        f"{metrics['recall_macro']:.1%}",
                    )
                    c4.metric(
                        "F1-score macro",
                        f"{metrics['f1_macro']:.1%}",
                    )

                    st.caption(
                        f"Nombre de commentaires évalués : {len(subset)}"
                    )

                    st.subheader("Matrice de confusion")
                    st.write(
                        "Les lignes représentent les sentiments attendus "
                        "et les colonnes les sentiments prédits."
                    )
                    st.dataframe(
                        metrics["confusion_matrix"],
                        width="stretch",
                    )

                    st.subheader("Rapport détaillé")
                    st.dataframe(
                        metrics["classification_report"],
                        width="stretch",
                    )

                    st.subheader("Prédictions à vérifier")
                    errors = subset[
                        subset["reference"] != subset["prediction"]
                    ]
                    st.write(f"Erreurs détectées : {len(errors)}")
                    st.dataframe(errors, width="stretch")

                    st.download_button(
                        "Exporter les résultats en Excel",
                        data=_to_excel(subset),
                        file_name="evaluation_sentiment.xlsx",
                        mime=(
                            "application/vnd.openxmlformats-officedocument."
                            "spreadsheetml.sheet"
                        ),
                    )

    except Exception as error:
        st.error(f"Erreur pendant l'évaluation : {error}")


def _to_excel(dataframe):
    import io

    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        dataframe.to_excel(
            writer,
            index=False,
            sheet_name="Evaluation",
        )

    return buffer.getvalue()
