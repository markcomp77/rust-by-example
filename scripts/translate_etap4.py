#!/usr/bin/env python3
"""Tłumaczenie Etapu 4: Flow of Control."""

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

# if_else.md
lit('{} is negative')
lit('{} is positive')
lit('{} is zero')
lit(', and is a small number, increase ten-fold')
lit(', and is a big number, halve the number')
lit('{} -> {}')

# loop.md
lit("Let's count until infinity!")
lit('three')
lit("OK, that's enough")

# loop/nested.md
lit('Entered the outer loop')
lit('Entered the inner loop')
lit('This point will never be reached')
lit('Exited the outer loop')

# while.md / for.md (shared)
lit('fizzbuzz')
lit('fizz')
lit('buzz')

# for.md
lit('Frank')
lit('Ferris')
lit('There is a rustacean among us!')
lit('Hello {}')
lit('names: {:?}')
lit('Hello')

# match.md
lit('Tell me about {}')
lit('One!')
lit('This is a prime')
lit('A teen')
lit("Ain't special")
lit('Tell me about {:?}')

# match/destructuring/destructure_tuple.md
lit("First is `0`, `y` is {:?}, and `z` is {:?}")
lit("First is `1` and the rest doesn't matter")
lit("last is `2` and the rest doesn't matter")
lit("First is `3`, last is `4`, and the rest doesn't matter")
lit("It doesn't matter what they are")

# match/destructuring/destructure_enum.md
lit('What color is it?')
lit('The color is Red!')
lit('The color is Blue!')
lit('The color is Green!')
lit('Red: {}, green: {}, and blue: {}!')
lit('Hue: {}, saturation: {}, value: {}!')
lit('Hue: {}, saturation: {}, lightness: {}!')
lit('Cyan: {}, magenta: {}, yellow: {}!')
lit('Cyan: {}, magenta: {}, yellow: {}, key (black): {}!')

# match/destructuring/destructure_pointers.md
lit('Got a value via destructuring: {:?}')
lit('Got a value via dereferencing: {:?}')
lit('Got a reference to a value: {:?}')
lit('We added 10. `mut_value`: {:?}')

# match/destructuring/destructure_structures.md
lit('First of x is 1, b = {},  y = {} ')
lit('y is 2, i = {:?}')
lit("y = {}, we don't care about x")
lit('Outside: x0 = {x0:?}, y0 = {y0}')
lit('Nested: nested_x = {nested_x:?}, nested_y = {nested_y:?}')

# match/guard.md
lit('{}C is above 30 Celsius')
lit('{}C is equal to or below 30 Celsius')
lit('{}F is above 86 Fahrenheit')
lit('{}F is equal to or below 86 Fahrenheit')
lit('Zero')
lit('Greater than zero')

# match/binding.md
lit('Tell me what type of person you are')
lit("I haven't celebrated my first birthday yet")
lit("I'm a child of age {:?}")
lit("I'm a teen of age {:?}")
lit("I'm an old person of age {:?}")
lit('The Answer: {}!')
lit('Not interesting... {}')

# if_let.md
lit('This is a really long string and `{:?}`')
lit('Matched {:?}!')
lit("Didn't match a number. Let's go with a letter!")
lit("I don't like letters. Let's go with an emoticon :)!")
lit('a is foobar')
lit('b is foobar')
lit('c is {}')
lit('c is one hundred')

# let_else.md
lit("Can't segment count item pair: '{s}'")
lit("Can't parse integer: '{count_str}'")
lit('3 chairs')
lit('chairs')

# Char literal
apply("msgid \"' '\"\nmsgstr \"\"",
      "msgid \"' '\"\nmsgstr \"' '\"", "' '")

# while_let.md
lit('Greater than 9, quit!')
lit('`i` is `{:?}`. Try again.')

# ============================================================
# JEDNOLINIJKOWE KOMENTARZE
# ============================================================

# if_else.md
comment('// This expression returns an `i32`.\\n',
        '// To wyrażenie zwraca `i32`.\\n')
comment('// This expression must return an `i32` as well.\\n',
        '// To wyrażenie musi też zwrócić `i32`.\\n')
comment('// TODO ^ Try suppressing this expression with a semicolon.\\n',
        '// TODO ^ Spróbuj pominąć to wyrażenie za pomocą średnika.\\n')

# loop.md
comment('// Infinite loop\\n', '// Nieskończona pętla\\n')
comment('// Skip the rest of this iteration\\n',
        '// Pomiń resztę tej iteracji\\n')
comment('// Exit this loop\\n', '// Wyjdź z tej pętli\\n')

# loop/nested.md
comment('// This breaks the outer loop\\n',
        '// To przerywa zewnętrzną pętlę\\n')

# while.md
comment('// A counter variable\\n', '// Zmienna licznika\\n')
comment('// Loop while `n` is less than 101\\n',
        '// Pętluj dopóki `n` < 101\\n')
comment('// Increment counter\\n', '// Zwiększ licznik\\n')

# for.md
comment('// TODO ^ Try deleting the & and matching just \\"Ferris\\"\\n',
        '// TODO ^ Spróbuj usunąć & i dopasować samo \\"Ferris\\"\\n')

# match.md
comment('// TODO ^ Try different values for `number`\\n',
        '// TODO ^ Spróbuj różnych wartości dla `number`\\n')
comment('// Match a single value\\n', '// Dopasuj pojedynczą wartość\\n')
comment('// Match several values\\n', '// Dopasuj kilka wartości\\n')
comment('// Handle the rest of cases\\n', '// Obsłuż pozostałe przypadki\\n')
comment('// Match is an expression too\\n', '// match to też wyrażenie\\n')
comment('// The arms of a match must cover all the possible values\\n',
        '// Ramiona match muszą pokrywać wszystkie możliwe wartości\\n')
