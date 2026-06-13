#!/usr/bin/env python3
"""Tłumaczenie Etapu 3: Types, Conversion."""

PO_FILE = 'po/pl.po'

with open(PO_FILE, 'r', encoding='utf-8') as f:
    text = f.read()

total = 0

def apply(old, new, label=''):
    global text, total
    n = text.count(old)
    if n == 0:
        print(f'NIE: {label}')
        return
    if n > 1:
        print(f'WIEL({n}): {label}')
    text = text.replace(old, new)
    total += n

def lit(content):
    old = f'msgid "\\"{content}\\""\nmsgstr ""'
    new = f'msgid "\\"{content}\\""\nmsgstr "\\"{content}\\""'
    apply(old, new, content[:40])

def comment(en, pl):
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{pl}"'
    apply(old, new, en[:40])

def prose(en, pl):
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{pl}"'
    apply(old, new, en[:40])

def multi(old_body, new_msgstr):
    old = old_body + '\nmsgstr ""'
    new = old_body + '\nmsgstr ""\n' + new_msgstr
    apply(old, new, old_body[8:48])

# ============================================================
# STRING LITERALS — VERBATIM
# ============================================================

# cast.md
lit('Casting: {} -> {} -> {}')
lit('1000 as a u16 is: {}')
lit('1000 as a u8 is : {}')
lit('  -1 as a u8 is : {}')
lit('1000 mod 256 is : {}')
lit(' 128 as a i16 is: {}')
lit(' 128 as a i8 is : {}')
lit(' 232 as a i8 is : {}')
lit(' 300.0 as u8 is : {}')
lit('-100.0 as u8 is : {}')
lit('   nan as u8 is : {}')

# literals.md
lit('size of `x` in bytes: {}')
lit('size of `y` in bytes: {}')
lit('size of `z` in bytes: {}')
lit('size of `i` in bytes: {}')
lit('size of `f` in bytes: {}')

# alias.md
lit('{} nanoseconds + {} inches = {} unit?')

# from_into.md
lit('My number is {:?}')

# string.md
lit('Circle of radius {}')
lit('5')
lit('10')
lit('Sum: {:?}')
lit('    3 ')

# ============================================================
# JEDNOLINIJKOWE KOMENTARZE
# ============================================================

comment('// Suppress all errors from casts which overflow.\\n',
        '// Wycisz wszystkie błędy wynikające z przepełnienia rzutowania.\\n')
comment('// Error! No implicit conversion\\n',
        '// Błąd! Brak niejawnej konwersji\\n')
comment('// Explicit conversion\\n', '// Jawna konwersja\\n')
comment('// 1000 already fits in a u16\\n',
        '// 1000 mieści się już w u16\\n')
comment('// -1 + 256 = 255\\n', '// -1 + 256 = 255\\n')
comment('// For positive numbers, this is the same as the modulus\\n',
        '// Dla liczb dodatnich to to samo co reszta z dzielenia\\n')
comment('// Unless it already fits, of course.\\n',
        '// Chyba że już się mieści, oczywiście.\\n')
comment('// 300.0 as u8 is 255\\n', '// 300.0 jako u8 to 255\\n')
comment('// -100.0 as u8 is 0\\n', '// -100.0 jako u8 to 0\\n')
comment('// nan as u8 is 0\\n', '// nan jako u8 to 0\\n')
comment('// 300.0 as u8 is 44\\n', '// 300.0 jako u8 to 44\\n')
comment('// -100.0 as u8 is 156\\n', '// -100.0 jako u8 to 156\\n')
comment('// Suffixed literals, their types are known at initialization\\n',
        '// Literały z sufiksem — ich typy są znane przy inicjalizacji\\n')
comment('// Unsuffixed literals, their types depend on how they are used\\n',
        '// Literały bez sufiksu — ich typy zależą od użycia\\n')
comment('// `size_of_val` returns the size of a variable in bytes\\n',
        '// `size_of_val` zwraca rozmiar zmiennej w bajtach\\n')
