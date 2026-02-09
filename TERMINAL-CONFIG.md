# ⚙️ Configuration du Terminal et Alias Git

Ce guide vous aidera à améliorer votre expérience avec Git en configurant votre terminal pour afficher le nom de la branche actuelle et en utilisant des alias pratiques pour les commandes Git les plus courantes.

---

## 📚 Table des matières

1. [Afficher le nom de la branche dans le terminal](#afficher-le-nom-de-la-branche-dans-le-terminal)
   - [🪟 Windows (PowerShell)](#-windows-powershell)
   - [🍎 macOS / 🐧 Linux (Bash)](#-macos---linux-bash)
   - [🐚 Zsh (macOS / Linux)](#-zsh-macos--linux)
2. [Alias Git utiles](#alias-git-utiles)
   - [🪟 Windows (PowerShell)](#-windows-powershell-1)
   - [🍎 macOS / 🐧 Linux (Bash / Zsh)](#-macos---linux-bash--zsh)

---

## Afficher le nom de la branche dans le terminal

Avoir le nom de la branche Git affiché dans votre terminal est extrêmement pratique pour savoir en permanence sur quelle branche vous travaillez, évitant ainsi les erreurs de manipulation.

### 🪟 Windows (PowerShell)

#### Installation de posh-git

**posh-git** est un module PowerShell qui ajoute des fonctionnalités Git à votre prompt, incluant l'affichage du nom de la branche.

**Installation :**

1. Ouvrez PowerShell en tant qu'administrateur
2. Installez posh-git via PowerShellGet :

```powershell
# Installer posh-git
Install-Module posh-git -Scope CurrentUser -Force

# Importer le module
Import-Module posh-git

# Ajouter posh-git au profil PowerShell pour qu'il se charge automatiquement
Add-PoshGitToProfile -AllHosts
```

**Vérification :**

Fermez et rouvrez PowerShell. Vous devriez maintenant voir le nom de la branche s'afficher dans votre prompt lorsque vous êtes dans un repository Git.

**Exemple de prompt avec posh-git :**
```
C:\Users\Dev\mon-projet [main ≡]>
```

#### Alternative : Starship

**Starship** est un prompt moderne, rapide et personnalisable qui fonctionne sur Windows, macOS et Linux.

**Installation :**

```powershell
# Via winget
winget install --id Starship.Starship

# Via Scoop
scoop install starship

# Via Chocolatey
choco install starship
```

**Configuration :**

Ajoutez à votre profil PowerShell (`$PROFILE`) :

```powershell
Invoke-Expression (&starship init powershell)
```

### 🍎 macOS / 🐧 Linux (Bash)

#### Option 1 : Configuration manuelle du prompt

Ajoutez le code suivant à votre fichier `~/.bashrc` ou `~/.bash_profile` :

```bash
# Fonction pour obtenir la branche Git actuelle
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# Configurer le prompt pour afficher la branche
export PS1="\[\e[32m\]\u@\h \[\e[34m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "
```

Rechargez votre configuration :
```bash
source ~/.bashrc
```

**Résultat :**
```
user@machine ~/projet (main)$
```

#### Option 2 : bash-git-prompt

**bash-git-prompt** offre un prompt Git plus riche avec des informations sur l'état du repository.

**Installation :**

```bash
# Cloner le repository
git clone https://github.com/magicmonty/bash-git-prompt.git ~/.bash-git-prompt --depth=1

# Ajouter à ~/.bashrc ou ~/.bash_profile
echo 'if [ -f "$HOME/.bash-git-prompt/gitprompt.sh" ]; then
    GIT_PROMPT_ONLY_IN_REPO=1
    source $HOME/.bash-git-prompt/gitprompt.sh
fi' >> ~/.bashrc

# Recharger
source ~/.bashrc
```

#### Option 3 : Starship

```bash
# Installation sur macOS via Homebrew
brew install starship

# Installation sur Linux
curl -sS https://starship.rs/install.sh | sh

# Ajouter à ~/.bashrc
echo 'eval "$(starship init bash)"' >> ~/.bashrc

# Recharger
source ~/.bashrc
```

### 🐚 Zsh (macOS / Linux)

#### Option 1 : Oh My Zsh

**Oh My Zsh** est un framework de configuration Zsh très populaire avec des centaines de plugins et thèmes.

**Installation :**

```bash
# Installer Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

**Configuration :**

Éditez `~/.zshrc` et modifiez le thème :

```bash
# Utiliser un thème qui affiche les informations Git
ZSH_THEME="robbyrussell"  # ou "agnoster", "powerlevel10k/powerlevel10k", etc.

# Activer les plugins Git
plugins=(git)
```

Rechargez :
```bash
source ~/.zshrc
```

#### Option 2 : Powerlevel10k (recommandé)

**Powerlevel10k** est un thème Zsh ultra-rapide avec une excellente intégration Git.

**Installation :**

```bash
# Cloner le repository
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# Définir le thème dans ~/.zshrc
# Remplacer : ZSH_THEME="robbyrussell"
# Par : ZSH_THEME="powerlevel10k/powerlevel10k"

# Recharger
source ~/.zshrc

# Lancer le wizard de configuration
p10k configure
```

#### Option 3 : Starship

```bash
# Installation sur macOS via Homebrew
brew install starship

# Installation sur Linux
curl -sS https://starship.rs/install.sh | sh

# Ajouter à ~/.zshrc
echo 'eval "$(starship init zsh)"' >> ~/.zshrc

# Recharger
source ~/.zshrc
```

---

## Alias Git utiles

Les alias permettent de raccourcir les commandes Git fréquemment utilisées, améliorant ainsi votre productivité.

### 🪟 Windows (PowerShell)

Ajoutez ces fonctions à votre profil PowerShell. Pour éditer votre profil :

```powershell
# Ouvrir le profil PowerShell dans l'éditeur par défaut
notepad $PROFILE

# Si le fichier n'existe pas, le créer d'abord
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}
```

**Alias de base :**

```powershell
# Alias Git pour PowerShell

# Status - Afficher l'état du repository
function gs { git status }

# Log - Afficher l'historique des commits en une ligne
function gl { git log --oneline }

# Log graphique - Visualiser l'historique en graphe
function glog { git log --graph --oneline --all --decorate }

# Add - Ajouter des fichiers à la staging area
function ga { git add @args }

# Add all - Ajouter tous les fichiers modifiés
function gaa { git add --all }

# Commit - Créer un commit
function gc { git commit @args }

# Commit avec message - Créer un commit avec message
function gcm { git commit -m @args }

# Commit amend - Modifier le dernier commit
function gca { git commit --amend }

# Checkout - Changer de branche
function gco { git checkout @args }

# Checkout nouvelle branche
function gcb { git checkout -b @args }

# Branch - Lister les branches
function gb { git branch @args }

# Branch delete - Supprimer une branche
function gbd { git branch -d @args }

# Branch force delete
function gbD { git branch -D @args }

# Pull - Récupérer les changements
function gpl { git pull }

# Push - Pousser les changements
function gp { git push }

# Push force (avec protection)
function gpf { git push --force-with-lease }

# Push force (sans protection - à utiliser avec précaution)
function gpff { git push --force }

# Diff - Voir les différences
function gd { git diff }

# Diff staged - Voir les différences des fichiers staged
function gds { git diff --staged }

# Stash - Mettre de côté les modifications
function gst { git stash }

# Stash pop - Récupérer les modifications mises de côté
function gstp { git stash pop }

# Stash list - Lister les stash
function gstl { git stash list }

# Rebase - Rebaser la branche
function gr { git rebase @args }

# Rebase continue - Continuer le rebase après résolution de conflits
function grc { git rebase --continue }

# Rebase abort - Annuler le rebase
function gra { git rebase --abort }

# Rebase skip - Passer le commit actuel
function grs { git rebase --skip }

# Rebase interactif
function gri { git rebase -i @args }

# Rebase interactif sur main/master
function grim {
    $mainBranch = if (git rev-parse --verify main 2>$null) { "main" } else { "master" }
    git rebase -i $mainBranch
}

# Rebase update from main/master (checkout main, pull, checkout back, rebase)
function grum {
    $currentBranch = git rev-parse --abbrev-ref HEAD
    $mainBranch = if (git rev-parse --verify main 2>$null) { "main" } else { "master" }
    git checkout $mainBranch
    git pull
    git checkout $currentBranch
    git rebase $mainBranch
}

# Fetch - Récupérer les changements sans merger
function gf { git fetch }

# Fetch all - Récupérer de tous les remotes
function gfa { git fetch --all }

# Merge - Fusionner une branche
function gm { git merge @args }

# Remote - Voir les remotes
function grv { git remote -v }

# Reset - Annuler des modifications
function grh { git reset HEAD @args }

# Reset hard - Annuler toutes les modifications
function grhh { git reset --hard }

# Clean - Supprimer les fichiers non suivis
function gclean { git clean -fd }

# Reflog - Voir l'historique de référence
function grl { git reflog }

# Show - Afficher les détails d'un commit
function gsh { git show @args }
```

**Utilisation :**

Après avoir ajouté ces alias à votre profil, rechargez-le :

```powershell
. $PROFILE
```

Vous pouvez maintenant utiliser les alias :

```powershell
gs              # au lieu de git status
gl              # au lieu de git log --oneline
gcm "Mon commit"  # au lieu de git commit -m "Mon commit"
gp              # au lieu de git push
```

### 🍎 macOS / 🐧 Linux (Bash / Zsh)

Ajoutez ces alias à votre fichier de configuration shell :
- Pour **Bash** : `~/.bashrc` ou `~/.bash_profile`
- Pour **Zsh** : `~/.zshrc`

**Alias de base :**

```bash
# Alias Git pour Bash/Zsh

# Status - Afficher l'état du repository
alias gs='git status'

# Log - Afficher l'historique des commits en une ligne
alias gl='git log --oneline'

# Log graphique - Visualiser l'historique en graphe
alias glog='git log --graph --oneline --all --decorate'

# Add - Ajouter des fichiers à la staging area
alias ga='git add'

# Add all - Ajouter tous les fichiers modifiés
alias gaa='git add --all'

# Commit - Créer un commit
alias gc='git commit'

# Commit avec message - Créer un commit avec message
alias gcm='git commit -m'

# Commit amend - Modifier le dernier commit
alias gca='git commit --amend'

# Checkout - Changer de branche
alias gco='git checkout'

# Checkout nouvelle branche
alias gcb='git checkout -b'

# Branch - Lister les branches
alias gb='git branch'

# Branch delete - Supprimer une branche
alias gbd='git branch -d'

# Branch force delete
alias gbD='git branch -D'

# Pull - Récupérer les changements
alias gpl='git pull'

# Push - Pousser les changements
alias gp='git push'

# Push force (avec protection)
alias gpf='git push --force-with-lease'

# Push force (sans protection - à utiliser avec précaution)
alias gpff='git push --force'

# Diff - Voir les différences
alias gd='git diff'

# Diff staged - Voir les différences des fichiers staged
alias gds='git diff --staged'

# Stash - Mettre de côté les modifications
alias gst='git stash'

# Stash pop - Récupérer les modifications mises de côté
alias gstp='git stash pop'

# Stash list - Lister les stash
alias gstl='git stash list'

# Rebase - Rebaser la branche
alias gr='git rebase'

# Rebase continue - Continuer le rebase après résolution de conflits
alias grc='git rebase --continue'

# Rebase abort - Annuler le rebase
alias gra='git rebase --abort'

# Rebase skip - Passer le commit actuel
alias grs='git rebase --skip'

# Rebase interactif
alias gri='git rebase -i'

# Fetch - Récupérer les changements sans merger
alias gf='git fetch'

# Fetch all - Récupérer de tous les remotes
alias gfa='git fetch --all'

# Merge - Fusionner une branche
alias gm='git merge'

# Remote - Voir les remotes
alias grv='git remote -v'

# Reset - Annuler des modifications
alias grh='git reset HEAD'

# Reset hard - Annuler toutes les modifications
alias grhh='git reset --hard'

# Clean - Supprimer les fichiers non suivis
alias gclean='git clean -fd'

# Reflog - Voir l'historique de référence
alias grl='git reflog'

# Show - Afficher les détails d'un commit
alias gsh='git show'
```

**Fonctions avancées :**

Ajoutez également ces fonctions utiles :

```bash
# Rebase interactif sur main/master
grim() {
    local main_branch
    if git rev-parse --verify main >/dev/null 2>&1; then
        main_branch="main"
    else
        main_branch="master"
    fi
    git rebase -i "$main_branch"
}

# Rebase update from main/master (checkout main, pull, checkout back, rebase)
grum() {
    local current_branch
    local main_branch
    
    current_branch=$(git rev-parse --abbrev-ref HEAD)
    
    if git rev-parse --verify main >/dev/null 2>&1; then
        main_branch="main"
    else
        main_branch="master"
    fi
    
    git checkout "$main_branch" && \
    git pull && \
    git checkout "$current_branch" && \
    git rebase "$main_branch"
}

# Créer une nouvelle branche et basculer dessus
gcnb() {
    if [ -z "$1" ]; then
        echo "Usage: gcnb <branch-name>"
        return 1
    fi
    git checkout -b "$1"
}

# Supprimer les branches locales déjà mergées
gbclean() {
    local main_branch
    if git rev-parse --verify main >/dev/null 2>&1; then
        main_branch="main"
    else
        main_branch="master"
    fi
    git branch --merged "$main_branch" | grep -v "$main_branch" | xargs -r git branch -d
}

# Afficher les commits non pushés
gunpushed() {
    git log @{u}.. --oneline
}
```

**Utilisation :**

Après avoir ajouté ces alias, rechargez votre configuration :

```bash
# Pour Bash
source ~/.bashrc

# Pour Zsh
source ~/.zshrc
```

Vous pouvez maintenant utiliser les alias :

```bash
gs              # au lieu de git status
gl              # au lieu de git log --oneline
gcm "Mon commit"  # au lieu de git commit -m "Mon commit"
gp              # au lieu de git push
grim            # rebase interactif sur main/master
grum            # met à jour depuis main et rebase
```

---

## 💡 Conseils d'utilisation

### Personnalisation

N'hésitez pas à personnaliser ces alias selon vos préférences :
- Ajoutez vos propres alias pour les commandes que vous utilisez fréquemment
- Modifiez les alias existants si vous préférez d'autres raccourcis
- Supprimez les alias que vous n'utilisez jamais

### Attention avec les alias

- **`gpf` vs `gpff`** : Préférez toujours `gpf` (push force with lease) à `gpff` (push force). Le `--force-with-lease` évite d'écraser accidentellement le travail de vos collègues.
- **`grhh`** : Le reset hard supprime définitivement vos modifications non commitées. Utilisez-le avec précaution !
- **`gclean`** : Cette commande supprime les fichiers non suivis. Vérifiez d'abord avec `git clean -fd -n` (dry-run).

### Intégration avec Oh My Zsh

Si vous utilisez **Oh My Zsh**, vous pouvez activer le plugin Git intégré qui fournit déjà de nombreux alias :

```bash
# Dans ~/.zshrc
plugins=(git)
```

Consultez la [liste complète des alias Oh My Zsh Git](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git) pour voir tous les alias disponibles.

---

## 📚 Ressources supplémentaires

- [Documentation posh-git](https://github.com/dahlbyk/posh-git)
- [Starship - Prompt personnalisable](https://starship.rs/)
- [Oh My Zsh](https://ohmyz.sh/)
- [Powerlevel10k](https://github.com/romkatv/powerlevel10k)
- [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt)

---

**Happy Git workflow! 🚀**
