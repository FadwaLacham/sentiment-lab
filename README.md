# Sentiment Lab — Application d'analyse de sentiment

<p align="center">
  <strong>Application web d'analyse de sentiment basée sur Python, Streamlit et les Transformers.</strong>
</p>

<p align="center">
  <a href="https://sentiment-lab-fadwa.streamlit.app/">Accéder à l'application en ligne</a>
  |
  <a href="https://github.com/FadwaLacham/sentiment-lab">Dépôt GitHub</a>
</p>

---

## 1. Présentation du projet

**Sentiment Lab** est une application web interactive développée avec Python et Streamlit pour analyser automatiquement le sentiment exprimé dans des textes.

L'application exploite un modèle de traitement automatique du langage naturel (*Natural Language Processing — NLP*) basé sur l'architecture Transformer afin de classifier les textes selon leur polarité émotionnelle.

Elle propose une interface accessible permettant d'effectuer des analyses individuelles, de traiter plusieurs textes en lot et d'évaluer les performances du modèle à partir de données étiquetées.

L'objectif est de simplifier l'utilisation d'un modèle préentraîné d'analyse de sentiment et de faciliter l'exploration, l'évaluation et l'exploitation des résultats.

### Liens du projet

- **Application déployée :** https://sentiment-lab-fadwa.streamlit.app/
- **Code source :** https://github.com/FadwaLacham/sentiment-lab

## 2. Objectifs du projet

Les principaux objectifs de Sentiment Lab sont :

- Automatiser la classification des sentiments exprimés dans des textes.
- Exploiter un modèle NLP préentraîné basé sur les Transformers.
- Proposer une interface utilisateur interactive et simple à utiliser.
- Permettre l'analyse d'un texte ou le traitement de plusieurs textes.
- Évaluer les performances du modèle sur un jeu de données de référence.
- Afficher des métriques de classification et faciliter l'identification des erreurs.
- Permettre l'exportation des résultats pour une analyse complémentaire.

## 3. Fonctionnalités principales

### 3.1. Analyse individuelle

Cette fonctionnalité permet à l'utilisateur de saisir un texte et d'obtenir une prédiction de sentiment.

Selon les classes prises en charge par le modèle, le résultat peut correspondre à un sentiment :

- **Positif**
- **Neutre**
- **Négatif**

L'interface présente la prédiction produite par le modèle et les informations complémentaires disponibles dans l'application.

### 3.2. Analyse en lot

L'analyse en lot permet de traiter plusieurs textes au cours d'une même opération à partir d'un fichier compatible avec l'application.

Cette fonctionnalité facilite l'analyse de collections de commentaires, d'avis ou de messages.

Les résultats peuvent être consultés sous forme de tableau pour examiner les prédictions obtenues sur l'ensemble des données.

### 3.3. Évaluation du modèle

La page d'évaluation permet de comparer les prédictions du modèle aux sentiments de référence contenus dans un jeu de données étiqueté.

Les métriques calculées peuvent inclure :

- **Accuracy (exactitude)** : proportion de prédictions correctes parmi l'ensemble des exemples.
- **Precision (précision)** : proportion de prédictions correctes parmi les exemples affectés à une classe par le modèle.
- **Recall (rappel)** : proportion d'exemples appartenant à une classe qui ont été correctement identifiés.
- **F1-score** : moyenne harmonique de la précision et du rappel.
- **Macro Precision, Macro Recall et Macro F1-score** : moyennes donnant le même poids à chaque classe.

La page permet également de consulter les résultats d'évaluation et les erreurs de classification. L'export Excel est disponible lorsque la fonctionnalité est activée et fonctionne dans la version utilisée.

### 3.4. Page À propos

Cette page présente le projet et fournit des informations complémentaires sur son objectif et son fonctionnement.

## 4. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Langage principal de développement |
| Streamlit | Création de l'interface web interactive |
| Hugging Face Transformers | Chargement et utilisation du modèle NLP |
| CardiffNLP XLM-RoBERTa | Modèle préentraîné d'analyse de sentiment |
| PyTorch | Exécution du modèle Transformer |
| Pandas | Manipulation et traitement des données |
| Scikit-learn | Calcul des métriques d'évaluation, selon l'implémentation |
| OpenPyXL | Génération de fichiers Excel pour l'export |
| Git | Gestion de versions |
| GitHub | Hébergement du code source |
| Streamlit Community Cloud | Déploiement et hébergement de l'application |

Les dépendances exactes sont définies dans `requirements.txt`.

## 5. Architecture du projet

L'application est organisée en plusieurs modules afin de séparer l'interface utilisateur, la logique de prédiction, le chargement des données et l'évaluation.