comment('// `NanoSecond`, `Inch`, and `U64` are new names for `u64`.\\n',
        '// `NanoSecond`, `Inch` i `U64` to nowe nazwy dla `u64`.\\n')
comment('// `NanoSecond` = `Inch` = `U64` = `u64`.\\n',
        '// `NanoSecond` = `Inch` = `U64` = `u64`.\\n')
comment('// Try removing the type annotation\\n',
        '// Spróbuj usunąć adnotację typu\\n')
comment('// Define `From`\\n', '// Zdefiniuj `From`\\n')
comment('// use `Into`\\n', '// użyj `Into`\\n')
comment('// TryFrom\\n', '// TryFrom\\n')
comment('// TryInto\\n', '// TryInto\\n')

# ============================================================
# JEDNOLINIJKOWA PROZA
# ============================================================

prose('`From`', '`From`')
prose('`Into`', '`Into`')
prose('`From` and `Into` are interchangeable',
      '`From` i `Into` są wymienne')
prose('For example we can easily convert a `str` into a `String`',
      'Na przykład możemy łatwo przekonwertować `str` na `String`')
prose('We can do something similar for defining a conversion for our own type.',
      'Możemy zrobić coś podobnego, definiując konwersję dla własnego typu.')
prose('To and from Strings', 'Konwersja do i z napisu String')
prose('Converting to String', 'Konwersja do String')
prose('Parsing a String', 'Parsowanie napisu String')
prose('[Attributes](../attribute.md)', '[Atrybuty](../attribute.md)')

# ============================================================
# WIELOLINIOWA PROZA I KOMENTARZE
# ============================================================

# cast.md:3 — no implicit type conversion
multi(
    'msgid ""\n'
    '"Rust provides no implicit type conversion (coercion) between primitive "\n'
    '"types. But, explicit type conversion (casting) can be performed using the "\n'
    '"`as` keyword."',
    '"Rust nie zapewnia niejawnej konwersji typów (koercji) między typami "\n'
    '"pierwotnymi. Jawna konwersja typów (rzutowanie) jest możliwa za pomocą "\n'
    '"słowa kluczowego `as`."'
)

# cast.md:6 — integral types
multi(
    'msgid ""\n'
    '"Rules for converting between integral types follow C conventions generally, "\n'
    '"except in cases where C has undefined behavior. The behavior of all casts "\n'
    '"between integral types is well defined in Rust."',
    '"Reguły konwersji między typami całkowitymi generalnie są zgodne z "\n'
    '"konwencjami C, z wyjątkiem przypadków, gdzie C ma niezdefiniowane zachowanie. "\n'
    '"Zachowanie wszystkich rzutowań między typami całkowitymi jest dobrze zdefiniowane w Rust."'
)

# cast.md:25 — Error! float to char
multi(
    'msgid ""\n'
    '"// Error! There are limitations in conversion rules.\\n"\n'
    '"    // A float cannot be directly converted to a char.\\n"',
    '"// Błąd! Reguły konwersji mają ograniczenia.\\n"\n'
    '"    // Zmiennoprzecinkowa nie może być bezpośrednio przekonwertowana na char.\\n"'
)

# cast.md:32 — unsigned type casting
multi(
    'msgid ""\n'
    '"// when casting any value to an unsigned type, T,\\n"\n'
    '"    // T::MAX + 1 is added or subtracted until the value\\n"\n'
    '"    // fits into the new type ONLY when the #![allow(overflowing_literals)]\\n"\n'
    '"    // lint is specified like above. Otherwise there will be a compiler error.\\n"',
    '"// Przy rzutowaniu dowolnej wartości na typ bez znaku T,\\n"\n'
    '"    // dodaje lub odejmuje się T::MAX + 1 aż wartość zmieści się w nowym\\n"\n'
    '"    // typie — TYLKO gdy podano lint #![allow(overflowing_literals)]\\n"\n'
    '"    // jak powyżej. W przeciwnym razie wystąpi błąd kompilatora.\\n"'
)

