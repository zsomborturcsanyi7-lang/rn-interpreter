# RN — Recursive Language (Lisp-like Interpreted Programming Language)

**A concise, recursive, Lisp-like programming language implemented in Python. Only 5 rules, ~150 lines.**

## 💻 Description

RN (Recursive Language) is a minimalist, Lisp-like interpreter that features:

- **5 core rules** — extremely simple, yet Turing-complete
- **~150-line** Python implementation
- **Recursive evaluation** — S-expressions and lambdas
- **Lexical scope** — variable and function isolation
- **Built-in arithmetic** — `+`, `-`, `*`, `/`, `%`
- **Data structures** — lists, numbers, strings, symbols
- **Conditional expressions** — `if`
- **Function definition** — `lambda` / `fn`

### Example Code

```lisp
; Function definition
(fn factorial [n]
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

; Usage
(factorial 5)
; → 120
```

## 📁 File Structure

```
rn/
├── rn.py                        # Interpreter (201 lines)
├── test_token.py                # Tokenizer test
├── pelda.rn                     # Example programs
├── pelda_simple.rn              # Simple examples
├── pelda2.rn                    # Additional examples
├── pelda3.rn                    # More examples
└── README.md
```

## 🚀 Usage

### Running the interpreter with a file

```bash
python rn.py pelda.rn
```

### Interactive REPL

```bash
python rn.py
```

### Running example programs

```bash
# Basic examples
python rn.py pelda.rn

# Simple examples
python rn.py pelda_simple.rn

# Advanced examples
python rn.py pelda2.rn
python rn.py pelda3.rn
```

### Tokenizer test

```bash
python test_token.py
```

## 📦 Dependencies

- **Python 3.8+** (standard library only)
- Only `sys`, `math`, `operator`, `functools` — all built-in

## 🔤 Language Rules

### The 5 Core Rules

| # | Rule | Description |
|---|------|-------------|
| 1 | **Number** | `42` → evaluates to itself |
| 2 | **String** | `"hello"` → evaluates to itself |
| 3 | **Symbol** | `x` → look up value in environment |
| 4 | **List** | `(fn x ...)` → special form |
| 5 | **Function call** | `(f a b)` → apply `f(a, b)` |

### Built-in Functions

| Function | Description |
|----------|-------------|
| `+`, `-`, `*`, `/`, `%` | Arithmetic operations |
| `<`, `>`, `<=`, `>=`, `=` | Comparisons |
| `if` | Conditional branching |
| `fn` | Lambda / function definition |
| `list` | List constructor |
| `car`, `cdr` | List head / tail |
| `cons` | Prepend element to list |
| `print` | Output |

### Example: Fibonacci

```lisp
(fn fib [n]
  (if (<= n 1)
      n
      (+ (fib (- n 1)) (fib (- n 2)))))

(print (fib 10))
; → 55
```

### Example: Map function

```lisp
(fn map [f lst]
  (if (= lst [])
      []
      (cons (f (car lst)) (map f (cdr lst)))))

(map (fn [x] (* x 2)) [1 2 3 4 5])
; → [2 4 6 8 10]
```

## 🔧 Architecture

```
rn.py
├── Tokenizer
│   ├── Character-by-character tokenization
│   ├── Number, string, symbol recognition
│   └── Parenthesis handling: () and []
├── Parser
│   └── Tokens → AST (nested lists)
├── Evaluator
│   ├── Environment (lexical scope)
│   ├── Special forms (fn, if, ...)
│   ├── Built-in functions
│   └── Recursive evaluation
└── REPL / File runner
```

## 🎯 Goals

- **Educational tool** — understanding programming language fundamentals
- **Minimal interpreter** — the fewest lines of code possible
- **Turing-complete** — capable of any computation in principle
- **Experimental platform** — rapid prototyping of new language features

## Author
Zsombi & Hermes Agent (Nous Research)
