#!/usr/bin/env python3
"""Tłumaczenie Etapu 2: Custom Types, Variable Bindings."""

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
    if n > 1:
        print(f'WIELOKROTNE ({n}): {label}')
    text = text.replace(old, new)
    total += n

def lit(content):
    """String literal — kopiuj verbatim."""
    old = f'msgid "\\"{content}\\""\nmsgstr ""'
    new = f'msgid "\\"{content}\\""\nmsgstr "\\"{content}\\""'
    apply(old, new, content[:40])

def comment(en, pl):
    """Jednolinijkowy komentarz."""
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{pl}"'
    apply(old, new, en[:40])

def prose(en, pl):
    """Jednolinijkowa proza."""
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{pl}"'
    apply(old, new, en[:40])

def multi(old_body, new_msgstr_lines):
    """Wieloliniowe msgid → wieloliniowe msgstr."""
    old = old_body + '\nmsgstr ""'
    new = old_body + '\nmsgstr ""\n' + '\n'.join(new_msgstr_lines)
    apply(old, new, old_body[8:48])

# ============================================================
# STRING LITERALS — VERBATIM (Rule 6)
# ============================================================

# structs.md
lit('point coordinates: ({}, {})')
lit('second point: ({}, {})')
lit('pair contains {:?} and {:?}')

# enum.md
lit('page loaded')
lit('page unloaded')
lit("pressed '{}'.")
lit('pasted \\\\\\"{}\\\\\\".') # pasted "{}". — escaped inner quotes
lit('clicked at x={}, y={}.')
lit('my text')

# enum_use.md
lit('Beginners are starting their learning journey!')
lit('Advanced learners are mastering their subjects...')
lit('Students are acquiring knowledge!')
lit('Teachers are spreading knowledge!')

# c_like.md
lit('zero is {}')
lit('one is {}')
lit('roses are #{:06x}')
lit('violets are #{:06x}')

# testcase_linked_list.md
lit('{}, {}')
lit('Nil')
lit('linked list has length: {}')

# constants.md
lit('Rust')
lit('This is {}')
lit('The threshold is {}')
lit('{} is {}')
lit('big')
lit('small')

# variable_bindings.md
lit('An integer: {}')
lit('A boolean: {}')
lit('Meet the unit value: {:?}')

# mut.md
lit('Before mutation: {}')
lit('After mutation: {}')

# scope.md
lit('inner short: {}')
lit('outer short: {}')
lit('outer long: {}')
lit('before being shadowed: {}')
lit('abc')
lit('shadowed in inner block: {}')
lit('outside inner block: {}')
lit('shadowed in outer block: {}')

# declare.md
lit('a binding: {}')
lit('another binding: {}')

# char literals
apply("msgid \"'x'\"\nmsgstr \"\"",
      "msgid \"'x'\"\nmsgstr \"'x'\"", "'x'")

# ============================================================
# JEDNOLINIJKOWE KOMENTARZE (Rule 3)
# ============================================================

comment('// An attribute to hide warnings for unused code.\\n',
        '// Atrybut ukrywający ostrzeżenia przed nieużywanym kodem.\\n')

comment('// A unit struct\\n', '// Struktura jednostkowa\\n')
comment('// A tuple struct\\n', '// Struktura krotkowa\\n')
comment('// A struct with two fields\\n', '// Struktura z dwoma polami\\n')
comment('// Structs can be reused as fields of another struct\\n',
        '// Struktury mogą być używane jako pola innej struktury\\n')
comment('// Create struct with field init shorthand\\n',
        '// Utwórz strukturę ze skróconą inicjalizacją pól\\n')
comment('// Print debug struct\\n', '// Wydrukuj strukturę w trybie debug\\n')
comment('// Instantiate a `Point`\\n', '// Stwórz instancję `Point`\\n')
comment('// Access the fields of the point\\n',
        '// Uzyskaj dostęp do pól punktu\\n')
comment('// Destructure the point using a `let` binding\\n',
        '// Destrukturyzuj punkt za pomocą wiązania `let`\\n')
