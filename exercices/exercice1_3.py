#!/usr/bin/env python3
"""
Exercice 1.3: Squash de commits
Ce script crée une branche avec des commits "fix:" qui doivent être squashés avec leurs commits précédents.
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
    run("git branch -D exercice1_3", check=False)
    
    # Create exercice1_3 branch
    print("\n=== Creating exercice1_3 branch ===")
    run("git checkout -b exercice1_3")
    
    # Create exercise directory
    os.makedirs("exercices/exercice1_3", exist_ok=True)
    
    # Commit 1: Initial setup
    with open("exercices/exercice1_3/setup.py", "w") as f:
        f.write("# Setup script\n")
        f.write("print('Setting up project')\n")
    run("git add exercices/exercice1_3")
    run("git commit -m 'Initial setup'")
    
    # Commit 2: Add feature
    with open("exercices/exercice1_3/feature.py", "w") as f:
        f.write("# Feature implementation\n")
        f.write("def calculate():\n")
        f.write("    return 42  # TODO: fix this\n")
    run("git add exercices/exercice1_3/feature.py")
    run("git commit -m 'Add feature'")
    
    # Commit 3: fix feature typo
    with open("exercices/exercice1_3/feature.py", "w") as f:
        f.write("# Feature implementation\n")
        f.write("def calculate():\n")
        f.write("    return 42\n")
    run("git add exercices/exercice1_3/feature.py")
    run("git commit -m 'fix: feature typo'")
    
    # Commit 4: Add tests
    with open("exercices/exercice1_3/test_feature.py", "w") as f:
        f.write("# Tests\n")
        f.write("def test_calculate()\n")  # syntax error volontaire
        f.write("    assert calculate() == 42\n")
    run("git add exercices/exercice1_3/test_feature.py")
    run("git commit -m 'Add tests'")
    
    # Commit 5: fix tests syntax
    with open("exercices/exercice1_3/test_feature.py", "w") as f:
        f.write("# Tests\n")
        f.write("def test_calculate():\n")
        f.write("    assert calculate() == 42\n")
    run("git add exercices/exercice1_3/test_feature.py")
    run("git commit -m 'fix: tests syntax'")
    
    # Commit 6: Add documentation
    with open("exercices/exercice1_3/README.md", "w") as f:
        f.write("# Documentation\n")
        f.write("\n")
        f.write("This feature calculates things.\n")
    run("git add exercices/exercice1_3/README.md")
    run("git commit -m 'Add documentation'")
    
    print("\n" + "="*60)
    print("✓ Exercice 1.3 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice1_3 (with 6 commits)")
    
    print("\n" + "="*60)
    print("EXERCICE 1.3 : SQUASH DE COMMITS")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Fusionnez les commits 'fix:' avec leurs commits précédents")
    print("   correspondants pour obtenir un historique propre")
    
    print("\n📝 CONTEXTE:")
    print("   L'historique contient des commits de 'fix' qui devraient")
    print("   être fusionnés avec les commits qu'ils corrigent.")
    print("   - 'fix: feature typo' doit être fusionné avec 'Add feature'")
    print("   - 'fix: tests syntax' doit être fusionné avec 'Add tests'")
    
    print("\n✅ RÉSULTAT ATTENDU (4 commits):")
    print("   * commit Add documentation")
    print("   * commit Add tests (incluant fix: tests syntax)")
    print("   * commit Add feature (incluant fix: feature typo)")
    print("   * commit Initial setup")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice1_3'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch (already on it, but make it explicit)
    run("git checkout exercice1_3")

if __name__ == "__main__":
    main()
