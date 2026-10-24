
import time
import streamlit as st

from utils.model import load_model, analyze_comments


st.set_page_config(
    page_title="Analyse individuelle | Sentiment Lab",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Analyse individuelle")
st.write("Analyse le sentiment d'un commentaire avec le modèle local.")

language = st.selectbox(
    "Langue du commentaire",
    ["Français", "Arabe", "Darija", "Anglais"],
)

comment = st.text_area(
    "Saisir le commentaire",
    placeholder="Exemple : Le service était excellent.",
    height=150,
)

if st.button("Analyser", type="primary"):
    if not comment.strip():
        st.warning("Saisis un commentaire avant de continuer.")
    else:
        try:
            with st.spinner("Analyse en cours..."):
                model = load_model()
                start = time.perf_counter()
                result = analyze_comments(model, [comment])[0]
                elapsed = time.perf_counter() - start

            st.subheader("Résultat")

            sentiment = result["sentiment"]
            confidence = result["confiance"]

            col1, col2, col3 = st.columns(3)
            col1.metric("Sentiment", sentiment.capitalize())
            col2.metric("Score du modèle", f"{confidence:.1%}")
            col3.metric("Temps d'analyse", f"{elapsed:.2f} s")

            st.progress(confidence)

            if confidence < 0.60:
                st.warning(
                    "Score faible : vérifie manuellement le résultat."
                )

            st.caption(
                f"Langue sélectionnée : {language}. "
                "Les performances peuvent varier selon la langue."
            )

        except Exception as error:
            st.error("Impossible de charger ou d'exécuter le modèle local.")
            st.code(str(error))