# cast.md:40 — 1000 - 256 * 3
multi(
    'msgid ""\n'
    '"// 1000 - 256 - 256 - 256 = 232\\n"\n'
    '"    // Under the hood, the first 8 least significant bits (LSB) are kept,\\n"\n'
    '"    // while the rest towards the most significant bit (MSB) get truncated.\\n"',
    '"// 1000 - 256 - 256 - 256 = 232\\n"\n'
    '"    // Pod spodem zachowywane jest pierwszych 8 najmniej znaczących bitów (LSB),\\n"\n'
    '"    // a reszta w kierunku najbardziej znaczącego bitu (MSB) jest obcinana.\\n"'
)

# cast.md:50 — signed type casting
multi(
    'msgid ""\n'
    '"// When casting to a signed type, the (bitwise) result is the same as\\n"\n'
    '"    // first casting to the corresponding unsigned type. If the most significant\\n"\n'
    '"    // bit of that value is 1, then the value is negative.\\n"',
    '"// Przy rzutowaniu na typ ze znakiem wynik (bitowy) jest taki sam jak\\n"\n'
    '"    // rzutowanie najpierw na odpowiedni typ bez znaku. Jeśli najbardziej\\n"\n'
    '"    // znaczący bit wyniku to 1, wartość jest ujemna.\\n"'
)

# cast.md:57 — boundary case 128
apply(
    'msgid ""\n'
    '"// In boundary case 128 value in 8-bit two\'s complement representation is "\n'
    '"-128\\n"\n'
    'msgstr ""',
    'msgid ""\n'
    '"// In boundary case 128 value in 8-bit two\'s complement representation is "\n'
    '"-128\\n"\n'
    'msgstr ""\n'
    '"// W przypadku granicznym wartość 128 w uzupełnieniu do dwóch na 8 bitach to -128\\n"',
    'boundary case 128'
)

# cast.md:60 — repeating example
apply(
    'msgid ""\n'
    '"// repeating the example above\\n"\n'
    '"    // 1000 as u8 -> 232\\n"\n'
    'msgstr ""',
    'msgid ""\n'
    '"// repeating the example above\\n"\n'
    '"    // 1000 as u8 -> 232\\n"\n'
    'msgstr ""\n'
    '"// powtarzając przykład powyżej\\n"\n'
    '"    // 1000 jako u8 -> 232\\n"',
    'repeating the example'
)

# cast.md:63 — 232 in two's complement
apply(
    "msgid \"\"\n"
    "\"// and the value of 232 in 8-bit two's complement representation is -24\\n\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"// and the value of 232 in 8-bit two's complement representation is -24\\n\"\n"
    "msgstr \"\"\n"
    "\"// a wartość 232 w uzupełnieniu do dwóch na 8 bitach to -24\\n\"",
    '232 in 8-bit'
)

# cast.md:66 — saturating cast
multi(
    'msgid ""\n'
    '"// Since Rust 1.45, the `as` keyword performs a *saturating cast*\\n"\n'
    '"    // when casting from float to int. If the floating point value exceeds\\n"\n'
    '"    // the upper bound or is less than the lower bound, the returned value\\n"\n'
    '"    // will be equal to the bound crossed.\\n"',
    '"// Od Rust 1.45 słowo kluczowe `as` wykonuje *rzutowanie saturujące*\\n"\n'
    '"    // przy konwersji z float do int. Jeśli wartość zmiennoprzecinkowa przekracza\\n"\n'
    '"    // górną lub dolną granicę, zwracana wartość jest równa przekroczonej granicy.\\n"'
)

# cast.md:78 — small runtime cost
multi(
    'msgid ""\n'
    '"// This behavior incurs a small runtime cost and can be avoided\\n"\n'
    '"    // with unsafe methods, however the results might overflow and\\n"\n'
    '"    // return **unsound values**. Use these methods wisely:\\n"',
    '"// To zachowanie powoduje mały koszt w czasie wykonania i można go uniknąć\\n"\n'
    '"    // metodami unsafe, jednak wyniki mogą przepełnić i zwrócić\\n"\n'
    '"    // **wartości niepoprawne**. Używaj tych metod rozważnie:\\n"'
)