comment('// struct instantiation is an expression too\\n',
        '// Tworzenie instancji struktury to też wyrażenie\\n')
comment('// Instantiate a unit struct\\n',
        '// Stwórz instancję struktury jednostkowej\\n')
comment('// Instantiate a tuple struct\\n',
        '// Stwórz instancję struktury krotkowej\\n')
comment('// Access the fields of a tuple struct\\n',
        '// Uzyskaj dostęp do pól struktury krotkowej\\n')
comment('// Destructure a tuple struct\\n',
        '// Destrukturyzuj strukturę krotkową\\n')

# enum.md
comment('// An `enum` variant may either be `unit-like`,\\n',
        '// Wariant `enum` może być `unit-like` (jednostkowy),\\n')
comment('// like tuple structs,\\n', '// jak struktury krotkowe,\\n')
comment('// or c-like structures.\\n', '// lub struktury podobne do C.\\n')
comment('// Destructure `c` from inside the `enum` variant.\\n',
        '// Destrukturyzuj `c` z wnętrza wariantu `enum`.\\n')
comment('// Destructure `Click` into `x` and `y`.\\n',
        '// Destrukturyzuj `Click` na `x` i `y`.\\n')
comment('// `to_owned()` creates an owned `String` from a string slice.\\n',
        '// `to_owned()` tworzy własny `String` z wycinka napisu.\\n')
comment('// Creates a type alias\\n', '// Tworzy alias typu\\n')

# enum_use.md
comment('// Equivalent to `Stage::Beginner`.\\n',
        '// Odpowiednik `Stage::Beginner`.\\n')
comment('// Equivalent to `Role::Student`.\\n',
        '// Odpowiednik `Role::Student`.\\n')
comment('// Note the lack of scoping because of the explicit `use` above.\\n',
        '// Brak kwalifikacji dzięki jawnym `use` powyżej.\\n')
comment('// Note again the lack of scoping.\\n',
        '// Ponownie brak kwalifikacji.\\n')

# c_like.md
comment('// enum with implicit discriminator (starts at 0)\\n',
        '// wyliczenie z niejawnym dyskryminatorem (zaczyna od 0)\\n')
comment('// enum with explicit discriminator\\n',
        '// wyliczenie z jawnym dyskryminatorem\\n')
comment('// `enums` can be cast as integers.\\n',
        '// `enum` można rzutować na liczby całkowite.\\n')

# testcase_linked_list.md
comment('// `Cons` also has type List\\n',
        '// `Cons` też ma typ List\\n')
comment('// Return the length of the list\\n',
        '// Zwróć długość listy\\n')
comment('// Base Case: An empty list has zero length\\n',
        '// Przypadek bazowy: pusta lista ma zerową długość\\n')
comment('// Return representation of the list as a (heap allocated) string\\n',
        '// Zwróć reprezentację listy jako napis (alokowany na stercie)\\n')
comment('// Create an empty linked list\\n',
        '// Utwórz pustą listę powiązaną\\n')
comment('// Prepend some elements\\n', '// Dodaj kilka elementów na początku\\n')
comment('// Show the final state of the list\\n',
        '// Pokaż końcowy stan listy\\n')

# constants.md
comment('// Globals are declared outside all other scopes.\\n',
        '// Zmienne globalne deklaruje się poza wszystkimi zasięgami.\\n')
comment('// Access constant in some function\\n',
        '// Dostęp do stałej w jakiejś funkcji\\n')
comment('// Access constant in the main thread\\n',
        '// Dostęp do stałej w wątku głównym\\n')
comment('// Error! Cannot modify a `const`.\\n',
        '// Błąd! Nie można modyfikować `const`.\\n')
comment('// FIXME ^ Comment out this line\\n',
        '// FIXME ^ Zakomentuj tę linię\\n')

# variable_bindings.md
comment('// copy `an_integer` into `copied_integer`\\n',
        '// skopiuj `an_integer` do `copied_integer`\\n')

