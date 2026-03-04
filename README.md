# 🎓 face-recognition-quiz - Application QCM avec Reconnaissance Faciale

## 📖 Description

face-recognition-quiz est une application développée en Python dans le cadre d’un projet de soutenance de Licence.  
L’application combine :

- 🔐 Authentification par reconnaissance faciale
- 🧠 QCM (Quiz à Choix Multiples) en informatique
- 📊 Affichage du score final personnalisé
- 🖥 Interface graphique moderne avec Flet

L'utilisateur doit d'abord être identifié via la caméra avant d'accéder au quiz.


## 🚀 Fonctionnalités

✅ Détection et reconnaissance faciale avec `face_recognition`  
✅ Capture vidéo en temps réel avec `OpenCV`  
✅ Interface graphique avec `Flet`  
✅ Système de routage entre différentes vues  
✅ Calcul et affichage dynamique du score  
✅ Interface interactive et animée  


## 🏗 Architecture du Projet
face-recognition-quiz/
│
├── main.py # Point d'entrée de l'application
├── views/
│ ├── home.py # Page d'accueil
│ ├── rec.py # Reconnaissance faciale
│ ├── qcm.py # Logique du quiz
│ ├── resultat.py # Affichage du résultat
│ ├── visages.py # Encodage des visages connus
└-└──quiz.py # Questions du QCM

## 🛠 Technologies Utilisées

- Python 3
- Flet (Interface graphique)
- OpenCV (Capture vidéo)
- face_recognition (Reconnaissance faciale)
- NumPy


## 📦 Installation

### Cloner le projet

git clone https://github.com/VOTRE_USERNAME/DRNmem.git
cd DRNmem


### Installer les dépendances
pip install flet
pip install flet-route
pip install face_recognition
pip install opencv-python
pip install numpy