# Exercices de manipulation d'historique Git

Ce document contient une série d'exercices pratiques pour maîtriser la manipulation d'historique Git.
Chaque exercice est accompagné d'un script Python qui initialise l'environnement nécessaire.

## Série 1 — Exercices élémentaires (6 exercices)

### Exercice 1 : Rebase de branche

Lancez `python exercice1_1.py` pour initialiser l'exercice.

Les branches `exercice1_1_main` et `exercice1_1_feature` vont être créées.

**Objectif** : Rebasez la branche `exercice1_1_feature` sur le HEAD de la branche `exercice1_1_main`.

**Commandes suggérées** :
```bash
git checkout exercice1_1_feature
git rebase exercice1_1_main
```

**Résultat attendu** :
```
* commit (exercice1_1_feature) Add feature implementation
* commit Fix bug in main
* commit Update configuration
* commit (exercice1_1_main) Initial setup
```

---

### Exercice 2 : Reword d'un ancien commit

Lancez `python exercice1_2.py` pour initialiser l'exercice.

La branche `exercice1_2` sera créée.

**Objectif** : Corrigez la faute d'orthographe dans le message du 2ème commit ("secnd" → "second").

**Commandes suggérées** :
```bash
git checkout exercice1_2
git rebase -i HEAD~3
# Marquez le commit avec 'reword' et corrigez le message
```

**Résultat attendu** :
```
* commit Add third file
* commit Add second file  ← Message corrigé
* commit Initial commit
```

**Question bonus** : Voyez-vous une 2ème façon d'obtenir le même résultat ?
<details>
<summary>Indice</summary>
Vous pouvez aussi utiliser <code>git commit --amend</code> si le commit à modifier est le dernier, ou <code>git filter-branch</code> pour des modifications plus complexes.
</details>

---

### Exercice 3 : Squash de commits

Lancez `python exercice1_3.py` pour initialiser l'exercice.

La branche `exercice1_3` sera créée.

**Objectif** : Fusionnez les commits qui commencent par "fix:" avec les commits précédents correspondants.

**Commandes suggérées** :
```bash
git checkout exercice1_3
git rebase -i HEAD~6
# Utilisez 'squash' ou 'fixup' pour les commits fix:
```

**Résultat attendu** :
```
* commit Add documentation
* commit Add tests (incluant fix: tests syntax)
* commit Add feature (incluant fix: feature typo)
* commit Initial setup
```

---

### Exercice 4 : Suppression de commit

Lancez `python exercice1_4.py` pour initialiser l'exercice.

La branche `exercice1_4` sera créée.

**Objectif** : Supprimez le commit 2 qui a été fait par erreur (celui qui ajoute un fichier temporaire).

**Commandes suggérées** :
```bash
git checkout exercice1_4
git rebase -i HEAD~4
# Marquez le commit à supprimer avec 'drop' ou supprimez la ligne
```

**Résultat attendu** :
```
* commit Add final feature
* commit Add core functionality
* commit Initial commit
```

---

### Exercice 5 : Réorganisation des commits

Lancez `python exercice1_5.py` pour initialiser l'exercice.

La branche `exercice1_5` sera créée.

**Objectif** : Réordonnez les commits pour obtenir une séquence logique : tests → feature → docs.

**Commandes suggérées** :
```bash
git checkout exercice1_5
git rebase -i HEAD~4
# Réorganisez les lignes dans l'ordre souhaité
```

**Résultat attendu** :
```
* commit Add documentation
* commit Add main feature
* commit Add tests
* commit Initial setup
```

---

### Exercice 6 : Récupérer une branche perdue depuis le reflog

Lancez `python exercice1_6.py` pour initialiser l'exercice.

La branche `exercice1_6` sera créée avec des commits, puis elle sera supprimée (simulant une suppression accidentelle).

**Objectif** : Récupérez la branche en utilisant le reflog.

**Commandes suggérées** :
```bash
git reflog
# Cherchez le dernier commit de la branche exercice1_6
git checkout -b exercice1_6 <commit-hash>
# ou
git branch exercice1_6 <commit-hash>
```

**Résultat attendu** :
```
* commit Important feature completed
* commit Work in progress
* commit Start new feature
```

---

## Série 2 — Challenges progressifs (4 exercices)

### Exercice 1 : Localisez et corrigez le commit fautif

Lancez `python exercice2_1.py` pour initialiser l'exercice.

**Contexte** : En exécutant `pytest exercices/exercice2_1`, des tests échouent.

