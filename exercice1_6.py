#!/usr/bin/env python3
"""
Exercice 1.6: Récupérer une branche perdue depuis le reflog
Ce script crée une branche puis la supprime pour simuler une suppression accidentelle.
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
    run("git branch -D exercice1_6", check=False)
    
    # Create exercice1_6 branch
    print("\n=== Creating exercice1_6 branch ===")
    run("git checkout -b exercice1_6")
    
    # Create exercise directory
    os.makedirs("exercices/exercice1_6", exist_ok=True)
    
    # Commit 1: Start new feature
    with open("exercices/exercice1_6/feature.py", "w") as f:
        f.write("# New feature in progress\n")
        f.write("def new_feature():\n")
        f.write("    pass  # TODO: implement\n")
    run("git add exercices/exercice1_6")
    run("git commit -m 'Start new feature'")
    
    # Commit 2: Work in progress
    with open("exercices/exercice1_6/feature.py", "w") as f:
        f.write("# New feature in progress\n")
        f.write("def new_feature():\n")
        f.write("    data = fetch_data()\n")
        f.write("    return data\n")
    run("git add exercices/exercice1_6/feature.py")
    run("git commit -m 'Work in progress'")
    
    # Commit 3: Important feature completed
    with open("exercices/exercice1_6/feature.py", "w") as f:
        f.write("# New feature - COMPLETED\n")
        f.write("def new_feature():\n")
        f.write("    data = fetch_data()\n")
        f.write("    processed = process(data)\n")
        f.write("    return processed\n")
        f.write("\n")
        f.write("def fetch_data():\n")
        f.write("    return 'data'\n")
        f.write("\n")
        f.write("def process(data):\n")
        f.write("    return data.upper()\n")
    run("git add exercices/exercice1_6/feature.py")
    run("git commit -m 'Important feature completed'")
    
    # Save the commit hash for display
    last_commit = run("git rev-parse HEAD").stdout.strip()
    
    # Now delete the branch (simulate accidental deletion)
    print("\n=== Simulating accidental branch deletion ===")
    run("git checkout main")
    run("git branch -D exercice1_6")
    
    print("\n" + "="*60)
    print("✓ Exercice 1.6 initialized successfully!")
    print("="*60)
    print("\nOops! The branch exercice1_6 was accidentally deleted!")
    print(f"Last commit was: {last_commit[:8]}")
    
    print("\n" + "="*60)
    print("EXERCICE 1.6 : RÉCUPÉRER UNE BRANCHE PERDUE (REFLOG)")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Récupérez la branche 'exercice1_6' qui a été supprimée")
    print("   en utilisant le reflog")
    
    print("\n📝 CONTEXTE:")
    print("   La branche 'exercice1_6' contenait 3 commits importants.")
    print("   Elle vient d'être supprimée par erreur avec 'git branch -D'.")
    print("   Le reflog garde une trace de toutes les opérations Git.")
    
    print("\n💡 COMMANDES À EXÉCUTER:")
    print("   git reflog                  # Voir l'historique des opérations")
    print("   # Cherchez 'Important feature completed' dans le reflog")
    print(f"   git checkout -b exercice1_6 {last_commit[:8]}")
    print("   # OU utilisez le HEAD@{{N}} trouvé dans le reflog:")
    print("   # git checkout -b exercice1_6 HEAD@{N}")
    print("   git log --oneline           # Vérifier que la branche est récupérée")
    
    print("\n✅ RÉSULTAT ATTENDU (3 commits):")
    print("   * commit Important feature completed")
    print("   * commit Work in progress")
    print("   * commit Start new feature")
    
    print("\n💡 ASTUCE:")
    print("   Le reflog conserve l'historique pendant 90 jours par défaut.")
    print("   Même après un 'git branch -D', les commits restent accessibles !")
    
    print("\n" + "="*60)
    print("Vous êtes actuellement sur la branche 'main'")
    print("Récupérez la branche 'exercice1_6' puis basculez dessus !")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