comment('// TODO ^ Try commenting out one of these arms\\n',
        '// TODO ^ Spróbuj zakomentować jedno z ramion\\n')

# match/destructuring/destructure_tuple.md
comment('// TODO ^ Try different values for `triple`\\n',
        '// TODO ^ Spróbuj różnych wartości dla `triple`\\n')
comment('// Match can be used to destructure a tuple\\n',
        '// match może destrukturyzować krotki\\n')
comment('// Destructure the second and third elements\\n',
        '// Destrukturyzuj drugi i trzeci element\\n')
comment('// `..` can be used to ignore the rest of the tuple\\n',
        '// `..` ignoruje resztę krotki\\n')
comment('// `_` means don\'t bind the value to a variable\\n',
        '// `_` oznacza: nie wiąż wartości ze zmienną\\n')

# match/destructuring/destructure_enum.md
comment('// TODO ^ Try different variants for `color`\\n',
        '// TODO ^ Spróbuj różnych wariantów dla `color`\\n')
comment('// An `enum` can be destructured using a `match`.\\n',
        '// `enum` można destrukturyzować za pomocą `match`.\\n')
comment('// Don\'t need another arm because all variants have been examined\\n',
        '// Nie potrzeba kolejnego ramienia — wszystkie warianty zostały sprawdzone\\n')

# match/destructuring/destructure_pointers.md
comment('// To avoid the `&`, you dereference before matching.\\n',
        '// Aby uniknąć `&`, wyłuskaj przed dopasowaniem.\\n')
comment('// Use `ref` keyword to create a reference.\\n',
        '// Użyj słowa kluczowego `ref`, aby stworzyć referencję.\\n')
comment('// Use `ref mut` similarly.\\n',
        '// Użyj `ref mut` podobnie.\\n')

# match/destructuring/destructure_structures.md
comment('// Try changing the values in the struct to see what happens\\n',
        '// Spróbuj zmienić wartości w strukturze, aby zobaczyć efekt\\n')
comment('// You do not need a match block to destructure structs:\\n',
        '// Nie potrzebujesz bloku match do destrukturyzacji struktur:\\n')
comment('// Destructuring works with nested structs as well:\\n',
        '// Destrukturyzacja działa też z zagnieżdżonymi strukturami:\\n')

# match/guard.md
comment('// ^ TODO try different values for `temperature`\\n',
        '// ^ TODO spróbuj różnych wartości dla `temperature`\\n')
comment('// The `if condition` part ^ is a guard\\n',
        '// Część `if condition` powyżej ^ to warunek ochronny\\n')

# match/binding.md
comment('// A function `age` which returns a `u32`.\\n',
        '// Funkcja `age` zwracająca `u32`.\\n')
comment('// Nothing bound. Return the result.\\n',
        '// Nic nie powiązane. Zwróć wynik.\\n')
comment('// Match anything else (`None` variant).\\n',
        '// Dopasuj wszystko inne (wariant `None`).\\n')
comment('// Match any other number.\\n',
        '// Dopasuj dowolną inną liczbę.\\n')

# if_let.md
comment('// Make `optional` of type `Option<i32>`\\n',
        '// Ustaw `optional` na typ `Option<i32>`\\n')
comment('// All have type `Option<i32>`\\n',
        '// Wszystkie mają typ `Option<i32>`\\n')
comment('// If you need to specify a failure, use an else:\\n',
        '// Jeśli chcesz obsłużyć brak dopasowania, użyj else:\\n')
comment('// Destructure failed. Change to the failure case.\\n',
        '// Destrukturyzacja nieudana. Przejdź do przypadku błędu.\\n')
comment('// Provide an altered failing condition.\\n',
        '// Podaj zmieniony warunek niepowodzenia.\\n')
comment('// The condition evaluated false. This branch is the default:\\n',
        '// Warunek zwrócił false. Ta gałąź jest domyślna:\\n')
comment('// Our example enum\\n', '// Nasz przykładowy enum\\n')
comment('// Create example variables\\n', '// Utwórz przykładowe zmienne\\n')
comment('// Variable a matches Foo::Bar\\n',
        '// Zmienna a pasuje do Foo::Bar\\n')
comment('// ^-- this causes a compile-time error. Use `if let` instead.\\n',
        '// ^-- to powoduje błąd kompilacji. Użyj zamiast tego `if let`.\\n')
comment('// Binding also works with `if let`\\n',
        '// Wiązanie działa też z `if let`\\n')

# while_let.md
comment('// Repeatedly try this test.\\n',
        '// Powtarzaj to sprawdzenie.\\n')
comment('// If `optional` destructures, evaluate the block.\\n',
        '// Jeśli `optional` się destrukturyzuje, wykonaj blok.\\n')
comment('// ^ Requires 3 indentations!\\n',
        '// ^ Wymaga 3 poziomów wcięcia!\\n')
comment('// Quit the loop when the destructure fails:\\n',
        '// Wyjdź z pętli gdy destrukturyzacja się nie powiedzie:\\n')
comment('// ^ Why should this be required? There must be a better way!\\n',
        '// ^ Dlaczego to jest konieczne? Musi być lepszy sposób!\\n')

# ============================================================
# JEDNOLINIJKOWA PROZA
# ============================================================

prose('Rust provides a `loop` keyword to indicate an infinite loop.',
      'Rust dostarcza słowo kluczowe `loop` oznaczające nieskończoną pętlę.')
prose('for loops', 'Pętle for')
prose('for and iterators', 'for i iteratory')
prose("Let's write FizzBuzz using `for` instead of `while`.",
      'Napiszmy FizzBuzz używając `for` zamiast `while`.')
prose('If you want to count down, you need to use .rev() instead',
      'Jeśli chcesz liczyć wstecz, użyj zamiast tego .rev()')
prose('A `match` block can destructure items in a variety of ways.',
      'Blok `match` może destrukturyzować elementy na różne sposoby.')
