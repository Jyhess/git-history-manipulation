#!/usr/bin/env python3
"""
Exercice 1.2: Reword d'un ancien commit
Ce script crée une branche avec une faute d'orthographe dans un message de commit.
"""

import os
import subprocess
import sys

def run(cmd, check=True):
    """Execute a shell command"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr and result.returncode != 0:
        print(result.stderr, file=sys.stderr)
    return result

def main():
    # Save current branch
    current_branch = run("git branch --show-current").stdout.strip()
    
    # Switch to main branch as base
    run("git checkout main", check=False)
    if run("git rev-parse --verify main", check=False).returncode != 0:
        print("Warning: 'main' branch doesn't exist, using current branch")
        run("git checkout -b main", check=False)
    
    # Clean up existing branch if it exists
    run("git branch -D exercice1_2", check=False)
    
    # Create exercice1_2 branch
    print("\n=== Creating exercice1_2 branch ===")
    run("git checkout -b exercice1_2")
    
    # Create exercise directory
    os.makedirs("exercices/exercice1_2", exist_ok=True)
    
    # Commit 1: Initial commit
    with open("exercices/exercice1_2/file1.txt", "w") as f:
        f.write("Hello world\n")
        f.write("This is the first file.\n")
    run("git add exercices/exercice1_2")
    run("git commit -m 'Initial commit'")
    
    # Commit 2: Add second file (avec faute d'orthographe)
    with open("exercices/exercice1_2/file2.txt", "w") as f:
        f.write("This is a secnd commit.\n")  # faute volontaire
        f.write("Some content here.\n")
    run("git add exercices/exercice1_2/file2.txt")
    run("git commit -m 'Add secnd file'")  # faute volontaire dans le message
    
    # Commit 3: Add third file
    with open("exercices/exercice1_2/file3.txt", "w") as f:
        f.write("Third file content\n")
        f.write("Everything is fine here.\n")
    run("git add exercices/exercice1_2/file3.txt")
    run("git commit -m 'Add third file'")
    
    print("\n" + "="*60)
    print("✓ Exercice 1.2 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice1_2 (with 3 commits)")
    
    print("\n" + "="*60)
    print("EXERCICE 1.2 : REWORD D'UN ANCIEN COMMIT")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Corrigez la faute d'orthographe dans le message du 2ème commit")
    print("   'Add secnd file' → 'Add second file'")
    
    print("\n📝 CONTEXTE:")
    print("   Un commit contient une faute d'orthographe dans son message.")
    print("   Vous devez corriger ce message sans modifier le contenu du commit.")
    
    print("\n💡 COMMANDES À EXÉCUTER:")
    print("   git log --oneline           # Voir les 3 commits")
    print("   git rebase -i HEAD~3        # Rebase interactif")
    print("   # Dans l'éditeur, remplacez 'pick' par 'reword' pour le 2ème commit")
    print("   # Sauvegardez et fermez l'éditeur")
    print("   # Corrigez le message dans le nouvel éditeur qui s'ouvre")
    print("   git log --oneline           # Vérifier la correction")
    
    print("\n✅ RÉSULTAT ATTENDU:")
    print("   * commit Add third file")
    print("   * commit Add second file  ← Message corrigé")
    print("   * commit Initial commit")
    
    print("\n❓ QUESTION BONUS:")
    print("   Voyez-vous une 2ème façon d'obtenir le même résultat ?")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice1_2'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch (already on it, but make it explicit)
    run("git checkout exercice1_2")

if __name__ == "__main__":
    main()
