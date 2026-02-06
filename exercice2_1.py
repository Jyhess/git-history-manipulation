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
    print("\nYour task:")
    print("  1. Run tests: pytest exercices/exercice2_1")
    print("  2. Identify which commit introduced the bug")
    print("  3. Fix the bug IN THE COMMIT that introduced it")
    print("\nCommands to use:")
    print("  git checkout exercice2_1")
    print("  pytest exercices/exercice2_1")
    print("  git log --oneline")
    print("  git rebase -i HEAD~5")
    print("  (Mark the faulty commit with 'edit', fix, then 'git commit --amend')")
    print("="*60)
    
    # Return to original branch
    if current_branch:
        run(f"git checkout {current_branch}", check=False)

if __name__ == "__main__":
    main()