prose('An `enum` is destructured similarly:',
      '`enum` jest destrukturyzowany podobnie:')
prose("Similarly, a `struct` can be destructured as shown:",
      'Podobnie `struct` można destrukturyzować w pokazany sposób:')
prose('Tuples can be destructured in a `match` as follows:',
      'Krotki można destrukturyzować w `match` w następujący sposób:')
prose('Dereferencing uses `*`', 'Wyłuskanie używa `*`')
prose('Destructuring uses `&`, `ref`, and `ref mut`',
      'Destrukturyzacja używa `&`, `ref` i `ref mut`')
prose('A `match` _guard_ can be added to filter the arm.',
      'Do ramienia `match` można dodać _warunek ochronny_ (guard), aby je filtrować.')
prose("For some use cases, when matching enums, `match` is awkward. For example:",
      'W niektórych przypadkach, gdy dopasowujemy enum, `match` jest niezgrabny. Na przykład:')
prose("In the same way, `if let` can be used to match any enum value:",
      'Tak samo `if let` można używać do dopasowywania dowolnych wartości enum:')
prose("Would you like a challenge? Fix the following example to use `if let`:",
      'Masz ochotę na wyzwanie? Napraw poniższy przykład, używając `if let`:')
prose('🛈 stable since: rust 1.65', '🛈 dostępne od: rust 1.65')
prose("Using `while let` makes this sequence much nicer:",
      'Użycie `while let` sprawia, że ta sekwencja jest o wiele czytelniejsza:')

# Links/references
prose('[Tuples](../../../primitives/tuples.md)',
      '[Krotki](../../../primitives/tuples.md)')
prose('[Structs](../../../custom_types/structs.md)',
      '[Struktury](../../../custom_types/structs.md)')
prose('[Iterator](../trait/iter.md)', '[Iterator](../trait/iter.md)')
prose('[The ref pattern](../../../scope/borrow/ref.md)',
      '[Wzorzec ref](../../../scope/borrow/ref.md)')
prose('[Tuples](../../primitives/tuples.md) [Enums](../../custom_types/enum.md)',
      '[Krotki](../../primitives/tuples.md) [Wyliczenia](../../custom_types/enum.md)')

# ============================================================
# WIELOLINIOWE
# ============================================================

# if_else.md:3
multi(
    'msgid ""\n'
    '"Branching with `if`\\\\\\\\-`else` is similar to other languages. Unlike many of "\n'
    '"them, the boolean condition doesn\'t need to be surrounded by parentheses, "\n'
    '"and each condition is followed by a block. `if`\\\\\\\\-`else` conditionals are "\n'
    '"expressions, and, all branches must return the same type."',
    '"Rozgałęzianie z `if`\\\\-`else` jest podobne do innych języków. W odróżnieniu "\n'
    '"od wielu z nich, warunek logiczny nie musi być otoczony nawiasami, "\n'
    '"a każdy warunek jest poprzedzony blokiem. Wyrażenia `if`\\\\-`else` to "\n'
    '"wyrażenia, więc wszystkie gałęzie muszą zwracać ten sam typ."'
)

# if_else.md:33 — multi-line comment
multi(
    'msgid ""\n'
    '"//   ^ Don\'t forget to put a semicolon here! All `let` bindings need it.\\n"',
    '"//   ^ Nie zapomnij wstawić tu średnika! Wszystkie wiązania `let` go wymagają.\\n"'
)

# loop.md:5
multi(
    'msgid ""\n'
    '"The `break` statement can be used to exit a loop at anytime, whereas the "\n'
    '"`continue` statement can be used to skip the rest of the iteration and start "\n'
    '"a new one."',
    '"Instrukcja `break` umożliwia wyjście z pętli w dowolnym momencie, "\n'
    '"a `continue` pozwala pominąć resztę bieżącej iteracji i rozpocząć nową."'
)

# loop/nested.md:3
apply(
    "msgid \"\"\n"
    "\"It's possible to `break` or `continue` outer loops when dealing with nested \"\n"
    "\"loops. In these cases, the loops must be annotated with some `'label`, and \"\n"
    "\"the label must be passed to the `break`/`continue` statement.\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"It's possible to `break` or `continue` outer loops when dealing with nested \"\n"
    "\"loops. In these cases, the loops must be annotated with some `'label`, and \"\n"
    "\"the label must be passed to the `break`/`continue` statement.\"\n"
    "msgstr \"\"\n"
    "\"Przy zagnieżdżonych pętlach możliwe jest `break` lub `continue` pętli zewnętrznych. \"\n"
    "\"W takich przypadkach pętle muszą być opatrzone etykietą `'etykieta`, \"\n"
    "\"którą przekazuje się do instrukcji `break`/`continue`.\"",
    'nested loops break/continue'
)

# loop/nested.md:17 — this would break only inner loop
multi(
    'msgid ""\n'
    '"// This would break only the inner loop\\n"\n'
    '"            //break;\\n"',
    '"// To przerwałoby tylko wewnętrzną pętlę\\n"\n'
    '"            //break;\\n"'
)

# loop/return.md:3
multi(
    'msgid ""\n'
    '"One of the uses of a `loop` is to retry an operation until it succeeds. If "\n'
    '"the operation returns a value though, you might need to pass it to the rest "\n'
    '"of the code: put it after the `break`, and it will be returned by the `loop` "\n'
    '"expression."',
    '"Jednym z zastosowań `loop` jest ponawianie operacji aż do sukcesu. "\n'
    '"Jeśli operacja zwraca wartość, możesz ją przekazać dalej: umieść ją "\n'
    '"po `break`, a zostanie zwrócona przez wyrażenie `loop`."'
)

# while.md:3
multi(
    'msgid ""\n'
    '"The `while` keyword can be used to run a loop while a condition is true."',
    '"Słowo kluczowe `while` służy do uruchamiania pętli dopóki warunek jest prawdziwy."'
)

