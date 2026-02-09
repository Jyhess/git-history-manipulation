#!/usr/bin/env python3
"""
Exercice 2.3: Extraction d'un fix dans le mauvais commit
Ce script crée une situation où un fix a été inclus dans le mauvais commit.
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
    run("git branch -D exercice2_3", check=False)
    
    # Create exercice2_3 branch
    print("\n=== Creating exercice2_3 branch ===")
    run("git checkout -b exercice2_3")
    
    # Create exercise directory
    os.makedirs("exercices/exercice2_3", exist_ok=True)
    
    # Commit 1: Initial implementation
    with open("exercices/exercice2_3/user.py", "w") as f:
        f.write("class User:\n")
        f.write("    def __init__(self, name):\n")
        f.write("        self.name = name\n")
        f.write("\n")
        f.write("    def greet(self):\n")
        f.write("        return f'Hello, {self.name}'\n")
    run("git add exercices/exercice2_3")
    run("git commit -m 'Add User class'")
    
    # Commit 2: Add validation (INCOMPLETE - missing age validation)
    with open("exercices/exercice2_3/user.py", "w") as f:
        f.write("class User:\n")
        f.write("    def __init__(self, name, age):\n")
        f.write("        self.name = name\n")
        f.write("        self.age = age  # BUG: No validation\n")
        f.write("\n")
        f.write("    def greet(self):\n")
        f.write("        return f'Hello, {self.name}'\n")
        f.write("\n")
        f.write("    def validate_name(self):\n")
        f.write("        return len(self.name) > 0\n")
    run("git add exercices/exercice2_3/user.py")
    run("git commit -m 'Add age and validation'")
    
    # Commit 3: Add profile method (WRONG: contains age validation fix)
    with open("exercices/exercice2_3/user.py", "w") as f:
        f.write("class User:\n")
        f.write("    def __init__(self, name, age):\n")
        f.write("        self.name = name\n")
        f.write("        if age < 0 or age > 150:  # FIX: This should be in commit 2!\n")
        f.write("            raise ValueError('Invalid age')\n")
        f.write("        self.age = age\n")
        f.write("\n")
        f.write("    def greet(self):\n")
        f.write("        return f'Hello, {self.name}'\n")
        f.write("\n")
        f.write("    def validate_name(self):\n")
        f.write("        return len(self.name) > 0\n")
        f.write("\n")
        f.write("    def get_profile(self):\n")
        f.write("        return f'{self.name}, {self.age} years old'\n")
    run("git add exercices/exercice2_3/user.py")
    run("git commit -m 'Add profile method'")
    
    # Commit 4: Add tests
    with open("exercices/exercice2_3/test_user.py", "w") as f:
        f.write("from user import User\n")
        f.write("import pytest\n")
        f.write("\n")
        f.write("def test_user_creation():\n")
        f.write("    user = User('Alice', 30)\n")
        f.write("    assert user.name == 'Alice'\n")
        f.write("    assert user.age == 30\n")
        f.write("\n")
        f.write("def test_invalid_age():\n")
        f.write("    with pytest.raises(ValueError):\n")
        f.write("        User('Bob', -5)\n")
        f.write("\n")
        f.write("def test_profile():\n")
        f.write("    user = User('Charlie', 25)\n")
        f.write("    assert user.get_profile() == 'Charlie, 25 years old'\n")
    run("git add exercices/exercice2_3/test_user.py")
    run("git commit -m 'Add tests'")
    
    print("\n" + "="*60)
    print("✓ Exercice 2.3 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice2_3 (with 4 commits)")
    
    print("\n" + "="*60)
    print("EXERCICE 2.3 : EXTRACTION D'UN FIX DU MAUVAIS COMMIT")
    print("="*60)
    print("\n📋 OBJECTIF:")
    print("   Déplacez la validation d'age du commit 3 vers le commit 2")
    print("   où elle aurait dû être initialement")
    
    print("\n📝 CONTEXTE:")
    print("   Le commit 2 'Add age and validation' ajoute un champ 'age'")
    print("   mais sans validation. Le commit 3 'Add profile method' ajoute")
    print("   une méthode get_profile() ET la validation d'age.")
    print("   La validation d'age devrait être dans le commit 2.")
    
    print("\n✅ RÉSULTAT ATTENDU:")
    print("   Le fix de validation est maintenant dans le commit 2,")
    print("   et le commit 3 contient seulement get_profile()")
    
    print("\n💡 ASTUCE AVANCÉE:")
    print("   Utilisez 'git add -p' pour ajouter seulement certaines lignes")
    print("   ou éditez manuellement le fichier entre deux commits")
    
    print("\n" + "="*60)
    print("Vous êtes maintenant sur la branche 'exercice2_3'")
    print("Vous pouvez commencer l'exercice !")
    print("="*60 + "\n")
    
    # Switch to exercise branch (already on it, but make it explicit)
    run("git checkout exercice2_3")

if __name__ == "__main__":
    main()