# literals.md:3
multi(
    'msgid ""\n'
    '"Numeric literals can be type annotated by adding the type as a suffix. As an "\n'
    '"example, to specify that the literal `42` should have the type `i32`, write "\n'
    '"`42i32`."',
    '"Literały numeryczne mogą mieć adnotację typu przez dodanie sufiksu. Na "\n'
    '"przykład, aby określić, że literał `42` ma typ `i32`, napisz `42i32`."'
)

# literals.md:6
multi(
    'msgid ""\n'
    '"The type of unsuffixed numeric literals will depend on how they are used. If "\n'
    '"no constraint exists, the compiler will use `i32` for integers, and `f64` "\n'
    '"for floating-point numbers."',
    '"Typ literałów numerycznych bez sufiksu zależy od sposobu ich użycia. Jeśli "\n'
    '"nie ma ograniczeń, kompilator użyje `i32` dla liczb całkowitych i `f64` "\n'
    '"dla zmiennoprzecinkowych."'
)

# literals.md:30 — impatient readers
apply(
    "msgid \"\"\n"
    "\"There are some concepts used in the previous code that haven't been \"\n"
    "\"explained yet, here's a brief explanation for the impatient readers:\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"There are some concepts used in the previous code that haven't been \"\n"
    "\"explained yet, here's a brief explanation for the impatient readers:\"\n"
    "msgstr \"\"\n"
    "\"W powyższym kodzie użyto kilku koncepcji, które jeszcze nie zostały wyjaśnione. \"\n"
    "\"Oto krótkie objaśnienie dla niecierpliwych czytelników:\"",
    'impatient readers'
)

# literals.md:33 — size_of_val full path
multi(
    'msgid ""\n'
    '"`std::mem::size_of_val` is a function, but called with its _full path_. Code "\n'
    '"can be split in logical units called _modules_. In this case, the "\n'
    '"`size_of_val` function is defined in the `mem` module, and the `mem` module "\n'
    '"is defined in the `std` _crate_. For more details, see [modules](../mod.md) "\n'
    '"and [crates](../crates.md)."',
    '"`std::mem::size_of_val` to funkcja wywoływana przez _pełną ścieżkę_. Kod "\n'
    '"można dzielić na logiczne jednostki zwane _modułami_. W tym przypadku funkcja "\n'
    '"`size_of_val` jest zdefiniowana w module `mem`, a moduł `mem` w _skrzyni_ `std`. "\n'
    '"Szczegóły: [moduły](../mod.md) i [skrzynie](../crates.md)."'
)

# inference.md:3 — type inference engine
apply(
    "msgid \"\"\n"
    "\"The type inference engine is pretty smart. It does more than looking at the \"\n"
    "\"type of the value expression during an initialization. It also looks at how \"\n"
    "\"the variable is used afterwards to infer its type. Here's an advanced \"\n"
    "\"example of type inference:\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"The type inference engine is pretty smart. It does more than looking at the \"\n"
    "\"type of the value expression during an initialization. It also looks at how \"\n"
    "\"the variable is used afterwards to infer its type. Here's an advanced \"\n"
    "\"example of type inference:\"\n"
    "msgstr \"\"\n"
    "\"Silnik wnioskowania typów jest całkiem sprytny. Robi więcej niż tylko patrzenie \"\n"
    "\"na typ wyrażenia wartości podczas inicjalizacji. Sprawdza też, jak zmienna \"\n"
    "\"jest używana później, aby wywnioskować jej typ. Oto zaawansowany przykład \"\n"
    "\"wnioskowania typów:\"",
    'type inference engine'
)

# inference.md:10 — because of annotation
apply(
    'msgid ""\n'
    '"// Because of the annotation, the compiler knows that `elem` has type u8.\\n"\n'
    'msgstr ""',
    'msgid ""\n'
    '"// Because of the annotation, the compiler knows that `elem` has type u8.\\n"\n'
    'msgstr ""\n'
    '"// Dzięki adnotacji kompilator wie, że `elem` ma typ u8.\\n"',
    'Because of annotation'
)

