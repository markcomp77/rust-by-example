#!/usr/bin/env python3
# Etap 7b: poprawki NIE z etap7 + pominięte wpisy

text = open('po/pl.po').read()
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

def prose(en, pl):
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{pl}"'
    apply(old, new, en[:40])

def comment(en, pl):
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{pl}"'
    apply(old, new, en[:40])

def verbatim(en):
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{en}"'
    apply(old, new, en[:40])

def multi(old_body, new_msgstr):
    old = old_body + 'msgstr ""'
    new = old_body + 'msgstr ""\n' + new_msgstr
    apply(old, new, old_body[8:48])

# ─── scope/move.md ─────────────────────────────────────────────────────────

# move.md:49 — multi-line format (not single-line)
multi(
    'msgid ""\n'
    '"// This function takes ownership of the heap allocated memory from `b`\\n"\n',
    '"// Ta funkcja przejmuje własność pamięci na stercie od `b`\\n"\n'
)

# move.md:52 — different line wrap: "compiler\\n" on separate line
multi(
    'msgid ""\n'
    '"// Since the heap memory has been freed at this point, this action would\\n"\n'
    '"    // result in dereferencing freed memory, but it\'s forbidden by the "\n'
    '"compiler\\n"\n'
    '"    // Error! Same reason as the previous Error\\n"\n'
    '"    //println!(\\"b contains: {}\\", b);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Ponieważ pamięć na stercie została już w tym miejscu zwolniona,\\n"\n'
    '"    // ta akcja spowodowałaby wyłuskanie zwolnionej pamięci,\\n"\n'
    '"    // co jest zabronione przez kompilator\\n"\n'
    '"    // Błąd! Taki sam powód jak poprzedni błąd\\n"\n'
    '"    //println!(\\"b contains: {}\\", b);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# ─── scope/move/partial_move.md ────────────────────────────────────────────

# partial_move.md:22 — has "TODO ^ Try uncommenting these lines\\n" not "//\\n"
multi(
    'msgid ""\n'
    '"// Error! cannot move out of a type which implements the `Drop` trait\\n"\n'
    '"    //impl Drop for Person {\\n"\n'
    '"    //    fn drop(&mut self) {\\n"\n'
    '"    //        println!(\\"Dropping the person struct {:?}\\", self)\\n"\n'
    '"    //    }\\n"\n'
    '"    //}\\n"\n'
    '"    // TODO ^ Try uncommenting these lines\\n"\n',
    '"// Błąd! nie można przenieść z typu implementującego cechę `Drop`\\n"\n'
    '"    //impl Drop for Person {\\n"\n'
    '"    //    fn drop(&mut self) {\\n"\n'
    '"    //        println!(\\"Dropping the person struct {:?}\\", self)\\n"\n'
    '"    //    }\\n"\n'
    '"    //}\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować te linie\\n"\n'
)

# partial_move.md:45 — multi-line format
multi(
    'msgid ""\n'
    '"// `person` cannot be used but `person.age` can be used as it is not moved\\n"\n',
    '"// `person` nie można użyć, ale `person.age` można, bo nie zostało przeniesione\\n"\n'
)

# partial_move.md:50 — last line: "from `person.age` without moving it.)" not "from the struct..."
multi(
    'msgid ""\n'
    '"(In this example, we store the `age` variable on the heap to illustrate the "\n'
    '"partial move: deleting `ref` in the above code would give an error as the "\n'
    '"ownership of `person.age` would be moved to the variable `age`. If `Person."\n'
    '"age` were stored on the stack, `ref` would not be required as the definition "\n'
    '"of `age` would copy the data from `person.age` without moving it.)"\n',
    '"(W tym przykładzie przechowujemy zmienną `age` na stercie, aby zilustrować "\n'
    '"częściowe przeniesienie: usunięcie `ref` w powyższym kodzie spowodowałoby "\n'
    '"błąd, ponieważ własność `person.age` zostałaby przeniesiona do zmiennej "\n'
    '"`age`. Gdyby `Person.age` było przechowywane na stosie, `ref` nie byłoby "\n'
    '"wymagane, bo definicja `age` skopiowałaby dane z `person.age` bez przenoszenia.)"\n'
)

# ─── scope/borrow.md ───────────────────────────────────────────────────────

# borrow.md:23 — "readability\\n" on separate continuation line
multi(
    'msgid ""\n'
    '"// Create a boxed i32 in the heap, and an i32 on the stack\\n"\n'
    '"    // Remember: numbers can have arbitrary underscores added for "\n'
    '"readability\\n"\n'
    '"    // 5_i32 is the same as 5i32\\n"\n',
    '"// Utwórz opakowane i32 na stercie i i32 na stosie\\n"\n'
    '"    // Pamiętaj: do liczb można dodawać podkreślenia dla czytelności\\n"\n'
    '"    // 5_i32 to to samo co 5i32\\n"\n'
)

# borrow.md:38 — "in scope.\\n" on separate continuation line
multi(
    'msgid ""\n'
    '"// Error!\\n"\n'
    '"        // Can\'t destroy `boxed_i32` while the inner value is borrowed later "\n'
    '"in scope.\\n"\n',
    '"// Błąd!\\n"\n'
    '"        // Nie można zniszczyć `boxed_i32`, gdy wewnętrzna wartość jest pożyczona później w zakresie.\\n"\n'
)

# borrow.md:48 — multi-line format
multi(
    'msgid ""\n'
    '"// `boxed_i32` can now give up ownership to `eat_box_i32` and be destroyed\\n"\n',
    '"// `boxed_i32` może teraz oddać własność do `eat_box_i32` i zostać zniszczone\\n"\n'
)

# ─── scope/borrow/mut.md ───────────────────────────────────────────────────

# borrow/mut.md:12 — multi-line format
multi(
    'msgid ""\n'
    '"// `&\'static str` is a reference to a string allocated in read only memory\\n"\n',
    '"// `&\'static str` to referencja do łańcucha znaków zaalokowanego w pamięci tylko do odczytu\\n"\n'
)

# borrow/mut.md:22 — "2014\\n" on separate continuation line
multi(
    'msgid ""\n'
    '"// This function takes a reference to a mutable book and changes `year` to "\n'
    '"2014\\n"\n',
    '"// Ta funkcja przyjmuje referencję do mutowalnej książki i zmienia `year` na 2014\\n"\n'
)

# ─── scope/lifetime/explicit.md ────────────────────────────────────────────

# explicit.md:37 — multi-line format
multi(
    'msgid ""\n'
    '"// A function which takes no arguments, but has a lifetime parameter `\'a`.\\n"\n',
    '"// Funkcja, która nie przyjmuje argumentów, ale ma parametr czasu życia `\'a`.\\n"\n'
)

# explicit.md:44 — "shorter\\n" and "one.\\n" on separate continuation lines
multi(
    'msgid ""\n'
    '"// Attempting to use the lifetime `\'a` as an explicit type annotation\\n"\n'
    '"    // inside the function will fail because the lifetime of `&_x` is "\n'
    '"shorter\\n"\n'
    '"    // than that of `_y`. A short lifetime cannot be coerced into a longer "\n'
    '"one.\\n"\n'
    '"    // let _z = longest(x, s);\\n"\n',
    '"// Próba użycia czasu życia `\'a` jako jawnej adnotacji typowej wewnątrz\\n"\n'
    '"    // funkcji się nie powiedzie, bo czas życia `&_x` jest krótszy niż\\n"\n'
    '"    // `_y`. Krótki czas życia nie może być przekształcony na dłuższy.\\n"\n'
    '"    // let _z = longest(x, s);\\n"\n'
)

# explicit.md:66 — multi-line format
multi(
    'msgid ""\n'
    '"[elision](elision.md) implicitly annotates lifetimes and so is different."\n',
    '"[Elizja](elision.md) niejawnie adnotuje czasy życia i dlatego jest inna."\n'
)

# ─── scope/lifetime/fn.md ──────────────────────────────────────────────────

# fn.md:6 — multi-line format
multi(
    'msgid ""\n'
    '"any reference being returned _must_ have the same lifetime as an input or be "\n'
    '"`static`."\n',
    '"każda zwracana referencja _musi_ mieć ten sam czas życia co wejście lub być `static`."\n'
)

# fn.md:35 — last line is "// a reference to invalid data to be returned.\\n" not "// a dangling pointer!\\n"
multi(
    'msgid ""\n'
    '"//fn invalid_output<\'a>() -> &\'a String { &String::from(\\"foo\\") }\\n"\n'
    '"// The above is invalid: `\'a` must live longer than the function.\\n"\n'
    '"// Here, `&String::from(\\"foo\\")` would create a `String`, followed by a\\n"\n'
    '"// reference. Then the data is dropped upon exiting the scope, leaving\\n"\n'
    '"// a reference to invalid data to be returned.\\n"\n',
    '"//fn invalid_output<\'a>() -> &\'a String { &String::from(\\"foo\\") }\\n"\n'
    '"// Powyższe jest nieprawidłowe: `\'a` musi żyć dłużej niż funkcja.\\n"\n'
    '"// Tu `&String::from(\\"foo\\")` tworzy `String`, a następnie referencję.\\n"\n'
    '"// Dane są upuszczane po wyjściu z zakresu, pozostawiając referencję\\n"\n'
    '"// do nieprawidłowych danych do zwrócenia.\\n"\n'
)

# ─── scope/lifetime/lifetime_bounds.md ────────────────────────────────────

# lifetime_bounds.md:7 — single-line format (with _All_ not _all_)
prose('`T: \'a`: _All_ references in `T` must outlive lifetime `\'a`.',
      '`T: \'a`: _Wszystkie_ referencje w `T` muszą przeżyć czas życia `\'a`.')

comment('// Trait to bound with.\\n', '// Cecha do ograniczenia.\\n')
comment('// A generic function which prints using the `Debug` trait.\\n',
        '// Funkcja ogólna drukująca za pomocą cechy `Debug`.\\n')
verbatim('\\"`print`: t is {:?}\\"')
verbatim('\\"`print_ref`: t is {:?}\\"')

# ─── scope/lifetime/lifetime_coercion.md ──────────────────────────────────

# lifetime_coercion.md:14 — "coercion.\\n" on separate continuation line
multi(
    'msgid ""\n'
    '"// `<\'a: \'b, \'b>` reads as lifetime `\'a` is at least as long as `\'b`.\\n"\n'
    '"// Here, we take in an `&\'a i32` and return a `&\'b i32` as a result of "\n'
    '"coercion.\\n"\n',
    '"// `<\'a: \'b, \'b>` czytamy: czas życia `\'a` jest co najmniej tak długi jak `\'b`.\\n"\n'
    '"// Tu przyjmujemy `&\'a i32` i zwracamy `&\'b i32` w wyniku koercji.\\n"\n'
)

comment('// Longer lifetime\\n', '// Dłuższy czas życia\\n')
comment('// Shorter lifetime\\n', '// Krótszy czas życia\\n')
verbatim('\\"The product is {}\\"')
verbatim('\\"{} is the first\\"')

# ─── scope/lifetime/static_lifetime.md ────────────────────────────────────

# static_lifetime.md:7 — single-line comment
comment('// A reference with \'static lifetime:\\n',
        '// Referencja z czasem życia \'static:\\n')

verbatim('\\"hello world\\"')

comment('// \'static as part of a trait bound:\\n',
        '// \'static jako ograniczenie cechy:\\n')

prose('Reference lifetime', 'Czas życia referencji')

prose('Make a constant with the `static` declaration.',
      'Utwórz stałą z deklaracją `static`.')

prose('Make a `string` literal which has type: `&\'static str`.',
      'Utwórz literał `string` o typie: `&\'static str`.')

prose('See the following example for a display of each method:',
      'Zobacz poniższy przykład prezentujący każdą metodę:')

comment('// Make a constant with `\'static` lifetime.\\n',
        '// Utwórz stałą z czasem życia `\'static`.\\n')

comment('// Make a `string` literal and print it:\\n',
        '// Utwórz literał `string` i go wydrukuj:\\n')

verbatim('\\"I\'m in read-only memory\\"')
verbatim('\\"static_string: {}\\"')

comment('// Make an integer to use for `coerce_static`:\\n',
        '// Utwórz liczbę całkowitą do użycia w `coerce_static`:\\n')

comment('// Coerce `NUM` to lifetime of `lifetime_num`:\\n',
        '// Przekształć `NUM` do czasu życia `lifetime_num`:\\n')

verbatim('\\"coerced_static: {}\\"')
verbatim('\\"NUM: {} stays accessible!\\"')

# static_lifetime.md:65 — different text (Box::leak paragraph in actual PO)
multi(
    'msgid ""\n'
    '"Since `\'static` references only need to be valid for the _remainder_ of a "\n'
    '"program\'s life, they can be created while the program is executed. Just to "\n'
    '"demonstrate, the below example uses [`Box::leak`](https://doc.rust-lang.org/"\n'
    '"std/boxed/struct.Box.html#method.leak) to dynamically create `\'static` "\n'
    '"references. In that case it definitely doesn\'t live for the entire duration, "\n'
    '"but only from the leaking point onward."\n',
    '"Ponieważ referencje `\'static` muszą być prawidłowe tylko przez _pozostały_ "\n'
    '"czas działania programu, mogą być tworzone podczas jego wykonywania. Dla "\n'
    '"demonstracji poniższy przykład używa [`Box::leak`](https://doc.rust-lang.org/"\n'
    '"std/boxed/struct.Box.html#method.leak) do dynamicznego tworzenia referencji "\n'
    '"`\'static`. W takim przypadku zdecydowanie nie żyją przez cały czas działania, "\n'
    '"ale tylko od momentu wycieku."\n'
)

prose('Trait bound', 'Ograniczenie cechy')

apply(
    "msgid \"\\\"\\'static value passed in is: {:?}\\\"\"\nmsgstr \"\"",
    "msgid \"\\\"\\'static value passed in is: {:?}\\\"\"\nmsgstr \"\\\"\\'static value passed in is: {:?}\\\"\"",
    "'static value passed in is"
)

comment('// i is owned and contains no references, thus it\'s \'static:\\n',
        '// i jest posiadane i nie zawiera referencji, więc jest \'static:\\n')

prose('The compiler will tell you:', 'Kompilator poinformuje cię:')

verbatim('[`\'static` constants](../../custom_types/constants.md)')

# ─── scope/lifetime/elision.md ─────────────────────────────────────────────

# elision.md:12 — "signatures\\n" on separate continuation line
multi(
    'msgid ""\n'
    '"// `elided_input` and `annotated_input` essentially have identical "\n'
    '"signatures\\n"\n'
    '"// because the lifetime of `elided_input` is inferred by the compiler:\\n"\n',
    '"// `elided_input` i `annotated_input` mają zasadniczo identyczne sygnatury,\\n"\n'
    '"// bo czas życia `elided_input` jest wnioskowany przez kompilator:\\n"\n'
)

verbatim('\\"`elided_input`: {}\\"')
verbatim('\\"`annotated_input`: {}\\"')
verbatim('\\"`elided_pass`: {}\\"')
verbatim('\\"`annotated_pass`: {}\\"')

# ───────────────────────────────────────────────────────────────────────────

open('po/pl.po', 'w').write(text)
print(f'\nŁącznie zmian: {total}')
