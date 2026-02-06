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
    with open("exercices/exercice1_4/temp_debug.log", "w") as f:
        f.write("DEBUG: This file was added by mistake\n")
        f.write("DEBUG: Should not be in version control\n")
        f.write("DEBUG: Contains temporary debugging info\n")
    run("git add exercices/exercice1_4/temp_debug.log")
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
    print("\nYour task:")
    print("  Delete the 2nd commit (temp_debug.log was added by mistake)")
    print("  Final result should have 3 commits:")
    print("  - Initial commit")
    print("  - Add core functionality")
    print("  - Add final feature")
    print("\nCommands to use:")
    print("  git checkout exercice1_4")
    print("  git rebase -i HEAD~4")
    print("  (Mark the 2nd commit with 'drop' or delete the line)")
    print("="*60)
    
    # Return to original branch
    if current_branch:
        run(f"git checkout {current_branch}", check=False)

if __name__ == "__main__":
    main()
