#!/usr/bin/env python3
"""
Exercice 1.4: Suppression de commit
Ce script crée une branche avec un commit à supprimer (fichier temporaire ajouté par erreur).
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
    run("git branch -D exercice1_4", check=False)
    
    # Create exercice1_4 branch
    print("\n=== Creating exercice1_4 branch ===")
    run("git checkout -b exercice1_4")
    
    # Create exercise directory
    os.makedirs("exercices/exercice1_4", exist_ok=True)
    
    # Commit 1: Initial commit
    with open("exercices/exercice1_4/main.py", "w") as f:
        f.write("# Main application\n")
        f.write("def main():\n")
        f.write("    print('Hello, World!')\n")
        f.write("\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    main()\n")
    run("git add exercices/exercice1_4")
    run("git commit -m 'Initial commit'")
    
    # Commit 2: Add temp file (TO BE DELETED)
    with open("exercices/exercice1_4/temp_debug.txt", "w") as f:
        f.write("DEBUG: This file was added by mistake\n")
        f.write("DEBUG: Should not be in version control\n")
        f.write("DEBUG: Contains temporary debugging info\n")
    run("git add exercices/exercice1_4/temp_debug.txt")
    run("git commit -m 'WIP: Add temporary debug file'")
    
    # Commit 3: Add core functionality
    with open("exercices/exercice1_4/core.py", "w") as f:
        f.write("# Core functionality\n")
        f.write("def process_data(data):\n")
        f.write("    return data.upper()\n")
    run("git add exercices/exercice1_4/core.py")
    run("git commit -m 'Add core functionality'")
    
    # Commit 4: Add final feature
    with open("exercices/exercice1_4/utils.py", "w") as f:
        f.write("# Utility functions\n")
        f.write("def validate(text):\n")
        f.write("    return len(text) > 0\n")
    run("git add exercices/exercice1_4/utils.py")
    run("git commit -m 'Add final feature'")
    
    print("\n" + "="*60)
    print("✓ Exercice 1.4 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice1_4 (with 4 commits)")
    
    print("\n" + "="*60)
    print("EXERCICE 1.4 : SUPPRESSION DE COMMIT")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Supprimez le 2ème commit qui a été ajouté par erreur")
    print("   (celui qui contient temp_debug.txt)")
    
    print("\n📝 CONTEXTE:")
    print("   Un fichier temporaire a été commité par erreur.")
    print("   Ce commit doit être complètement supprimé de l'historique.")
    
    print("\n✅ RÉSULTAT ATTENDU (3 commits):")
    print("   * commit Add final feature")
    print("   * commit Add core functionality")
    print("   * commit Initial commit")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice1_4'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch (already on it, but make it explicit)
    run("git checkout exercice1_4")

if __name__ == "__main__":
    main()
