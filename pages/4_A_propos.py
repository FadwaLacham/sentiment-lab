
import streamlit as st

from utils.model import MODEL_ID


st.set_page_config(
    page_title="À propos | Sentiment Lab",
    page_icon="ℹ️",
    layout="wide",
)

st.title("ℹ️ À propos de Sentiment Lab")

st.markdown(
    """
    ## Présentation

    **Sentiment Lab** est une application de test et d'évaluation
    d'un modèle d'analyse de sentiment multilingue.

    ### Fonctionnalités

    - Analyse individuelle d'un commentaire.
    - Analyse en lot à partir de fichiers CSV et Excel.
    - Évaluation avec des sentiments de référence.
    - Calcul de l'accuracy, de la précision, du rappel et du F1-score.
    - Visualisation des erreurs de prédiction.
    - Export des résultats en CSV ou Excel.

    ### Informations techniques

    - **Technologie :** Python et Streamlit.
    - **Modèle :** CardiffNLP XLM-RoBERTa.
    - **Exécution :** modèle local sur CPU.
    - **Données :** import CSV et Excel.
    - **Classes :** négatif, neutre et positif.

    ### Limites

    Le score de confiance affiché par le modèle n'est pas nécessairement
    une probabilité calibrée.

    Les performances peuvent varier selon la langue, le domaine et
    la qualité des commentaires. La reconnaissance de la darija
    marocaine doit notamment être évaluée sur un jeu de données adapté.

    Les résultats doivent être vérifiés avant toute utilisation métier.
    """
)

st.divider()

st.caption(f"Identifiant du modèle local : {MODEL_ID}")
st.caption("Sentiment Lab — Application de test et d'évaluation.")
