# Commandes Git de base

Voici une liste des commandes Git utiles pour les exercices :

### Commandes générales
- `git init` : Initialiser un dépôt Git.
- `git status` : Vérifier l'état du dépôt.
- `git add <fichier>` : Ajouter un fichier à l'index.
- `git commit -m "message"` : Créer un commit.
- `git log` : Afficher l'historique des commits.
- `git log --oneline` : Visualiser l'historique sur une seule ligne
- `git log --oneline --graph --all` : Visualiser tout l'historique

### Commandes pour les branches
- `git branch` : Lister les branches.
- `git checkout <branche>` : Changer de branche.
- `git merge <branche>` : Fusionner une branche dans la branche courante.
- `git rebase <branche>` : Rebaser la branche courante sur une autre branche.

### Commandes pour la réécriture de l'historique
- `git rebase -i HEAD~N` : Rebase interactif sur les N derniers commits.
- `git rebase -i <branche>` : Rebase interactif sur un autre branche.
- `git reset --hard <commit>` : Revenir à un commit spécifique.
- `git reset --hard <branche>` : Revenir à un commit spécifique.
- `git cherry-pick <commit>` : Appliquer un commit spécifique.

### Commandes pour le reflog
- `git reflog` : Voir l'historique des opérations Git.
- `git reset --hard HEAD@{N}` : Revenir à un état antérieur visible dans le reflog.

### Ajoutées récemment
- `git rebase/rebase/reset main` : Commandes pour manipuler la branche principale.
