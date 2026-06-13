#!/usr/bin/env python3
"""Tłumaczenie literałów i komentarzy — poprawiona wersja ze ścisłymi wzorcami."""

PO_FILE = 'po/pl.po'

with open(PO_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

total = 0

def apply(old, new, label=''):
    global text, total
    n = text.count(old)
    if n == 0:
        print(f'NIE ZNALEZIONO: {label}')
        return
    text = text.replace(old, new)
    total += n

# ===== LITERAŁY RUST — KOPJOWANE VERBATIM =====
# Format: msgid "\"{content}\"" → msgstr "\"{content}\""
# W Pythonie: 'msgid "\\"{content}\\""' → 'msgid "\\"{content}\\""\nmsgstr "\\"{content}\\""'

def lit(content, translation=None):
    """String literal — domyślnie kopiuj verbatim."""
    if translation is None:
        translation = content
    old = f'msgid "\\"{content}\\""\nmsgstr ""'
    new = f'msgid "\\"{content}\\""\nmsgstr "\\"{translation}\\""'
    apply(old, new, content[:40])

# print.md literals
lit('{} days')
lit('{0}, this is {1}. {1}, this is {0}')
lit('Alice')
lit('Bob')
lit('{subject} {verb} {object}')
lit('the lazy dog')
lit('the quick brown fox')
lit('jumps over')
lit('Base 10:               {}')
lit('Base 2 (binary):       {:b}')
lit('Base 8 (octal):        {:o}')
lit('Base 16 (hexadecimal): {:x}')
lit('{number:>5}')
lit('{number:0>5}')
lit('{number:0<5}')
lit('{number:0>width$}')
lit('{number:>width$}')
lit('My name is {0}, {1} {0}')
lit('Bond')

# print_debug.md literals
lit('{:?} months in a year.')
lit('{1:?} {0:?} is the {actor:?} name.')
lit('Slater')
lit('Christian')
lit("actor\\'s")
lit('Now {:?} will print!')
lit('Peter')
lit('{:#?}')

# print_display.md literals
lit('{}')
lit('({}, {})')
lit('x: {}, y: {}')
lit('Compare structures:')
lit('Display: {}')
lit('Debug: {:?}')
lit('The big range is {big} and the small is {small}')
lit('Compare points:')

# testcase_list.md literals
lit('[')
lit(', ')
lit(']')

# fmt.md literals
lit('{}: {:.3}\xb0{} {:.3}\xb0{}')  # degree sign °
lit('Dublin')
lit('Oslo')
lit('Vancouver')
lit('{:?}')

# literals.md literals
lit('1 + 2 = {}')
lit('1 - 2 = {}')
lit('1e4 is {}, -2.5e-3 is {}')
lit('true AND false is {}')
lit('true OR false is {}')
lit('NOT true is {}')
lit('0011 AND 0101 is {:04b}')
lit('0011 OR 0101 is {:04b}')
lit('0011 XOR 0101 is {:04b}')
lit('1 << 5 is {}')
lit('0x80 >> 2 is 0x{:x}')
lit('One million is written as {}')

# tuples.md literals
lit('Long tuple first value: {}')
lit('Long tuple second value: {}')
lit('tuple of tuples: {:?}')
lit('Pair is {:?}')
lit('The reversed pair is {:?}')
lit('One element tuple: {:?}')
lit('Just an integer: {:?}')
lit('hello')
lit('{:?}, {:?}, {:?}, {:?}')
lit('Matrix:\\\\n{}')   # file has \\n (literal backslash-n)
lit('Transpose:\\\\n{}')

# array.md literals
lit('First element of the slice: {}')
lit('The slice has {} elements')
lit('First element of the array: {}')
lit('Second element of the array: {}')
lit('Number of elements in array: {}')
lit('Array occupies {} bytes')
lit('Borrow the whole array as a slice.')
lit('Borrow a section of the array as a slice.')
lit('{}: {}')
lit('Slow down! {} is too far!')

# ===== KOMENTARZE WIELOLINIOWE =====

# fmt.md:28 — f is a buffer
old = ('msgid ""\n'
       '"// `f` is a buffer, and this method must write the formatted string into "\n'
       '"it.\\n"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"// `f` is a buffer, and this method must write the formatted string into "\n'
       '"it.\\n"\n'
       'msgstr ""\n'
       '"// `f` to bufor, a ta metoda musi zapisać do niego sformatowany napis.\\n"')
apply(old, new, 'f is a buffer')

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
