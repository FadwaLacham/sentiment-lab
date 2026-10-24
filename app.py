
import streamlit as st

st.set_page_config(
    page_title="Sentiment Lab",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Sentiment Lab")

st.markdown(
    """
    ### Plateforme d'analyse et d'évaluation du sentiment

    Bienvenue dans **Sentiment Lab**, une application dédiée au test
    d'un modèle de sentiment multilingue.

    #### Fonctionnalités disponibles

    - **Analyse individuelle :** analyser un commentaire.
    - **Analyse en lot :** traiter un fichier CSV ou Excel.
    - **Évaluation du modèle :** mesurer les performances à partir
      de sentiments de référence.
    - **À propos :** consulter les informations techniques et les limites.

    #### Pour commencer

    Sélectionne la fonctionnalité souhaitée dans le menu de navigation
    situé dans la barre latérale.
    """
)

st.divider()

st.info(
    "Le modèle est exécuté localement. "
    "Les prédictions doivent être vérifiées avant une utilisation métier."
)
