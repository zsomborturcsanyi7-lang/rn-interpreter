# rn-interpreter

Minimalist recursive Lisp-like interpreter written in Python.

## Overview & Purpose
rn-interpreter is a lightweight, educational programming language interpreter that parses and evaluates S-expression syntax using recursive tree evaluation.

## Key Features
- S-expression parsing and tokenization.
- Recursive environment lookup and variable binding.
- Arithmetic and logical evaluation primitives.

## Tech Stack & Dependencies
- **Language**: Python 3.8+

## Project Structure
```text
rn-interpreter/
├── interpreter.py
├── test_eval.py
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8+

### Steps
```bash
git clone https://github.com/zsomborturcsanyi7-lang/rn-interpreter.git
cd rn-interpreter
python interpreter.py
```

## Usage Examples
```bash
python interpreter.py --code "(+ 5 (* 2 10))"
```

## Status & License
Status: Educational Prototype.
License: MIT