```text
sentiment_tester_streamlit/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── 1_Analyse_individuelle.py
│   ├── 2_Analyse_en_lot.py
│   ├── 3_Evaluation_du_modele.py
│   └── 4_A_propos.py
│
├── utils/
│   ├── model.py
│   ├── data_loader.py
│   └── metrics.py
│
├── modele_sentiment/       # Modèle local éventuel
└── .venv/                  # Environnement virtuel local
```

### Description des principaux fichiers

| Fichier ou dossier | Description |
|---|---|
| `app.py` | Point d'entrée principal de l'application Streamlit |
| `requirements.txt` | Liste des dépendances Python |
| `pages/1_Analyse_individuelle.py` | Interface d'analyse d'un texte |
| `pages/2_Analyse_en_lot.py` | Interface de traitement de plusieurs textes |
| `pages/3_Evaluation_du_modele.py` | Évaluation du modèle et affichage des métriques |
| `pages/4_A_propos.py` | Informations sur le projet |
| `utils/model.py` | Chargement du modèle et fonctions de prédiction |
| `utils/data_loader.py` | Fonctions de chargement des données |
| `utils/metrics.py` | Fonctions liées aux métriques d'évaluation |
| `modele_sentiment/` | Emplacement éventuel des fichiers du modèle local |
| `.venv/` | Environnement virtuel utilisé en développement |

Le dossier `.venv/`, les caches Python et les modèles volumineux ne doivent généralement pas être ajoutés directement au dépôt GitHub.

## 6. Modèle d'analyse de sentiment

Le projet utilise le modèle préentraîné suivant lorsque le modèle local n'est pas disponible :

`cardiffnlp/twitter-xlm-roberta-base-sentiment`

Ce modèle est fondé sur l'architecture XLM-RoBERTa, une architecture Transformer multilingue adaptée à des tâches de traitement automatique du langage naturel.

### Fonctionnement du modèle

Le processus de prédiction suit les étapes générales suivantes :

1. Le texte est fourni par l'utilisateur.
2. Le texte est préparé et transmis au tokenizer.
3. Le modèle Transformer calcule des scores pour les classes de sentiment.
4. La sortie est interprétée pour déterminer la classe prédite.
5. L'application présente le résultat à l'utilisateur.

Le projet peut utiliser une copie locale du modèle si elle est disponible dans le chemin prévu par le code. Dans le cas contraire, il peut charger le modèle à partir de Hugging Face.

Le premier téléchargement peut nécessiter une connexion Internet et un espace disque suffisant.

## 7. Installation et configuration en local

### 7.1. Prérequis

Avant de commencer, il est recommandé de disposer de :

- Python compatible avec les dépendances du projet.
- Git, pour cloner le dépôt.
- Une connexion Internet pour installer les bibliothèques et télécharger le modèle si nécessaire.
- Un ordinateur disposant de suffisamment de mémoire pour charger le modèle Transformer.

### 7.2. Cloner le dépôt GitHub

Ouvrir un terminal et exécuter :

```bash
git clone https://github.com/FadwaLacham/sentiment-lab.git
cd sentiment-lab
```

Si le projet est déjà présent sur l'ordinateur, ouvrir directement son dossier dans le terminal.

### 7.3. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 7.4. Activer l'environnement virtuel

Sous Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Sous Windows avec l'invite de commandes :

```cmd
.venv\Scripts\activate.bat
```

Sous macOS ou Linux :

```bash
source .venv/bin/activate
```

### 7.5. Installer les dépendances

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Si la génération des fichiers Excel nécessite `openpyxl` et que cette bibliothèque n'est pas installée :

```bash
pip install openpyxl
```

Il est également recommandé de déclarer cette dépendance dans `requirements.txt` afin qu'elle soit installée automatiquement lors du déploiement.

## 8. Lancement de l'application

Depuis la racine du projet, avec l'environnement virtuel activé, exécuter :

```bash
python -m streamlit run app.py
```

Streamlit affiche généralement l'adresse locale suivante :

```text
http://localhost:8501
```

Ouvrir cette adresse dans un navigateur pour accéder à l'application.

Pour arrêter le serveur local, utiliser `Ctrl + C` dans le terminal.

## 9. Utilisation de l'application

### Analyse individuelle

1. Ouvrir la page **Analyse individuelle**.
2. Saisir le texte à analyser.
3. Lancer l'analyse.
4. Consulter la prédiction et les informations présentées par l'application.

### Analyse en lot

1. Ouvrir la page **Analyse en lot**.
2. Importer un fichier compatible.
3. Vérifier que les colonnes nécessaires sont présentes.
4. Lancer le traitement.
5. Examiner les résultats obtenus.

### Évaluation du modèle

1. Préparer un jeu de données contenant les textes et leurs étiquettes de référence.
2. Ouvrir la page **Évaluation du modèle**.
3. Importer le jeu de données.
4. Vérifier les colonnes et les valeurs attendues.
5. Lancer le calcul des métriques.
6. Examiner les scores et les erreurs de classification.
7. Télécharger les résultats au format Excel si l'option est disponible.

