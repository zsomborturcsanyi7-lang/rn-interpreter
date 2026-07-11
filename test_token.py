"""RN tokenizer test."""
code = '(print "hello")'
print("Code length:", len(code))
i = 0
while i < len(code):
    c = code[i]
    if c == '(':
        print(f"  [{i}] OPEN (")
        i += 1
    elif c == ')':
        print(f"  [{i}] CLOSE )")
        i += 1
    elif c == '"':
        i += 1
        s = ""
        while i < len(code) and code[i] != '"':
            s += code[i]
            i += 1
        print(f"  [{i}] STR {repr(s)}")
        i += 1
    elif c in ' \t\n':
        i += 1
    else:
        s = ""
        while i < len(code) and code[i] not in '() \t\n':
            s += code[i]
            i += 1
        print(f"  [{i}] ATOM {s}")
print("Done, i =", i)
