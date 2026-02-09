#!/usr/bin/env python3
"""
Exercice 1.1: Rebase de branche
Ce script crée deux branches avec des commits divergents pour pratiquer le rebase.
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
    
    # Clean up existing branches if they exist
    run("git branch -D exercice1_1_main", check=False)
    run("git branch -D exercice1_1_feature", check=False)
    
    # Create exercice1_1_main branch
    print("\n=== Creating exercice1_1_main branch ===")
    run("git checkout -b exercice1_1_main")
    
    # Create exercise directory
    os.makedirs("exercices/exercice1_1", exist_ok=True)
    
    # Commit 1: Initial setup
    with open("exercices/exercice1_1/config.txt", "w") as f:
        f.write("# Configuration\n")
        f.write("version=1.0\n")
    run("git add exercices/exercice1_1")
    run("git commit -m 'Initial setup'")
    
    # Save this point to create feature branch
    base_commit = run("git rev-parse HEAD").stdout.strip()
    
    # Commit 2: Update configuration (on main)
    with open("exercices/exercice1_1/config.txt", "a") as f:
        f.write("debug=false\n")
    run("git add exercices/exercice1_1/config.txt")
    run("git commit -m 'Update configuration'")
    
    # Commit 3: Fix bug in main
    with open("exercices/exercice1_1/bugfix.txt", "w") as f:
        f.write("Fixed critical bug in main branch\n")
    run("git add exercices/exercice1_1/bugfix.txt")
    run("git commit -m 'Fix bug in main'")
    
    # Create feature branch from earlier point
    print("\n=== Creating exercice1_1_feature branch ===")
    run(f"git checkout -b exercice1_1_feature {base_commit}")
    
    # Commit on feature: Add feature implementation
    with open("exercices/exercice1_1/feature.txt", "w") as f:
        f.write("# New Feature\n")
        f.write("This is the new feature implementation\n")
    run("git add exercices/exercice1_1/feature.txt")
    run("git commit -m 'Add feature implementation'")
    
    print("\n" + "="*60)
    print("✓ Exercice 1.1 initialized successfully!")
    print("="*60)
    print("\nBranches created:")
    print("  - exercice1_1_main (with 3 commits)")
    print("  - exercice1_1_feature (diverged, with 2 commits)")
    
    print("\n" + "="*60)
    print("EXERCICE 1.1 : REBASE DE BRANCHE")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Rebasez la branche 'exercice1_1_feature' sur le HEAD")
    print("   de la branche 'exercice1_1_main'")
    
    print("\n📝 CONTEXTE:")
    print("   Deux branches ont divergé depuis un point commun.")
    print("   La branche 'exercice1_1_main' a avancé avec 2 nouveaux commits.")
    print("   La branche 'exercice1_1_feature' a 1 commit de fonctionnalité.")
       
    print("\n✅ RÉSULTAT ATTENDU:")
    print("   * commit (exercice1_1_feature) Add feature implementation")
    print("   * commit Fix bug in main")
    print("   * commit Update configuration")
    print("   * commit (exercice1_1_main) Initial setup")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice1_1_feature'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch
    run("git checkout exercice1_1_feature")

if __name__ == "__main__":
    main()
