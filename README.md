# 🔄 Git History Manipulation

## 📖 Objectif du Repository

Ce repository est un guide éducatif conçu pour aider les développeurs à maîtriser la manipulation de l'historique Git. Il contient des explications détaillées, des schémas ASCII et des exemples pratiques couvrant les concepts essentiels tels que :

- Les bases de l'historique Git et ses zones (working directory, staging area, repository)
- La différence entre `merge` et `rebase`
- Le rebase interactif pour nettoyer l'historique
- Le reflog pour récupérer des commits perdus
- Les configurations Git utiles pour améliorer votre workflow

**Public cible** : Développeurs débutants à intermédiaires souhaitant approfondir leurs connaissances en Git.

## 🎯 Exercices pratiques

**Nouveau !** Ce repository contient maintenant un système d'exercices complet pour pratiquer la manipulation d'historique Git.

📖 **Consultez le fichier [`exercices.md`](exercices.md)** pour accéder à tous les exercices.

### Comment utiliser les exercices ?

1. Chaque exercice dispose d'un script Python d'initialisation (`exercice1_1.py`, `exercice1_2.py`, etc.)
2. Lancez le script pour créer l'environnement Git de l'exercice
3. Suivez les instructions dans `exercices.md` pour pratiquer
4. Les scripts sont idempotents : vous pouvez les relancer autant de fois que nécessaire

**Exemple :**
```bash
python exercice1_1.py
# Suivez ensuite les instructions dans exercices.md
```

### Structure des exercices

- **Série 1** : 6 exercices élémentaires (rebase, reword, squash, delete, reorder, reflog)
- **Série 2** : 4 challenges progressifs (debug, cleanup, fix extraction, history rewrite)

---

## ⚙️ Prérequis

### Installation de Python

Ce repository utilise Python pour des exemples de code et des tests. Vous devez avoir Python 3.9 ou supérieur installé sur votre système.

#### 🪟 Installation sur Windows

1. **Télécharger Python** :
   - Rendez-vous sur [python.org](https://www.python.org/downloads/)
   - Téléchargez la dernière version de Python 3.9+
   - Lancez l'installateur

2. **Configuration importante** :
   - ✅ Cochez la case **"Add Python to PATH"** lors de l'installation
   - Choisissez "Install Now" pour une installation standard

3. **Vérification** :
   ```bash
   python --version
   # ou
   python3 --version
   ```

#### 🐧 Installation sur Linux

**Ubuntu/Debian** :
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Fedora** :
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux** :
```bash
sudo pacman -S python python-pip
```

**Vérification** :
```bash
python3 --version
pip3 --version
```

---

## 🚀 Configuration de l'environnement de développement

### 1. Cloner le repository

```bash
git clone https://github.com/Jyhess/git-history-manipulation.git
cd git-history-manipulation
```

### 2. Créer un environnement virtuel

Un environnement virtuel permet d'isoler les dépendances de ce projet.

**Sur Windows** :
```bash
python -m venv venv
venv\Scripts\activate
```

**Sur Linux/macOS** :
```bash
python3 -m venv venv
source venv/bin/activate
```

Vous devriez voir `(venv)` apparaître au début de votre ligne de commande, indiquant que l'environnement virtuel est activé.

### 3. Installer les dépendances

```bash
pip install -e ".[dev]"
```

Cette commande installe le projet en mode éditable avec les dépendances de développement (pytest, pytest-cov, etc.).

### 4. Vérifier l'installation

```bash
# Lancer les tests
pytest

# Vérifier la couverture de code
pytest --cov=src
```

### 5. Désactiver l'environnement virtuel

Lorsque vous avez terminé de travailler sur le projet :

```bash
deactivate
```

---

## 📚 Commencer le tutoriel

Une fois votre environnement configuré, consultez le guide complet de manipulation Git :

👉 **[LESSON.md](LESSON.md)** - Guide complet sur la manipulation de l'historique Git

Le guide couvre :
- Les trois zones de Git
- Merge vs Rebase
- Le rebase interactif
- Le reflog
- Configurations Git utiles
- Et bien plus encore !

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request pour proposer des améliorations.

---

## 📝 Licence

Ce projet est un guide éducatif libre d'utilisation pour l'apprentissage.

---

**Happy Git Learning! 🚀**