# while.md:5
apply(
    "msgid \"\"\n"
    "\"Let's write the infamous [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) \"\n"
    "\"using a `while` loop.\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"Let's write the infamous [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) \"\n"
    "\"using a `while` loop.\"\n"
    "msgstr \"\"\n"
    "\"Napiszmy słynną grę [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) \"\n"
    "\"używając pętli `while`.\"",
    'FizzBuzz while'
)

# for.md:5
multi(
    'msgid ""\n'
    '"The `for in` construct can be used to iterate through an `Iterator`. One of "\n'
    '"the easiest ways to create an iterator is to use the range notation `a..b`. "\n'
    '"This yields values from `a` (inclusive) to `b` (exclusive) in steps of one."',
    '"Konstrukcja `for in` służy do iterowania przez `Iterator`. Jednym "\n'
    '"z najprostszych sposobów tworzenia iteratora jest zakres `a..b`, który "\n'
    '"generuje wartości od `a` (włącznie) do `b` (wyłącznie) co jedną."'
)

# for.md:14 — n will take values
multi(
    'msgid ""\n'
    '"// `n` will take the values: 1, 2, ..., 100 in each iteration\\n"',
    '"// `n` przyjmie wartości: 1, 2, ..., 100 w każdej iteracji\\n"'
)

# for.md:29 — Alternatively a..=b
multi(
    'msgid ""\n'
    '"Alternatively, `a..=b` can be used for a range that is inclusive on both "\n'
    '"ends. The above can be written as:"',
    '"Alternatywnie `a..=b` można użyć dla zakresu włączającego oba końce. "\n'
    '"Powyższy przykład można zapisać jako:"'
)

# for.md:49 — Just remember
multi(
    'msgid ""\n'
    '"Just remember that even though you can compile the code when a>b, the loop "\n'
    '"gets never executed."',
    '"Pamiętaj, że choć kod kompiluje się gdy a>b, pętla nigdy nie zostanie wykonana."'
)

# for.md:64 — for in interact with Iterator
multi(
    'msgid ""\n'
    '"The `for in` construct is able to interact with an `Iterator` in several "\n'
    '"ways. As discussed in the section on the [Iterator](../trait/iter.md) trait, "\n'
    '"by default the `for` loop will apply the `into_iter` function to the "\n'
    '"collection. However, this is not the only means of converting collections "\n'
    '"into iterators."',
    '"Konstrukcja `for in` może współdziałać z `Iterator` na kilka sposobów. "\n'
    '"Jak opisano w sekcji o cesze [Iterator](../trait/iter.md), domyślnie "\n'
    '"pętla `for` stosuje funkcję `into_iter` do kolekcji. Nie jest to jednak "\n'
    '"jedyny sposób konwersji kolekcji na iteratory."'
)

# for.md:69 — into_iter, iter, iter_mut all handle
multi(
    'msgid ""\n'
    '"`into_iter`, `iter` and `iter_mut` all handle the conversion of a collection "\n'
    '"into an iterator in different ways, by providing different views on the data "\n'
    '"within."',
    '"`into_iter`, `iter` i `iter_mut` obsługują konwersję kolekcji na iterator "\n'
    '"na różne sposoby, oferując różne widoki na dane wewnątrz."'
)

# for.md:73 — iter borrows
multi(
    'msgid ""\n'
    '"`iter` - This borrows each element of the collection through each iteration. "\n'
    '"Thus leaving the collection untouched and available for reuse after the loop."',
    '"`iter` — pożycza każdy element kolekcji w każdej iteracji, "\n'
    '"pozostawiając kolekcję niezmienioną i dostępną do ponownego użycia po pętli."'
)

# for.md:92 — into_iter consumes
apply(
    "msgid \"\"\n"
    "\"`into_iter` - This consumes the collection so that on each iteration the \"\n"
    "\"exact data is provided. Once the collection has been consumed it is no \"\n"
    "\"longer available for reuse as it has been 'moved' within the loop.\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"`into_iter` - This consumes the collection so that on each iteration the \"\n"
    "\"exact data is provided. Once the collection has been consumed it is no \"\n"
    "\"longer available for reuse as it has been 'moved' within the loop.\"\n"
    "msgstr \"\"\n"
    "\"`into_iter` — konsumuje kolekcję, dostarczając w każdej iteracji właściwe dane. \"\n"
    "\"Po skonsumowaniu kolekcja nie jest już dostępna, bo została 'przeniesiona' \"\n"
    "\"wewnątrz pętli.\"",
    'into_iter consumes'
)

# for.md:107 — names has been moved
multi(
    'msgid ""\n'
    '"// `names` has been \'moved\' and can no longer be used.\\n"\n'
    '"    // Try uncommenting the line below to see the compiler error:\\n"\n'
    '"    // println!(\\"names: {:?}\\", names);\\n"',
    '"// `names` zostało \'przeniesione\' i nie można go już używać.\\n"\n'
    '"    // Spróbuj odkomentować linię poniżej, aby zobaczyć błąd kompilatora:\\n"\n'
    '"    // println!(\\"names: {:?}\\", names);\\n"'
)

# for.md:113 — iter_mut mutably borrows
multi(
    'msgid ""\n'
    '"`iter_mut` - This mutably borrows each element of the collection, allowing "\n'
    '"for the collection to be modified in place."',
    '"`iter_mut` — mutowalnie pożycza każdy element kolekcji, umożliwiając "\n'
    '"jej modyfikację w miejscu."'
)

# for.md:131 — above snippets note type
multi(
    'msgid ""\n'
    '"In the above snippets note the type of `match` branch, that is the key "\n'
    '"difference in the types of iteration. The difference in type then of course "\n'
    '"implies differing actions that are able to be performed."',
    '"W powyższych fragmentach zwróć uwagę na typ ramienia `match` — to kluczowa "\n'
    '"różnica między typami iteracji. Różnica typów implikuje oczywiście "\n'
    '"różne możliwe do wykonania operacje."'
)

