# 🧮 Project 02: Simple Calculator – CLI Math Wizard 🧙‍♂️➕➖✖️➗

Welcome to **Project 2** of the *Pure Python Project Series*!

This isn’t just your average calculator – this one lives in your terminal and keeps crunching numbers until you tell it to stop. Whether you want to add, subtract, multiply, or divide – this CLI math wizard has you covered.

---

## 🔍 What is This Project About?

The **Simple Calculator** is a command-line tool that:

✅ Accepts two numbers  
✅ Asks for an operation (add, subtract, multiply, divide)  
✅ Returns the result  
✅ Loops until the user says "exit" or "stop"

---

## 🧠 What You'll Learn

Let’s break down the key Python concepts you’ll practice in this project:

| ⁉ Concept           | 💡 Description |
|---------------------|----------------|
| `input()`           | Used to get user-entered numbers and operations |
| `while` loop        | Keeps the calculator running until the user quits |
| `functions`         | Each operation is inside a function for reusability |
| `try/except`        | Prevents crashing from bad input (e.g. dividing by zero, text instead of numbers) |
| Arithmetic Operators| You'll use `+`, `-`, `*`, and `/` to perform calculations |

---

## 🔄 How the Program Works

Here’s the **step-by-step flow** of the calculator:

1. 🎯 Start the program with a welcome message.
2. 🔢 Ask the user for the **first number**.
3. ➕ Ask for the **operation** (`+`, `-`, `*`, `/`).
4. 🔢 Ask for the **second number**.
5. 🧮 Perform the calculation using a **function**.
6. 💬 Show the result.
7. 🔁 Ask if they want to **continue or exit**.

This repeats until the user types `"exit"` or `"stop"`.

---

## 💥 Example Run

```bash
Welcome to the Simple Calculator! 📱
Type "exit" anytime to quit.

Enter first number: 10
Enter operation (+, -, *, /): *
Enter second number: 5
Result: 50

Would you like to calculate again? (yes/exit): yes

Enter first number: 100
Enter operation (+, -, *, /): /
Enter second number: 0
Error: Division by zero is not allowed.

Would you like to calculate again? (yes/exit): exit

Thanks for using the calculator! 👋
```