# 🔄 Git History Manipulation - Guide Complet

Ce repository est conçu pour aider les équipes de développement à maîtriser la manipulation de l'historique Git. Ce guide contient des explications détaillées, des schémas et des exemples pratiques.

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

## 📚 Table des matières

1. [Qu'est-ce que l'historique Git ?](#1-quest-ce-que-lhistorique-git-)
2. [Différence entre Merge et Rebase](#2-différence-entre-merge-et-rebase)
3. [Le Rebase Interactif](#3-le-rebase-interactif)
4. [Les cas particuliers du Rebase](#4-les-cas-particuliers-du-rebase)
5. [Le Reflog](#5-le-reflog)
6. [Configuration Git utile](6-configuration-git-utile)
7. [Conclusion](-conclusion)

---

## 1. Qu'est-ce que l'historique Git ?

L'historique Git est une séquence chronologique de commits qui représente l'évolution de votre code au fil du temps. Pour bien comprendre Git, il faut distinguer trois zones principales.

### Les trois zones de Git

```
┌──────────────────────┐
│  Répertoire de       │
│  travail (Working    │  ←── Vos fichiers locaux non suivis
│  Directory)          │
└──────────────────────┘
          ↓ git add
┌──────────────────────┐
│  Zone de transit     │
│  (Staging Area/      │  ←── Fichiers prêts à être committé
│  Index)              │
└──────────────────────┘
          ↓ git commit
┌──────────────────────┐
│  Dépôt local         │
│  (Local Repository)  │  ←── Historique local des commits
└──────────────────────┘
          ↓ git push
┌──────────────────────┐
│  Dépôt distant       │
│  (Remote Repository) │  ←── Historique partagé (GitHub, GitLab, etc.)
└──────────────────────┘
```

### Détail des zones

#### 1. **Répertoire de travail (Working Directory)**
- Contient vos fichiers en cours de modification
- Les changements ne sont pas encore suivis par Git
- État visible avec : `git status`

**Exemple :**
```bash
$ git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        nouveau_fichier.txt

nothing added to commit but untracked files present
```

#### 2. **Zone de transit (Staging Area / Index)**
- Zone intermédiaire où vous préparez votre prochain commit
- Permet de sélectionner précisément les changements à inclure
- Ajout avec : `git add <fichier>`

**Exemple :**
```bash
$ git add nouveau_fichier.txt
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   nouveau_fichier.txt
```

#### 3. **Dépôt local (Local Repository)**
- Contient l'historique complet de tous vos commits locaux
- Stocké dans le dossier `.git/`
- Création d'un commit : `git commit -m "message"`

**Exemple :**
```bash
$ git commit -m "Ajout du nouveau fichier"
[main abc1234] Ajout du nouveau fichier
 1 file changed, 10 insertions(+)
 create mode 100644 nouveau_fichier.txt
```

#### 4. **Dépôt distant (Remote Repository)**
- Hébergé sur un serveur (GitHub, GitLab, Bitbucket, etc.)
- Permet le travail collaboratif
- Synchronisation avec : `git push` et `git pull`

**Exemple :**
```bash
$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Writing objects: 100% (3/3), 301 bytes | 301.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:user/repo.git
   def5678..abc1234  main -> main
```

### Schéma du workflow complet

```
┌─────────────────┐
│  Working Dir    │
│  - fichier.txt  │ ──┐
│    (modifié)    │   │ git add fichier.txt
└─────────────────┘   │
                      ↓
┌─────────────────────────────┐
│  Staging Area               │
│  - fichier.txt (staged)     │ ──┐
└─────────────────────────────┘   │ git commit -m "message"
                                  ↓
┌────────────────────────────────────────┐
│  Local Repository (.git/)              │
│  abc1234 - "message"                   │ ──┐
│  def5678 - "previous commit"           │   │ git push origin main
│  ...                                   │   │
└────────────────────────────────────────┘   │
                                             ↓
┌────────────────────────────────────────────────┐
│  Remote Repository (GitHub)                    │
│  abc1234 - "message"                           │
│  def5678 - "previous commit"                   │
│  ...                                           │
└────────────────────────────────────────────────┘
```

---

## 2. Différence entre Merge et Rebase

Les deux commandes permettent d'intégrer les changements d'une branche dans une autre, mais de manière très différente.

### Merge

Le **merge** crée un nouveau commit de fusion qui a deux parents.

**Schéma avant le merge :**
```
          A---B---C  feature
         /
    D---E---F---G  main
```

**Commande :**
```bash
$ git checkout main
$ git merge feature
```

**Schéma après le merge :**
```
          A---B---C
         /         \
    D---E---F---G---H  main
                   (merge commit)
```

**Avantages du merge :**
- ✅ Préserve l'historique complet et exact
- ✅ Facile à comprendre pour les débutants
- ✅ Aucune réécriture d'historique
- ✅ Traçabilité claire de quand les branches ont été fusionnées

**Inconvénients du merge :**
- ❌ Crée des commits de merge qui peuvent polluer l'historique
- ❌ L'historique peut devenir complexe avec de nombreuses branches
- ❌ Graphe difficile à lire avec de nombreux merges

### Rebase

Le **rebase** réécrit l'historique en réappliquant les commits de votre branche sur une autre base.

**Schéma avant le rebase :**
```
          A---B---C  feature
         /
    D---E---F---G  main
```

**Commande :**
```bash
$ git checkout feature
$ git rebase main
```

**Schéma après le rebase :**
```
                  A'--B'--C'  feature
                 /
    D---E---F---G  main
```

Les commits A, B, C sont "rejoués" sur G, créant de nouveaux commits A', B', C' avec le même contenu mais des SHA différents.

**Avantages du rebase :**
- ✅ Historique linéaire et propre
- ✅ Facilite la lecture de l'historique
- ✅ Pas de commits de merge superflus
- ✅ Idéal avant de merger une feature dans main
- ✅ Plus facile de gérer les conflits sur les branches longues (résolution commit par commit, avec possibilité de recompiler et réexécuter les tests à chaque étape)
- ✅ Permet de déplacer son travail d'une branche à l'autre (ex: commencé sur main, puis déplacé sur la branche de maintenance)
- ✅ Possibilité de réorganiser l'historique (rebase interactif, voir plus loin)

**Inconvénients du rebase :**
- ❌ Réécrit l'historique (attention aux branches partagées !)
- ❌ Plus complexe à comprendre au début
- ❌ Peut causer des conflits à résoudre un par un

### Comparaison visuelle complète

**Scénario : Vous travaillez sur `feature` pendant que `main` évolue**

**État initial :**
```
    A---B  feature
   /
  C---D  main
```

**Après quelques commits sur main :**
```
    A---B  feature
   /
  C---D---E---F  main
```

#### Option 1 : Merge

```bash
$ git checkout feature
$ git merge main
```

**Résultat :**
```
    A---B-------M  feature
   /           /
  C---D---E---F  main
              (M = merge commit)
```

#### Option 2 : Rebase

```bash
$ git checkout feature
$ git rebase main
```

**Résultat :**
```
                A'--B'  feature
               /
  C---D---E---F  main
```

### Quand utiliser quoi ?

| Situation | Recommandation |
|-----------|---------------|
| Branche de feature locale (jamais pushée) | **Rebase** - pour garder un historique propre |
| Branche de feature partagée avec l'équipe | **Merge** - pour éviter de casser l'historique des autres |
| Intégration de main dans votre feature | **Rebase** - pour maintenir un historique linéaire |
| Fusion de feature dans main (via PR) | **Merge** ou **Squash and merge** - pour garder la traçabilité |
| Branches publiques (main, develop) | **Ne jamais rebase** - toujours merger |

### Règle d'or du rebase

> ⚠️ **Ne jamais rebaser des commits qui ont été pushés sur une branche publique/partagée !**

Si vous rebasez une branche partagée, vous créez des conflits pour tous les autres développeurs qui ont basé leur travail dessus.

### ⚠️ Point d'attention sur la direction

Une nuance importante à retenir :
- On **merge DANS** une branche : `git merge feature` (merge feature **dans** la branche courante)
- On **rebase SUR** une branche : `git rebase main` (rebase la branche courante **sur** main)

---

## 3. Le Rebase Interactif

Le rebase interactif est un outil puissant qui permet de réécrire l'historique local avant de le partager.

### À quoi ça sert ?

Le rebase interactif (`git rebase -i`) permet de :
- ✏️ Modifier des messages de commit
- 🔧 Corriger des bugs dans des commits passés
- 📦 Fusionner plusieurs commits en un seul (squash)
- ✂️ Diviser un commit en plusieurs
- 🔄 Réorganiser l'ordre des commits
- 🗑️ Supprimer des commits

### Comment l'utiliser ?

**Syntaxe de base :**
```bash
# Rebaser les N derniers commits
$ git rebase -i HEAD~N

# Rebaser depuis un commit spécifique
$ git rebase -i <commit-sha>

# Rebaser depuis la base de la branche
$ git rebase -i main
```

**L'éditeur interactif :**

Quand vous lancez `git rebase -i HEAD~3`, Git ouvre un éditeur avec :

```
pick abc1234 Premier commit
pick def5678 Deuxième commit
pick ghi9012 Troisième commit

# Commands:
# p, pick = utiliser le commit
# r, reword = utiliser le commit, mais modifier le message
# e, edit = utiliser le commit, mais s'arrêter pour modification
# s, squash = utiliser le commit, mais le fusionner avec le précédent
# f, fixup = comme squash, mais ignorer le message de ce commit
# d, drop = supprimer le commit
```

Vous pouvez alors changer le verbe de chaque début de ligne pour dire ce que vous voulez faire avec ce commit.

### Exemples concrets

#### Exemple 1 : Modifier un message de commit

**Situation :** Vous avez fait une faute de frappe dans un message de commit.

```bash
$ git log --oneline
abc1234 Ajout de la fonctinalité de connexion  # ← faute de frappe !
def5678 Création de la page d'accueil
ghi9012 Initial commit
```

**Solution :**
```bash
# 1. Lancer le rebase interactif sur les 3 derniers commits
$ git rebase -i HEAD~3

# 2. Dans l'éditeur, changer "pick" en "reword" (ou "r") pour le commit à modifier
reword abc1234 Ajout de la fonctinalité de connexion
pick def5678 Création de la page d'accueil
pick ghi9012 Initial commit

# 3. Sauvegarder et fermer l'éditeur
# 4. Un nouvel éditeur s'ouvre pour modifier le message
# 5. Corriger le message : "Ajout de la fonctionnalité de connexion"
# 6. Sauvegarder et fermer
```

**Résultat :**
```bash
$ git log --oneline
xyz7890 Ajout de la fonctionnalité de connexion  # ← corrigé !
def5678 Création de la page d'accueil
ghi9012 Initial commit
```

#### Exemple 2 : Corriger un bug introduit plus tôt

**Situation :** Vous découvrez un bug dans un commit précédent.

```bash
$ git log --oneline
abc1234 Utilisation de la fonction de calcul
def5678 Ajout de la fonction de calcul  # ← bug ici !
ghi9012 Création de la structure
```

**Solution :**
```bash
# 1. Lancer le rebase interactif
$ git rebase -i HEAD~3

# 2. Marquer le commit à modifier avec "edit" (ou "e")
pick ghi9012 Création de la structure
edit def5678 Ajout de la fonction de calcul  # ← changer "pick" en "edit"
pick abc1234 Utilisation de la fonction de calcul

# 3. Sauvegarder et fermer
# Git s'arrête sur le commit def5678

# 4. Faire les corrections nécessaires
$ nano calcul.py  # Corriger le bug
$ git add calcul.py
$ git commit --amend --no-edit  # Modifier le commit actuel

# 5. Continuer le rebase
$ git rebase --continue
```

**Alternative avec fixup commit :**
```bash
# 1. Corriger le bug maintenant
$ nano calcul.py
$ git add calcul.py
$ git commit -m "fix: correction bug calcul"

# 2. Rebase interactif
$ git rebase -i HEAD~4

# 3. Dans l'éditeur, déplacer le commit "fix" juste après celui à corriger
pick ghi9012 Création de la structure
pick def5678 Ajout de la fonction de calcul
fixup jkl3456 fix: correction bug calcul  # ← fusionné avec le commit précédent
pick abc1234 Utilisation de la fonction de calcul
```

#### Exemple 3 : Réorganiser les commits pour un ordre plus logique

**Situation :** Vous avez committé dans le désordre.

```bash
$ git log --oneline
abc1234 Ajout des tests pour la fonction B
def5678 Implémentation de la fonction A
ghi9012 Implémentation de la fonction B  # ← devrait être avant les tests !
jkl3456 Ajout des tests pour la fonction A
```

**Solution :**
```bash
# 1. Lancer le rebase interactif
$ git rebase -i HEAD~4

# 2. Réorganiser les lignes pour obtenir un ordre logique
pick def5678 Implémentation de la fonction A
pick jkl3456 Ajout des tests pour la fonction A
pick ghi9012 Implémentation de la fonction B
pick abc1234 Ajout des tests pour la fonction B

# 3. Sauvegarder et fermer
```

**Résultat :** L'historique est maintenant dans un ordre logique !

### Exemple complet : Workflow TDD avec conventions de nommage

Voici comment j'utilise le rebase interactif dans mon workflow TDD quotidien.

#### Convention de nommage des commits

- 📝 **Message explicite** : Pour les phases principales (ex: "feat: ajout authentification utilisateur")
- 🔧 **"fix"** : Pour les commits destinés à être squashés avec le commit précédent
- 🎯 **"fix XXX"** : Pour les commits destinés à être squashés avec un commit spécifique

#### Workflow type sur une feature

**Phase 1 : Développement avec TDD**

```bash
# 1. Refactoring de préparation
$ git add .
$ git commit -m "refactor: préparation de la structure pour l'authentification"

# 2. Test rouge
$ git add tests/test_auth.py
$ git commit -m "test: ajout test de validation du mot de passe"

# 3. Implémentation
$ git add auth.py
$ git commit -m "feat: implémentation de la validation du mot de passe"

# 4. Oups, j'ai oublié un cas limite
$ git add tests/test_auth.py
$ git commit -m "fix test"  # ← sera squashé avec le test

# 5. Correction du code
$ git add auth.py
$ git commit -m "fix feat"  # ← sera squashé avec feat

# 6. Refactoring de fin
$ git add auth.py
$ git commit -m "refactor: amélioration de la lisibilité"

# 7. Ah zut, un typo dans le refactoring de préparation
$ git add .
$ git commit -m "fix refactor: préparation"  # ← sera squashé avec le premier commit
```

**Historique actuel (désordonné et brouillon) :**
```bash
$ git log --oneline
abc1234 fix refactor: préparation
def5678 refactor: amélioration de la lisibilité
ghi9012 fix feat
jkl3456 feat: implémentation de la validation du mot de passe
mno7890 fix test
pqr2345 test: ajout test de validation du mot de passe
stu6789 refactor: préparation de la structure pour l'authentification
```

**Phase 2 : Nettoyage avec rebase interactif**

```bash
$ git rebase -i HEAD~7
```

**Dans l'éditeur :**
```
pick stu6789 refactor: préparation de la structure pour l'authentification
fixup abc1234 fix refactor: préparation
pick pqr2345 test: ajout test de validation du mot de passe
fixup mno7890 fix test
pick jkl3456 feat: implémentation de la validation du mot de passe
fixup ghi9012 fix feat
pick def5678 refactor: amélioration de la lisibilité

# Explication :
# - Les commits "fix" sont fusionnés (fixup) avec leurs commits parents
# - L'ordre est réorganisé : refactor préparation → test → feat → refactor fin
```

**Historique final (propre et logique) :**
```bash
$ git log --oneline
xyz1234 refactor: amélioration de la lisibilité
wxy9876 feat: implémentation et test de la validation du mot de passe
rst2109 refactor: préparation de la structure pour l'authentification
```

#### Avantages de cette méthode

1. **Pendant le développement :**
   - Commit fréquemment sans se soucier de la propreté
   - Pas de perte de travail en cas de problème
   - Facilite les retours en arrière

2. **Avant le push :**
   - Un historique propre et professionnel
   - Chaque commit est autonome et cohérent
   - Facilite la revue de code
   - Simplifie les futurs cherry-picks ou reverts

3. **Pour l'équipe :**
   - Historique facile à comprendre
   - Bisect plus efficace pour trouver les bugs
   - Documentation naturelle du processus de développement

#### Astuce pour les gros rebases

Quand il y a beaucoup de commits à modifier, ne pas hésiter à faire le rebase en plusieurs étapes.
Par exemple, en réorganisant les commits feature après feature, plutôt que de tout faire d'un coup.
Cela réduit les risques d'erreur et facilite la gestion des conflits.

---

## 4. Les cas particuliers du Rebase

Pendant un rebase, vous pouvez rencontrer différentes situations nécessitant des commandes spéciales.

### Commandes essentielles

#### `git rebase --continue`

**Utilisation :** Après avoir résolu un conflit, continuer le rebase.

**Exemple :**
```bash
$ git rebase main
# CONFLICT: Merge conflict in fichier.py
# Résoudre le conflit manuellement

$ git add fichier.py
$ git rebase --continue
```

#### `git rebase --skip`

**Utilisation :** Ignorer le commit actuel et continuer avec le suivant.

**Quand l'utiliser :**
- Le commit actuel est devenu obsolète
- Le commit a déjà été appliqué dans la branche de base
- Vous voulez simplement l'abandonner

**Exemple :**
```bash
$ git rebase main
# CONFLICT in fichier.py
# Vous réalisez que ce commit n'est plus nécessaire

$ git rebase --skip
```

#### `git rebase --abort`

**Utilisation :** Annuler complètement le rebase et revenir à l'état initial.

**Quand l'utiliser :**
- Trop de conflits complexes
- Vous avez fait une erreur dans le processus
- Vous voulez recommencer différemment

**Exemple :**
```bash
$ git rebase main
# Oh non, j'ai fait n'importe quoi !

$ git rebase --abort
# Tout revient à l'état d'avant le rebase
```

#### `git rebase --edit-todo`

**Utilisation :** Pendant un rebase interactif, modifier la liste des actions restantes.

**Exemple :**
```bash
$ git rebase -i HEAD~5
# Le rebase est en cours...
# Vous réalisez que vous voulez changer le plan

$ git rebase --edit-todo
# L'éditeur s'ouvre à nouveau avec les commits restants
```

### Gestion des conflits pendant un rebase

**Scénario complet :**

```bash
# 1. Démarrer le rebase
$ git rebase main
# Auto-merging fichier.py
# CONFLICT (content): Merge conflict in fichier.py
# error: could not apply abc1234... Mon commit

# 2. Vérifier l'état
$ git status
# rebase in progress; onto def5678
# You are currently rebasing branch 'feature' on 'def5678'.
#
# Unmerged paths:
#   both modified:   fichier.py

# 3. Voir le conflit
$ cat fichier.py
# <<<<<<< HEAD
# version de main
# =======
# votre version
# >>>>>>> abc1234 (Mon commit)

# 4. Résoudre manuellement
$ nano fichier.py  # Éditer pour résoudre le conflit

# 5. Marquer comme résolu
$ git add fichier.py

# 6. Continuer le rebase
$ git rebase --continue

# Si d'autres conflits apparaissent, répéter 3-6
# Si vous abandonnez : git rebase --abort
```

### Le rebase avec autostash

**Option utile :** `--autostash` permet de stasher automatiquement les changements non commités.

```bash
# Vous avez des modifications non commitées
$ git status
# Changes not staged for commit:
#   modified:   fichier.py

# Rebase avec autostash
$ git rebase main --autostash
# Saved working directory and index state WIP on feature
# Vos changements sont temporairement mis de côté
# Le rebase s'effectue
# Applied autostash.
# Vos changements sont réappliqués automatiquement
```

### Forcer le push après un rebase

⚠️ **Attention :** Après un rebase, votre historique local diverge du distant.

```bash
# Tentative de push normal
$ git push origin feature
# ! [rejected]        feature -> feature (non-fast-forward)

# Solution : force push (UNIQUEMENT sur vos branches personnelles !)
$ git push origin feature --force-with-lease

# Ou (plus dangereux, éviter)
$ git push origin feature --force
```

**Différence entre --force et --force-with-lease :**

- `--force` : Écrase tout, même si quelqu'un d'autre a pushé
- `--force-with-lease` : Refuse si quelqu'un d'autre a pushé entre-temps (RECOMMANDÉ)

### Récapitulatif des commandes de rebase

| Commande | Action | Quand l'utiliser |
|----------|--------|------------------|
| `git rebase --continue` | Continuer après résolution | Après avoir résolu un conflit |
| `git rebase --skip` | Ignorer le commit actuel | Commit obsolète ou déjà appliqué |
| `git rebase --abort` | Annuler tout le rebase | Trop de conflits ou erreur |
| `git rebase --edit-todo` | Modifier le plan restant | Changer la stratégie en cours |
| `git rebase --autostash` | Mettre de côté les changements | Rebase avec working dir modifié |

---

## 5. Le Reflog

Le reflog (reference log) est votre filet de sécurité Git. C'est un journal local qui enregistre tous les mouvements de HEAD, même ceux qui ne sont plus visibles dans l'historique.

### Qu'est-ce que le reflog ?

Le reflog enregistre **TOUTES** les modifications de HEAD :
- Commits
- Checkouts
- Resets
- Rebases
- Merges
- Cherry-picks
- Etc.

**Point important :** Le reflog est **local** à votre machine, il n'est jamais partagé avec le dépôt distant.

### Comment l'utiliser ?

#### Voir le reflog

```bash
# Afficher tout le reflog
$ git reflog

# Sortie exemple :
abc1234 (HEAD -> main) HEAD@{0}: commit: Ajout de la feature X
def5678 HEAD@{1}: rebase -i (finish): returning to refs/heads/main
ghi9012 HEAD@{2}: rebase -i (squash): Mise à jour de la doc
jkl3456 HEAD@{3}: commit: WIP: test
mno7890 HEAD@{4}: checkout: moving from feature to main
pqr2345 HEAD@{5}: reset: moving to HEAD~1
stu6789 HEAD@{6}: commit: Ajout fichier à supprimer

# Afficher le reflog d'une branche spécifique
$ git reflog show feature

# Afficher avec des dates
$ git reflog --date=relative
abc1234 HEAD@{0}: commit: Ajout de la feature X (2 minutes ago)
def5678 HEAD@{1}: rebase -i (finish): returning to refs/heads/main (10 minutes ago)
```

### Dans quels cas utiliser le reflog ?

#### Cas 1 : Récupérer un commit perdu après un reset

**Problème :**
```bash
$ git log --oneline
abc1234 Commit récent
def5678 Commit important
ghi9012 Ancien commit

$ git reset --hard HEAD~2
# Oups ! J'ai supprimé les commits abc1234 et def5678

$ git log --oneline
ghi9012 Ancien commit
# Où sont passés mes commits ?!
```

**Solution avec reflog :**
```bash
# 1. Consulter le reflog
$ git reflog
ghi9012 (HEAD -> main) HEAD@{0}: reset: moving to HEAD~2
abc1234 HEAD@{1}: commit: Commit récent
def5678 HEAD@{2}: commit: Commit important

# 2. Récupérer le commit perdu
$ git reset --hard abc1234
# OU
$ git reset --hard HEAD@{1}

# 3. Vérifier
$ git log --oneline
abc1234 Commit récent        # ← Récupéré !
def5678 Commit important      # ← Récupéré !
ghi9012 Ancien commit
```

#### Cas 2 : Annuler un rebase qui a mal tourné

**Problème :**
```bash
$ git rebase main
# ... beaucoup de conflits ...
# ... résolutions hasardeuses ...
$ git rebase --continue
# Le résultat final est un désastre !
```

**Solution avec reflog :**
```bash
# 1. Voir l'état avant le rebase
$ git reflog
abc1234 (HEAD -> feature) HEAD@{0}: rebase -i (finish): ...
def5678 HEAD@{1}: rebase -i (start): checkout main
ghi9012 HEAD@{2}: commit: Mon dernier commit avant rebase

# 2. Revenir à l'état avant le rebase
$ git reset --hard HEAD@{2}
# OU
$ git reset --hard ghi9012

# Votre branche est restaurée comme avant le rebase !
```

#### Cas 3 : Récupérer une branche supprimée

**Problème :**
```bash
$ git branch -D feature-importante
# Deleted branch feature-importante (was abc1234).
# Oh non ! J'avais besoin de cette branche !
```

**Solution avec reflog :**
```bash
# 1. Trouver le dernier commit de la branche supprimée
$ git reflog
# Cherchez les entrées mentionnant cette branche
def5678 HEAD@{3}: checkout: moving from feature-importante to main
abc1234 HEAD@{4}: commit: Dernier commit de la branche

# 2. Recréer la branche
$ git checkout -b feature-importante abc1234
# OU
$ git branch feature-importante abc1234

# Branche restaurée !
```

#### Cas 4 : Retrouver du code après un commit --amend

**Problème :**
```bash
$ git log --oneline
abc1234 Mon commit avec du code important

$ git commit --amend -m "Nouveau message"
# J'ai modifié le commit, mais j'ai aussi changé du code !
# Comment récupérer la version précédente ?
```

**Solution avec reflog :**
```bash
# 1. Voir l'ancien commit
$ git reflog
def5678 (HEAD -> main) HEAD@{0}: commit (amend): Nouveau message
abc1234 HEAD@{1}: commit: Mon commit avec du code important

# 2. Comparer les versions
$ git diff abc1234 def5678

# 3. Récupérer un fichier spécifique de l'ancien commit
$ git checkout abc1234 -- fichier.py

# 4. Ou revenir complètement à l'ancien commit
$ git reset --hard abc1234
```

### Schéma du reflog

```
Historique Git normal (git log) :
    
    A---B---C (main)

Vous faites un reset --hard vers A :
    
    A (main)
    
Les commits B et C semblent perdus !

Mais le reflog se souvient de tout :

git reflog :
    A (HEAD -> main) HEAD@{0}: reset: moving to A
    C HEAD@{1}: commit: C
    B HEAD@{2}: commit: B
    A HEAD@{3}: commit: A

Vous pouvez donc revenir à C :

    $ git reset --hard HEAD@{1}
    
    A---B---C (main)  ← Récupéré !
```

### Durée de conservation du reflog

Par défaut, Git garde les entrées du reflog pendant :
- **90 jours** pour les commits accessibles
- **30 jours** pour les commits inaccessibles (orphelins)

Vous pouvez changer ces valeurs :
```bash
$ git config gc.reflogExpire "60 days"
$ git config gc.reflogExpireUnreachable "15 days"
```

### Commandes utiles avec le reflog

```bash
# Voir le reflog complet
$ git reflog

# Voir le reflog avec plus de détails
$ git log -g

# Voir le reflog d'une branche spécifique
$ git reflog show branche

# Voir uniquement les 10 dernières entrées
$ git reflog -10

# Chercher dans le reflog
$ git reflog | grep "rebase"

# Nettoyer le reflog (attention !)
$ git reflog expire --expire=now --all
$ git gc --prune=now
```

### Le reflog : votre assurance tous risques

Le reflog est comme un historique de vos historiques. Tant que vous n'avez pas vidé le reflog (avec `git gc`), vous pouvez récupérer presque n'importe quoi.

**Règle d'or :**
> En cas de doute ou d'erreur grave avec Git, consultez d'abord le reflog !

**Ce que le reflog peut sauver :**
- ✅ Commits supprimés avec reset
- ✅ Branches supprimées
- ✅ Rebase raté
- ✅ Merge raté
- ✅ Commit amendé à tort
- ✅ Cherry-pick perdu

**Ce que le reflog ne peut PAS sauver :**
- ❌ Changements non commités (dans working directory)
- ❌ Fichiers non trackés supprimés
- ❌ Historique vieux de plus de 90 jours (par défaut)

---

## 6. Configuration Git utile

### Configurer Git pour rebaser par défaut lors d'un pull

Par défaut, `git pull` effectue un merge. Vous pouvez configurer Git pour qu'il effectue un rebase automatiquement à la place.

**Configuration globale (pour tous vos projets) :**
```bash
$ git config --global pull.rebase true
```

**Configuration locale (pour le projet actuel uniquement) :**
```bash
$ git config pull.rebase true
```

**Vérifier la configuration :**
```bash
$ git config --get pull.rebase
true
```

**Comportement :**

Avant la configuration :
```bash
$ git pull origin main
# Effectue : git fetch + git merge origin/main
# Crée un commit de merge
```

Après la configuration :
```bash
$ git pull origin main
# Effectue : git fetch + git rebase origin/main
# Rebase vos commits locaux sur la version distante
```

**Avantages :**
- ✅ Historique linéaire automatique
- ✅ Pas de commits de merge lors des synchronisations
- ✅ Plus propre pour les branches de feature

**Options supplémentaires :**

```bash
# Rebaser uniquement si le fast-forward n'est pas possible
$ git config pull.rebase merges

# Rebaser en préservant les merges locaux
$ git config pull.rebase preserve

# Revenir au comportement par défaut (merge)
$ git config pull.rebase false
```

### Autres configurations utiles

```bash
# Définir l'éditeur par défaut pour les rebases interactifs
$ git config --global core.editor "nano"  # ou "vim", "code --wait", etc.

# Activer la coloration syntaxique
$ git config --global color.ui auto

# Définir un alias pour le rebase interactif
$ git config --global alias.rbi "rebase -i"
# Utilisation : git rbi HEAD~3

# Activer l'autostash automatiquement lors des rebases
$ git config --global rebase.autoStash true
```

---

## 🎯 Conclusion

La manipulation de l'historique Git est un outil puissant qui demande de la pratique mais qui transforme votre workflow quotidien :

1. **Historique Git** : Comprendre les trois zones (working, staging, repository) est fondamental
2. **Merge vs Rebase** : Choisir selon le contexte (branche publique vs locale)
3. **Rebase interactif** : Votre meilleur ami pour un historique propre et professionnel
4. **Commandes de rebase** : Skip, abort, continue sont vos filets de sécurité
5. **Reflog** : Votre ultime bouée de sauvetage en cas d'erreur

### Conseils finaux

- 🧪 **Pratiquez** dans un repository de test avant de l'utiliser en production
- 💾 **Committez souvent** pendant le développement, nettoyez ensuite
- ⚠️ **Ne rebasez jamais** des commits déjà pushés sur une branche partagée
- 📖 **Consultez le reflog** dès que quelque chose semble perdu
- 🤝 **Communiquez** avec votre équipe sur les pratiques adoptées

### Ressources supplémentaires

- [Documentation officielle Git](https://git-scm.com/doc)
- [Pro Git Book (gratuit)](https://git-scm.com/book/fr/v2)
- [Git Flight Rules (guide de survie)](https://github.com/k88hudson/git-flight-rules)
- [Learn Git Branching (interactif)](https://learngitbranching.js.org/?locale=fr_FR)

---

**Happy Git manipulation! 🚀**