# match.md:3
multi(
    'msgid ""\n'
    '"Rust provides pattern matching via the `match` keyword, which can be used "\n'
    '"like a C `switch`. The first matching arm is evaluated and all possible "\n'
    '"values must be covered."',
    '"Rust dostarcza dopasowywanie wzorców przez słowo kluczowe `match`, które "\n'
    '"działa jak `switch` w C. Pierwsze pasujące ramię jest ewaluowane i wszystkie "\n'
    '"możliwe wartości muszą być pokryte."'
)

# match.md:18 — TODO Try adding 13
multi(
    'msgid ""\n'
    '"// TODO ^ Try adding 13 to the list of prime values\\n"\n'
    '"        // Match an inclusive range\\n"',
    '"// TODO ^ Spróbuj dodać 13 do listy liczb pierwszych\\n"\n'
    '"        // Dopasuj zakres włączający\\n"'
)

# match.md:23 — TODO commenting out catch-all
multi(
    'msgid ""\n'
    '"// TODO ^ Try commenting out this catch-all arm\\n"',
    '"// TODO ^ Spróbuj zakomentować to ramię catch-all\\n"'
)

# match.md:29 — arms must cover
multi(
    'msgid ""\n'
    '"// The arms of a match must cover all the possible values\\n"',
    '"// Ramiona match muszą pokrywać wszystkie możliwe wartości\\n"'
)

# match.md:32 — TODO commenting out one arm
multi(
    'msgid ""\n'
    '"// TODO ^ Try commenting out one of these arms\\n"',
    '"// TODO ^ Spróbuj zakomentować jedno z tych ramion\\n"'
)

# destructuring.md links
prose('[Destructuring Tuples](destructuring/destructure_tuple.md)',
      '[Destrukturyzacja krotek](destructuring/destructure_tuple.md)')
prose('[Destructuring Arrays and Slices](destructuring/destructure_slice.md)',
      '[Destrukturyzacja tablic i wycinków](destructuring/destructure_slice.md)')
prose('[Destructuring Enums](destructuring/destructure_enum.md)',
      '[Destrukturyzacja wyliczeń](destructuring/destructure_enum.md)')
prose('[Destructuring Pointers](destructuring/destructure_pointers.md)',
      '[Destrukturyzacja wskaźników](destructuring/destructure_pointers.md)')
prose('[Destructuring Structures](destructuring/destructure_structures.md)',
      '[Destrukturyzacja struktur](destructuring/destructure_structures.md)')
prose('[The Rust Reference for Destructuring](https://doc.rust-lang.org/reference/patterns.html#r-patterns.destructure)',
      '[Dokumentacja Rust dla destrukturyzacji](https://doc.rust-lang.org/reference/patterns.html#r-patterns.destructure)')

# destructure_enum.md link
multi(
    'msgid ""\n'
    '"`[#[allow(...)]]`(../../../attribute/unused.md), [color models](https://en."\n'
    '"wikipedia.org/wiki/Color_model) and [`enum`](../../../custom_types/enum.md)"',
    '"`[#[allow(...)]]`(../../../attribute/unused.md), [modele kolorów](https://en."\n'
    '"wikipedia.org/wiki/Color_model) i [`enum`](../../../custom_types/enum.md)"'
)

# destructure_pointers.md:3
multi(
    'msgid ""\n'
    '"For pointers, a distinction needs to be made between destructuring and "\n'
    '"dereferencing as they are different concepts which are used differently from "\n'
    '"languages like C/C++."',
    '"Dla wskaźników należy rozróżnić destrukturyzację i wyłuskanie, ponieważ "\n'
    '"to różne koncepcje, stosowane inaczej niż w językach jak C/C++."'
)

# destructure_pointers.md:12 — Assign a reference
multi(
    'msgid ""\n'
    '"// Assign a reference of type `i32`. The `&` signifies there\\n"\n'
    '"    // is a reference being assigned.\\n"',
    '"// Przypisz referencję typu `i32`. `&` oznacza, że\\n"\n'
    '"    // przypisywana jest referencja.\\n"'
)

# destructure_pointers.md:17 — If reference is pattern matched
multi(
    'msgid ""\n'
    '"// If `reference` is pattern matched against `&val`, it results\\n"\n'
    '"        // in a comparison like:\\n"\n'
    '"        // `&i32`\\n"\n'
    '"        // `&val`\\n"\n'
    '"        // ^ We see that if the matching `&`s are dropped, then the `i32`\\n"\n'
    '"        // should be assigned to `val`.\\n"',
    '"// Jeśli `reference` jest dopasowane do wzorca `&val`, daje to\\n"\n'
    '"        // porównanie jak:\\n"\n'
    '"        // `&i32`\\n"\n'
    '"        // `&val`\\n"\n'
    '"        // ^ Widząc że pasujące `&` są usuwane, `i32`\\n"\n'
    '"        // powinno być przypisane do `val`.\\n"'
)

# destructure_pointers.md:26 — avoid the & dereference
multi(
    'msgid ""\n'
    '"// To avoid the `&`, you dereference before matching.\\n"',
    '"// Aby uniknąć `&`, wyłuskaj przed dopasowaniem.\\n"'
)

# destructure_pointers.md:31 — What if you don't start
multi(
    'msgid ""\n'
    '"// What if you don\'t start with a reference? `reference` was a `&`\\n"\n'
    '"    // because the right side was already a reference. This is not\\n"\n'
    '"    // a reference because the right side is not one.\\n"',
    '"// Co jeśli nie zaczniesz od referencji? `reference` było `&`,\\n"\n'
    '"    // bo prawa strona była już referencją. To nie jest\\n"\n'
    '"    // referencja, bo prawa strona nią nie jest.\\n"'
)