# inference.md:13 — create empty vector
comment("// Create an empty vector (a growable array).\\n",
        "// Utwórz pusty wektor (tablica o zmiennym rozmiarze).\\n")

# inference.md:15 — doesn't know exact type
apply(
    "msgid \"\"\n"
    "\"// At this point the compiler doesn't know the exact type of `vec`, it\\n\"\n"
    "\"    // just knows that it's a vector of something (`Vec<_>`).\\n\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"// At this point the compiler doesn't know the exact type of `vec`, it\\n\"\n"
    "\"    // just knows that it's a vector of something (`Vec<_>`).\\n\"\n"
    "msgstr \"\"\n"
    "\"// W tym miejscu kompilator nie zna dokładnego typu `vec`,\\n\"\n"
    "\"    // wie tylko, że to wektor czegoś (`Vec<_>`).\\n\"",
    "doesn't know exact type"
)

# inference.md:18
comment("// Insert `elem` in the vector.\\n",
        "// Wstaw `elem` do wektora.\\n")

# inference.md:20 — Aha! Now
apply(
    'msgid ""\n'
    '"// Aha! Now the compiler knows that `vec` is a vector of `u8`s (`Vec<u8>`)\\n"\n'
    '"    // TODO ^ Try commenting out the `vec.push(elem)` line\\n"\n'
    'msgstr ""',
    'msgid ""\n'
    '"// Aha! Now the compiler knows that `vec` is a vector of `u8`s (`Vec<u8>`)\\n"\n'
    '"    // TODO ^ Try commenting out the `vec.push(elem)` line\\n"\n'
    'msgstr ""\n'
    '"// Aha! Teraz kompilator wie, że `vec` to wektor `u8` (`Vec<u8>`)\\n"\n'
    '"    // TODO ^ Spróbuj zakomentować linię `vec.push(elem)`\\n"',
    'Aha! Now compiler knows'
)

# inference.md:27 — no annotation needed
multi(
    'msgid ""\n'
    '"No type annotation of variables was needed, the compiler is happy and so is "\n'
    '"the programmer!"',
    '"Żadna adnotacja typów zmiennych nie była potrzebna — kompilator jest szczęśliwy "\n'
    '"i programista też!"'
)

# alias.md:3 — type statement
multi(
    'msgid ""\n'
    '"The `type` statement can be used to give a new name to an existing type. "\n'
    '"Types must have `UpperCamelCase` names, or the compiler will raise a "\n'
    '"warning. The exception to this rule are the primitive types: `usize`, `f32`, "\n'
    '"etc."',
    '"Instrukcja `type` pozwala nadać nową nazwę istniejącemu typowi. "\n'
    '"Typy muszą mieć nazwy w `UpperCamelCase`, inaczej kompilator zgłosi "\n'
    '"ostrzeżenie. Wyjątkiem są typy pierwotne: `usize`, `f32` itd."'
)

# alias.md:18 — type aliases don't provide safety
multi(
    'msgid ""\n'
    '"// Note that type aliases *don\'t* provide any extra type safety, because\\n"\n'
    '"    // aliases are *not* new types\\n"',
    '"// Aliasy typów *nie* zapewniają dodatkowego bezpieczeństwa typów,\\n"\n'
    '"    // bo aliasy *nie* są nowymi typami\\n"'
)

# alias.md:27 — main use of aliases
multi(
    'msgid ""\n'
    '"The main use of aliases is to reduce boilerplate; for example the `io::"\n'
    '"Result<T>` type is an alias for the `Result<T, io::Error>` type."',
    '"Główne zastosowanie aliasów to redukcja powtarzalnego kodu; na przykład "\n'
    '"typ `io::Result<T>` to alias dla `Result<T, io::Error>`."'
)

