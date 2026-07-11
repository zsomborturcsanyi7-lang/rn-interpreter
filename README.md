# RN — Rekurzív Nyelv (Lisp-szerű Interpretált Programozási Nyelv)

**Egy tömör, rekurzív, Lisp-szerű programozási nyelv Pythonban implementálva. Mindössze 5 szabály, ~150 sor.**

## 💻 Leírás

Az RN (Rekurzív Nyelv) egy minimalista, Lisp-szerű értelmező, amely:

- **5 alapszabály** — rendkívül egyszerű, mégis Turing-teljes
- **~150 soros** Python implementáció
- **Rekurzív kiértékelés** — S-kifejezések és lambdák
- **Lexikális scope** — változók és függvények izolációja
- **Beépített aritmetika** — `+`, `-`, `*`, `/`, `%`
- **Adatszerkezetek** — listák, számok, stringek, szimbólumok
- **Feltételes kifejezés** — `if`
- **Függvény definíció** — `lambda` / `fn`

### Példa kód

```lisp
; Függvény definíció
(fn factorial [n]
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

; Használat
(factorial 5)
; → 120
```

## 📁 Fájlszerkezet

```
rn/
├── rn.py                        # Interpreter (201 sor)
├── test_token.py                # Tokenizer teszt
├── pelda.rn                     # Példa programok
├── pelda_simple.rn              # Egyszerű példák
├── pelda2.rn                    # További példák
├── pelda3.rn                    # Még több példa
└── README.md
```

## 🚀 Használat

### Interpreter indítása fájllal

```bash
python rn.py pelda.rn
```

### Interaktív REPL

```bash
python rn.py
```

### Példaprogramok futtatása

```bash
# Alap példák
python rn.py pelda.rn

# Egyszerű példák
python rn.py pelda_simple.rn

# Haladó példák
python rn.py pelda2.rn
python rn.py pelda3.rn
```

### Tokenizer teszt

```bash
python test_token.py
```

## 📦 Függőségek

- **Python 3.8+** (standard library only)
- Csak `sys`, `math`, `operator`, `functools` — mind beépített

## 🔤 Nyelvi szabályok

### Az 5 alapszabály

| # | Szabály | Leírás |
|---|--------|--------|
| 1 | **Szám** | `42` → önmaga |
| 2 | **String** | `"hello"` → önmaga |
| 3 | **Szimbólum** | `x` → környezetből érték keresése |
| 4 | **Lista** | `(fn x ...)` → speciális forma |
| 5 | **Függvényhívás** | `(f a b)` → `f(a, b)` alkalmazása |

### Beépített függvények

| Függvény | Leírás |
|----------|--------|
| `+`, `-`, `*`, `/`, `%` | Aritmetikai műveletek |
| `<`, `>`, `<=`, `>=`, `=` | Összehasonlítások |
| `if` | Feltételes elágazás |
| `fn` | Lambda / függvény definíció |
| `list` | Lista konstruktor |
| `car`, `cdr` | Lista fej / farok |
| `cons` | Elem lista elejére |
| `print` | Kiíratás |

### Példa: Fibonacci

```lisp
(fn fib [n]
  (if (<= n 1)
      n
      (+ (fib (- n 1)) (fib (- n 2)))))

(print (fib 10))
; → 55
```

### Példa: Map függvény

```lisp
(fn map [f lst]
  (if (= lst [])
      []
      (cons (f (car lst)) (map f (cdr lst)))))

(map (fn [x] (* x 2)) [1 2 3 4 5])
; → [2 4 6 8 10]
```

## 🔧 Architektúra

```
rn.py
├── Tokenizer
│   ├── Karakterenkénti tokenizálás
│   ├── Szám, string, szimbólum felismerés
│   └── Zárójel kezelés: () és []
├── Parser
│   └── Tokenek → AST (beágyazott listák)
├── Evaluator
│   ├── Környezet (lexikális scope)
│   ├── Speciális formák (fn, if, ...)
│   ├── Beépített függvények
│   └── Rekurzív kiértékelés
└── REPL / Fájl futtató
```

## 🎯 Célok

- **Oktatási eszköz** — programozási nyelvek alapjainak megértése
- **Minimális interpreter** — a lehető legkevesebb kód
- **Turing-teljes** — elvileg bármilyen számítás elvégezhető
- **Kísérleti platform** — új nyelvi funkciók gyors prototipizálása