# destructure_pointers.md:36 — Rust provides ref
multi(
    'msgid ""\n'
    '"// Rust provides `ref` for exactly this purpose. It modifies the\\n"\n'
    '"    // assignment so that a reference is created for the element; this\\n"\n'
    '"    // reference is assigned.\\n"',
    '"// Rust dostarcza `ref` właśnie do tego celu. Modyfikuje\\n"\n'
    '"    // przypisanie tak, że tworzona jest referencja do elementu;\\n"\n'
    '"    // ta referencja jest przypisywana.\\n"'
)

# destructure_pointers.md:41 — by defining 2 values
multi(
    'msgid ""\n'
    '"// Accordingly, by defining 2 values without references, references\\n"\n'
    '"    // can be retrieved via `ref` and `ref mut`.\\n"',
    '"// Odpowiednio, definiując 2 wartości bez referencji, referencje\\n"\n'
    '"    // można uzyskać przez `ref` i `ref mut`.\\n"'
)

# destructure_pointers.md:54 — Got a reference. Gotta dereference
multi(
    'msgid ""\n'
    '"// Got a reference. Gotta dereference it before we can\\n"\n'
    '"            // add anything to it.\\n"',
    '"// Mamy referencję. Musimy ją wyłuskać, zanim\\n"\n'
    '"            // będziemy mogli coś do niej dodać.\\n"'
)

# destructure_structures.md:18 — can destructure structs and rename
multi(
    'msgid ""\n'
    '"// you can destructure structs and rename the variables,\\n"\n'
    '"        // the order is not important\\n"',
    '"// można destrukturyzować struktury i zmieniać nazwy zmiennych,\\n"\n'
    '"        // kolejność nie ma znaczenia\\n"'
)

# destructure_structures.md:22 — also ignore some variables
multi(
    'msgid ""\n'
    '"// and you can also ignore some variables:\\n"',
    '"// można też pominąć niektóre zmienne:\\n"'
)

# destructure_structures.md:24 — error pattern does not mention
multi(
    'msgid ""\n'
    '"// this will give an error: pattern does not mention field `x`\\n"\n'
    '"        //Foo { y } => println!(\\"y = {}\\", y),\\n"',
    '"// to da błąd: wzorzec nie wymienia pola `x`\\n"\n'
    '"        //Foo { y } => println!(\\"y = {}\\", y),\\n"'
)

# match/guard.md:27
apply(
    "msgid \"\"\n"
    "\"Note that the compiler won't take guard conditions into account when \"\n"
    "\"checking if all patterns are covered by the match expression.\"\n"
    "msgstr \"\"",
    "msgid \"\"\n"
    "\"Note that the compiler won't take guard conditions into account when \"\n"
    "\"checking if all patterns are covered by the match expression.\"\n"
    "msgstr \"\"\n"
    "\"Kompilator nie bierze warunków ochronnych pod uwagę podczas sprawdzania, \"\n"
    "\"czy wyrażenie match pokrywa wszystkie wzorce.\"",
    'guard conditions not covered'
)

# match/guard.md:37 — unreachable comment
multi(
    'msgid ""\n'
    '"// _ => unreachable!(\\"Should never happen.\\"),\\n"\n'
    '"        // TODO ^ uncomment to fix compilation\\n"',
    '"// _ => unreachable!(\\"Nie powinno się zdarzyć.\\"),\\n"\n'
    '"        // TODO ^ odkomentuj, aby naprawić kompilację\\n"'
)

# match/guard.md links
multi(
    'msgid ""\n'
    '"[Tuples](../../primitives/tuples.md) [Enums](../../custom_types/enum.md)"',
    '"[Krotki](../../primitives/tuples.md) [Wyliczenia](../../custom_types/enum.md)"'
)

# match/binding.md:3
multi(
    'msgid ""\n'
    '"Indirectly accessing a variable makes it impossible to branch and use that "\n'
    '"variable without re-binding. `match` provides the `@` sigil for binding "\n'
    '"values to names:"',
    '"Pośredni dostęp do zmiennej uniemożliwia rozgałęzienie i użycie jej "\n'
    '"bez ponownego powiązania. `match` dostarcza symbol `@` do wiązania "\n'
    '"wartości z nazwami:"'
)

# match/binding.md:18 — Could match 1..=12 comment
multi(
    'msgid ""\n'
    '"// Could `match` 1 ..= 12 directly but then what age\\n"\n'
    '"        // would the child be?\\n"\n'
    '"        // Could `match` n and use an `if` guard, but would\\n"\n'
    '"        // not contribute to exhaustiveness checks.\\n"\n'
    '"        // (Although in this case that would not matter since\\n"\n'
    '"        // a \\"catch-all\\" pattern is present at the bottom)\\n"\n'
    '"        // Instead, bind to `n` for the sequence of 1 ..= 12.\\n"\n'
    '"        // Now the age can be reported.\\n"',
    '"// Można dopasować `match` 1 ..= 12 bezpośrednio, ale jaki wiek\\n"\n'
    '"        // miałoby dziecko?\\n"\n'
    '"        // Można dopasować n i użyć warunku `if`, ale to nie\\n"\n'
    '"        // przyczyni się do sprawdzania wyczerpania.\\n"\n'
    '"        // (Choć w tym przypadku to nie ma znaczenia, bo\\n"\n'
    '"        // wzorzec \\"catch-all\\" jest obecny na dole)\\n"\n'
    '"        // Zamiast tego powiąż `n` z sekwencją 1 ..= 12.\\n"\n'
    '"        // Teraz można podać wiek.\\n"'
)

# match/binding.md:28 — similar binding for several values
multi(
    'msgid ""\n'
    '"// A similar binding can be done when matching several values.\\n"',
    '"// Podobne wiązanie można zastosować przy dopasowaniu kilku wartości.\\n"'
)

