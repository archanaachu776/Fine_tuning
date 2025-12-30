"""
============================================================
QUICK DEMO - Run this for a fast 5-minute demonstration!
============================================================

Perfect for showing the core concept quickly.
No interaction required - just run and watch!
"""

from groq import Groq  
import time

GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

def slow_print(text, delay=0.02):
    """Print text slowly for dramatic effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    print("\n" + "="*70)
    slow_print("   FINE-TUNING EXPLAINED IN 5 MINUTES")
    print("="*70)

    time.sleep(1)

    # Part 1: The Analogy
    print("\n" + "-"*70)
    slow_print("PART 1: What is Fine-Tuning?")
    print("-"*70)

    slow_print("""
    Think of AI like a MEDICAL SCHOOL GRADUATE:

    Medical Graduate          →    General Doctor
    (Base AI Model)               (Knows everything, but not specialized)

                    ↓ SPECIALIZED TRAINING ↓

    After Residency           →    Heart Surgeon
    (Fine-Tuned Model)            (Expert in YOUR specific area)

    Fine-tuning = Teaching AI to be expert in YOUR specific task!
    """, 0.01)

    time.sleep(2)

    # Part 2: Live Demo
    print("\n" + "-"*70)
    slow_print("PART 2: Live Demonstration")
    print("-"*70)

    question = "How do I return a product?"
    slow_print(f"\n    Customer asks: '{question}'")
    print("\n")

    # Base model
    slow_print("    [BASE MODEL - Generic AI]", 0.01)
    slow_print("    Thinking...", 0.05)

    response1 = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": question}],
        max_tokens=100
    )
    print(f"\n    {response1.choices[0].message.content[:200]}...")

    time.sleep(2)

    # Fine-tuned model (simulated)
    slow_print("\n    [FINE-TUNED MODEL - Trained for TechMart Store]", 0.01)
    slow_print("    Thinking...", 0.05)

    techmart_system = """You are TechMart's customer support agent. Our policy:
    - 30-day returns with receipt
    - Free pickup for defective items
    - Refund in 3-5 business days
    Always mention TechMart and be friendly!"""

    response2 = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": techmart_system},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    print(f"\n    {response2.choices[0].message.content[:300]}")

    time.sleep(2)

    # Part 3: Two Types
    print("\n" + "-"*70)
    slow_print("PART 3: Two Types of Fine-Tuning")
    print("-"*70)

    slow_print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │                                                                 │
    │   TYPE 1: FULL FINE-TUNING                                      │
    │   ─────────────────────────                                     │
    │   - Updates ENTIRE model (all 7 billion parameters)             │
    │   - Like rewriting an entire textbook                           │
    │   - Cost: $1,000+ | Time: Days | Data: 10,000+ examples         │
    │                                                                 │
    │   TYPE 2: LoRA (RECOMMENDED!)                                   │
    │   ─────────────────────────────                                 │
    │   - Updates only 0.1% of model                                  │
    │   - Like adding sticky notes to a textbook                      │
    │   - Cost: $10-100 | Time: Hours | Data: 100-1000 examples       │
    │                                                                 │
    │   ★ START WITH LoRA - It's 100x cheaper and almost as good!     │
    │                                                                 │
    └─────────────────────────────────────────────────────────────────┘
    """, 0.005)

    time.sleep(2)

    # Part 4: Training Data
    print("\n" + "-"*70)
    slow_print("PART 4: Training Data is Simple!")
    print("-"*70)

    slow_print("""
    Training data = Just INPUT → OUTPUT pairs

    Example for Customer Support:
    ┌────────────────────────────────────────────────────────────────┐
    │ INPUT:  "How do I return a product?"                           │
    │ OUTPUT: "At TechMart, returns are easy! Just bring your        │
    │          receipt within 30 days..."                            │
    └────────────────────────────────────────────────────────────────┘

    Example for Sentiment Analysis:
    ┌────────────────────────────────────────────────────────────────┐
    │ INPUT:  "This product is amazing!"                             │
    │ OUTPUT: "POSITIVE"                                             │
    └────────────────────────────────────────────────────────────────┘

    That's it! Just examples of what you want the AI to learn.
    """, 0.008)

    time.sleep(2)

    # Summary
    print("\n" + "="*70)
    slow_print("   KEY TAKEAWAYS")
    print("="*70)

    slow_print("""
    1. Fine-tuning = Teaching AI YOUR specific knowledge

    2. Use LoRA (not full fine-tuning) - it's cheaper & easier

    3. Training data = Simple input/output examples

    4. Start with 100-500 examples

    5. Quality > Quantity (100 good examples beat 1000 bad ones)

    """, 0.01)

    print("="*70)
    slow_print("   Demo Complete! Questions?")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}")
        print("Make sure you have: pip install groq")