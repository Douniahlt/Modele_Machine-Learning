# 🛒 Analyse des Tendances d'Achat avec Machine Learning

## Description
Ce projet implémente un **modèle de Machine Learning** visant à analyser les préférences d'achat des clients en fonction de leur âge.  
À l'aide d'un **jeu de données** détaillé, nous avons exploré et pré-traité les informations avant de tester plusieurs algorithmes de classification.

---

## 📊 Jeu de Données
Nous avons utilisé le dataset **Customer Shopping Trends Dataset** disponible sur Kaggle :  
🔗 [Lien du dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset)

Ce dataset contient des informations détaillées sur les clients et leurs habitudes d'achat :
- **Identifiant client**
- **Âge et genre**
- **Articles achetés et catégorie**
- **Montant des achats**
- **Localisation des achats**
- **Évaluation des achats**
- **Statut d'abonnement**
- **Méthode de paiement préférée**
- **Fréquence d'achat**

---

## Pré-traitement des Données
Avant d’entraîner notre modèle, nous avons effectué les étapes suivantes :
✔ **Visualisation des relations entre variables**  
✔ **Encodage des données catégoriques** en valeurs numériques  
✔ **Sélection des variables pertinentes** (âge et type de produit)  
✔ **Regroupement des âges** en tranches  

---

## Modèles Testés
Nous avons exploré plusieurs modèles d’apprentissage automatique :
- 📈 **Régression Logistique**
- 🌲 **Arbres de décision**
- 🌳 **Forêts Aléatoires**
- 🧠 **Réseaux de Neurones**
- 🧮 **Classification Naïve Bayes**
- 📊 **SVM (Support Vector Machines)**

**Modèle choisi : Régression Logistique**  
Ce choix a été motivé par :
- Sa capacité à gérer plusieurs catégories de produits  
- Son interprétabilité facile  
- Son temps d'entraînement rapide  

---

##  Résultats du Modèle
**Accuracy Score** : **45%**  
**Cross Validation Score** : **45%**  

**Interprétation** : Malgré la simplicité du modèle, son score reste relativement faible, suggérant que d'autres variables influencent les décisions d'achat.

---

## Installation et Exécution
### 1️⃣ **Installation des dépendances**
Assurez-vous d’avoir **Python 3+** installé, puis installez les bibliothèques nécessaires :

    pip install pandas numpy scikit-learn matplotlib seaborn

    2️⃣ Exécuter le modèle

Lancez le script Jupyter Notebook :

    jupyter notebook Untitled1.ipynb
    
👥 Auteurs

👤 Dounia Hullot
📅 Projet IA - 2024