# mut.md
comment('// Ok\\n', '// Ok\\n')
comment('// Error! Cannot assign a new value to an immutable variable\\n',
        '// Błąd! Nie można przypisać nowej wartości do niemutowalnej zmiennej\\n')

# scope.md
comment('// This binding lives in the main function\\n',
        '// To wiązanie istnieje w funkcji main\\n')
comment('// This binding only exists in this block\\n',
        '// To wiązanie istnieje tylko w tym bloku\\n')
comment('// End of the block\\n', '// Koniec bloku\\n')
comment('// Error! `short_lived_binding` doesn\'t exist in this scope\\n',
        '// Błąd! `short_lived_binding` nie istnieje w tym zasięgu\\n')
comment('// This binding *shadows* the outer one\\n',
        '// To wiązanie *przesłania* zewnętrzne\\n')
comment('// This binding *shadows* the previous binding\\n',
        '// To wiązanie *przesłania* poprzednie wiązanie\\n')

# declare.md
comment('// Declare a variable binding\\n', '// Deklaruj wiązanie zmiennej\\n')
comment('// Initialize the binding\\n', '// Zainicjalizuj wiązanie\\n')
comment('// Error! Use of uninitialized binding\\n',
        '// Błąd! Użycie niezainicjalizowanego wiązania\\n')

# freeze.md
comment('// Shadowing by immutable `_mutable_integer`\\n',
        '// Przesłanianie przez niemutowalne `_mutable_integer`\\n')
comment('// Error! `_mutable_integer` is frozen in this scope\\n',
        '// Błąd! `_mutable_integer` jest zamrożone w tym zasięgu\\n')
comment('// `_mutable_integer` goes out of scope\\n',
        '// `_mutable_integer` wychodzi poza zasięg\\n')
comment('// Ok! `_mutable_integer` is not frozen in this scope\\n',
        '// Ok! `_mutable_integer` nie jest zamrożone w tym zasięgu\\n')

# ============================================================
# PROZA — JEDNOLINIJKOWA
# ============================================================

prose('Tuple structs, which are, basically, named tuples.',
      'Struktury krotkowe (tuple structs) — w zasadzie nazwane krotki.')
prose('Unit structs, which are field-less, are useful for generics.',
      'Struktury jednostkowe (unit structs) — bez pól, przydatne w typach ogólnych.')
prose('See also', 'Zobacz także')
prose('`enum` can also be used as C-like enums.',
      '`enum` można też używać jako wyliczenia podobne do C.')
prose('Type aliases', 'Aliasy typów')
prose('The most common place you\'ll see this is in `impl` blocks using the `Self` alias.',  # noqa
      'Najczęściej zobaczysz to w blokach `impl` z aliasem `Self`.')
prose('`const`: An unchangeable value (the common case).',
      '`const`: Wartość niezmieniana (typowy przypadek).')
prose('The compiler will throw a detailed diagnostic about mutability errors.',
      'Kompilator wyświetli szczegółową diagnozę dotyczącą błędów mutowalności.')

# ============================================================
# PROZA — WIELOLINIOWA
# ============================================================

# structs.md:3
multi(
    'msgid ""\n'
    '"There are three types of structures (\\"structs\\") that can be created using "\n'
    '"the `struct` keyword:"',
    ['"Można tworzyć trzy typy struktur (\\"struct\\"), używając słowa kluczowego `struct`:"']
)

# structs.md:7 — C structs link
multi(
    'msgid ""\n'
    '"The classic [C structs](https://en.wikipedia.org/wiki/"\n'
    '"Struct_(C_programming_language))"',
    ['"Klasyczne [struktury C](https://en.wikipedia.org/wiki/"\n'
     '"Struct_(C_programming_language))"']
)

# structs.md:91 — rect_area
multi(
    'msgid ""\n'
    '"Add a function `rect_area` which calculates the area of a `Rectangle` (try "\n'
    '"using nested destructuring)."',
    ['"Dodaj funkcję `rect_area` obliczającą pole `Rectangle` (spróbuj "\n'
     '"użyć zagnieżdżonej destrukturyzacji)."']
)

