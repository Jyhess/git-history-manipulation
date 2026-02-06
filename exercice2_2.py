#!/usr/bin/env python3
"""
Exercice 2.2: Nettoyage massif - squash + reword
Ce script crée une branche avec de nombreux petits commits désorganisés à nettoyer.
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
    run("git branch -D exercice2_2", check=False)
    
    # Create exercice2_2 branch
    print("\n=== Creating exercice2_2 branch ===")
    run("git checkout -b exercice2_2")
    
    # Create exercise directory
    os.makedirs("exercices/exercice2_2", exist_ok=True)
    
    # Theme 1: Préparation (commits 1-3)
    with open("exercices/exercice2_2/config.json", "w") as f:
        f.write('{"version": "1.0"}\n')
    run("git add exercices/exercice2_2/config.json")
    run("git commit -m 'add config'")
    
    with open("exercices/exercice2_2/.gitignore", "w") as f:
        f.write("*.pyc\n__pycache__/\n")
    run("git add exercices/exercice2_2/.gitignore")
    run("git commit -m 'gitignore'")
    
    with open("exercices/exercice2_2/requirements.txt", "w") as f:
        f.write("pytest==7.0.0\n")
    run("git add exercices/exercice2_2/requirements.txt")
    run("git commit -m 'deps'")
    
    # Theme 2: Feature (commits 4-7)
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("def login():\n    pass\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'start auth'")
    
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("def login(user, pwd):\n    return True\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'wip'")
    
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("def login(user, pwd):\n    return user == 'admin'\n\ndef logout():\n    pass\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'logout'")
    
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("def login(user, pwd):\n    return user == 'admin' and pwd == 'secret'\n\ndef logout():\n    return True\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'fix login and logout'")
    
    # Theme 3: Refactor (commits 8-10)
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("\"\"\"Authentication module\"\"\"\n\ndef login(user, pwd):\n    return user == 'admin' and pwd == 'secret'\n\ndef logout():\n    return True\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'add docstring'")
    
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("\"\"\"Authentication module\"\"\"\n\ndef validate_credentials(username, password):\n    return username == 'admin' and password == 'secret'\n\ndef logout():\n    return True\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'rename function'")
    
    with open("exercices/exercice2_2/auth.py", "w") as f:
        f.write("\"\"\"Authentication module\"\"\"\n\nADMIN_USER = 'admin'\nADMIN_PASS = 'secret'\n\ndef validate_credentials(username, password):\n    return username == ADMIN_USER and password == ADMIN_PASS\n\ndef logout():\n    return True\n")
    run("git add exercices/exercice2_2/auth.py")
    run("git commit -m 'extract constants'")
    
    print("\n" + "="*60)
    print("✓ Exercice 2.2 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice2_2 (with 10 messy commits)")
    print("\nYour task:")
    print("  Clean up the history to get 3 clear commits:")
    print("  1. Preparation: Initial setup and configuration")
    print("  2. Feature: Implement user authentication")
    print("  3. Refactor: Clean and optimize code")
    print("\nCommands to use:")
    print("  git checkout exercice2_2")
    print("  git log --oneline")
    print("  git rebase -i HEAD~10")
    print("  (Squash related commits and reword messages)")
    print("="*60)
    
    # Return to original branch
    if current_branch:
        run(f"git checkout {current_branch}", check=False)

if __name__ == "__main__":
    main()