**Objectif** : 
1. Localisez le commit ayant introduit l'erreur (utilisez `git bisect` si nécessaire)
2. Corrigez le bug dans *le commit qui l'a introduit* (rebase + edit)

**Commandes suggérées** :
```bash
git checkout exercice2_1
pytest exercices/exercice2_1  # Vérifier que les tests échouent
git log --oneline
git rebase -i HEAD~5
# Marquez le commit fautif avec 'edit'
# Corrigez le bug dans le fichier
git add .
git commit --amend
git rebase --continue
pytest exercices/exercice2_1  # Vérifier que les tests passent
```

**Résultat attendu** : Tous les tests passent et l'historique est propre.

---

### Exercice 2 : Nettoyage massif : squash + reword

Lancez `python exercice2_2.py` pour initialiser l'exercice.

**Contexte** : L'historique contient beaucoup de petits commits désorganisés.

**Objectif** : Regroupez les commits par thème pour aboutir à 3 commits propres :
1. **Préparation** : Configuration initiale et setup
2. **Feature** : Implémentation de la fonctionnalité principale
3. **Refactor** : Nettoyage et amélioration du code

**Commandes suggérées** :
```bash
git checkout exercice2_2
git log --oneline  # Observer le désordre
git rebase -i HEAD~10
# Utilisez squash/fixup et réorganisez pour obtenir 3 commits clairs
```

**Résultat attendu** :
```
* commit Refactor: Clean and optimize code
* commit Feature: Implement user authentication
* commit Preparation: Initial setup and configuration
```

---

### Exercice 3 : Extraction d'un fix dans le mauvais commit

Lancez `python exercice2_3.py` pour initialiser l'exercice.

**Contexte** : Un fix important a été inclus dans le mauvais commit.

**Objectif** : Le fix du test `test_validation` a été ajouté dans le 3ème commit alors qu'il aurait dû l'être dans le 2ème. Remettez le fix dans le bon commit.

**Commandes suggérées** :
```bash
git checkout exercice2_3
git log --oneline
git rebase -i HEAD~4
# Marquez le 3ème commit avec 'edit'
# Utilisez git reset HEAD^ pour défaire le commit
# Créez deux commits séparés ou déplacez les changements
```

**Résultat attendu** : Le fix est dans le commit où il devrait être, l'historique est cohérent.

---

### Exercice 4 : Réécriture complète d'un historique sale

Lancez `python exercice2_4.py` pour initialiser l'exercice.

**Contexte** : Un historique chaotique avec plus de 12 commits mal organisés, des messages peu clairs, des commits de debug, etc.

**Objectif** : Produisez un historique propre et lisible à partir de ce chaos. Aboutissez à 4 commits clairs et bien structurés :
1. **Setup** : Configuration initiale
2. **Core feature** : Fonctionnalité principale
3. **Testing** : Tests et validation
4. **Documentation** : Documentation complète

**Commandes suggérées** :
```bash
git checkout exercice2_4
git log --oneline  # Observer le chaos
git rebase -i HEAD~13
# Réorganisez, squashez, reword pour obtenir 4 commits propres
```

**Résultat attendu** :
```
* commit Documentation: Add complete project documentation
* commit Testing: Add comprehensive test suite
* commit Core feature: Implement complete feature
* commit Setup: Initial project configuration
```

---

## Conseils généraux

### Commandes utiles

- `git log --oneline --graph --all` : Visualiser l'historique
- `git rebase -i HEAD~N` : Rebase interactif sur les N derniers commits
- `git reflog` : Voir l'historique de toutes les opérations Git
- `git reset --hard HEAD@{N}` : Revenir à un état antérieur (visible dans reflog)
- `git cherry-pick <commit>` : Appliquer un commit spécifique

### Actions possibles en rebase interactif

- `pick` : Garder le commit tel quel
- `reword` : Modifier le message du commit
- `edit` : Modifier le contenu du commit
- `squash` : Fusionner avec le commit précédent (garder les messages)
- `fixup` : Fusionner avec le commit précédent (garder seulement le message du commit précédent)
- `drop` : Supprimer le commit

### Annuler une opération qui a mal tourné

Si vous vous trompez pendant un rebase :
```bash
git rebase --abort  # Annuler le rebase en cours
git reflog  # Trouver l'état avant le rebase
git reset --hard HEAD@{N}  # Revenir à cet état
```

---

**Bon courage et amusez-vous bien avec ces exercices ! 🚀**
