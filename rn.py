#!/usr/bin/env python3
"""
RN - Rekurzív Nyelv
Egy tömör, rekurzív programozási nyelv. 5 szabály, ~150 sor.
"""

import sys, math, operator as op, functools

# ============================================================
# TOKENIZER
# ============================================================

def tokenize(code):
    """Karakterenként tokenizál. Szám, szimbólum, string, lista-jelek."""
    tokens = []
    i = 0
    while i < len(code):
        c = code[i]
        if c == '(':
            tokens.append(('list', '('))
            i += 1
        elif c == ')':
            tokens.append(('close', ''))
            i += 1
        elif c == '[':
            tokens.append(('data', '['))
            i += 1
        elif c == ']':
            tokens.append(('close', ''))
            i += 1
        elif c in ' \t\n\r': 
            i += 1
        elif c == ';':  # komment
            while i < len(code) and code[i] != '\n': i += 1
        elif c == '"':  # string
            i += 1
            s = ''
            while i < len(code) and code[i] != '"':
                s += code[i]; i += 1
            tokens.append(('str', s))
            i += 1  # záró "
        else:
            # szimbólum vagy szám
            s = ''
            while i < len(code) and code[i] not in '()[] \t\n\r;':
                s += code[i]; i += 1
            tokens.append(('atom', s))
    return tokens

def parse(tokens):
    """Tokenek → AST. Rekurzív descent parser."""
    if not tokens: return None
    t = tokens.pop(0)
    typ, val = t
    
    if typ in ('list', 'data'):
        items = []
        while tokens and tokens[0][0] != 'close':
            items.append(parse(tokens))
        if tokens: tokens.pop(0)  # consume close token
        if typ == 'data':
            return DataList(items)
        return items  # kódlista: függvényhívás lesz belőle
    elif typ == 'str':
        return val
    elif typ == 'atom':
        try: return int(val)
        except ValueError:
            try: return float(val)
            except ValueError: return Symbol(val)
    return None

class Symbol(str): pass
class DataList(list): pass

# ============================================================
# KÖRNYEZET
# ============================================================

class Env(dict):
    def __init__(self, outer=None, bindings=None):
        super().__init__()
        self.outer = outer
        if bindings: self.update(bindings)
    def find(self, key):
        if key in self: return self[key]
        if self.outer: return self.outer.find(key)
        raise NameError(f"Nincs ilyen: {key}")

def default_env():
    env = Env()
    for name, fn in [('+', lambda *a: functools.reduce(op.add, a)),
                     ('-', lambda *a: functools.reduce(op.sub, a)),
                     ('*', lambda *a: functools.reduce(op.mul, a)),
                     ('/', lambda *a: functools.reduce(op.truediv, a)),
                     ('=', op.eq), ('<', op.lt), ('>', op.gt),
                     ('<=', op.le), ('>=', op.ge), ('%', op.mod)]:
        env[name] = fn
    env['print'] = lambda *a: print(*[pprint(x) for x in a], flush=True) or (a[-1] if a else None)
    env['range'] = lambda *a: list(range(*a))
    env['len'] = len
    env['first'] = lambda lst: lst[0]
    env['rest'] = lambda lst: lst[1:]
    env['get'] = lambda lst, i: lst[i]
    env['map'] = lambda f, lst: [f(x) for x in lst]
    env['filter'] = lambda f, lst: [x for x in lst if f(x)]
    env['reduce'] = lambda f, lst, init: functools.reduce(f, lst, init)
    env['pipe'] = lambda val, *fns: functools.reduce(lambda v, fn: fn(v), fns, val)
    env['pi'] = math.pi
    env['True'] = True; env['False'] = False
    return env

# ============================================================
# INTERPRETER
# ============================================================

def evaluate(expr, env):
    if isinstance(expr, (int, float)): return expr
    if isinstance(expr, Symbol): return env.find(expr)
    if isinstance(expr, str): return expr
    if isinstance(expr, DataList): return list(expr)  # adatlista: kiértékelés nélkül
    
    if isinstance(expr, list):
        if not expr: return expr
        head = expr[0]
        
        if head == 'if':
            _, cond, then_, else_ = expr
            return evaluate(then_, env) if evaluate(cond, env) else evaluate(else_, env)
        elif head == 'fn':
            _, params, body = expr
            return lambda *args: evaluate(body, Env(outer=env, bindings=dict(zip(params, args))))
        elif head == 'defn':
            _, name, params, body = expr
            fn = lambda *args: evaluate(body, Env(outer=env, bindings=dict(zip(params, args))))
            env[name] = fn
            return fn
        elif head == 'do':
            result = None
            for e in expr[1:]:
                result = evaluate(e, env)
            return result
        elif head == 'let':
            _, bindings, body = expr
            new_env = Env(outer=env)
            for k, v in zip(bindings[0::2], bindings[1::2]):
                new_env[k] = evaluate(v, env)
            return evaluate(body, new_env)
        else:
            fn = evaluate(head, env)
            args = [evaluate(e, env) for e in expr[1:]]
            if callable(fn):
                return fn(*args)
            raise TypeError(f"Nem hívható: {head}")
    return expr

def pprint(val):
    if isinstance(val, list):
        return '[' + ' '.join(pprint(v) for v in val) + ']'
    if isinstance(val, DataList):
        return '[' + ' '.join(pprint(v) for v in val) + ']'
    if isinstance(val, Symbol): return str(val)
    if val is True: return 'True'
    if val is False: return 'False'
    if val is None: return '()'
    return str(val)

# ============================================================
# REPL / RUNNER
# ============================================================

def run(code, env=None):
    if env is None: env = default_env()
    tokens = tokenize(code)
    result = None
    while tokens:
        ast = parse(tokens)
        if ast is not None:
            result = evaluate(ast, env)
    return result

def repl():
    env = default_env()
    print("RN - Rekurzív Nyelv.  (exit) = kilépés")
    while True:
        try:
            code = input('rn> ')
            if code.strip() in ('(exit)', 'exit', 'q'): break
            if code.strip():
                result = run(code, env)
                if result is not None:
                    print(pprint(result))
        except Exception as e:
            print(f"  Hiba: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            run(f.read())
    else:
        repl()
