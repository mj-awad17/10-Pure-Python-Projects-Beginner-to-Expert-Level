# 🎯 Project 01: Number Guessing Game (Pure Python)

Welcome to **Project 01** of the *Pure Python Project Series*!  
This is a **beginner-level** command-line game built using **only Python's standard features** — no external libraries are required.

---

## 🕹️ What is the Game?

In the **Number Guessing Game**, the computer randomly selects a number between **1 and 100**, and your goal is to guess it.

After each guess, the program tells you whether your guess is:

- 📉 Too low
- 📈 Too high
- ✅ Correct

You keep guessing until you find the correct number, and the program tracks how many attempts you take.

---

## 🧠 What You'll Learn

By building this simple game, you’ll practice key programming skills:

| Concept              | Description                                 |
|----------------------|---------------------------------------------|
| `input()`            | Reading input from the user                 |
| `int()`              | Converting input to integers                |
| `random.randint()`   | Generating random numbers                   |
| `if/elif/else`       | Conditional logic                           |
| `while loop`         | Repeating the guessing logic                |
| `try/except`         | Handling non-numeric input errors           |
| `Variables`          | Tracking guesses and attempts               |

---

## 🔧 How We Tackled the Project

### Step 1: Import `random`
We use Python’s built-in `random` module to generate the secret number.

```python
import random
secret_number = random.randint(1, 100)
```

### Step 2: Get User Input
User to guess the number using the `input()` function and convert it to an integer:

`guess = int(input("Take a guess: "))