# match/binding.md:30 — nothing bound
multi(
    'msgid ""\n'
    '"// Nothing bound. Return the result.\\n"',
    '"// Nic nie powiązane. Zwróć wynik.\\n"'
)

# match/binding.md:36 — You can also use binding
multi(
    'msgid ""\n'
    '"You can also use binding to \\"destructure\\" `enum` variants, such as "\n'
    '"`Option`:"',
    '"Można też używać wiązania do \\"destrukturyzowania\\" wariantów `enum`, "\n'
    '"takich jak `Option`:"'
)

# match/binding.md:45 — Got Some variant
multi(
    'msgid ""\n'
    '"// Got `Some` variant, match if its value, bound to `n`,\\n"\n'
    '"        // is equal to 42.\\n"\n'
    '"        // Could also use `Some(42)` and print `\\"The Answer: 42!\\"`\\n"\n'
    '"        // but that would require changing `42` in 2 spots should\\n"\n'
    '"        // you ever wish to change it.\\n"\n'
    '"        // Could also use `Some(n) if n == 42` and print `\\"The Answer: {n}!\\"`,\\n"\n'  # noqa (no actual backslash escape issue)
    '"        // but that would not contribute to exhaustiveness checks.\\n"\n'
    '"        // (Although in this case that would not matter since\\n"\n'
    '"        // the next arm is a \\"catch-all\\" pattern)\\n"',
    '"// Mamy wariant `Some`, dopasuj jeśli jego wartość powiązana z `n`,\\n"\n'
    '"        // jest równa 42.\\n"\n'
    '"        // Można użyć `Some(42)` i drukować `\\"The Answer: 42!\\"`,\\n"\n'
    '"        // ale to wymagałoby zmiany `42` w 2 miejscach.\\n"\n'
    '"        // Można użyć `Some(n) if n == 42` i drukować `\\"The Answer: {n}!\\"`,\\n"\n'
    '"        // ale to nie przyczyni się do sprawdzania wyczerpania.\\n"\n'
    '"        // (Choć w tym przypadku to nie ma znaczenia, bo\\n"\n'
    '"        // następne ramię jest wzorcem \\"catch-all\\")\\n"'
)

# match/binding.md links
multi(
    'msgid ""\n'
    '"`[functions]`(../../fn.md), [`enums`](../../custom_types/enum.md) and "\n'
    '"`[Option]`(../../std/option.md)"',
    '"`[funkcje]`(../../fn.md), [`wyliczenia`](../../custom_types/enum.md) i "\n'
    '"`[Option]`(../../std/option.md)"'
)

# if_let.md:12 — Required because match is exhaustive
multi(
    'msgid ""\n'
    '"// ^ Required because `match` is exhaustive. Doesn\'t it seem\\n"\n'
    '"    // like wasted space?\\n"',
    '"// ^ Wymagane, bo `match` jest wyczerpujący. Czy to nie wygląda\\n"\n'
    '"    // jak zmarnowane miejsce?\\n"'
)

# if_let.md:18 — if let is cleaner
multi(
    'msgid ""\n'
    '"`if let` is cleaner for this use case and in addition allows various failure "\n'
    '"options to be specified:"',
    '"`if let` jest czystszy w tym przypadku i dodatkowo pozwala określić "\n'
    '"różne opcje dla przypadku braku dopasowania:"'
)

# if_let.md:28 — The if let construct reads
multi(
    'msgid ""\n'
    '"// The `if let` construct reads: \\"if `let` destructures `number` into\\n"\n'
    '"    // `Some(i)`, evaluate the block (`{}`).\\n"',
    '"// Konstrukcja `if let` czyta się: \\"jeśli `let` destrukturyzuje `number\\"\\n"\n'
    '"    // na `Some(i)`, wykonaj blok (`{}`).\\n"'
)

# if_let.md:47 — Destructure failed evaluate else if
multi(
    'msgid ""\n'
    '"// Destructure failed. Evaluate an `else if` condition to see if the\\n"\n'
    '"    // alternate failure branch should be taken:\\n"',
    '"// Destrukturyzacja nieudana. Sprawdź warunek `else if`, aby zobaczyć czy\\n"\n'
    '"    // gałąź alternatywna powinna być wybrana:\\n"'
)

# if_let.md:52 — condition evaluated false
multi(
    'msgid ""\n'
    '"// The condition evaluated false. This branch is the default:\\n"',
    '"// Warunek zwrócił false. Ta gałąź jest domyślna:\\n"'
)

# if_let.md:79 — b does not match
multi(
    'msgid ""\n'
    '"// Variable b does not match Foo::Bar\\n"\n'
    '"    // So this will print nothing\\n"',
    '"// Zmienna b nie pasuje do Foo::Bar\\n"\n'
    '"    // Więc to nic nie wydrukuje\\n"'
)

# if_let.md:85 — c matches Foo::Qux
multi(
    'msgid ""\n'
    '"// Variable c matches Foo::Qux which has a value\\n"\n'
    '"    // Similar to Some() in the previous example\\n"',
    '"// Zmienna c pasuje do Foo::Qux, która ma wartość\\n"\n'
    '"    // Podobnie do Some() w poprzednim przykładzie\\n"'
)

# if_let.md:98 — Another benefit
multi(
    'msgid ""\n'
    '"Another benefit is that `if let` allows us to match non-parameterized enum "\n'
    '"variants. This is true even in cases where the enum doesn\'t implement or "\n'
    '"derive `PartialEq`. In such cases `if Foo::Bar == a` would fail to compile, "\n'
    '"because instances of the enum cannot be equated, however `if let` will "\n'
    '"continue to work."',
    '"Kolejną korzyścią jest to, że `if let` pozwala dopasowywać nieparametryzowane "\n'
    '"warianty enum. Dotyczy to nawet przypadków, gdy enum nie implementuje ani nie "\n'
    '"wyprowadza `PartialEq`. W takich przypadkach `if Foo::Bar == a` nie skompiluje "\n'
    '"się, bo instancji enum nie można porównywać, ale `if let` nadal działa."'
)