# structs.md:93 — square
multi(
    'msgid ""\n'
    '"Add a function `square` which takes a `Point` and a `f32` as arguments, and "\n'
    '"returns a `Rectangle` with its top left corner on the point, and a width and "\n'
    '"height corresponding to the `f32`."',
    ['"Dodaj funkcję `square`, która przyjmuje `Point` i `f32` jako argumenty "\n'
     '"i zwraca `Rectangle` z lewym górnym rogiem w tym punkcie oraz szerokością "\n'
     '"i wysokością równą `f32`."']
)

# structs.md:99 — attributes link
multi(
    'msgid ""\n'
    '"[`attributes`](../attribute.md), [raw identifiers](../compatibility/"\n'
    '"raw_identifiers.md) and [destructuring](../flow_control/match/destructuring."\n'
    '"md)"',
    ['"[`atrybuty`](../attribute.md), [surowe identyfikatory](../compatibility/"\n'
     '"raw_identifiers.md) i [destrukturyzacja](../flow_control/match/destructuring."\n'
     '"md)"']
)

# enum.md:3
multi(
    'msgid ""\n'
    '"The `enum` keyword allows the creation of a type which may be one of a few "\n'
    '"different variants. Any variant which is valid as a `struct` is also valid "\n'
    '"in an `enum`."',
    ['"Słowo kluczowe `enum` pozwala tworzyć typ, który może być jednym z kilku "\n'
     '"różnych wariantów. Każdy wariant poprawny jako `struct` jest też poprawny "\n'
     '"w `enum`."']
)

# enum.md:8 — multi-line comment
multi(
    'msgid ""\n'
    '"// Create an `enum` to classify a web event. Note how both\\n"\n'
    '"// names and type information together specify the variant:\\n"\n'
    '"// `PageLoad != PageUnload` and `KeyPress(char) != Paste(String)`.\\n"\n'
    '"// Each is different and independent.\\n"',
    ['"// Stwórz `enum` do klasyfikacji zdarzenia sieciowego. Zauważ, że\\n"\n'
     '"// nazwy i informacje o typie razem określają wariant:\\n"\n'
     '"// `PageLoad != PageUnload` i `KeyPress(char) != Paste(String)`.\\n"\n'
     '"// Każdy jest inny i niezależny.\\n"']
)

# enum.md:22 — function comment
multi(
    'msgid ""\n'
    '"// A function which takes a `WebEvent` enum as an argument and\\n"\n'
    '"// returns nothing.\\n"',
    ['"// Funkcja przyjmująca `WebEvent` enum jako argument\\n"\n'
     '"// i nic nie zwracająca.\\n"']
)

# enum.md:58 — type alias description
multi(
    'msgid ""\n'
    '"If you use a type alias, you can refer to each enum variant via its alias. "\n'
    '"This might be useful if the enum\'s name is too long or too generic, and you "\n'
    '"want to rename it."',
    ['"Używając aliasu typu, można odwoływać się do wariantów enum przez alias. "\n'
     '"Przydaje się to, gdy nazwa enum jest zbyt długa lub zbyt ogólna "\n'
     '"i chcemy ją przemianować."']
)

# enum.md:72 — can refer via alias comment
multi(
    'msgid ""\n'
    '"// We can refer to each variant via its alias, not its long and inconvenient\\n"\n'
    '"    // name.\\n"',
    ['"// Możemy odwoływać się do wariantów przez alias, nie przez długą\\n"\n'
     '"    // i niewygodną nazwę.\\n"']
)

# enum.md:96 — stabilization report
multi(
    'msgid ""\n'
    '"To learn more about enums and type aliases, you can read the [stabilization "\n'
    '"report](https://github.com/rust-lang/rust/pull/61682/"\n'
    '"#issuecomment-502472847) from when this feature was stabilized into Rust."',
    ['"Aby dowiedzieć się więcej o wyliczeniach i aliasach typów, przeczytaj "\n'
     '"[raport stabilizacji](https://github.com/rust-lang/rust/pull/61682/"\n'
     '"#issuecomment-502472847) z chwili stabilizacji tej funkcji w Rust."']
)

