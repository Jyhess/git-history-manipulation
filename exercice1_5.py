#!/usr/bin/env python3
"""
Exercice 1.5: Réorganisation des commits
Ce script crée une branche avec des commits dans le mauvais ordre.
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
    run("git branch -D exercice1_5", check=False)
    
    # Create exercice1_5 branch
    print("\n=== Creating exercice1_5 branch ===")
    run("git checkout -b exercice1_5")
    
    # Create exercise directory
    os.makedirs("exercices/exercice1_5", exist_ok=True)
    
    # Commit 1: Initial setup
    with open("exercices/exercice1_5/config.yaml", "w") as f:
        f.write("# Project configuration\n")
        f.write("project: myapp\n")
        f.write("version: 1.0\n")
    run("git add exercices/exercice1_5")
    run("git commit -m 'Initial setup'")
    
    # Commit 2: Add documentation (MAUVAIS ORDRE)
    with open("exercices/exercice1_5/README.md", "w") as f:
        f.write("# Documentation\n")
        f.write("\n")
        f.write("## Usage\n")
        f.write("Run the main feature to process data.\n")
    run("git add exercices/exercice1_5/README.md")
    run("git commit -m 'Add documentation'")
    
    # Commit 3: Add main feature (MAUVAIS ORDRE)
    with open("exercices/exercice1_5/feature.py", "w") as f:
        f.write("# Main feature\n")
        f.write("def process():\n")
        f.write("    return 'Processed'\n")
    run("git add exercices/exercice1_5/feature.py")
    run("git commit -m 'Add main feature'")
    
    # Commit 4: Add tests (MAUVAIS ORDRE)
    with open("exercices/exercice1_5/test_feature.py", "w") as f:
        f.write("# Tests\n")
        f.write("def test_process():\n")
        f.write("    assert process() == 'Processed'\n")
    run("git add exercices/exercice1_5/test_feature.py")
    run("git commit -m 'Add tests'")
    
    print("\n" + "="*60)
    print("✓ Exercice 1.5 initialized successfully!")
    print("="*60)
    print("\nBranch created:")
    print("  - exercice1_5 (with 4 commits in wrong order)")
    print("\nCurrent order:")
    print("  1. Initial setup")
    print("  2. Add documentation")
    print("  3. Add main feature")
    print("  4. Add tests")
    print("\nYour task:")
    print("  Reorder commits to get logical sequence:")
    print("  1. Initial setup")
    print("  2. Add tests")
    print("  3. Add main feature")
    print("  4. Add documentation")
    print("\nCommands to use:")
    print("  git checkout exercice1_5")
    print("  git rebase -i HEAD~4")
    print("  (Reorder the lines in the desired sequence)")
    print("="*60)
    
    # Return to original branch
    if current_branch:
        run(f"git checkout {current_branch}", check=False)

if __name__ == "__main__":
    main()
