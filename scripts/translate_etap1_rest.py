#!/usr/bin/env python3
"""Tłumaczenie brakujących wpisów Etapu 1 w po/pl.po.
Strategia: dokładne zastępowanie bloków msgid+msgstr.
Literały kopiowane verbatim, komentarze tłumaczone.
"""

PO_FILE = 'po/pl.po'

def replace(text, old, new, label=''):
    count = text.count(old)
    if count == 0:
        print(f'NIE ZNALEZIONO: {label!r}')
        return text, 0
    if count > 1:
        print(f'WIELOKROTNE ({count}): {label!r}')
    result = text.replace(old, new)
    return result, count


def make_single(msgid_inner, msgstr_inner):
    """Tworzy parę (old, new) dla jednolinijkowego wpisu."""
    old = f'msgid "{msgid_inner}"\nmsgstr ""'
    new = f'msgid "{msgid_inner}"\nmsgstr "{msgstr_inner}"'
    return old, new


def make_multi_msgid(msgid_lines, msgstr_lines, label=''):
    """Tworzy parę (old, new) dla wieloliniowego msgid."""
    msgid_body = '\n'.join(msgid_lines)
    old = f'{msgid_body}\nmsgstr ""'
    msgstr_body = '\n'.join(msgstr_lines)
    new = f'{msgid_body}\nmsgstr ""\n{msgstr_body}'
    return old, new