# from_into.md:3 — From and Into traits
multi(
    'msgid ""\n'
    '"The [`From`](https://doc.rust-lang.org/std/convert/trait.From.html) and "\n'
    '"[`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html) traits are "\n'
    '"inherently linked, and this is actually part of its implementation. If you "\n'
    '"are able to convert type A from type B, then it should be easy to believe "\n'
    '"that we should be able to convert type B to type A."',
    '"Cechy [`From`](https://doc.rust-lang.org/std/convert/trait.From.html) i "\n'
    '"[`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html) są "\n'
    '"inherentnie powiązane — to część ich implementacji. Jeśli można przekonwertować "\n'
    '"typ A z typu B, to powinno być możliwe przekonwertowanie B na A."'
)

# from_into.md:9 — From trait allows
multi(
    'msgid ""\n'
    '"The [`From`](https://doc.rust-lang.org/std/convert/trait.From.html) trait "\n'
    '"allows for a type to define how to create itself from another type, hence "\n'
    '"providing a very simple mechanism for converting between several types. "\n'
    '"There are numerous implementations of this trait within the standard library "\n'
    '"for conversion of primitive and common types."',
    '"Cecha [`From`](https://doc.rust-lang.org/std/convert/trait.From.html) pozwala "\n'
    '"typowi zdefiniować, jak się tworzyć z innego typu, zapewniając prosty mechanizm "\n'
    '"konwersji między wieloma typami. Biblioteka standardowa ma liczne implementacje "\n'
    '"tej cechy dla typów pierwotnych i powszechnych."'
)

# from_into.md:45 — Into trait
multi(
    'msgid ""\n'
    '"The [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html) trait is "\n'
    '"simply the reciprocal of the `From` trait. It defines how to convert a type "\n'
    '"into another type."',
    '"Cecha [`Into`](https://doc.rust-lang.org/std/convert/trait.Into.html) to "\n'
    '"po prostu odwrotność cechy `From`. Definiuje, jak przekonwertować typ "\n'
    '"na inny typ."'
)

# from_into.md:48 — Calling into()
multi(
    'msgid ""\n'
    '"Calling `into()` typically requires us to specify the result type as the "\n'
    '"compiler is unable to determine this most of the time."',
    '"Wywołanie `into()` zazwyczaj wymaga podania typu wyniku, ponieważ "\n'
    '"kompilator w większości przypadków nie może go określić."'
)

# from_into.md:74 — From and Into complementary
multi(
    'msgid ""\n'
    '"`From` and `Into` are designed to be complementary. We do not need to "\n'
    '"provide an implementation for both traits. If you have implemented the "\n'
    '"`From` trait for your type, `Into` will call it when necessary. Note, "\n'
    '"however, that the converse is not true: implementing `Into` for your type "\n'
    '"will not automatically provide it with an implementation of `From`."',
    '"`From` i `Into` są zaprojektowane jako uzupełniające się. Nie trzeba "\n'
    '"implementować obu cech. Jeśli zaimplementowałeś `From` dla swojego typu, "\n'
    '"`Into` będzie je wywoływać gdy potrzeba. Uwaga: odwrotność nie jest prawdą — "\n'
    '"implementacja `Into` nie zapewnia automatycznie implementacji `From`."'
)

# try_from_try_into.md:3 — Similar to From and Into
multi(
    'msgid ""\n'
    '"Similar to [`From` and `Into`](from_into.html), [`TryFrom`](https://doc.rust-"\n'
    '"lang.org/std/convert/trait.TryFrom.html) and [`TryInto`](https://doc.rust-"\n'
    '"lang.org/std/convert/trait.TryInto.html) are generic traits for converting "\n'
    '"between types. Unlike `From`/`Into`, the `TryFrom`/`TryInto` traits are used "\n'
    '"for fallible conversions, and as such, return [`Result`](https://doc.rust-"\n'
    '"lang.org/std/result/enum.Result.html)s."',
    '"Podobnie do [`From` i `Into`](from_into.html), [`TryFrom`](https://doc.rust-"\n'
    '"lang.org/std/convert/trait.TryFrom.html) i [`TryInto`](https://doc.rust-"\n'
    '"lang.org/std/convert/trait.TryInto.html) to cechy ogólne do konwersji "\n'
    '"między typami. W odróżnieniu od `From`/`Into`, cechy `TryFrom`/`TryInto` "\n'
    '"służą do konwersji zawodnych i zwracają [`Result`](https://doc.rust-"\n'
    '"lang.org/std/result/enum.Result.html)."'
)