# if_let.md:103 — enum purposely neither
multi(
    'msgid ""\n'
    '"// This enum purposely neither implements nor derives PartialEq.\\n"\n'
    '"// That is why comparing Foo::Bar == a fails below.\\n"',
    '"// Ten enum celowo nie implementuje ani nie wyprowadza PartialEq.\\n"\n'
    '"// Dlatego porównanie Foo::Bar == a kończy się niepowodzeniem poniżej.\\n"'
)

# if_let.md links
multi(
    'msgid ""\n'
    '"`[enum]`(../custom_types/enum.md), [`Option`](../std/option.md), and the "\n'
    '"`[RFC]`(https://github.com/rust-lang/rfcs/pull/160)"',
    '"`[enum]`(../custom_types/enum.md), [`Option`](../std/option.md) i "\n'
    '"`[RFC]`(https://github.com/rust-lang/rfcs/pull/160)"'
)

# let_else.md:5
prose('🛈 you can target specific edition by compiling like this `rustc --edition=2021 main.rs`',
      '🛈 możesz targetować konkretną edycję kompilując tak: `rustc --edition=2021 main.rs`')

# let_else.md:8
apply(
    'msgid ""\n'
    '"With `let`\\\\\\\\-`else`, a refutable pattern can match and bind variables in the "\n'
    '"surrounding scope like a normal `let`, or else diverge (e.g. `break`, "\n'
    '"`return`, `panic!`) when the pattern doesn\'t match."\n'
    'msgstr ""',
    'msgid ""\n'
    '"With `let`\\\\\\\\-`else`, a refutable pattern can match and bind variables in the "\n'
    '"surrounding scope like a normal `let`, or else diverge (e.g. `break`, "\n'
    '"`return`, `panic!`) when the pattern doesn\'t match."\n'
    'msgstr ""\n'
    '"Dzięki `let`\\\\-`else` wzorzec obalający może dopasować i powiązać zmienne w "\n'
    '"otaczającym zasięgu jak normalne `let`, lub rozejść się (np. `break`, "\n'
    '"`return`, `panic!`) gdy wzorzec nie pasuje."',
    'let-else refutable pattern'
)

# let_else.md:31
apply(
    'msgid ""\n'
    '"The scope of name bindings is the main thing that makes this different from "\n'
    '"`match` or `if let`\\\\\\\\-`else` expressions. You could previously approximate "\n'
    '"these patterns with an unfortunate bit of repetition and an outer `let`:"\n'
    'msgstr ""',
    'msgid ""\n'
    '"The scope of name bindings is the main thing that makes this different from "\n'
    '"`match` or `if let`\\\\\\\\-`else` expressions. You could previously approximate "\n'
    '"these patterns with an unfortunate bit of repetition and an outer `let`:"\n'
    'msgstr ""\n'
    '"Zasięg wiązań nazw to główna różnica w stosunku do wyrażeń `match` lub "\n'
    '"`if let`\\\\-`else`. Wcześniej można było przybliżyć te wzorce niefortunnymi "\n'
    '"powtórzeniami i zewnętrznym `let`:"',
    'scope of name bindings'
)

# let_else.md:57
multi(
    'msgid ""\n'
    '"[option](../std/option.md), [match](./match.md), [if let](./if_let.md) and "\n'
    '"the [let-else RFC](https://rust-lang.github.io/rfcs/3137-let-else.html)."',
    '"[option](../std/option.md), [match](./match.md), [if let](./if_let.md) i "\n'
    '"[RFC let-else](https://rust-lang.github.io/rfcs/3137-let-else.html)."'
)

# while_let.md:3
multi(
    'msgid ""\n'
    '"Similar to `if let`, `while let` can make awkward `match` sequences more "\n'
    '"tolerable. Consider the following sequence that increments `i`:"',
    '"Podobnie do `if let`, `while let` może uczynić niezgrabne sekwencje `match` "\n'
    '"bardziej znośnymi. Rozważ następującą sekwencję zwiększającą `i`:"'
)

# while_let.md:38 — This reads: while let
multi(
    'msgid ""\n'
    '"// This reads: \\"while `let` destructures `optional` into\\n"\n'
    '"    // `Some(i)`, evaluate the block (`{}`). Else `break`.\\n"',
    '"// Czyta się: \\"dopóki `let` destrukturyzuje `optional` na\\n"\n'
    '"    // `Some(i)`, wykonuj blok (`{}`). W przeciwnym razie `break`.\\n"'
)

# while_let.md:48 — Less rightward drift
multi(
    'msgid ""\n'
    '"// ^ Less rightward drift and doesn\'t require\\n"\n'
    '"        // explicitly handling the failing case.\\n"',
    '"// ^ Mniej dryfu w prawo i nie wymaga\\n"\n'
    '"        // jawnej obsługi przypadku braku dopasowania.\\n"'
)

# while_let.md:51 — if let had additional
multi(
    'msgid ""\n'
    '"// ^ `if let` had additional optional `else`/`else if`\\n"\n'
    '"    // clauses. `while let` does not have these.\\n"',
    '"// ^ `if let` miał opcjonalne klauzule `else`/`else if`.\\n"\n'
    '"    // `while let` ich nie posiada.\\n"'
)

# while_let.md links
multi(
    'msgid ""\n'
    '"`[enum]`(../custom_types/enum.md), [`Option`](../std/option.md), and the "\n'
    '"`[RFC]`(https://github.com/rust-lang/rfcs/pull/214)"',
    '"`[enum]`(../custom_types/enum.md), [`Option`](../std/option.md) i "\n'
    '"`[RFC]`(https://github.com/rust-lang/rfcs/pull/214)"'
)

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