with open(PO_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

total = 0

# ========== LITERAŁY SKOPIOWANE VERBATIM ==========
# (Rule 6: string literals in code examples — copy as-is)

literals = [
    # print.md string literals
    ('"{} days"', '"{} days"'),
    ('"{0}, this is {1}. {1}, this is {0}"', '"{0}, this is {1}. {1}, this is {0}"'),
    ('"Alice"', '"Alice"'),
    ('"Bob"', '"Bob"'),
    ('"{subject} {verb} {object}"', '"{subject} {verb} {object}"'),
    ('"the lazy dog"', '"the lazy dog"'),
    ('"the quick brown fox"', '"the quick brown fox"'),
    ('"jumps over"', '"jumps over"'),
    ('"Base 10:               {}"', '"Base 10:               {}"'),
    ('"Base 2 (binary):       {:b}"', '"Base 2 (binary):       {:b}"'),
    ('"Base 8 (octal):        {:o}"', '"Base 8 (octal):        {:o}"'),
    ('"Base 16 (hexadecimal): {:x}"', '"Base 16 (hexadecimal): {:x}"'),
    ('"{number:>5}"', '"{number:>5}"'),
    ('"{number:0>5}"', '"{number:0>5}"'),
    ('"{number:0<5}"', '"{number:0<5}"'),
    ('"{number:0>width$}"', '"{number:0>width$}"'),
    ('"{number:>width$}"', '"{number:>width$}"'),
    ('"My name is {0}, {1} {0}"', '"My name is {0}, {1} {0}"'),
    ('"Bond"', '"Bond"'),
    # print_debug.md string literals
    ('"{:?} months in a year."', '"{:?} months in a year."'),
    ('"{1:?} {0:?} is the {actor:?} name."', '"{1:?} {0:?} is the {actor:?} name."'),
    ('"Slater"', '"Slater"'),
    ('"Christian"', '"Christian"'),
    ('"actor\'s"', '"actor\'s"'),
    ('"Now {:?} will print!"', '"Now {:?} will print!"'),
    ('"Peter"', '"Peter"'),
    ('"{:#?}"', '"{:#?}"'),
    # print_display.md string literals
    ('"{}"', '"{}"'),
    ('"({}, {})"', '"({}, {})"'),
    ('"x: {}, y: {}"', '"x: {}, y: {}"'),
    ('"Compare structures:"', '"Compare structures:"'),
    ('"Display: {}"', '"Display: {}"'),
    ('"Debug: {:?}"', '"Debug: {:?}"'),
    ('"The big range is {big} and the small is {small}"', '"The big range is {big} and the small is {small}"'),
    ('"Compare points:"', '"Compare points:"'),
    # testcase_list.md string literals
    ('"["', '"["'),
    ('", "', '", "'),
    ('"]"', '"]"'),
    # fmt.md string literals
    ('"{}: {:.3}\xb0{} {:.3}\xb0{}"', '"{}: {:.3}\xb0{} {:.3}\xb0{}"'),
    ('"Dublin"', '"Dublin"'),
    ('"Oslo"', '"Oslo"'),
    ('"Vancouver"', '"Vancouver"'),
    ('"{:?}"', '"{:?}"'),
    # fmt.md char literals
    ("'N'", "'N'"),
    ("'S'", "'S'"),
    ("'E'", "'E'"),
    ("'W'", "'W'"),
    # literals.md string literals
    ('"1 + 2 = {}"', '"1 + 2 = {}"'),
    ('"1 - 2 = {}"', '"1 - 2 = {}"'),
    ('"1e4 is {}, -2.5e-3 is {}"', '"1e4 is {}, -2.5e-3 is {}"'),
    ('"true AND false is {}"', '"true AND false is {}"'),
    ('"true OR false is {}"', '"true OR false is {}"'),
    ('"NOT true is {}"', '"NOT true is {}"'),
    ('"0011 AND 0101 is {:04b}"', '"0011 AND 0101 is {:04b}"'),
    ('"0011 OR 0101 is {:04b}"', '"0011 OR 0101 is {:04b}"'),
    ('"0011 XOR 0101 is {:04b}"', '"0011 XOR 0101 is {:04b}"'),
    ('"1 << 5 is {}"', '"1 << 5 is {}"'),
    ('"0x80 >> 2 is 0x{:x}"', '"0x80 >> 2 is 0x{:x}"'),
    ('"One million is written as {}"', '"One million is written as {}"'),
    # tuples.md string literals
    ("'a'", "'a'"),
    ('"Long tuple first value: {}"', '"Long tuple first value: {}"'),
    ('"Long tuple second value: {}"', '"Long tuple second value: {}"'),
    ('"tuple of tuples: {:?}"', '"tuple of tuples: {:?}"'),
    ('"Pair is {:?}"', '"Pair is {:?}"'),
    ('"The reversed pair is {:?}"', '"The reversed pair is {:?}"'),
    ('"One element tuple: {:?}"', '"One element tuple: {:?}"'),
    ('"Just an integer: {:?}"', '"Just an integer: {:?}"'),
    ('"hello"', '"hello"'),
    ('"{:?}, {:?}, {:?}, {:?}"', '"{:?}, {:?}, {:?}, {:?}"'),
    ('"Matrix:\\n{}"', '"Matrix:\\n{}"'),
    ('"Transpose:\\n{}"', '"Transpose:\\n{}"'),
    # array.md string literals
    ('"First element of the slice: {}"', '"First element of the slice: {}"'),
    ('"The slice has {} elements"', '"The slice has {} elements"'),
    ('"First element of the array: {}"', '"First element of the array: {}"'),
    ('"Second element of the array: {}"', '"Second element of the array: {}"'),
    ('"Number of elements in array: {}"', '"Number of elements in array: {}"'),
    ('"Array occupies {} bytes"', '"Array occupies {} bytes"'),
    ('"Borrow the whole array as a slice."', '"Borrow the whole array as a slice."'),
    ('"Borrow a section of the array as a slice."', '"Borrow a section of the array as a slice."'),
    ('"{}: {}"', '"{}: {}"'),
    ('"Slow down! {} is too far!"', '"Slow down! {} is too far!"'),
]

for msgid_inner, msgstr_inner in literals:
    old, new = make_single(msgid_inner, msgstr_inner)
    text, n = replace(text, old, new, msgid_inner[:40])
    total += n

# ========== KOMENTARZE NUMERYCZNE — COPY VERBATIM ==========
# (To są wartości wyjściowe, nie tekst do tłumaczenia)
numeric_comments = [
    ('// 69420\\n', '// 69420\\n'),
    ('// 10000111100101100\\n', '// 10000111100101100\\n'),
    ('// 207454\\n', '// 207454\\n'),
    ('// 10f2c\\n', '// 10f2c\\n'),
    ('// 10000\\n', '// 10000\\n'),
]

for msgid_inner, msgstr_inner in numeric_comments:
    old, new = make_single(msgid_inner, msgstr_inner)
    text, n = replace(text, old, new, msgid_inner[:40])
    total += n

# ========== KOMENTARZE DO TŁUMACZENIA — JEDNOLINIJKOWE ==========

single_comments = [
    # print.md
    ('// As can named arguments.\\n',
     '// Podobnie można używać nazwanych argumentów.\\n'),
    ('// You can pad numbers with extra zeroes,\\n',
     '// Możesz dopełnić liczby dodatkowymi zerami,\\n'),
    ('// disable `dead_code` which warn against unused module\\n',
     '// wyłącz `dead_code`, który ostrzeża przed nieużywanym modułem\\n'),
    # print_debug.md
    ('// Printing with `{:?}` is similar to with `{}`.\\n',
     '// Drukowanie z `{:?}` jest podobne do `{}`.\\n'),
    ('// `Structure` is printable!\\n',
     '// `Structure` można teraz drukować!\\n'),
    ('// Pretty print\\n',
     '// Ładne drukowanie\\n'),
    # print_display.md
    ('// Import (via `use`) the `fmt` module to make it available.\\n',
     '// Importuj (przez `use`) moduł `fmt`, aby był dostępny.\\n'),
    ('// This trait requires `fmt` with this exact signature.\\n',
     '// Ta cecha wymaga `fmt` z dokładnie taką sygnaturą.\\n'),
    ('// Import `fmt`\\n',
     '// Importuj `fmt`\\n'),
    ('// Implement `Display` for `MinMax`.\\n',
     '// Zaimplementuj `Display` dla `MinMax`.\\n'),
    ('// Use `self.number` to refer to each positional data point.\\n',
     '// Użyj `self.number`, aby odwołać się do każdego punktu danych.\\n'),
    ('// Define a structure where the fields are nameable for comparison.\\n',
     '// Zdefiniuj strukturę, gdzie pola mają nazwy dla porównania.\\n'),
    ('// Similarly, implement `Display` for `Point2D`.\\n',
     '// Analogicznie zaimplementuj `Display` dla `Point2D`.\\n'),
    ('// Customize so only `x` and `y` are denoted.\\n',
     '// Dostosuj tak, aby wyświetlać tylko `x` i `y`.\\n'),
    # testcase_list.md
    ('// Import the `fmt` module.\\n',
     '// Importuj moduł `fmt`.\\n'),
    ('// Define a structure named `List` containing a `Vec`.\\n',
     '// Zdefiniuj strukturę o nazwie `List` zawierającą `Vec`.\\n'),
    ('// Create a reference to the Vec<i32> stored in the List struct.\\n',
     '// Utwórz referencję do Vec<i32> przechowywanego w strukturze List.\\n'),
    ('// Close the opened bracket and return a fmt::Result value.\\n',
     '// Zamknij otwartą klamerę i zwróć wartość fmt::Result.\\n'),
    # fmt.md
    ('// `f` is a buffer, and this method must write the formatted string into it.\\n',
     '// `f` to bufor, a ta metoda musi zapisać do niego sformatowany napis.\\n'),
    # tuples.md
    ('// Tuples can be used as function arguments and as return values.\\n',
     '// Krotki mogą być używane jako argumenty funkcji i wartości zwracane.\\n'),
    ('// `let` can be used to bind the members of a tuple to variables.\\n',
     '// `let` może wiązać elementy krotki ze zmiennymi.\\n'),
    ('// The following struct is for the activity.\\n',
     '// Poniższa struktura służy do ćwiczenia.\\n'),
    ('// A tuple with a bunch of different types.\\n',
     '// Krotka zawierająca różne typy.\\n'),
    ('// Values can be extracted from the tuple using tuple indexing.\\n',
     '// Wartości można wyodrębnić z krotki za pomocą indeksowania.\\n'),
    ('// Tuples can be tuple members.\\n',
     '// Krotki mogą być elementami krotek.\\n'),
    ('// Tuples are printable.\\n',
     '// Krotki można drukować.\\n'),
    ('// Tuples can be destructured to create bindings.\\n',
     '// Krotki można destrukturyzować, tworząc wiązania.\\n'),
    # array.md
    ('// This function borrows a slice.\\n',
     '// Ta funkcja pożycza wycinek.\\n'),
    ('// Fixed-size array (type signature is superfluous).\\n',
     '// Tablica o stałym rozmiarze (adnotacja typu jest zbędna).\\n'),
    ('// All elements can be initialized to the same value.\\n',
     '// Wszystkie elementy można zainicjalizować tą samą wartością.\\n'),
    ('// Indexing starts at 0.\\n',
     '// Indeksowanie zaczyna się od 0.\\n'),
    ('// `len` returns the count of elements in the array.\\n',
     '// `len` zwraca liczbę elementów tablicy.\\n'),
    ('// Arrays are stack allocated.\\n',
     '// Tablice są alokowane na stosie.\\n'),
    ('// Arrays can be automatically borrowed as slices.\\n',
     '// Tablice mogą być automatycznie pożyczane jako wycinki.\\n'),
    ('// Example of empty slice `&[]`:\\n',
     '// Przykład pustego wycinka `&[]`:\\n'),
    ('// Same but more verbose\\n',
     '// To samo, ale bardziej rozbudowane\\n'),
    ('// Oops, one element too far!\\n',
     '// Ups, jeden element za daleko!\\n'),
]

for msgid_inner, msgstr_inner in single_comments:
    old, new = make_single(msgid_inner, msgstr_inner)
    text, n = replace(text, old, new, msgid_inner[:40])
    total += n

# ========== KOMENTARZE DO TŁUMACZENIA — WIELOLINIOWE ==========

# print.md:23 — Positional arguments
old, new = make_multi_msgid(
    ['msgid ""',
     '"// Positional arguments can be used. Specifying an integer inside `{}`\\n"',
     '"    // determines which additional argument will be replaced. Arguments "',
     '"start\\n"',
     '"    // at 0 immediately after the format string.\\n"'],
    ['"// Można używać argumentów pozycyjnych. Podanie liczby całkowitej wewnątrz `{}`\\n"',
     '"    // określa, który dodatkowy argument zostanie zastąpiony. Argumenty\\n"',
     '"    // numerowane są od 0, zaraz po ciągu formatującym.\\n"'],
    'Positional arguments'
)
text, n = replace(text, old, new, 'Positional arguments')
total += n

# print.md:41 — right-justify
old, new = make_multi_msgid(
    ['msgid ""',
     '"// You can right-justify text with a specified width. This will\\n"',
     '"    // output \\"    1\\". (Four white spaces and a \\"1\\", for a total width "',
     '"of 5.)\\n"'],
    ['"// Tekst można wyrównać do prawej, podając szerokość. To wydrukuje\\n"',
     '"    // \\"    1\\". (Cztery spacje i cyfra \\"1\\", łączna szerokość 5.)\\n"'],
    'right-justify'
)
text, n = replace(text, old, new, 'right-justify')
total += n

# print.md:55 — FIXME
old = 'msgid "// FIXME ^ Add the missing argument: \\"James\\"\\n"\nmsgstr ""'
new = 'msgid "// FIXME ^ Add the missing argument: \\"James\\"\\n"\nmsgstr "// FIXME ^ Dodaj brakujący argument: \\"James\\"\\n"'
text, n = replace(text, old, new, 'FIXME James')
total += n

# print_display.md:21 — Write strictly the first element
old, new = make_multi_msgid(
    ['msgid ""',
     '"// Write strictly the first element into the supplied output\\n"',
     '"        // stream: `f`. Returns `fmt::Result` which indicates whether the\\n"',
     '"        // operation succeeded or failed. Note that `write!` uses syntax "',
     '"which\\n"',
     '"        // is very similar to `println!`.\\n"'],
    ['"// Zapisz ściśle pierwszy element do dostarczonego strumienia\\n"',
     '"        // wyjściowego: `f`. Zwraca `fmt::Result`, który wskazuje, czy\\n"',
     '"        // operacja się powiodła. Uwaga: `write!` używa składni\\n"',
     '"        // bardzo podobnej do `println!`.\\n"'],
    'Write strictly first element'
)
text, n = replace(text, old, new, 'Write strictly first element')
total += n

# print_display.md:48 — A structure holding two numbers
old, new = make_multi_msgid(
    ['msgid ""',
     '"// A structure holding two numbers. `Debug` will be derived so the results "',
     '"can\\n"',
     '"// be contrasted with `Display`.\\n"'],
    ['"// Struktura przechowująca dwie liczby. `Debug` zostanie wyprowadzone,\\n"',
     '"// aby wyniki można było porównać z `Display`.\\n"'],
    'structure holding two numbers'
)
text, n = replace(text, old, new, 'structure holding two numbers')
total += n

# tuples.md:38 — long Tuples comment
old, new = make_multi_msgid(
    ['msgid ""',
     '"// But long Tuples (more than 12 elements) cannot be printed.\\n"',
     '"    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);\\n"',
     '"    //println!(\\"Too long tuple: {:?}\\", too_long_tuple);\\n"',
     '"    // TODO ^ Uncomment the above 2 lines to see the compiler error\\n"'],
    ['"// Ale długie krotki (ponad 12 elementów) nie mogą być drukowane.\\n"',
     '"    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);\\n"',
     '"    //println!(\\"Too long tuple: {:?}\\", too_long_tuple);\\n"',
     '"    // TODO ^ Odkomentuj powyższe 2 linie, aby zobaczyć błąd kompilatora\\n"'],
    'long Tuples'
)
text, n = replace(text, old, new, 'long Tuples')
total += n

# tuples.md:48 — one element tuples
old, new = make_multi_msgid(
    ['msgid ""',
     '"// To create one element tuples, the comma is required to tell them apart\\n"',
     '"    // from a literal surrounded by parentheses.\\n"'],
    ['"// Aby stworzyć krotki jednoelementowe, wymagany jest przecinek,\\n"',
     '"    // aby odróżnić je od wyrażenia w nawiasach.\\n"'],
    'one element tuples'
)
text, n = replace(text, old, new, 'one element tuples')
total += n

# array.md:43 — Slices can point
old, new = make_multi_msgid(
    ['msgid ""',
     '"// Slices can point to a section of an array.\\n"',
     '"    // They are of the form [starting_index..ending_index].\\n"',
     '"    // `starting_index` is the first position in the slice.\\n"',
     '"    // `ending_index` is one more than the last position in the slice.\\n"'],
    ['"// Wycinki mogą wskazywać na fragment tablicy.\\n"',
     '"    // Mają postać [indeks_początkowy..indeks_końcowy].\\n"',
     '"    // `indeks_początkowy` to pierwsza pozycja wycinka.\\n"',
     '"    // `indeks_końcowy` jest o 1 większy niż ostatnia pozycja wycinka.\\n"'],
    'Slices can point'
)
text, n = replace(text, old, new, 'Slices can point')
total += n

# array.md:55 — Arrays can be safely accessed
old, new = make_multi_msgid(
    ['msgid ""',
     '"// Arrays can be safely accessed using `.get`, which returns an\\n"',
     '"    // `Option`. This can be matched as shown below, or used with\\n"',
     '"    // `.expect()` if you would like the program to exit with a nice\\n"',
     '"    // message instead of happily continue.\\n"'],
    ['"// Tablice można bezpiecznie indeksować przez `.get`, które zwraca\\n"',
     '"    // `Option`. Można je dopasować jak poniżej lub użyć\\n"',
     '"    // `.expect()`, jeśli program ma zakończyć się z komunikatem\\n"',
     '"    // zamiast działać dalej.\\n"'],
    'Arrays can be safely accessed'
)
text, n = replace(text, old, new, 'Arrays can be safely accessed')
total += n

# array.md:66 — Out of bound indexing
old, new = make_multi_msgid(
    ['msgid ""',
     '"// Out of bound indexing on array with constant value causes compile time "',
     '"error.\\n"',
     '"    //println!(\\"{}\\", xs[5]);\\n"',
     '"    // Out of bound indexing on slice causes runtime error.\\n"',
     '"    //println!(\\"{}\\", xs[..][5]);\\n"'],
    ['"// Indeksowanie poza zakresem tablicy ze stałą wartością powoduje błąd kompilacji.\\n"',
     '"    //println!(\\"{}\\", xs[5]);\\n"',
     '"    // Indeksowanie poza zakresem wycinka powoduje błąd czasu wykonania.\\n"',
     '"    //println!(\\"{}\\", xs[..][5]);\\n"'],
    'Out of bound indexing'
)
text, n = replace(text, old, new, 'Out of bound indexing')
total += n

# ========== TEKST OPISOWY (PROSE) ==========

# fmt.md:5 — format! example
old = ('msgid "`format!(\\"{}\\", foo)` -> `\\"3735928559\\"`"\n'
       'msgstr ""')
new = ('msgid "`format!(\\"{}\\", foo)` -> `\\"3735928559\\"`"\n'
       'msgstr "`format!(\\"{}\\", foo)` -> `\\"3735928559\\"`"')
text, n = replace(text, old, new, 'format! foo example 1')
total += n

old = ('msgid "`format!(\\"0o{:o}\\", foo)` -> `\\"0o33653337357\\"`"\n'
       'msgstr ""')
new = ('msgid "`format!(\\"0o{:o}\\", foo)` -> `\\"0o33653337357\\"`"\n'
       'msgstr "`format!(\\"0o{:o}\\", foo)` -> `\\"0o33653337357\\"`"')
text, n = replace(text, old, new, 'format! foo example 2')
total += n

# tuples.md:66 — _Recap_
old, new = make_multi_msgid(
    ['msgid ""',
     '"_Recap_: Add the `fmt::Display` trait to the `Matrix` struct in the above "',
     '"example, so that if you switch from printing the debug format `{:?}` to the "',
     '"display format `{}`, you see the following output:"'],
    ['"_Podsumowanie_: Dodaj cechę `fmt::Display` do struktury `Matrix` w powyższym "',
     '"przykładzie, tak aby po przełączeniu z formatu debugowania `{:?}` na "',
     '"format wyświetlania `{}`, zobaczyć następujące wyjście:"'],
    '_Recap_ Matrix'
)
text, n = replace(text, old, new, '_Recap_ Matrix')
total += n

# tuples.md:75 — refer back to example
old, new = make_multi_msgid(
    ['msgid ""',
     '"You may want to refer back to the example for [print display](../hello/print/"',
     '"print_display.md)."'],
    ['"Możesz odnieść się do przykładu dla [drukowania Display](../hello/print/"',
     '"print_display.md)."'],
    'refer back to example'
)
text, n = replace(text, old, new, 'refer back to example')
total += n

# tuples.md:76 — Add a transpose function
old, new = make_multi_msgid(
    ['msgid ""',
     '"Add a `transpose` function using the `reverse` function as a template, which "',
     '"accepts a matrix as an argument, and returns a matrix in which two elements "',
     '"have been swapped. For example:"'],
    ['"Dodaj funkcję `transpose`, używając funkcji `reverse` jako wzorca, która "',
     '"przyjmuje macierz jako argument i zwraca macierz, w której dwa elementy "',
     '"zostały zamienione. Na przykład:"'],
    'Add transpose function'
)
text, n = replace(text, old, new, 'Add transpose function')
total += n

# tuples.md:85 — Results in the output
old = 'msgid "Results in the output:"\nmsgstr ""'
new = 'msgid "Results in the output:"\nmsgstr "Co daje wyjście:"'
text, n = replace(text, old, new, 'Results in the output')
total += n

# literals.md:29 — TODO comment
old = ('msgid ""\n'
       '"// TODO ^ Try changing `1i32` to `1u32` to see why the type is important\\n"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"// TODO ^ Try changing `1i32` to `1u32` to see why the type is important\\n"\n'
       'msgstr ""\n'
       '"// TODO ^ Spróbuj zmienić `1i32` na `1u32`, aby zobaczyć, dlaczego typ jest ważny\\n"')
text, n = replace(text, old, new, 'TODO Try changing 1i32')
total += n

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nLacznie zmian: {total}')