# string.md:5 — ToString trait
multi(
    'msgid ""\n'
    '"To convert any type to a `String` is as simple as implementing the "\n'
    '"[`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html) trait "\n'
    '"for the type. Rather than doing so directly, you should implement the [`fmt::"\n'
    '"Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html) trait which "\n'
    '"automatically provides [`ToString`](https://doc.rust-lang.org/std/string/"\n'
    '"trait.ToString.html) and also allows printing the type as discussed in the "\n'
    '"section on [`print!`](../hello/print.md)."',
    '"Konwersja dowolnego typu do `String` sprowadza się do implementacji cechy "\n'
    '"[`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html). "\n'
    '"Zamiast robić to bezpośrednio, zaimplementuj cechę [`fmt::Display`]"\n'
    '"(https://doc.rust-lang.org/std/fmt/trait.Display.html), która automatycznie "\n'
    '"zapewnia [`ToString`](https://doc.rust-lang.org/std/string/trait.ToString.html) "\n'
    '"i pozwala drukować typ, jak opisano w sekcji [`print!`](../hello/print.md)."'
)

# string.md:31 — parsing strings
apply(
    "msgid \"\"\n"
    "\"It's useful to convert strings into many types, but one of the more common \"\n"
    "\"string operations is to convert them from string to number. The idiomatic \"\n"
    "\"approach to this is to use the [`parse`](https://doc.rust-lang.org/std/\"\n"
    "\"primitive.str.html#method.parse) function and either to arrange for type \"\n"
    "\"inference or to specify the type to parse using the 'turbofish' syntax. Both \"\n"
    "\"alternatives are shown in the following example.\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"It's useful to convert strings into many types, but one of the more common \"\n"
    "\"string operations is to convert them from string to number. The idiomatic \"\n"
    "\"approach to this is to use the [`parse`](https://doc.rust-lang.org/std/\"\n"
    "\"primitive.str.html#method.parse) function and either to arrange for type \"\n"
    "\"inference or to specify the type to parse using the 'turbofish' syntax. Both \"\n"
    "\"alternatives are shown in the following example.\"\n"
    "msgstr \"\"\n"
    "\"Przydatne jest konwertowanie napisów na wiele typów, a jedną z częstszych \"\n"
    "\"operacji jest konwersja napisu na liczbę. Idiomatycznym podejściem jest użycie \"\n"
    "\"funkcji [`parse`](https://doc.rust-lang.org/std/primitive.str.html#method.parse) \"\n"
    "\"i albo wnioskowanie typów, albo podanie typu do sparsowania składnią 'turbofish'. \"\n"
    "\"Obie alternatywy pokazano w poniższym przykładzie.\"",
    'parsing strings'
)

# string.md:37 — FromStr trait
multi(
    'msgid ""\n'
    '"This will convert the string into the type specified as long as the "\n'
    '"[`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) trait is "\n'
    '"implemented for that type. This is implemented for numerous types within the "\n'
    '"standard library."',
    '"Konwertuje napis na podany typ, o ile cecha "\n'
    '"[`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) jest "\n'
    '"zaimplementowana dla tego typu. Jest zaimplementowana dla licznych typów "\n'
    '"w bibliotece standardowej."'
)

# string.md:51 — obtain functionality
multi(
    'msgid ""\n'
    '"To obtain this functionality on a user defined type simply implement the "\n'
    '"[`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) trait for "\n'
    '"that type."',
    '"Aby uzyskać tę funkcjonalność dla własnego typu, zaimplementuj cechę "\n'
    '"[`FromStr`](https://doc.rust-lang.org/std/str/trait.FromStr.html) dla niego."'
)

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
