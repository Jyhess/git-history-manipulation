#!/usr/bin/env python3
"""
Exercice 2.1: Localisez et corrigez le commit fautif
Ce script crée une branche avec plusieurs commits, dont un introduit un bug.
Des tests sont fournis pour détecter le bug.
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
    run("git branch -D exercice2_1", check=False)
    
    # Create exercice2_1 branch
    print("\n=== Creating exercice2_1 branch ===")
    run("git checkout -b exercice2_1")
    
    # Create exercise directory
    os.makedirs("exercices/exercice2_1", exist_ok=True)
    
    # Commit 1: Initial implementation
    with open("exercices/exercice2_1/calculator.py", "w") as f:
        f.write("\"\"\"Simple calculator module\"\"\"\n")
        f.write("\n")
        f.write("def add(a, b):\n")
        f.write("    return a + b\n")
        f.write("\n")
        f.write("def subtract(a, b):\n")
        f.write("    return a - b\n")
    run("git add exercices/exercice2_1")
    run("git commit -m 'Initial calculator implementation'")
    
    # Commit 2: Add multiply function
    with open("exercices/exercice2_1/calculator.py", "w") as f:
        f.write("\"\"\"Simple calculator module\"\"\"\n")
        f.write("\n")
        f.write("def add(a, b):\n")
        f.write("    return a + b\n")
        f.write("\n")
        f.write("def subtract(a, b):\n")
        f.write("    return a - b\n")
        f.write("\n")
        f.write("def multiply(a, b):\n")
        f.write("    return a * b\n")
    run("git add exercices/exercice2_1/calculator.py")
    run("git commit -m 'Add multiply function'")
    
    # Commit 3: Add divide function (WITH BUG)
    with open("exercices/exercice2_1/calculator.py", "w") as f:
        f.write("\"\"\"Simple calculator module\"\"\"\n")
        f.write("\n")
        f.write("def add(a, b):\n")
        f.write("    return a + b\n")
        f.write("\n")
        f.write("def subtract(a, b):\n")
        f.write("    return a - b\n")
        f.write("\n")
        f.write("def multiply(a, b):\n")
        f.write("    return a * b\n")
        f.write("\n")
        f.write("def divide(a, b):\n")
        f.write("    return a * b  # BUG: should be a / b\n")
    run("git add exercices/exercice2_1/calculator.py")
    run("git commit -m 'Add divide function'")
    
    # Commit 4: Add power function
    with open("exercices/exercice2_1/calculator.py", "w") as f:
        f.write("\"\"\"Simple calculator module\"\"\"\n")
        f.write("\n")
        f.write("def add(a, b):\n")
        f.write("    return a + b\n")
        f.write("\n")
        f.write("def subtract(a, b):\n")
        f.write("    return a - b\n")
        f.write("\n")
        f.write("def multiply(a, b):\n")
        f.write("    return a * b\n")
        f.write("\n")
        f.write("def divide(a, b):\n")
        f.write("    return a * b  # BUG persists\n")
        f.write("\n")
        f.write("def power(a, b):\n")
        f.write("    return a ** b\n")
    run("git add exercices/exercice2_1/calculator.py")
    run("git commit -m 'Add power function'")
    
    # Commit 5: Add tests
    with open("exercices/exercice2_1/test_calculator.py", "w") as f:
        f.write("\"\"\"Tests for calculator module\"\"\"\n")
        f.write("from calculator import add, subtract, multiply, divide, power\n")
        f.write("\n")
        f.write("def test_add():\n")
        f.write("    assert add(2, 3) == 5\n")
        f.write("    assert add(-1, 1) == 0\n")
        f.write("\n")
        f.write("def test_subtract():\n")
        f.write("    assert subtract(5, 3) == 2\n")
        f.write("    assert subtract(1, 1) == 0\n")
        f.write("\n")
        f.write("def test_multiply():\n")
        f.write("    assert multiply(2, 3) == 6\n")
        f.write("    assert multiply(4, 5) == 20\n")
        f.write("\n")
        f.write("def test_divide():\n")
        f.write("    assert divide(6, 2) == 3\n")
        f.write("    assert divide(10, 5) == 2\n")
        f.write("\n")
        f.write("def test_power():\n")
        f.write("    assert power(2, 3) == 8\n")
        f.write("    assert power(5, 2) == 25\n")
    run("git add exercices/exercice2_1/test_calculator.py")
    run("git commit -m 'Add comprehensive tests'")
    
    print("\n" + "="*60)
    print("✓ Exercice 2.1 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice2_1 (with 5 commits, one contains a bug)")
    
    print("\n" + "="*60)
    print("EXERCICE 2.1 : LOCALISER ET CORRIGER LE COMMIT FAUTIF")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   1. Exécutez les tests et constatez qu'ils échouent")
    print("   2. Identifiez quel commit a introduit le bug")
    print("   3. Corrigez le bug DANS le commit qui l'a introduit")
    
    print("\n📝 CONTEXTE:")
    print("   Une suite de tests pytest est fournie. Un des commits")
    print("   de l'historique contient un bug qui fait échouer les tests.")
    print("   Vous devez trouver ce commit et corriger le bug directement")
    print("   dans ce commit (pas dans un nouveau commit).")
    
    print("\n💡 COMMANDES À EXÉCUTER:")
    print("   # 1. Vérifier que les tests échouent")
    print("   cd exercices/exercice2_1")
    print("   python -m pytest -v")
    print("   cd ../..")
    print("   ")
    print("   # 2. Examiner l'historique")
    print("   git log --oneline")
    print("   ")
    print("   # 3. Corriger le commit fautif")
    print("   git rebase -i HEAD~5")
    print("   # Marquez le commit 'Add divide function' avec 'edit'")
    print("   # Dans le fichier calculator.py, changez 'return a * b' en 'return a / b'")
    print("   git add exercices/exercice2_1/calculator.py")
    print("   git commit --amend")
    print("   git rebase --continue")
    print("   ")
    print("   # 4. Vérifier que les tests passent maintenant")
    print("   cd exercices/exercice2_1 && python -m pytest -v && cd ../..")
    
    print("\n✅ RÉSULTAT ATTENDU:")
    print("   Tous les tests passent et le bug est corrigé dans l'historique")
    
    print("\n💡 ASTUCE:")
    print("   Utilisez 'git log -p' pour voir les modifications de chaque commit")
    print("   Le bug est dans la fonction divide() qui utilise * au lieu de /")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice2_1'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch (already on it, but make it explicit)
    run("git checkout exercice2_1")

if __name__ == "__main__":
    main()
