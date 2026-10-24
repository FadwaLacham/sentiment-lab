
import io
import pandas as pd
import streamlit as st

from utils.model import load_model, analyze_comments
from utils.data_loader import read_file


st.set_page_config(
    page_title="Analyse en lot | Sentiment Lab",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Analyse en lot")
st.write("Analyse plusieurs commentaires depuis un fichier CSV ou Excel.")

uploaded_file = st.file_uploader(
    "Importer un fichier CSV ou Excel",
    type=["csv", "xlsx", "xls"],
)

if uploaded_file:
    try:
        df = read_file(uploaded_file)

        if df.empty or len(df.columns) == 0:
            st.warning("Le fichier est vide.")
        else:
            st.subheader("Aperçu du fichier")
            st.dataframe(df.head(10), width="stretch")

            text_column = st.selectbox(
                "Sélectionner la colonne des commentaires",
                df.columns.tolist(),
            )

            limit = st.number_input(
                "Nombre maximal de lignes (0 = toutes)",
                min_value=0,
                max_value=len(df),
                value=min(len(df), 500),
            )

            if st.button("Lancer l'analyse", type="primary"):
                subset = df.iloc[
                    :len(df) if limit == 0 else int(limit)
                ].copy()

                valid = (
                    subset[text_column].notna()
                    & subset[text_column].astype(str).str.strip().ne("")
                )

                comments = subset.loc[
                    valid, text_column
                ].astype(str).tolist()

                if not comments:
                    st.warning("Aucun commentaire non vide.")
                else:
                    with st.spinner(
                        f"Analyse de {len(comments)} commentaires..."
                    ):
                        model = load_model()
                        predictions = analyze_comments(model, comments)

                    subset["sentiment_predit"] = None
                    subset["score_confiance"] = None

                    for index, prediction in zip(
                        subset.index[valid], predictions
                    ):
                        subset.loc[index, "sentiment_predit"] = (
                            prediction["sentiment"]
                        )
                        subset.loc[index, "score_confiance"] = (
                            prediction["confiance"]
                        )

                    st.session_state["batch_results"] = subset

    except Exception as error:
        st.error(f"Erreur de lecture ou d'analyse : {error}")

results_df = st.session_state.get("batch_results")

if results_df is not None:
    st.subheader("Résultats de l'analyse")
    st.dataframe(results_df, width="stretch")

    st.download_button(
        "Télécharger les résultats en CSV",
        data=results_df.to_csv(index=False).encode("utf-8-sig"),
        file_name="resultats_sentiment.csv",
        mime="text/csv",
    )

    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        results_df.to_excel(
            writer,
            index=False,
            sheet_name="Resultats",
        )

    st.download_button(
        "Télécharger les résultats en Excel",
        data=excel_buffer.getvalue(),
        file_name="resultats_sentiment.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