# enum.md:102 — links
multi(
    'msgid ""\n'
    '"[`match`](../flow_control/match.md), [`fn`](../fn.md), and [`String`](../std/"\n'
    '"str.md), [\\"Type alias enum variants\\" RFC](https://rust-lang.github.io/"\n'
    '"rfcs/2338-type-alias-enum-variants.html)"',
    ['"[`match`](../flow_control/match.md), [`fn`](../fn.md) i [`String`](../std/"\n'
     '"str.md), [RFC \\"Warianty wyliczeń przez alias typu\\"](https://rust-lang.github.io/"\n'
     '"rfcs/2338-type-alias-enum-variants.html)"']
)

# enum_use.md:3
prose('The `use` declaration can be used to avoid typing the full module path to access a name:',  # noqa
      'Deklaracja `use` pozwala uniknąć wpisywania pełnej ścieżki modułu przy dostępie do nazwy:')

# enum_use.md:20 — multi-line comment
multi(
    'msgid ""\n'
    '"// Explicitly `use` each name so they are available without\\n"\n'
    '"    // manual scoping.\\n"',
    ['"// Jawnie użyj `use` dla każdej nazwy, aby były dostępne bez\\n"\n'
     '"    // ręcznego kwalifikowania.\\n"']
)

# enum_use.md:23
prose('// Automatically `use` each name inside `Role`.\\n',
      '// Automatycznie `use` każdej nazwy wewnątrz `Role`.\\n')

# enum_use.md:47 — link
prose('[`match`](../../flow_control/match.md) and [`use`](../../mod/use.md)',
      '[`match`](../../flow_control/match.md) i [`use`](../../mod/use.md)')

# c_like.md:35
prose('[casting](../../types/cast.md)', '[rzutowanie](../../types/cast.md)')

# testcase_linked_list.md:31 — long self comment
multi(
    'msgid ""\n'
    '"// `self` has to be matched, because the behavior of this method\\n"\n'
    '"        // depends on the variant of `self`\\n"\n'
    '"        // `self` has type `&List`, and `*self` has type `List`, matching on "\n'
    '"a\\n"\n'
    '"        // concrete type `T` is preferred over a match on a reference `&T`\\n"\n'
    '"        // after Rust 2018 you can use self here and tail (with no ref) "\n'
    '"below as well,\\n"\n'
    '"        // rust will infer &s and ref tail.\\n"\n'
    '"        // See https://doc.rust-lang.org/edition-guide/rust-2018/ownership-"\n'
    '"and-lifetimes/default-match-bindings.html\\n"',
    ['"// `self` musi zostać dopasowane, bo zachowanie tej metody\\n"\n'
     '"        // zależy od wariantu `self`\\n"\n'
     '"        // `self` ma typ `&List`, a `*self` ma typ `List`; dopasowanie\\n"\n'
     '"        // do konkretnego typu `T` jest preferowane nad referencję `&T`\\n"\n'
     '"        // od Rust 2018 możesz użyć tu self i tail (bez ref),\\n"\n'
     '"        // rust wywnioskuje &s i ref tail.\\n"\n'
     '"        // Zob. https://doc.rust-lang.org/edition-guide/rust-2018/ownership-"\n'
     '"and-lifetimes/default-match-bindings.html\\n"']
)

# testcase_linked_list.md:39 — can't take ownership
multi(
    'msgid ""\n'
    '"// Can\'t take ownership of the tail, because `self` is borrowed;\\n"\n'
    '"            // instead take a reference to the tail\\n"\n'
    '"            // And it\'s a non-tail recursive call which may cause stack "\n'
    '"overflow for long lists.\\n"',
    ['"// Nie można przejąć własności ogona, bo `self` jest pożyczone;\\n"\n'
     '"            // zamiast tego weź referencję do ogona\\n"\n'
     '"            // To nieogonowe wywołanie rekurencyjne, które może przepełnić\\n"\n'
     '"            // stos dla długich list.\\n"']
)

