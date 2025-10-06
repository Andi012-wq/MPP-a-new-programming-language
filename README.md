# ⚙️ M++ Programming Language

Welcome to **M++**, a lightweight, stack-based, and colorful interpreted programming language built with Python.  
M++ mixes the minimalism of assembly, the logic of stack-based languages, and the creativity of modern scripting — all in one fast, easy-to-learn package.

---

## 🧠 What Is M++?

M++ is a **custom-built interpreted language** that runs through a Python interpreter (`mpp_interpreter.py`).  
It features **manual memory control**, **typed variables**, **stack operations**, **loops**, **labels**, and **terminal colors**, letting you build anything from small games to logic-based programs.

Think of it as your **own assembly-like playground** — simple, powerful, and fully customizable.

---

## 🚀 Features

- 🧮 **Stack-based execution model** (push, pop, arithmetic)
- 💾 **Memory system** with 1,000,000 cells
- 💡 **Typed variables**:
  - `NU` — number  
  - `FL` — float  
  - `ST` — string  
  - `BO` — boolean  
- 🔁 **Flow control** with labels, loops, and conditional jumps
- 🎨 **Color output** in the terminal (`COLOR RED`, etc.)
- 🎲 **Random number generation** with `~`
- 📥 **User input** via `INPUT`
- ⚙️ **Functions**, **reversible stacks**, and **memory randomization**
- 🧩 **Cross-platform** — runs on any system with Python 3+

---

## 🧰 Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/yourusername/mpp-language.git
   cd mpp-language
   ```

2. **Run any M++ file**:
   ```bash
   python mpp_interpreter.py program.m++
   ```

3. Make sure your `.m++` file is in the same directory as the interpreter.

---

## 📜 Syntax Overview

| Command | Description |
|----------|-------------|
| `# text` | Print text (supports `$variable` substitution) |
| `COLOR RED` | Change text color |
| `P value` | Push value to stack |
| `O` | Pop and print top of stack |
| `+ - * / %` | Arithmetic operations |
| `>` `<` `=` | Comparison operators |
| `~ limit` | Push random number between 0 and limit |
| `MSET addr val` | Set memory cell |
| `MGET addr` | Push memory value |
| `[` `]` | Create loop |
| `? label` | Jump to label if popped value = 0 |
| `CJ label` | Jump to label if popped value ≠ 0 |
| `{` `}` | Function start/end |
| `RM` | Randomize first 16 memory cells |
| `RS` | Reverse stack |
| `DU` | Duplicate top of stack |
| `@` | Swap top two stack elements |
| `!!` | Print stack as text (ASCII) |
| `XY` | Push sum of memory[0] and memory[1] |
| `INPUT name` | Ask user for input and store in variable |
| `NU name val` | Number variable |
| `FL name val` | Float variable |
| `ST name "text"` | String variable |
| `BO name true/false` | Boolean variable |
| `Q` | Quit program |

---

## 🧩 Examples

### 🖨️ Hello World
```m++
# Hello, World!
Q
```

### 🔢 Using Variables and Math
```m++
NU X 10
NU Y 5
P $X
P $Y
+
# Result:
O
Q
```

### 🔁 Loop Example
```m++
NU i 0
start:
P $i
# i =
O
P $i
P 1
+
NU i $i
P $i
P 5
<
CJ start
Q
```

### 🎨 Colors and Input
```m++
COLOR CYAN
# Welcome to M++
COLOR RESET
INPUT name
# Hello, $name!
Q
```

### 🎲 Random Numbers
```m++
# Random number (0–100):
~ 100
O
Q
```

---

## 💡 Challenges

Try these to level up your M++ skills:

1. 🔁 Print numbers from 1 to 20 using loops  
2. ➗ Create a basic calculator with stack operations  
3. 🧠 Ask the user for their name and print it in multiple colors  
4. 🎲 Generate 10 random numbers and calculate their sum  
5. 🪙 Build a coin flip game using `~ 2` and booleans  

---

## 🧱 Example Folder Structure

```
📂 mpp-language
 ┣ 📜 mpp_interpreter.py
 ┣ 📄 hello.m++
 ┣ 📄 calculator.m++
 ┣ 📄 loop.m++
 ┣ 📰Import_this_in_notepad++_for highlights.xml
 ┗ 📘 README.md
```

---

## ⚖️ License

**MIT License**
You’re free to use, modify, and distribute M++ — just keep the credit to the original author.
And send me your modification on email: andihoti012@gmail.com
---

## 👨‍💻 Author

Developed by **Andi Hoti**
💬 “A minimal language for maximal creativity.”

⭐ If you like M++, give it a star on GitHub and share your own `.m++` projects!