Les noms de colonnes et les formats de fichiers acceptés dépendent de l'implémentation de chaque page.

## 10. Évaluation des performances

L'évaluation permet d'estimer la capacité du modèle à classifier correctement des exemples dont le sentiment de référence est connu.

### Interprétation des métriques

- **Accuracy** mesure la proportion globale de prédictions correctes.
- **Precision** mesure la fiabilité des prédictions pour une classe.
- **Recall** mesure la capacité à retrouver les exemples d'une classe.
- **F1-score** combine la précision et le rappel.
- **Macro averages** accordent un poids identique à chaque classe, quelle que soit sa fréquence.

Il est préférable d'utiliser un jeu de test représentatif et distinct des données ayant servi à entraîner ou à ajuster le modèle.

Les résultats obtenus dépendent notamment de la qualité des données, de l'équilibre entre les classes et de la cohérence des étiquettes.

## 11. Format des données

Pour l'évaluation, le jeu de données doit contenir :

- Une colonne avec le texte à analyser.
- Une colonne avec le sentiment réel servant de référence.

Exemple illustratif :

| text | sentiment |
|---|---|
| This product is excellent. | positive |
| The service was disappointing. | negative |
| The product arrived today. | neutral |

Cet exemple est indicatif. Les noms des colonnes et les valeurs des étiquettes doivent correspondre au format attendu par le code de l'application.

Avant l'importation, il est recommandé de vérifier les valeurs manquantes, les doublons et la cohérence des étiquettes.

## 12. Déploiement de l'application

Sentiment Lab est accessible en ligne grâce à **Streamlit Community Cloud**, qui permet d'héberger une application Streamlit à partir d'un dépôt GitHub.

### 12.1. Application en ligne

**Accéder à Sentiment Lab :**

https://sentiment-lab-fadwa.streamlit.app/

L'application peut être ouverte depuis un navigateur compatible sans installer localement l'environnement Python, sous réserve de sa disponibilité et de ses paramètres d'accès.

### 12.2. Architecture du déploiement

Le déploiement s'appuie sur les composants suivants :

- **GitHub** héberge le code source.
- **Streamlit Community Cloud** récupère le dépôt et exécute l'application.
- **`app.py`** constitue le point d'entrée de l'application.
- **`requirements.txt`** indique les bibliothèques à installer.
- **Hugging Face Transformers** permet de charger le modèle d'analyse de sentiment lorsque nécessaire.

Le processus général est le suivant :

1. Les modifications sont enregistrées dans Git.
2. Le code est envoyé sur GitHub.
3. Streamlit Community Cloud récupère le dépôt et la branche configurés.
4. Les dépendances sont installées.
5. L'application est démarrée à partir de `app.py`.
6. Une URL permet d'accéder à l'application en ligne.

### 12.3. Préparer le projet pour le déploiement

Avant de déployer l'application, vérifier que :

- `app.py` se trouve à la racine du dépôt.
- `requirements.txt` contient les dépendances nécessaires.
- Toutes les pages et tous les modules requis sont présents dans le dépôt.
- Les chemins vers les fichiers fonctionnent sous Linux, en tenant compte de la casse des noms.
- Les fichiers volumineux sont gérés de manière adaptée.
- Aucune clé API, aucun mot de passe et aucune donnée confidentielle ne sont exposés.

### 12.4. Publier les modifications sur GitHub

Après avoir modifié le code ou la documentation, ouvrir le terminal dans le dossier du projet et exécuter :

```bash
git add .
git commit -m "Update Sentiment Lab"
git push origin main
```

Ces commandes enregistrent les modifications et les envoient vers la branche `main` du dépôt distant.

Si les modifications ont déjà été ajoutées à un commit, il suffit généralement d'exécuter :

```bash
git push origin main
```

### 12.5. Déployer avec Streamlit Community Cloud

Pour créer un nouveau déploiement :

