"""
============================================================
FINE-TUNING CLASS - MAIN MENU
============================================================

Run this file to navigate through all class materials.

============================================================
"""

import subprocess
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("""
    ============================================================
           FINE-TUNING LLMs - CLASS MATERIALS
           For Non-Technical Audience
    ============================================================

    MODULES:

    1. Simple Explanation
       - What is fine-tuning?
       - Base model vs Fine-tuned model demo

    2. Types of Fine-Tuning
       - Full Fine-Tuning explained
       - LoRA (Parameter-Efficient) explained
       - Visual comparisons

    3. Practical Demo
       - Before/After comparison
       - Real examples using Groq API

    4. Hands-On Exercise
       - Create your own training data
       - Interactive sentiment analysis

    5. Summary & Cheatsheet
       - Quick reference guide
       - Quiz to test knowledge

    0. Exit

    ============================================================
    """)

def run_module(module_num):
    modules = {
        1: "01_simple_explanation.py",
        2: "02_types_of_finetuning.py",
        3: "03_practical_demo.py",
        4: "04_hands_on_exercise.py",
        5: "05_summary_cheatsheet.py"
    }

    if module_num in modules:
        print(f"\n\nRunning: {modules[module_num]}")
        print("="*60 + "\n")
        subprocess.run([sys.executable, modules[module_num]])
        input("\n\nPress Enter to return to menu...")

def main():
    while True:
        clear_screen()
        print_menu()

        choice = input("Enter module number (0-5): ")

        if choice == '0':
            print("\nThank you for attending the Fine-Tuning class!")
            print("Happy fine-tuning! 🚀\n")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            run_module(int(choice))
        else:
            print("\nInvalid choice. Please enter 0-5.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    # First check if groq is installed
    try:
        from groq import Groq
        print("Groq library found!")
    except ImportError:
        print("Installing groq library...")
        subprocess.run([sys.executable, "-m", "pip", "install", "groq"])

    main()