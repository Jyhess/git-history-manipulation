#!/usr/bin/env python3
"""
Exercice 2.5: Réécriture complète d'un historique sale
Ce script crée un historique très désorganisé avec beaucoup de commits à nettoyer.
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
    run("git branch -D exercice2_5", check=False)
    
    # Create exercice2_5 branch
    print("\n=== Creating exercice2_5 branch ===")
    run("git checkout -b exercice2_5")
    
    # Create exercise directory
    os.makedirs("exercices/exercice2_5", exist_ok=True)
    
    # Chaotic commits - Theme 1: Setup (should be combined)
    with open("exercices/exercice2_5/config.ini", "w") as f:
        f.write("[app]\n")
    run("git add exercices/exercice2_5/config.ini")
    run("git commit -m 'init'")
    
    with open("exercices/exercice2_5/.gitignore", "w") as f:
        f.write("*.log\n")
    run("git add exercices/exercice2_5/.gitignore")
    run("git commit -m 'gitignore'")
    
    with open("exercices/exercice2_5/config.ini", "w") as f:
        f.write("[app]\nname=myapp\n")
    run("git add exercices/exercice2_5/config.ini")
    run("git commit -m 'update config'")
    
    with open("exercices/exercice2_5/requirements.txt", "w") as f:
        f.write("requests\n")
    run("git add exercices/exercice2_5/requirements.txt")
    run("git commit -m 'add deps'")
    
    # Theme 2: Core Feature (messy)
    with open("exercices/exercice2_5/main.py", "w") as f:
        f.write("# TODO: implement\n")
    run("git add exercices/exercice2_5/main.py")
    run("git commit -m 'wip'")
    
    with open("exercices/exercice2_5/main.py", "w") as f:
        f.write("def fetch():\n    pass\n")
    run("git add exercices/exercice2_5/main.py")
    run("git commit -m 'add fetch'")
    
    with open("exercices/exercice2_5/main.py", "w") as f:
        f.write("import requests\ndef fetch():\n    return requests.get('api')\n")
    run("git add exercices/exercice2_5/main.py")
    run("git commit -m 'implement fetch'")
    
    with open("exercices/exercice2_5/main.py", "w") as f:
        f.write("import requests\ndef fetch(url):\n    return requests.get(url)\n")
    run("git add exercices/exercice2_5/main.py")
    run("git commit -m 'fix'")
    
    with open("exercices/exercice2_5/processor.py", "w") as f:
        f.write("def process(data):\n    return data.upper()\n")
    run("git add exercices/exercice2_5/processor.py")
    run("git commit -m 'process data'")
    
    # Theme 3: Tests (scattered)
    with open("exercices/exercice2_5/test_main.py", "w") as f:
        f.write("def test_fetch():\n    pass\n")
    run("git add exercices/exercice2_5/test_main.py")
    run("git commit -m 'test'")
    
    with open("exercices/exercice2_5/test_processor.py", "w") as f:
        f.write("def test_process():\n    from processor import process\n    assert process('hi') == 'HI'\n")
    run("git add exercices/exercice2_5/test_processor.py")
    run("git commit -m 'more tests'")
    
    # Theme 4: Documentation (incomplete)
    with open("exercices/exercice2_5/README.md", "w") as f:
        f.write("# Project\n")
    run("git add exercices/exercice2_5/README.md")
    run("git commit -m 'readme'")
    
    with open("exercices/exercice2_5/README.md", "w") as f:
        f.write("# Project\n\n## Usage\nRun main.py\n")
    run("git add exercices/exercice2_5/README.md")
    run("git commit -m 'update readme'")
    
    with open("exercices/exercice2_5/API.md", "w") as f:
        f.write("# API Documentation\n\n## fetch(url)\nFetches data from URL\n")
    run("git add exercices/exercice2_5/API.md")
    run("git commit -m 'api docs'")
    
    print("\n" + "="*60)
    print("✓ Exercice 2.5 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice2_5 (with 14 chaotic commits)")
    
    print("\n" + "="*60)
    print("EXERCICE 2.5 : RÉÉCRITURE COMPLÈTE D'UN HISTORIQUE SALE")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Transformez 14 commits chaotiques en 4 commits propres et structurés")
    
    print("\n📝 CONTEXTE:")
    print("   L'historique est un vrai chaos: messages peu clairs (wip, fix, etc.),")
    print("   commits mal ordonnés, pas de structure. Vous devez le nettoyer")
    print("   complètement et créer un historique professionnel.")
    
    print("\n💡 THÈMES À REGROUPER:")
    print("   1. Setup (commits 1-4): Configuration initiale")
    print("   2. Core Feature (commits 5-9): Fonctionnalité principale")
    print("   3. Testing (commits 10-11): Tests")
    print("   4. Documentation (commits 12-14): Documentation")
    
    print("\n✅ RÉSULTAT ATTENDU (4 commits):")
    print("   * commit Documentation: Add complete project documentation")
    print("   * commit Testing: Add comprehensive test suite")
    print("   * commit Core feature: Implement complete feature")
    print("   * commit Setup: Initial project configuration")
    
    print("\n💡 CONSEIL:")
    print("   C'est un exercice difficile! Prenez votre temps pour analyser")
    print("   chaque commit et déterminer à quel thème il appartient.")
    print("   N'hésitez pas à utiliser 'git rebase --abort' si vous vous perdez.")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice2_5'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch (already on it, but make it explicit)
    run("git checkout exercice2_5")

if __name__ == "__main__":
    main()