1. Accéder à [Streamlit Community Cloud](https://share.streamlit.io/).
2. Se connecter avec le compte GitHub qui dispose des droits nécessaires.
3. Créer une nouvelle application.
4. Sélectionner le dépôt `FadwaLacham/sentiment-lab`.
5. Choisir la branche `main`.
6. Indiquer `app.py` comme fichier principal.
7. Lancer le déploiement.

Si l'application existe déjà, il est possible de conserver sa configuration et de publier les mises à jour depuis GitHub.

### 12.6. Vérifications après déploiement

Après le démarrage de l'application, vérifier :

- L'accès à l'URL de l'application.
- L'affichage correct de la page principale.
- Le fonctionnement de l'analyse individuelle.
- Le fonctionnement de l'analyse en lot.
- Le calcul des métriques d'évaluation.
- Le téléchargement des résultats Excel, si disponible.
- L'absence d'erreurs dans les journaux de déploiement.

Un déploiement réussi doit être suivi de tests fonctionnels dans l'environnement distant.

### 12.7. Gestion des mises à jour

Pour publier une nouvelle version :

1. Modifier le code localement.
2. Tester l'application.
3. Enregistrer les modifications dans Git.
4. Envoyer les changements sur GitHub.
5. Vérifier le redéploiement et tester les fonctionnalités en ligne.

Commandes habituelles :

```bash
git add .
git commit -m "Improve sentiment analysis application"
git push origin main
```

Streamlit Community Cloud détecte normalement les modifications de la branche configurée et redéploie l'application automatiquement.

### 12.8. Gestion du modèle et des ressources

Le modèle `cardiffnlp/twitter-xlm-roberta-base-sentiment` peut nécessiter un téléchargement initial si aucune copie locale utilisable n'est disponible.

Le déploiement doit tenir compte :

- De la mémoire nécessaire au chargement du modèle.
- Du temps de démarrage.
- De la taille des fichiers téléchargés.
- Des limites de ressources de la plateforme.
- De la disponibilité des dépendances.

Les modèles volumineux ne doivent généralement pas être versionnés directement dans Git. Un téléchargement contrôlé, un cache ou un stockage d'artefacts adapté peut être utilisé si nécessaire.

### 12.9. Dépannage du déploiement

**Erreur de dépendance :** vérifier `requirements.txt`, puis envoyer la correction sur GitHub.

**Erreur de chargement du modèle :** vérifier l'identifiant du modèle, la connexion réseau, les ressources disponibles et les journaux de démarrage.

**Fichier introuvable :** vérifier que le fichier existe dans le dépôt et que son chemin respecte la structure du projet.

**Modifications non visibles :** vérifier la branche GitHub, l'état du déploiement et les journaux de Streamlit Community Cloud.

**Erreur d'export Excel :** vérifier que `openpyxl` est installé et que le code de génération du fichier fonctionne dans l'environnement distant.

### 12.10. Sécurité et accès

Les paramètres d'accès à l'application dépendent de la configuration de Streamlit Community Cloud.

Il est recommandé de ne jamais stocker de secrets dans le dépôt GitHub. Si des clés ou des identifiants sont nécessaires, utiliser le mécanisme de gestion des secrets de la plateforme.

Il faut également éviter de transmettre des données personnelles ou confidentielles dans l'application sans autorisation appropriée.

## 13. Limites du projet

Les prédictions d'un modèle d'analyse de sentiment peuvent être influencées par :

- Le sarcasme et l'ironie.
- Les fautes d'orthographe et les abréviations.
- Le mélange de langues.
- Le contexte manquant.
- Les expressions spécifiques à un domaine.
- La qualité et la représentativité des données.
- Les différences entre les données d'entraînement et les textes analysés.

Les résultats doivent être considérés comme des estimations et non comme des vérités absolues. Une vérification humaine peut être nécessaire pour les analyses sensibles ou les décisions importantes.

## 14. Améliorations futures

Plusieurs évolutions peuvent être envisagées :

- Ajouter des graphiques présentant la distribution des sentiments.
- Ajouter une matrice de confusion.
- Permettre le filtrage et la recherche dans les résultats.
- Comparer plusieurs modèles d'analyse de sentiment.
- Améliorer la validation des fichiers importés.
- Ajouter des jeux de données d'exemple.
- Optimiser le chargement et le cache du modèle.
- Ajouter des tests automatisés.
- Documenter plus précisément les formats de données attendus.

## 15. Dépannage local

### L'application ne démarre pas

Vérifier que l'environnement virtuel est activé et que les dépendances sont installées :

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

### Le modèle ne se charge pas

Vérifier la connexion Internet, l'identifiant du modèle, les fichiers locaux et les messages d'erreur du terminal.

### Un fichier est rejeté

Vérifier le format du fichier, les noms des colonnes, les valeurs manquantes et les étiquettes attendues.

### Une ancienne erreur apparaît toujours

Arrêter le serveur avec `Ctrl + C`, relancer l'application et actualiser le navigateur.

## 16. Licence

La licence du projet doit être définie par son auteur si une redistribution publique est prévue. Les conditions d'utilisation du modèle préentraîné utilisé doivent également être respectées.

---

## Accès au projet

- **Application en ligne :** https://sentiment-lab-fadwa.streamlit.app/
- **Dépôt GitHub :** https://github.com/FadwaLacham/sentiment-lab
- **Plateforme de déploiement :** https://share.streamlit.io/

**Sentiment Lab** — Application interactive d'analyse de sentiment développée avec Python, Streamlit et les Transformers.