# testcase_linked_list.md:52 — format! comment
multi(
    'msgid ""\n'
    '"// `format!` is similar to `print!`, but returns a heap\\n"\n'
    '"                // allocated string instead of printing to the console\\n"',
    ['"// `format!` jest podobne do `print!`, ale zwraca napis\\n"\n'
     '"                // alokowany na stercie zamiast drukować na konsolę\\n"']
)

# testcase_linked_list.md:80 — link
prose('[`Box`](../../std/box.md) and [methods](../../fn/methods.md)',
      '[`Box`](../../std/box.md) i [metody](../../fn/methods.md)')

# constants.md:3
multi(
    'msgid ""\n'
    '"Rust has two different types of constants which can be declared in any scope "\n'
    '"including global. Both require explicit type annotation:"',
    ['"Rust ma dwa rodzaje stałych, które można deklarować w dowolnym zasięgu, "\n'
     '"w tym globalnym. Obie wymagają jawnej adnotacji typu:"']
)

# constants.md:7 — static
multi(
    'msgid ""\n'
    '"`static`: A possibly mutable variable with [`\'static`](../scope/lifetime/"\n'
    '"static_lifetime.md) lifetime. The static lifetime is inferred and does not "\n'
    '"have to be specified. Accessing or modifying a mutable static variable is "\n'
    '"[`unsafe`](../unsafe.md)."',
    ['"`static`: Potencjalnie mutowalna zmienna z czasem życia [`\'static`](../scope/lifetime/"\n'
     '"static_lifetime.md). Czas życia static jest wnioskowany i nie trzeba go podawać. "\n'
     '"Dostęp lub modyfikacja mutowalnej zmiennej static wymaga [`unsafe`](../unsafe.md)."']
)

# constants.md:37 — RFC link
multi(
    'msgid ""\n'
    '"[The `const`/`static` RFC](https://github.com/rust-lang/rfcs/blob/master/"\n'
    '"text/0246-const-vs-static.md), [`\'static` lifetime](../scope/lifetime/"\n'
    '"static_lifetime.md)"',
    ['"[RFC `const`/`static`](https://github.com/rust-lang/rfcs/blob/master/"\n'
     '"text/0246-const-vs-static.md), [czas życia `\'static`](../scope/lifetime/"\n'
     '"static_lifetime.md)"']
)

# variable_bindings.md:3
multi(
    'msgid ""\n'
    '"Rust provides type safety via static typing. Variable bindings can be type "\n'
    '"annotated when declared. However, in most cases, the compiler will be able "\n'
    '"to infer the type of the variable from the context, heavily reducing the "\n'
    '"annotation burden."',
    ['"Rust zapewnia bezpieczeństwo typów przez statyczne typowanie. Wiązania zmiennych "\n'
     '"mogą mieć adnotację typu przy deklaracji. W większości przypadków kompilator "\n'
     '"wnioskuje typ zmiennej z kontekstu, znacznie zmniejszając liczbę adnotacji."']
)

# variable_bindings.md:8
multi(
    'msgid ""\n'
    '"Values (like literals) can be bound to variables, using the `let` binding."',
    ['"Wartości (np. literały) można wiązać ze zmiennymi za pomocą wiązania `let`."']
)

# variable_bindings.md:23 — compiler warns comment
multi(
    'msgid ""\n'
    '"// The compiler warns about unused variable bindings; these warnings can\\n"\n'
    '"    // be silenced by prefixing the variable name with an underscore\\n"',
    ['"// Kompilator ostrzega przed nieużywanymi wiązaniami zmiennych; ostrzeżenia\\n"\n'
     '"    // można wyciszyć, poprzedzając nazwę zmiennej podkreśleniem\\n"']
)

# variable_bindings.md:28 — FIXME prefix
multi(
    'msgid ""\n'
    '"// FIXME ^ Prefix with an underscore to suppress the warning\\n"\n'
    '"    // Please note that warnings may not be shown in a browser\\n"',
    ['"// FIXME ^ Poprzedź podkreśleniem, aby wyciszyć ostrzeżenie\\n"\n'
     '"    // Uwaga: ostrzeżenia mogą nie być wyświetlane w przeglądarce\\n"']
)

# variable_bindings/mut.md:3
multi(
    'msgid ""\n'
    '"Variable bindings are immutable by default, but this can be overridden using "\n'
    '"the `mut` modifier."',
    ['"Wiązania zmiennych są domyślnie niemutowalne, ale można to zmienić "\n'
     '"modyfikatorem `mut`."']
)

# variable_bindings/scope.md:3
multi(
    'msgid ""\n'
    '"Variable bindings have a scope, and are constrained to live in a _block_. A "\n'
    '"block is a collection of statements enclosed by braces `{}`."',
    ['"Wiązania zmiennych mają zasięg i są ograniczone do życia w _bloku_. "\n'
     '"Blok to zbiór instrukcji ujętych w nawiasy klamrowe `{}`."']
)

# variable_bindings/scope.md:11 — This is a block comment
multi(
    'msgid ""\n'
    '"// This is a block, and has a smaller scope than the main function\\n"',
    ['"// To jest blok o mniejszym zasięgu niż funkcja main\\n"']
)

# variable_bindings/scope.md:20 — Error! comment
multi(
    'msgid ""\n'
    '"// Error! `short_lived_binding` doesn\'t exist in this scope\\n"',
    ['"// Błąd! `short_lived_binding` nie istnieje w tym zasięgu\\n"']
)

# variable_bindings/scope.md:28 — variable shadowing
multi(
    'msgid ""\n'
    '"Also, [variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing) "\n'
    '"is allowed."',
    ['"Dozwolone jest też [przesłanianie zmiennych](https://en.wikipedia.org/wiki/"\n'
     '"Variable_shadowing)."\n']
)

# variable_bindings/declare.md:3
multi(
    'msgid ""\n'
    '"It is possible to declare variable bindings first and initialize them later, "\n'
    '"but all variable bindings must be initialized before they are used: the "\n'
    '"compiler forbids use of uninitialized variable bindings, as it would lead to "\n'
    '"undefined behavior."',
    ['"Można najpierw deklarować wiązania zmiennych, a inicjalizować je później, "\n'
     '"ale wszystkie wiązania muszą być zainicjalizowane przed użyciem: kompilator "\n'
     '"zabrania używania niezainicjalizowanych wiązań, bo prowadziłoby to do "\n'
     '"niezdefiniowanego zachowania."']
)

# variable_bindings/declare.md:5
multi(
    'msgid ""\n'
    '"It is not common to declare a variable binding and initialize it later in "\n'
    '"the function. It is more difficult for a reader to find the initialization "\n'
    '"when initialization is separated from declaration. It is common to declare "\n'
    '"and initialize a variable binding near where the variable will be used."',
    ['"Rzadko praktykuje się deklarowanie wiązania zmiennej i inicjalizowanie jej "\n'
     '"później w funkcji. Czytającemu trudniej znaleźć inicjalizację, gdy jest "\n'
     '"oddzielona od deklaracji. Zwyczajowo deklaruje się i inicjalizuje wiązanie "\n'
     '"blisko miejsca użycia zmiennej."']
)

# variable_bindings/freeze.md:3
multi(
    'msgid ""\n'
    '"When data is bound by the same name immutably, it also _freezes_. _Frozen_ "\n'
    '"data can\'t be modified until the immutable binding goes out of scope:"',
    ['"Gdy dane są wiązane tą samą nazwą niemutowalnie, _zamrażają się_. "\n'
     '"_Zamrożonych_ danych nie można modyfikować, dopóki niemutowalne wiązanie "\n'
     '"nie wyjdzie poza zasięg:"']
)

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
