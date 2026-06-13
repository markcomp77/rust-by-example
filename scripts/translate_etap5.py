#!/usr/bin/env python3
"""Tłumaczenie Etapu 5: Functions, Modules, Crates."""

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
    old = old_body + 'msgstr ""'
    new = old_body + 'msgstr ""\n' + new_msgstr
    apply(old, new, old_body[8:48])

# ============================================================
# fn.md — FUNCTIONS
# ============================================================

# String literals (verbatim)
lit('Destroying Pair({}, {})')
lit('Rectangle perimeter: {}')
lit('Rectangle area: {}')

# fn.md prose/comments
prose("Let's rewrite FizzBuzz using functions!",
      'Napiszmy FizzBuzz ponownie z użyciem funkcji!')

# fn.md:3
multi(
    'msgid ""\n'
    '"Functions are declared using the `fn` keyword. Its arguments are type "\n'
    '"annotated, just like variables, and, if the function returns a value, the "\n'
    '"return type must be specified after an arrow `->`."\n',
    '"Funkcje deklaruje się słowem kluczowym `fn`. Argumenty mają adnotacje "\n'
    '"typów, tak jak zmienne, a jeśli funkcja zwraca wartość, "\n'
    '"typ zwracany musi być podany po strzałce `->`."\n'
)

# fn.md:7
multi(
    'msgid ""\n'
    '"The final expression in the function will be used as return value. "\n'
    '"Alternatively, the `return` statement can be used to return a value earlier "\n'
    '"from within the function, even from inside loops or `if` statements."\n',
    '"Ostatnie wyrażenie w funkcji będzie użyte jako wartość zwracana. "\n'
    '"Alternatywnie instrukcja `return` może zwrócić wartość wcześniej, "\n'
    '"nawet z wnętrza pętli lub instrukcji `if`."\n'
)

# fn.md:14
multi(
    'msgid ""\n'
    '"// Unlike C/C++, there\'s no restriction on the order of function "\n'
    '"definitions\\n"\n',
    '"// W odróżnieniu od C/C++, kolejność definicji funkcji nie ma znaczenia\\n"\n'
)

comment('// We can use this function here, and define it somewhere later\\n',
        '// Możemy użyć tej funkcji tutaj i zdefiniować ją gdzieś dalej\\n')
comment('// Function that returns a boolean value\\n',
        '// Funkcja zwracająca wartość boolowską\\n')
comment('// Corner case, early return\\n',
        '// Skrajny przypadek, wczesne wyjście\\n')
comment('// This is an expression, the `return` keyword is not necessary here\\n',
        '// To jest wyrażenie, słowo kluczowe `return` nie jest tu potrzebne\\n')

# fn.md:9 — Functions that "don't" return
multi(
    'msgid ""\n'
    '"// Functions that \\"don\'t\\" return a value, actually return the unit type "\n'
    '"`()`\\n"\n',
    '"// Funkcje, które \\"nie zwracają\\" wartości, faktycznie zwracają typ jednostkowy "\n'
    '"`()`\\n"\n'
)

# fn.md:10 — When a function returns ()
multi(
    'msgid ""\n'
    '"// When a function returns `()`, the return type can be omitted from the\\n"\n'
    '"// signature\\n"\n',
    '"// Gdy funkcja zwraca `()`, typ zwracany można pominąć w sygnaturze\\n"\n'
    '"\\n"\n'
)

# ============================================================
# fn/methods.md — METHODS
# ============================================================

prose('Associated functions & Methods',
      'Funkcje skojarzone i metody')

# methods:3
multi(
    'msgid ""\n'
    '"Some functions are connected to a particular type. These come in two forms: "\n'
    '"associated functions, and methods. Associated functions are functions that "\n'
    '"are defined on a type generally, while methods are associated functions that "\n'
    '"are called on a particular instance of a type."\n',
    '"Niektóre funkcje są powiązane z określonym typem. Występują w dwóch formach: "\n'
    '"funkcje skojarzone i metody. Funkcje skojarzone to takie, które są "\n'
    '"zdefiniowane dla danego typu ogólnie, natomiast metody to funkcje skojarzone, "\n'
    '"wywoływane na konkretnej instancji typu."\n'
)

# methods:impl block
multi(
    'msgid ""\n'
    '"// Implementation block, all `Point` associated functions & methods go in "\n'
    '"here\\n"\n',
    '"// Blok implementacji — wszystkie funkcje skojarzone i metody `Point` tu się znajdą\\n"\n'
)

# methods:associated function
multi(
    'msgid ""\n'
    '"// This is an \\"associated function\\" because this function is associated "\n'
    '"with\\n"\n'
    '"    // a particular type, that is, Point.\\n"\n'
    '"    //\\n"\n'
    '"    // Associated functions don\'t need to be called with an instance.\\n"\n'
    '"    // These functions are generally used like constructors.\\n"\n',
    '"// To jest \\"funkcja skojarzona\\", bo jest powiązana\\n"\n'
    '"    // z konkretnym typem, czyli Point.\\n"\n'
    '"    //\\n"\n'
    '"    // Funkcje skojarzone nie wymagają instancji do wywołania.\\n"\n'
    '"    // Są zwykle używane jako konstruktory.\\n"\n'
)

comment('// Another associated function, taking two arguments:\\n',
        '// Kolejna funkcja skojarzona przyjmująca dwa argumenty:\\n')

# methods:This is a method
multi(
    'msgid ""\n'
    '"// This is a method\\n"\n'
    '"    // `&self` is sugar for `self: &Self`, where `Self` is the type of the\\n"\n'
    '"    // caller object. In this case `Self` = `Rectangle`\\n"\n',
    '"// To jest metoda\\n"\n'
    '"    // `&self` to skrót od `self: &Self`, gdzie `Self` to typ obiektu\\n"\n'
    '"    // wywołującego. W tym przypadku `Self` = `Rectangle`\\n"\n'
)

comment('// `self` gives access to the struct fields via the dot operator\\n',
        '// `self` daje dostęp do pól struktury przez operator kropki\\n')

# methods:abs method
multi(
    'msgid ""\n'
    '"// `abs` is a `f64` method that returns the absolute value of the\\n"\n'
    '"        // caller\\n"\n',
    '"// `abs` to metoda `f64` zwracająca wartość bezwzględną\\n"\n'
    '"        // obiektu wywołującego\\n"\n'
)

# methods:requires mutable caller
multi(
    'msgid ""\n'
    '"// This method requires the caller object to be mutable\\n"\n'
    '"    // `&mut self` desugars to `self: &mut Self`\\n"\n',
    '"// Ta metoda wymaga, aby obiekt wywołujący był mutowalny\\n"\n'
    '"    // `&mut self` to skrót od `self: &mut Self`\\n"\n'
)

comment('// `Pair` owns resources: two heap allocated integers\\n',
        '// `Pair` posiada zasoby: dwie liczby całkowite alokowane na stercie\\n')

# methods:consumes the caller
multi(
    'msgid ""\n'
    '"// This method \\"consumes\\" the resources of the caller object\\n"\n'
    '"    // `self` desugars to `self: Self`\\n"\n',
    '"// Ta metoda \\"konsumuje\\" zasoby obiektu wywołującego\\n"\n'
    '"    // `self` to skrót od `self: Self`\\n"\n'
)

comment('// Destructure `self`\\n', '// Destrukturyzuj `self`\\n')
comment('// `first` and `second` go out of scope and get freed\\n',
        '// `first` i `second` wychodzą z zasięgu i są zwalniane\\n')
comment('// Associated functions are called using double colons\\n',
        '// Funkcje skojarzone wywołuje się za pomocą podwójnego dwukropka\\n')

# methods:Methods are called using the dot operator
multi(
    'msgid ""\n'
    '"// Methods are called using the dot operator\\n"\n'
    '"    // Note that the first argument `&self` is implicitly passed, i.e.\\n"\n'
    '"    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`\\n"\n',
    '"// Metody wywołuje się za pomocą operatora kropki\\n"\n'
    '"    // Pierwszy argument `&self` jest przekazywany niejawnie, tj.\\n"\n'
    '"    // `rectangle.perimeter()` === `Rectangle::perimeter(&rectangle)`\\n"\n'
)

# methods:Error! rectangle is immutable
multi(
    'msgid ""\n'
    '"// Error! `rectangle` is immutable, but this method requires a mutable\\n"\n'
    '"    // object\\n"\n'
    '"    //rectangle.translate(1.0, 0.0);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `rectangle` jest niemutowalne, ale ta metoda wymaga mutowalnego\\n"\n'
    '"    // obiektu\\n"\n'
    '"    //rectangle.translate(1.0, 0.0);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

comment('// Okay! Mutable objects can call mutable methods\\n',
        '// OK! Mutowalne obiekty mogą wywoływać mutowalne metody\\n')

# methods:Error! Previous destroy call consumed pair
multi(
    'msgid ""\n'
    '"// Error! Previous `destroy` call \\"consumed\\" `pair`\\n"\n'
    '"    //pair.destroy();\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! Poprzednie wywołanie `destroy` \\"skonsumowało\\" `pair`\\n"\n'
    '"    //pair.destroy();\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# ============================================================
# fn/closures.md — CLOSURES
# ============================================================

# closures.md:3
multi(
    'msgid ""\n'
    '"Closures are functions that can capture the enclosing environment. For "\n'
    '"example, a closure that captures the `x` variable:"\n',
    '"Domknięcia to funkcje, które mogą przechwytywać otaczające środowisko. "\n'
    '"Na przykład domknięcie przechwytujące zmienną `x`:"\n'
)

# closures.md:5
multi(
    'msgid ""\n'
    '"The syntax and capabilities of closures make them very convenient for on the "\n'
    '"fly usage. Calling a closure is exactly like calling a function. However, "\n'
    '"both input and return types _can_ be inferred and input variable names "\n'
    '"_must_ be specified."\n',
    '"Składnia i możliwości domknięć czynią je bardzo wygodnymi do użycia na "\n'
    '"bieżąco. Wywołanie domknięcia jest dokładnie takie jak wywołanie funkcji. "\n'
    '"Jednak typy wejścia i wyjścia _mogą_ być wnioskowane, a nazwy zmiennych "\n'
    '"wejściowych _muszą_ być podane."\n'
)

prose('Other characteristics of closures include:',
      'Inne cechy domknięć obejmują:')
prose('using `||` instead of `()` around input variables.',
      'używanie `||` zamiast `()` wokół zmiennych wejściowych.')

# closures:optional body delimitation
multi(
    'msgid ""\n'
    '"optional body delimitation (`{}`) for a single line expression (mandatory "\n'
    '"otherwise)."\n',
    '"opcjonalne ograniczenie ciała (`{}`) dla wyrażeń jednolinijkowych "\n'
    '"(obowiązkowe w pozostałych przypadkach)."\n'
)

prose('the ability to capture the outer environment variables.',
      'zdolność do przechwytywania zmiennych z zewnętrznego środowiska.')

# closures:regular function can't refer
multi(
    'msgid ""\n'
    '"// A regular function can\'t refer to variables in the enclosing environment\\n"\n'
    '"    //fn function(i: i32) -> i32 { i + outer_var }\\n"\n'
    '"    // TODO: uncomment the line above and see the compiler error. The "\n'
    '"compiler\\n"\n'
    '"    // suggests that we define a closure instead.\\n"\n',
    '"// Zwykła funkcja nie może odwoływać się do zmiennych z otaczającego środowiska\\n"\n'
    '"    //fn function(i: i32) -> i32 { i + outer_var }\\n"\n'
    '"    // TODO: odkomentuj powyższą linię, aby zobaczyć błąd kompilatora.\\n"\n'
    '"compiler\\n"\n'
    '"    // Kompilator sugeruje zdefiniowanie domknięcia.\\n"\n'
)

# closures:anonymous, binding them to references
multi(
    'msgid ""\n'
    '"// Closures are anonymous, here we are binding them to references.\\n"\n'
    '"    // Annotation is identical to function annotation but is optional\\n"\n'
    '"    // as are the `{}` wrapping the body. These nameless functions\\n"\n'
    '"    // are assigned to appropriately named variables.\\n"\n',
    '"// Domknięcia są anonimowe; tu wiążemy je z referencjami.\\n"\n'
    '"    // Adnotacja jest identyczna jak dla funkcji, ale opcjonalna,\\n"\n'
    '"    // podobnie jak `{}` otaczające ciało. Te bezimienne funkcje\\n"\n'
    '"    // są przypisywane do odpowiednio nazwanych zmiennych.\\n"\n'
)

comment('// Call the closures.\\n', '// Wywołaj domknięcia.\\n')

lit('closure_annotated: {}')
lit('closure_inferred: {}')

# closures:type inferred cannot be inferred again
multi(
    'msgid ""\n'
    '"// Once closure\'s type has been inferred, it cannot be inferred again with "\n'
    '"another type.\\n"\n'
    '"    //println!(\\"cannot reuse closure_inferred with another type: {}\\", "\n'
    '"closure_inferred(42i64));\\n"\n'
    '"    // TODO: uncomment the line above and see the compiler error.\\n"\n',
    '"// Po wnioskowaniu o typie domknięcia, nie można ponownie wnioskować\\n"\n'
    '"another type.\\n"\n'
    '"    //println!(\\"cannot reuse closure_inferred with another type: {}\\", "\n'
    '"closure_inferred(42i64));\\n"\n'
    '"    // TODO: odkomentuj powyższą linię, aby zobaczyć błąd kompilatora.\\n"\n'
)

# closures:taking no arguments which returns an i32
multi(
    'msgid ""\n'
    '"// A closure taking no arguments which returns an `i32`.\\n"\n'
    '"    // The return type is inferred.\\n"\n',
    '"// Domknięcie bez argumentów zwracające `i32`.\\n"\n'
    '"    // Typ zwracany jest wnioskowany.\\n"\n'
)

lit('closure returning one: {}')

# ============================================================
# fn/closures/capture.md
# ============================================================

# capture.md:3
multi(
    'msgid ""\n'
    '"Closures are inherently flexible and will do what the functionality requires "\n'
    '"to make the closure work without annotation. This allows capturing to "\n'
    '"flexibly adapt to the use case, sometimes moving and sometimes borrowing. "\n'
    '"Closures can capture variables:"\n',
    '"Domknięcia są z natury elastyczne i dostosowują się do wymagań "\n'
    '"bez adnotacji. Pozwala to na elastyczne przechwytywanie — czasem "\n'
    '"przez przeniesienie, a czasem przez pożyczanie. "\n'
    '"Domknięcia mogą przechwytywać zmienne:"\n'
)

prose('by reference: `&T`', 'przez referencję: `&T`')
prose('by mutable reference: `&mut T`', 'przez mutowalną referencję: `&mut T`')
prose('by value: `T`', 'przez wartość: `T`')

# capture:They preferentially capture
multi(
    'msgid ""\n'
    '"They preferentially capture variables by reference and only go lower when "\n'
    '"required."\n',
    '"Domknięcia preferencyją przechwytują zmienne przez referencję i sięgają "\n'
    '"głębiej tylko gdy jest to konieczne."\n'
)

lit('green')

# capture:closure to print color
multi(
    'msgid ""\n'
    '"// A closure to print `color` which immediately borrows (`&`) `color` and\\n"\n'
    '"    // stores the borrow and closure in the `print` variable. It will "\n'
    '"remain\\n"\n'
    '"    // borrowed until `print` is used the last time.\\n"\n'
    '"    //\\n"\n'
    '"    // `println!` only requires arguments by immutable reference so it "\n'
    '"doesn\'t\\n"\n'
    '"    // impose anything more restrictive.\\n"\n',
    '"// Domknięcie drukujące `color`, które natychmiast pożycza (`&`) `color`\\n"\n'
    '"    // i zapisuje pożyczenie oraz domknięcie w zmiennej `print`. Pozostanie\\n"\n'
    '"    // pożyczone do ostatniego użycia `print`.\\n"\n'
    '"    //\\n"\n'
    '"    // `println!` wymaga jedynie niemutowalnej referencji do argumentów,\\n"\n'
    '"    // więc nie nakłada żadnych dodatkowych ograniczeń.\\n"\n'
)

lit('`color`: {}')
comment('// Call the closure using the borrow.\\n', '// Wywołaj domknięcie przez pożyczenie.\\n')

# capture:color can be borrowed immutably again
multi(
    'msgid ""\n'
    '"// `color` can be borrowed immutably again, because the closure only holds\\n"\n'
    '"    // an immutable reference to `color`.\\n"\n',
    '"// `color` można ponownie pożyczyć niemutowalnie, bo domknięcie\\n"\n'
    '"    // trzyma jedynie niemutowalną referencję do `color`.\\n"\n'
)

comment('// A move or reborrow is allowed after the final use of `print`\\n',
        '// Po ostatnim użyciu `print` dozwolone jest przeniesienie lub ponowne pożyczenie\\n')

# capture:closure to increment count
multi(
    'msgid ""\n'
    '"// A closure to increment `count` could take either `&mut count` or `count`\\n"\n'
    '"    // but `&mut count` is less restrictive so it takes that. Immediately\\n"\n'
    '"    // borrows `count`.\\n"\n'
    '"    //\\n"\n'
    '"    // A `mut` is required on `inc` because a `&mut` is stored inside. "\n'
    '"Thus,\\n"\n'
    '"    // calling the closure mutates `count` which requires a `mut`.\\n"\n',
    '"// Domknięcie inkrementujące `count` mogłoby przyjąć `&mut count` lub `count`,\\n"\n'
    '"    // ale `&mut count` jest mniej restrykcyjne, więc je wybierze. Natychmiast\\n"\n'
    '"    // pożycza `count`.\\n"\n'
    '"    //\\n"\n'
    '"    // `mut` jest wymagane dla `inc`, bo wewnątrz jest `&mut`. Dlatego\\n"\n'
    '"    // wywołanie domknięcia mutuje `count`, co wymaga `mut`.\\n"\n'
)

lit('`count`: {}')
comment('// Call the closure using a mutable borrow.\\n',
        '// Wywołaj domknięcie przez mutowalne pożyczenie.\\n')

# capture:closure still mutably borrows
multi(
    'msgid ""\n'
    '"// The closure still mutably borrows `count` because it is called later.\\n"\n'
    '"    // An attempt to reborrow will lead to an error.\\n"\n'
    '"    // let _reborrow = &count;\\n"\n'
    '"    // ^ TODO: try uncommenting this line.\\n"\n',
    '"// Domknięcie nadal mutowalnie pożycza `count`, bo jest wywoływane później.\\n"\n'
    '"    // Próba ponownego pożyczenia spowoduje błąd.\\n"\n'
    '"    // let _reborrow = &count;\\n"\n'
    '"    // ^ TODO: spróbuj odkomentować tę linię.\\n"\n'
)

# capture:closure no longer needs to borrow
multi(
    'msgid ""\n'
    '"// The closure no longer needs to borrow `&mut count`. Therefore, it is\\n"\n'
    '"    // possible to reborrow without an error\\n"\n',
    '"// Domknięcie nie potrzebuje już pożyczać `&mut count`. Ponowne pożyczenie\\n"\n'
    '"    // jest więc możliwe bez błędu\\n"\n'
)

comment('// A non-copy type.\\n', '// Typ nie-kopiujący.\\n')

# capture:mem::drop requires T
multi(
    'msgid ""\n'
    '"// `mem::drop` requires `T` so this must take by value. A copy type\\n"\n'
    '"    // would copy into the closure leaving the original untouched.\\n"\n'
    '"    // A non-copy must move and so `movable` immediately moves into\\n"\n'
    '"    // the closure.\\n"\n',
    '"// `mem::drop` wymaga `T`, więc musi przyjmować przez wartość. Typ kopiujący\\n"\n'
    '"    // skopiowałby się do domknięcia, nie ruszając oryginału.\\n"\n'
    '"    // Typ nie-kopiujący musi zostać przeniesiony — `movable` natychmiast\\n"\n'
    '"    // przenosi się do domknięcia.\\n"\n'
)

lit('`movable`: {:?}')
comment('// `consume` consumes the variable so this can only be called once.\\n',
        '// `consume` konsumuje zmienną, więc można ją wywołać tylko raz.\\n')

# capture:consume try uncommenting
multi(
    'msgid ""\n'
    '"// consume();\\n"\n'
    '"    // ^ TODO: Try uncommenting this line.\\n"\n',
    '"// consume();\\n"\n'
    '"    // ^ TODO: Spróbuj odkomentować tę linię.\\n"\n'
)

# capture:Using move before vertical pipes
multi(
    'msgid ""\n'
    '"Using `move` before vertical pipes forces closure to take ownership of "\n'
    '"captured variables:"\n',
    '"Użycie `move` przed pionowymi kreskami zmusza domknięcie do przejęcia "\n'
    '"własności przechwyconych zmiennych:"\n'
)

comment('// `Vec` has non-copy semantics.\\n', '// `Vec` ma semantykę nie-kopiującą.\\n')

# capture:println There're elements
multi(
    'msgid ""\n'
    '"// println!(\\"There\'re {} elements in vec\\", haystack.len());\\n"\n'
    '"    // ^ Uncommenting above line will result in compile-time error\\n"\n'
    '"    // because borrow checker doesn\'t allow re-using variable after it\\n"\n'
    '"    // has been moved.\\n"\n',
    '"// println!(\\"There\'re {} elements in vec\\", haystack.len());\\n"\n'
    '"    // ^ Odkomentowanie powyższej linii spowoduje błąd kompilacji,\\n"\n'
    '"    // bo kontroler pożyczania nie pozwala ponownie używać zmiennej\\n"\n'
    '"    // po jej przeniesieniu.\\n"\n'
)

# capture:Removing move from closure's signature
multi(
    'msgid ""\n'
    '"// Removing `move` from closure\'s signature will cause closure\\n"\n'
    '"    // to borrow _haystack_ variable immutably, hence _haystack_ is still\\n"\n'
    '"    // available and uncommenting above line will not cause an error.\\n"\n',
    '"// Usunięcie `move` z sygnatury domknięcia spowoduje pożyczenie\\n"\n'
    '"    // _haystack_ niemutowalnie — _haystack_ nadal będzie dostępne\\n"\n'
    '"    // i odkomentowanie powyższej linii nie spowoduje błędu.\\n"\n'
)

# capture:Box and std::mem::drop link
multi(
    'msgid ""\n'
    '"[`Box`](../../std/box.md) and [`std::mem::drop`](https://doc.rust-lang.org/"\n'
    '"std/mem/fn.drop.html)"\n',
    '"[`Box`](../../std/box.md) i [`std::mem::drop`](https://doc.rust-lang.org/"\n'
    '"std/mem/fn.drop.html)"\n'
)

# ============================================================
# fn/closures/input_parameters.md
# ============================================================

# input_parameters:3
multi(
    'msgid ""\n'
    '"While Rust chooses how to capture variables on the fly mostly without type "\n'
    '"annotation, this ambiguity is not allowed when writing functions. When "\n'
    '"taking a closure as an input parameter, the closure\'s complete type must be "\n'
    '"annotated using one of a few `traits`, and they\'re determined by what the "\n'
    '"closure does with captured value. In order of decreasing restriction, they "\n'
    '"are:"\n',
    '"Choć Rust wybiera sposób przechwytywania zmiennych w locie, "\n'
    '"to niejednoznaczność ta jest niedopuszczalna w funkcjach. "\n'
    '"Gdy domknięcie jest parametrem wejściowym, jego pełny typ musi być "\n'
    '"opatrzony adnotacją jednej z kilku `cech`, zależnie od tego, co domknięcie "\n'
    '"robi z pechwyconą wartością. W kolejności malejących ograniczeń są to:"\n'
)

prose('`Fn`: the closure uses the captured value by reference (`&T`)',
      '`Fn`: domknięcie używa przechwyconej wartości przez referencję (`&T`)')

# FnMut (multi-line due to backtick line break)
multi(
    'msgid ""\n'
    '"`FnMut`: the closure uses the captured value by mutable reference (`&mut T`)"\n',
    '"`FnMut`: domknięcie używa przechwyconej wartości przez mutowalną referencję (`&mut T`)"\n'
)

prose('`FnOnce`: the closure uses the captured value by value (`T`)',
      '`FnOnce`: domknięcie używa przechwyconej wartości przez wartość (`T`)')

# input_parameters:On a variable-by-variable basis
multi(
    'msgid ""\n'
    '"On a variable-by-variable basis, the compiler will capture variables in the "\n'
    '"least restrictive manner possible."\n',
    '"Dla każdej zmiennej z osobna kompilator przechwytuje ją w sposób "\n'
    '"o jak najmniejszych ograniczeniach."\n'
)

# input_parameters:For instance, consider a parameter annotated as FnOnce
multi(
    'msgid ""\n'
    '"For instance, consider a parameter annotated as `FnOnce`. This specifies "\n'
    '"that the closure _may_ capture by `&T`, `&mut T`, or `T`, but the compiler "\n'
    '"will ultimately choose based on how the captured variables are used in the "\n'
    '"closure."\n',
    '"Na przykład parametr opatrzony adnotacją `FnOnce` oznacza, że domknięcie "\n'
    '"_może_ przechwytywać przez `&T`, `&mut T` lub `T`, ale kompilator "\n'
    '"ostatecznie wybierze sposób na podstawie użycia przechwyconych zmiennych."\n'
)

# input_parameters:This is because if a move is possible
multi(
    'msgid ""\n'
    '"This is because if a move is possible, then any type of borrow should also "\n'
    '"be possible. Note that the reverse is not true. If the parameter is "\n'
    '"annotated as `Fn`, then capturing variables by `&mut T` or `T` are not "\n'
    '"allowed. However, `&T` is allowed."\n',
    '"Wynika to z faktu, że jeśli przeniesienie jest możliwe, każdy rodzaj "\n'
    '"pożyczania powinien być też możliwy. Odwrotność nie jest prawdą: jeśli "\n'
    '"parametr ma adnotację `Fn`, przechwytywanie przez `&mut T` lub `T` "\n'
    '"jest niedozwolone, ale `&T` jest dozwolone."\n'
)

# input_parameters:try swapping usage of Fn, FnMut, FnOnce
multi(
    'msgid ""\n'
    '"In the following example, try swapping the usage of `Fn`, `FnMut`, and "\n'
    '"`FnOnce` to see what happens:"\n',
    '"W poniższym przykładzie spróbuj zamieniać użycie `Fn`, `FnMut` i "\n'
    '"`FnOnce`, aby zobaczyć co się stanie:"\n'
)

# input_parameters:A function which takes a closure (multi-line comment)
multi(
    'msgid ""\n'
    '"// A function which takes a closure as an argument and calls it.\\n"\n'
    '"// <F> denotes that F is a \\"Generic type parameter\\"\\n"\n',
    '"// Funkcja przyjmująca domknięcie jako argument i wywołująca je.\\n"\n'
    '"// <F> oznacza, że F jest \\"Ogólnym parametrem typowym\\"\\n"\n'
)

comment('// The closure takes no input and returns nothing.\\n',
        '// Domknięcie nie przyjmuje wejścia i nic nie zwraca.\\n')
comment('// ^ TODO: Try changing this to `Fn` or `FnMut`.\\n',
        '// ^ TODO: Spróbuj zmienić to na `Fn` lub `FnMut`.\\n')
comment('// A function which takes a closure and returns an `i32`.\\n',
        '// Funkcja przyjmująca domknięcie i zwracająca `i32`.\\n')
comment('// The closure takes an `i32` and returns an `i32`.\\n',
        '// Domknięcie przyjmuje `i32` i zwraca `i32`.\\n')

# input_parameters:A non-copy type. to_owned
multi(
    'msgid ""\n'
    '"// A non-copy type.\\n"\n'
    '"    // `to_owned` creates owned data from borrowed one\\n"\n',
    '"// Typ nie-kopiujący.\\n"\n'
    '"    // `to_owned` tworzy dane własne z pożyczonych\\n"\n'
)

lit('goodbye')

# input_parameters:Capture greeting by reference and farewell by value
multi(
    'msgid ""\n'
    '"// Capture 2 variables: `greeting` by reference and\\n"\n'
    '"    // `farewell` by value.\\n"\n',
    '"// Przechwyć 2 zmienne: `greeting` przez referencję\\n"\n'
    '"    // i `farewell` przez wartość.\\n"\n'
)

comment('// `greeting` is by reference: requires `Fn`.\\n',
        '// `greeting` jest przez referencję: wymaga `Fn`.\\n')
lit('I said {}.')

# input_parameters:Mutation forces farewell
multi(
    'msgid ""\n'
    '"// Mutation forces `farewell` to be captured by\\n"\n'
    '"        // mutable reference. Now requires `FnMut`.\\n"\n',
    '"// Mutacja wymusza przechwycenie `farewell` przez\\n"\n'
    '"        // mutowalną referencję. Teraz wymaga `FnMut`.\\n"\n'
)

lit('!!!')
lit('Then I screamed {}.')
lit('Now I can sleep. zzzzz')

# input_parameters:Manually calling drop forces farewell
multi(
    'msgid ""\n'
    '"// Manually calling drop forces `farewell` to\\n"\n'
    '"        // be captured by value. Now requires `FnOnce`.\\n"\n',
    '"// Ręczne wywołanie drop wymusza przechwycenie `farewell`\\n"\n'
    '"        // przez wartość. Teraz wymaga `FnOnce`.\\n"\n'
)

comment('// Call the function which applies the closure.\\n',
        '// Wywołaj funkcję stosującą domknięcie.\\n')
comment('// `double` satisfies `apply_to_3`\'s trait bound\\n',
        '// `double` spełnia ograniczenie cechy `apply_to_3`\\n')
lit('3 doubled: {}')

# input_parameters: std::mem::drop, Fn, FnMut links
multi(
    'msgid ""\n'
    '"[`std::mem::drop`](https://doc.rust-lang.org/std/mem/fn.drop.html), [`Fn`]"\n'
    '"(https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://doc."\n'
    '"rust-lang.org/std/ops/trait.FnMut.html), [Generics](../../generics.md), "\n'
    '"[where](../../generics/where.md) and [`FnOnce`](https://doc.rust-lang.org/"\n'
    '"std/ops/trait.FnOnce.html)"\n',
    '"[`std::mem::drop`](https://doc.rust-lang.org/std/mem/fn.drop.html), [`Fn`]"\n'
    '"(https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://doc."\n'
    '"rust-lang.org/std/ops/trait.FnMut.html), [Typy ogólne](../../generics.md), "\n'
    '"[where](../../generics/where.md) i [`FnOnce`](https://doc.rust-lang.org/"\n'
    '"std/ops/trait.FnOnce.html)"\n'
)

# ============================================================
# fn/closures/anonymity.md
# ============================================================

# anonymity:3
multi(
    'msgid ""\n'
    '"Closures succinctly capture variables from enclosing scopes. Does this have "\n'
    '"any consequences? It surely does. Observe how using a closure as a function "\n'
    '"parameter requires [generics](../../generics.md), which is necessary because "\n'
    '"of how they are defined:"\n',
    '"Domknięcia zwięźle przechwytują zmienne z otaczających zasięgów. Czy ma "\n'
    '"to konsekwencje? Oczywiście. Obserwuj, jak użycie domknięcia jako parametru "\n'
    '"funkcji wymaga [typów ogólnych](../../generics.md), co wynika z ich definicji:"\n'
)

comment('// `F` must be generic.\\n', '// `F` musi być ogólny.\\n')

# anonymity:When a closure is defined
multi(
    'msgid ""\n'
    '"When a closure is defined, the compiler implicitly creates a new anonymous "\n'
    '"structure to store the captured variables inside, meanwhile implementing the "\n'
    '"functionality via one of the `traits`: `Fn`, `FnMut`, or `FnOnce` for this "\n'
    '"unknown type. This type is assigned to the variable which is stored until "\n'
    '"calling."\n',
    '"Gdy definiowane jest domknięcie, kompilator niejawnie tworzy nową anonimową "\n'
    '"strukturę przechowującą przechwycone zmienne, implementując jednocześnie "\n'
    '"funkcjonalność przez jedną z `cech`: `Fn`, `FnMut` lub `FnOnce` dla "\n'
    '"tego nieznanego typu. Typ ten jest przypisywany do zmiennej przechowywanej "\n'
    '"do czasu wywołania."\n'
)

# anonymity:Since this new type is of unknown type
multi(
    'msgid ""\n'
    '"Since this new type is of unknown type, any usage in a function will require "\n'
    '"generics. However, an unbounded type parameter `<T>` would still be "\n'
    '"ambiguous and not be allowed. Thus, bounding by one of the `traits`: `Fn`, "\n'
    '"`FnMut`, or `FnOnce` (which it implements) is sufficient to specify its type."\n',
    '"Ponieważ nowy typ jest nieznany, każde użycie w funkcji wymaga typów ogólnych. "\n'
    '"Nieograniczony parametr typowy `<T>` byłby jednak niejednoznaczny i niedozwolony. "\n'
    '"Wystarczy więc ograniczyć przez jedną z `cech`: `Fn`, `FnMut` lub `FnOnce` "\n'
    '"(którą implementuje), aby określić typ."\n'
)

# anonymity:F must implement Fn for a closure
multi(
    'msgid ""\n'
    '"// `F` must implement `Fn` for a closure which takes no\\n"\n'
    '"// inputs and returns nothing - exactly what is required\\n"\n'
    '"// for `print`.\\n"\n',
    '"// `F` musi implementować `Fn` dla domknięcia bez wejścia\\n"\n'
    '"// i bez wyjścia — dokładnie to co jest wymagane\\n"\n'
    '"// dla `print`.\\n"\n'
)

# anonymity:Capture x into anonymous type
multi(
    'msgid ""\n'
    '"// Capture `x` into an anonymous type and implement\\n"\n'
    '"    // `Fn` for it. Store it in `print`.\\n"\n',
    '"// Przechwyć `x` do anonimowego typu i zaimplementuj\\n"\n'
    '"    // dla niego `Fn`. Zapisz w `print`.\\n"\n'
)

# anonymity:thorough analysis link
multi(
    'msgid ""\n'
    '"[A thorough analysis](https://huonw.github.io/blog/2015/05/finding-closure-"\n'
    '"in-rust/), [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`]"\n'
    '"(https://doc.rust-lang.org/std/ops/trait.FnMut.html), and [`FnOnce`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.FnOnce.html)"\n',
    '"[Dokładna analiza](https://huonw.github.io/blog/2015/05/finding-closure-"\n'
    '"in-rust/), [`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`]"\n'
    '"(https://doc.rust-lang.org/std/ops/trait.FnMut.html) i [`FnOnce`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.FnOnce.html)"\n'
)

# ============================================================
# fn/closures/input_functions.md
# ============================================================

# input_functions:3
multi(
    'msgid ""\n'
    '"Since closures may be used as arguments, you might wonder if the same can be "\n'
    '"said about functions. And indeed they can! If you declare a function that "\n'
    '"takes a closure as parameter, then any function that satisfies the trait "\n'
    '"bound of that closure can be passed as a parameter."\n',
    '"Skoro domknięcia mogą być argumentami, można zapytać czy to samo dotyczy "\n'
    '"funkcji. I owszem! Jeśli zadeklarujesz funkcję przyjmującą domknięcie jako "\n'
    '"parametr, to dowolna funkcja spełniająca ograniczenie cechy tego domknięcia "\n'
    '"może być przekazana jako parametr."\n'
)

# input_functions:Define a function which takes a generic F bounded by Fn
multi(
    'msgid ""\n'
    '"// Define a function which takes a generic `F` argument\\n"\n'
    '"// bounded by `Fn`, and calls it\\n"\n',
    '"// Zdefiniuj funkcję przyjmującą ogólny argument `F`\\n"\n'
    '"// ograniczony przez `Fn` i wywołaj go\\n"\n'
)

comment('// Define a wrapper function satisfying the `Fn` bound\\n',
        '// Zdefiniuj funkcję opakowującą spełniającą ograniczenie `Fn`\\n')
lit("I'm a function!")
comment('// Define a closure satisfying the `Fn` bound\\n',
        '// Zdefiniuj domknięcie spełniające ograniczenie `Fn`\\n')
lit("I'm a closure!")

# input_functions:additional note, Fn, FnMut, FnOnce dictate
multi(
    'msgid ""\n'
    '"As an additional note, the `Fn`, `FnMut`, and `FnOnce` `traits` dictate how "\n'
    '"a closure captures variables from the enclosing scope."\n',
    '"Dodatkowo cechy `Fn`, `FnMut` i `FnOnce` określają sposób w jaki domknięcie "\n'
    '"przechwytuje zmienne z otaczającego zasięgu."\n'
)

# input_functions:Fn, FnMut, FnOnce links
multi(
    'msgid ""\n'
    '"[`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.FnMut.html), and [`FnOnce`](https://doc.rust-"\n'
    '"lang.org/std/ops/trait.FnOnce.html)"\n',
    '"[`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.FnMut.html) i [`FnOnce`](https://doc.rust-"\n'
    '"lang.org/std/ops/trait.FnOnce.html)"\n'
)

# ============================================================
# fn/closures/output_parameters.md
# ============================================================

# output_parameters:3
multi(
    'msgid ""\n'
    '"Closures as input parameters are possible, so returning closures as output "\n'
    '"parameters should also be possible. However, anonymous closure types are, by "\n'
    '"definition, unknown, so we have to use `impl Trait` to return them."\n',
    '"Skoro domknięcia mogą być parametrami wejściowymi, powinny też móc być "\n'
    '"parametrami wyjściowymi. Anonimowe typy domknięć są jednak z definicji "\n'
    '"nieznane, więc musimy użyć `impl Trait` do ich zwracania."\n'
)

prose('The valid traits for returning a closure are:',
      'Prawidłowe cechy do zwracania domknięcia to:')
prose('`Fn`', '`Fn`')
prose('`FnMut`', '`FnMut`')
prose('`FnOnce`', '`FnOnce`')

# output_parameters:move keyword must be used
multi(
    'msgid ""\n'
    '"Beyond this, the `move` keyword must be used, which signals that all "\n'
    '"captures occur by value. This is required because any captures by reference "\n'
    '"would be dropped as soon as the function exited, leaving invalid references "\n'
    '"in the closure."\n',
    '"Dodatkowo musi być użyte słowo kluczowe `move`, sygnalizujące, że wszystkie "\n'
    '"przechwycenia następują przez wartość. Jest to konieczne, bo przechwycenia "\n'
    '"przez referencję zostałyby upuszczone po wyjściu z funkcji, pozostawiając "\n'
    '"nieważne referencje w domknięciu."\n'
)

lit('Fn')
lit('This is a: {}')
lit('FnMut')
lit('FnOnce')

# output_parameters:Fn, FnMut, Generics, impl Trait links
multi(
    'msgid ""\n'
    '"[`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.FnMut.html), [Generics](../../generics.md) "\n'
    '"and [impl Trait](../../trait/impl_trait.md)."\n',
    '"[`Fn`](https://doc.rust-lang.org/std/ops/trait.Fn.html), [`FnMut`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.FnMut.html), [Typy ogólne](../../generics.md) "\n'
    '"i [impl Trait](../../trait/impl_trait.md)."\n'
)

# ============================================================
# fn/closures/closure_examples.md
# ============================================================

# closure_examples:3
multi(
    'msgid ""\n'
    '"This section contains a few examples of using closures from the `std` "\n'
    '"library."\n',
    '"Ta sekcja zawiera kilka przykładów użycia domknięć z biblioteki `std`."\n'
)

# ============================================================
# fn/closures/closure_examples/iter_any.md
# ============================================================

# iter_any:3
multi(
    'msgid ""\n'
    '"`Iterator::any` is a function which when passed an iterator, will return "\n'
    '"`true` if any element satisfies the predicate. Otherwise `false`. Its "\n'
    '"signature:"\n',
    '"`Iterator::any` to funkcja, która przyjmując iterator, zwraca `true` jeśli "\n'
    '"dowolny element spełnia predykat, inaczej `false`. Jej sygnatura:"\n'
)

comment('// The type being iterated over.\\n',
        '// Typ po którym iterujemy.\\n')

# iter_any:any takes &mut self
multi(
    'msgid ""\n'
    '"// `any` takes `&mut self` meaning the caller may be borrowed\\n"\n'
    '"    // and modified, but not consumed.\\n"\n',
    '"// `any` przyjmuje `&mut self`, co oznacza, że wywołujący może być\\n"\n'
    '"    // pożyczony i zmodyfikowany, ale nie skonsumowany.\\n"\n'
)

# iter_any:FnMut meaning modified not consumed
multi(
    'msgid ""\n'
    '"// `FnMut` meaning any captured variable may at most be\\n"\n'
    '"        // modified, not consumed. `Self::Item` is the closure parameter "\n'
    '"type,\\n"\n'
    '"        // which is determined by the iterator (e.g., `&T` for `.iter()`,\\n"\n'
    '"        // `T` for `.into_iter()`).\\n"\n',
    '"// `FnMut` oznacza, że każda przechwycona zmienna może być co najwyżej\\n"\n'
    '"        // zmodyfikowana, nie skonsumowana. `Self::Item` to typ parametru\\n"\n'
    '"        // domknięcia wyznaczany przez iterator (np. `&T` dla `.iter()`,\\n"\n'
    '"        // `T` dla `.into_iter()`).\\n"\n'
)

comment('// `iter()` for vecs yields `&i32`. Destructure to `i32`.\\n',
        '// `iter()` dla vec-ów daje `&i32`. Destrukturyzuj do `i32`.\\n')
lit('2 in vec1: {}')
comment('// `into_iter()` for vecs yields `i32`. No destructuring required.\\n',
        '// `into_iter()` dla vec-ów daje `i32`. Destrukturyzacja nie jest potrzebna.\\n')
lit('2 in vec2: {}')

# iter_any:iter() only borrows vec1
multi(
    'msgid ""\n'
    '"// `iter()` only borrows `vec1` and its elements, so they can be used again\\n"\n',
    '"// `iter()` jedynie pożycza `vec1` i jego elementy, więc można ich użyć ponownie\\n"\n'
)

lit('vec1 len: {}')
lit('First element of vec1 is: {}')

# iter_any:into_iter does move vec2
multi(
    'msgid ""\n'
    '"// `into_iter()` does move `vec2` and its elements, so they cannot be used "\n'
    '"again\\n"\n'
    '"    // println!(\\"First element of vec2 is: {}\\", vec2[0]);\\n"\n'
    '"    // println!(\\"vec2 len: {}\\", vec2.len());\\n"\n'
    '"    // TODO: uncomment two lines above and see compiler errors.\\n"\n',
    '"// `into_iter()` przenosi `vec2` i jego elementy, więc nie można ich użyć ponownie\\n"\n'
    '"    // println!(\\"First element of vec2 is: {}\\", vec2[0]);\\n"\n'
    '"    // println!(\\"vec2 len: {}\\", vec2.len());\\n"\n'
    '"    // TODO: odkomentuj dwie linie powyżej, aby zobaczyć błędy kompilatora.\\n"\n'
)

comment('// `iter()` for arrays yields `&i32`.\\n',
        '// `iter()` dla tablic daje `&i32`.\\n')
lit('2 in array1: {}')
comment('// `into_iter()` for arrays yields `i32`.\\n',
        '// `into_iter()` dla tablic daje `i32`.\\n')
lit('2 in array2: {}')

# iter_any:std::iter::Iterator::any link
multi(
    'msgid ""\n'
    '"[`std::iter::Iterator::any`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.any)"\n',
    '"[`std::iter::Iterator::any`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.any)"\n'
)

# ============================================================
# fn/closures/closure_examples/iter_find.md
# ============================================================

# iter_find:3
multi(
    'msgid ""\n'
    '"`Iterator::find` is a function which iterates over an iterator and searches "\n'
    '"for the first value which satisfies some condition. If none of the values "\n'
    '"satisfy the condition, it returns `None`. Its signature:"\n',
    '"`Iterator::find` to funkcja, która iteruje przez iterator i szuka "\n'
    '"pierwszej wartości spełniającej warunek. Jeśli żadna wartość go nie spełnia, "\n'
    '"zwraca `None`. Jej sygnatura:"\n'
)

# iter_find:find takes &mut self
multi(
    'msgid ""\n'
    '"// `find` takes `&mut self` meaning the caller may be borrowed\\n"\n'
    '"    // and modified, but not consumed.\\n"\n',
    '"// `find` przyjmuje `&mut self`, co oznacza, że wywołujący może być\\n"\n'
    '"    // pożyczony i zmodyfikowany, ale nie skonsumowany.\\n"\n'
)

# iter_find:FnMut modified not consumed &Self::Item
multi(
    'msgid ""\n'
    '"// `FnMut` meaning any captured variable may at most be\\n"\n'
    '"        // modified, not consumed. `&Self::Item` states it takes\\n"\n'
    '"        // arguments to the closure by reference.\\n"\n',
    '"// `FnMut` oznacza, że każda przechwycona zmienna może być co najwyżej\\n"\n'
    '"        // zmodyfikowana, nie skonsumowana. `&Self::Item` oznacza, że\\n"\n'
    '"        // argumenty domknięcia są przekazywane przez referencję.\\n"\n'
)

comment('// `vec1.iter()` yields `&i32`.\\n', '// `vec1.iter()` daje `&i32`.\\n')
comment('// `vec2.into_iter()` yields `i32`.\\n', '// `vec2.into_iter()` daje `i32`.\\n')

# iter_find:iter() yields &i32 find passes &Item
multi(
    'msgid ""\n'
    '"// `iter()` yields `&i32`, and `find` passes `&Item` to the predicate.\\n"\n'
    '"    // Since `Item = &i32`, the closure argument has type `&&i32`,\\n"\n'
    '"    // which we pattern-match to dereference down to `i32`.\\n"\n',
    '"// `iter()` daje `&i32`, a `find` przekazuje predykatowi `&Item`.\\n"\n'
    '"    // Ponieważ `Item = &i32`, argument domknięcia ma typ `&&i32`,\\n"\n'
    '"    // który dopasowujemy wzorcem do wyłuskania do `i32`.\\n"\n'
)

lit('Find 2 in vec1: {:?}')

# iter_find:into_iter yields i32 find passes &Item
multi(
    'msgid ""\n'
    '"// `into_iter()` yields `i32`, and `find` passes `&Item` to the predicate.\\n"\n'
    '"    // Since `Item = i32`, the closure argument has type `&i32`,\\n"\n'
    '"    // which we pattern-match to dereference down to `i32`.\\n"\n',
    '"// `into_iter()` daje `i32`, a `find` przekazuje predykatowi `&Item`.\\n"\n'
    '"    // Ponieważ `Item = i32`, argument domknięcia ma typ `&i32`,\\n"\n'
    '"    // który dopasowujemy wzorcem do wyłuskania do `i32`.\\n"\n'
)

lit('Find 2 in vec2: {:?}')

# iter_find:array1.iter() yields &i32 find passes &Item
multi(
    'msgid ""\n'
    '"// `array1.iter()` yields `&i32`, and `find` passes `&Item` to the\\n"\n'
    '"    // predicate. Since `Item = &i32`, the closure argument has type "\n'
    '"`&&i32`.\\n"\n',
    '"// `array1.iter()` daje `&i32`, a `find` przekazuje predykatowi `&Item`.\\n"\n'
    '"    // Ponieważ `Item = &i32`, argument domknięcia ma typ `&&i32`.\\n"\n'
)

lit('Find 2 in array1: {:?}')

# iter_find:array2.into_iter yields i32 Rust 2021
multi(
    'msgid ""\n'
    '"// `array2.into_iter()` yields `i32` (since Rust 2021 edition), and\\n"\n'
    '"    // `find` passes `&Item` to the predicate. Since `Item = i32`, the\\n"\n'
    '"    // closure argument has type `&i32`.\\n"\n',
    '"// `array2.into_iter()` daje `i32` (od edycji Rust 2021), a\\n"\n'
    '"    // `find` przekazuje predykatowi `&Item`. Ponieważ `Item = i32`,\\n"\n'
    '"    // argument domknięcia ma typ `&i32`.\\n"\n'
)

lit('Find 2 in array2: {:?}')

# iter_find:find gives reference, position
multi(
    'msgid ""\n'
    '"`Iterator::find` gives you a reference to the item. But if you want the "\n'
    '"_index_ of the item, use `Iterator::position`."\n',
    '"`Iterator::find` daje referencję do elementu. Jeśli potrzebujesz "\n'
    '"_indeksu_ elementu, użyj `Iterator::position`."\n'
)

# iter_find:position passes iterator's Item by value
multi(
    'msgid ""\n'
    '"// `position` passes the iterator\'s `Item` by value to the predicate.\\n"\n'
    '"    // `vec.iter()` yields `&i32`, so the predicate receives `&i32`,\\n"\n'
    '"    // which we pattern-match to dereference to `i32`.\\n"\n',
    '"// `position` przekazuje predykatowi `Item` iteratora przez wartość.\\n"\n'
    '"    // `vec.iter()` daje `&i32`, więc predykat otrzymuje `&i32`,\\n"\n'
    '"    // który dopasowujemy wzorcem do wyłuskania do `i32`.\\n"\n'
)

# iter_find:vec.into_iter yields i32 directly
multi(
    'msgid ""\n'
    '"// `vec.into_iter()` yields `i32`, so the predicate receives `i32` "\n'
    '"directly.\\n"\n',
    '"// `vec.into_iter()` daje `i32`, więc predykat otrzymuje `i32` bezpośrednio.\\n"\n'
)

# iter_find:std::iter::Iterator::find link
multi(
    'msgid ""\n'
    '"[`std::iter::Iterator::find`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.find)"\n',
    '"[`std::iter::Iterator::find`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.find)"\n'
)

# iter_find:find_map link
multi(
    'msgid ""\n'
    '"[`std::iter::Iterator::find_map`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.find_map)"\n',
    '"[`std::iter::Iterator::find_map`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.find_map)"\n'
)

# iter_find:position link
multi(
    'msgid ""\n'
    '"[`std::iter::Iterator::position`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.position)"\n',
    '"[`std::iter::Iterator::position`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.position)"\n'
)

# iter_find:rposition link
multi(
    'msgid ""\n'
    '"[`std::iter::Iterator::rposition`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.rposition)"\n',
    '"[`std::iter::Iterator::rposition`](https://doc.rust-lang.org/std/iter/trait."\n'
    '"Iterator.html#method.rposition)"\n'
)

# ============================================================
# fn/hof.md — HIGHER ORDER FUNCTIONS
# ============================================================

# hof:3
multi(
    'msgid ""\n'
    '"Rust provides Higher Order Functions (HOF). These are functions that take "\n'
    '"one or more functions and/or produce a more useful function. HOFs and lazy "\n'
    '"iterators give Rust its functional flavor."\n',
    '"Rust dostarcza Funkcje Wyższego Rzędu (HOF). To funkcje przyjmujące jedną "\n'
    '"lub więcej funkcji i/lub produkujące bardziej użyteczną funkcję. "\n'
    '"HOF i leniwe iteratory nadają Rustowi funkcyjny charakter."\n'
)

lit('Find the sum of all the numbers with odd squares under 1000')

# hof:Imperative approach
multi(
    'msgid ""\n'
    '"// Imperative approach\\n"\n'
    '"    // Declare accumulator variable\\n"\n',
    '"// Podejście imperatywne\\n"\n'
    '"    // Zadeklaruj zmienną akumulatora\\n"\n'
)

comment('// Iterate: 0, 1, 2, ... to infinity\\n', '// Iteruj: 0, 1, 2, ... do nieskończoności\\n')
comment('// Square the number\\n', '// Podnieś liczbę do kwadratu\\n')
comment('// Break loop if exceeded the upper limit\\n', '// Przerwij pętlę jeśli przekroczono górny limit\\n')
comment("// Accumulate value, if it's odd\\n", '// Akumuluj wartość jeśli jest nieparzysta\\n')
lit('imperative style: {}')
comment('// Functional approach\\n', '// Podejście funkcyjne\\n')
comment('// Below upper limit\\n', '// Poniżej górnego limitu\\n')
comment('// That are odd\\n', '// Które są nieparzyste\\n')
comment('// Sum them\\n', '// Zsumuj je\\n')
lit('functional style: {}')

# hof:Option and Iterator implement their fair share
multi(
    'msgid ""\n'
    '"[Option](https://doc.rust-lang.org/core/option/enum.Option.html) and "\n'
    '"[Iterator](https://doc.rust-lang.org/core/iter/trait.Iterator.html) "\n'
    '"implement their fair share of HOFs."\n',
    '"[Option](https://doc.rust-lang.org/core/option/enum.Option.html) i "\n'
    '"[Iterator](https://doc.rust-lang.org/core/iter/trait.Iterator.html) "\n'
    '"implementują znaczną część HOF."\n'
)

# ============================================================
# fn/diverging.md — DIVERGING FUNCTIONS
# ============================================================

# diverging:3
multi(
    'msgid ""\n'
    '"Diverging functions never return. They are marked using `!`, which is an "\n'
    '"empty type."\n',
    '"Funkcje rozbieżne nigdy nie zwracają. Są oznaczane za pomocą `!`, który jest "\n'
    '"typem pustym."\n'
)

lit('This call never returns.')

# diverging:As opposed to all the other types
multi(
    'msgid ""\n'
    '"As opposed to all the other types, this one cannot be instantiated, because "\n'
    '"the set of all possible values this type can have is empty. Note that, it is "\n'
    '"different from the `()` type, which has exactly one possible value."\n',
    '"W odróżnieniu od wszystkich innych typów, tego nie można zinstancjonować, "\n'
    '"ponieważ zbiór wszystkich możliwych wartości tego typu jest pusty. Pamiętaj, "\n'
    '"że różni się od typu `()`, który ma dokładnie jedną możliwą wartość."\n'
)

# diverging:For example this function returns as usual
multi(
    'msgid ""\n'
    '"For example, this function returns as usual, although there is no "\n'
    '"information in the return value."\n',
    '"Na przykład ta funkcja zwraca normalnie, choć w wartości zwracanej "\n'
    '"nie ma żadnej informacji."\n'
)

lit('This function returns and you can see this line.')

# diverging:As opposed to this function which will never return
multi(
    'msgid ""\n'
    '"As opposed to this function, which will never return the control back to the "\n'
    '"caller."\n',
    '"W odróżnieniu od tej funkcji, która nigdy nie zwróci sterowania do wywołującego."\n'
)

lit('You will never see this line!')

# diverging:Although this might seem like an abstract concept
multi(
    'msgid ""\n'
    '"Although this might seem like an abstract concept, it is actually very "\n'
    '"useful and often handy. The main advantage of this type is that it can be "\n'
    '"cast to any other type, making it versatile in situations where an exact "\n'
    '"type is required, such as in match branches. This flexibility allows us to "\n'
    '"write code like this:"\n',
    '"Choć może to wyglądać abstrakcyjnie, ten typ jest naprawdę bardzo użyteczny. "\n'
    '"Jego główną zaletą jest możliwość rzutowania na dowolny inny typ, co czyni go "\n'
    '"wszechstronnym tam gdzie wymagany jest konkretny typ, np. w ramionach match. "\n'
    '"Ta elastyczność pozwala pisać kod taki jak ten:"\n'
)

# diverging:Notice that the return type of match must be u32
multi(
    'msgid ""\n'
    '"// Notice that the return type of this match expression must be u32\\n"\n'
    '"            // because of the type of the \\"addition\\" variable.\\n"\n',
    '"// Zauważ, że typ zwracany przez to wyrażenie match musi być u32\\n"\n'
    '"            // ze względu na typ zmiennej \\"addition\\".\\n"\n'
)

comment('// The \\"i\\" variable is of type u32, which is perfectly fine.\\n',
        '// Zmienna \\"i\\" ma typ u32, co jest całkowicie poprawne.\\n')

# diverging:On the other hand the continue expression
multi(
    'msgid ""\n'
    '"// On the other hand, the \\"continue\\" expression does not return\\n"\n'
    '"                // u32, but it is still fine, because it never returns and "\n'
    '"therefore\\n"\n'
    '"                // does not violate the type requirements of the match "\n'
    '"expression.\\n"\n',
    '"// Z drugiej strony wyrażenie \\"continue\\" nie zwraca\\n"\n'
    '"                // u32, ale to wciąż poprawne, bo nigdy nie zwraca i dlatego\\n"\n'
    '"                // nie narusza wymagań typowych wyrażenia match.\\n"\n'
)

lit('Sum of odd numbers up to 9 (excluding): {}')

# diverging:It is also the return type of functions that loop forever
multi(
    'msgid ""\n'
    '"It is also the return type of functions that loop forever (e.g. `loop {}`) "\n'
    '"like network servers or functions that terminate the process (e.g. `exit()`)."\n',
    '"Jest też typem zwracanym przez funkcje, które pętlują w nieskończoność "\n'
    '"(np. `loop {}`), takie jak serwery sieciowe, lub funkcje kończące proces "\n'
    '"(np. `exit()`)."\n'
)

# ============================================================
# mod.md — MODULES
# ============================================================

# mod:3
multi(
    'msgid ""\n'
    '"Rust provides a powerful module system that can be used to hierarchically "\n'
    '"split code in logical units (modules), and manage visibility (public/"\n'
    '"private) between them."\n',
    '"Rust dostarcza potężny system modułów, który może być użyty do "\n'
    '"hierarchicznego podziału kodu na logiczne jednostki (moduły) i zarządzania "\n'
    '"widocznością (publiczna/prywatna) między nimi."\n'
)

# mod:A module is a collection of items
multi(
    'msgid ""\n'
    '"A module is a collection of items: functions, structs, traits, `impl` "\n'
    '"blocks, and even other modules."\n',
    '"Moduł to zbiór elementów: funkcji, struktur, cech, bloków `impl` i innych modułów."\n'
)

# mod:By default, the items in a module
multi(
    'msgid ""\n'
    '"By default, the items in a module have private visibility, but this can be "\n'
    '"overridden with the `pub` modifier. Only the public items of a module can be "\n'
    '"accessed from outside the module scope."\n',
    '"Domyślnie elementy modułu mają prywatną widoczność, ale można to zmienić "\n'
    '"modyfikatorem `pub`. Tylko publiczne elementy modułu są dostępne spoza zasięgu modułu."\n'
)

# ============================================================
# mod/visibility.md
# ============================================================

comment('// A module named `my_mod`\\n', '// Moduł o nazwie `my_mod`\\n')
comment('// Items in modules default to private visibility.\\n',
        '// Elementy modułów domyślnie mają prywatną widoczność.\\n')
lit('called `my_mod::private_function()`')
comment('// Use the `pub` modifier to override default visibility.\\n',
        '// Użyj modyfikatora `pub`, aby nadpisać domyślną widoczność.\\n')
lit('called `my_mod::function()`')

# visibility:Items can access other items in the same module
multi(
    'msgid ""\n'
    '"// Items can access other items in the same module,\\n"\n'
    '"    // even when private.\\n"\n',
    '"// Elementy mogą uzyskiwać dostęp do innych elementów w tym samym module,\\n"\n'
    '"    // nawet prywatnych.\\n"\n'
)

lit('called `my_mod::indirect_access()`, that\\\\n> ')
comment('// Modules can also be nested\\n', '// Moduły mogą być też zagnieżdżone\\n')
lit('called `my_mod::nested::function()`')
lit('called `my_mod::nested::private_function()`')

# visibility:Functions declared using pub(in path)
multi(
    'msgid ""\n'
    '"// Functions declared using `pub(in path)` syntax are only visible\\n"\n'
    '"        // within the given path. `path` must be a parent or ancestor "\n'
    '"module\\n"\n',
    '"// Funkcje zadeklarowane składnią `pub(in path)` są widoczne tylko\\n"\n'
    '"        // w podanej ścieżce. `path` musi być modułem nadrzędnym\\n"\n'
)

lit('called `my_mod::nested::public_function_in_my_mod()`, that\\\\n> ')

# visibility:Functions declared using pub(self)
multi(
    'msgid ""\n'
    '"// Functions declared using `pub(self)` syntax are only visible within\\n"\n'
    '"        // the current module, which is the same as leaving them private\\n"\n',
    '"// Funkcje zadeklarowane składnią `pub(self)` są widoczne tylko\\n"\n'
    '"        // w bieżącym module, co jest równoważne z pozostawieniem ich prywatnymi\\n"\n'
)

lit('called `my_mod::nested::public_function_in_nested()`')

# visibility:Functions declared using pub(super)
multi(
    'msgid ""\n'
    '"// Functions declared using `pub(super)` syntax are only visible within\\n"\n'
    '"        // the parent module\\n"\n',
    '"// Funkcje zadeklarowane składnią `pub(super)` są widoczne tylko\\n"\n'
    '"        // w module nadrzędnym\\n"\n'
)

lit('called `my_mod::nested::public_function_in_super_mod()`')
lit('called `my_mod::call_public_function_in_my_mod()`, that\\\\n> ')
lit('> ')
comment('// pub(crate) makes functions visible only within the current crate\\n',
        '// pub(crate) sprawia, że funkcje są widoczne tylko w bieżącej skrzyni\\n')
lit('called `my_mod::public_function_in_crate()`')
comment('// Nested modules follow the same rules for visibility\\n',
        '// Zagnieżdżone moduły podlegają tym samym regułom widoczności\\n')
lit('called `my_mod::private_nested::function()`')

# visibility:Private parent items will still restrict
multi(
    'msgid ""\n'
    '"// Private parent items will still restrict the visibility of a child item,\\n"\n'
    '"        // even if it is declared as visible within a bigger scope.\\n"\n',
    '"// Prywatne elementy nadrzędne nadal ograniczają widoczność elementów podrzędnych,\\n"\n'
    '"        // nawet jeśli są zadeklarowane jako widoczne w szerszym zasięgu.\\n"\n'
)

lit('called `my_mod::private_nested::restricted_function()`')
lit('called `function()`')

# visibility:Modules allow disambiguation
multi(
    'msgid ""\n'
    '"// Modules allow disambiguation between items that have the same name.\\n"\n',
    '"// Moduły pozwalają na rozróżnianie elementów o tej samej nazwie.\\n"\n'
)

# visibility:Public items including those inside nested
multi(
    'msgid ""\n'
    '"// Public items, including those inside nested modules, can be\\n"\n'
    '"    // accessed from outside the parent module.\\n"\n',
    '"// Publiczne elementy, w tym te wewnątrz zagnieżdżonych modułów,\\n"\n'
    '"    // są dostępne spoza modułu nadrzędnego.\\n"\n'
)

comment('// pub(crate) items can be called from anywhere in the same crate\\n',
        '// Elementy pub(crate) można wywołać z dowolnego miejsca w tej samej skrzyni\\n')

# visibility:pub(in path) items can only be called
multi(
    'msgid ""\n'
    '"// pub(in path) items can only be called from within the module specified\\n"\n'
    '"    // Error! function `public_function_in_my_mod` is private\\n"\n'
    '"    //my_mod::nested::public_function_in_my_mod();\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Elementy pub(in path) można wywołać tylko z podanego modułu\\n"\n'
    '"    // Błąd! funkcja `public_function_in_my_mod` jest prywatna\\n"\n'
    '"    //my_mod::nested::public_function_in_my_mod();\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# visibility:Private items of a module cannot be directly accessed
multi(
    'msgid ""\n'
    '"// Private items of a module cannot be directly accessed, even if\\n"\n'
    '"    // nested in a public module:\\n"\n',
    '"// Prywatne elementy modułu nie mogą być bezpośrednio dostępne, nawet\\n"\n'
    '"    // jeśli są zagnieżdżone w publicznym module:\\n"\n'
)

# visibility:Error! private_function is private (my_mod)
multi(
    'msgid ""\n'
    '"// Error! `private_function` is private\\n"\n'
    '"    //my_mod::private_function();\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `private_function` jest prywatna\\n"\n'
    '"    //my_mod::private_function();\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# visibility:Error! private_function is private (nested)
multi(
    'msgid ""\n'
    '"// Error! `private_function` is private\\n"\n'
    '"    //my_mod::nested::private_function();\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `private_function` jest prywatna\\n"\n'
    '"    //my_mod::nested::private_function();\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# visibility:Error! private_nested is a private module (function)
multi(
    'msgid ""\n'
    '"// Error! `private_nested` is a private module\\n"\n'
    '"    //my_mod::private_nested::function();\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `private_nested` jest prywatnym modułem\\n"\n'
    '"    //my_mod::private_nested::function();\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# visibility:Error! private_nested is a private module (restricted)
multi(
    'msgid ""\n'
    '"// Error! `private_nested` is a private module\\n"\n'
    '"    //my_mod::private_nested::restricted_function();\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `private_nested` jest prywatnym modułem\\n"\n'
    '"    //my_mod::private_nested::restricted_function();\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# ============================================================
# mod/struct_visibility.md
# ============================================================

# struct_visibility:3
multi(
    'msgid ""\n'
    '"Structs have an extra level of visibility with their fields. The visibility "\n'
    '"defaults to private, and can be overridden with the `pub` modifier. This "\n'
    '"visibility only matters when a struct is accessed from outside the module "\n'
    '"where it is defined, and has the goal of hiding information (encapsulation)."\n',
    '"Struktury mają dodatkowy poziom widoczności dla pól. Domyślnie prywatna, "\n'
    '"może być nadpisana modyfikatorem `pub`. Ta widoczność ma znaczenie tylko gdy "\n'
    '"struktura jest dostępna spoza modułu, w którym jest zdefiniowana, w celu "\n'
    '"ukrywania informacji (enkapsulacja)."\n'
)

comment('// A public struct with a public field of generic type `T`\\n',
        '// Publiczna struktura z publicznym polem ogólnego typu `T`\\n')
comment('// A public struct with a private field of generic type `T`\\n',
        '// Publiczna struktura z prywatnym polem ogólnego typu `T`\\n')
comment('// A public constructor method\\n', '// Publiczna metoda konstruktora\\n')
comment('// Public structs with public fields can be constructed as usual\\n',
        '// Publiczne struktury z publicznymi polami można konstruować normalnie\\n')
lit('public information')
comment('// and their fields can be normally accessed.\\n',
        '// a ich pola mogą być normalnie dostępne.\\n')
lit('The open box contains: {}')

# struct_visibility:Public structs with private fields cannot be constructed
multi(
    'msgid ""\n'
    '"// Public structs with private fields cannot be constructed using field "\n'
    '"names.\\n"\n'
    '"    // Error! `ClosedBox` has private fields\\n"\n'
    '"    //let closed_box = my::ClosedBox { contents: \\"classified "\n'
    '"information\\" };\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Publicznych struktur z prywatnymi polami nie można konstruować nazwami pól.\\n"\n'
    '"    // Błąd! `ClosedBox` ma prywatne pola\\n"\n'
    '"    //let closed_box = my::ClosedBox { contents: \\"classified "\n'
    '"information\\" };\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# struct_visibility:However structs with private fields can be created using public constructors
multi(
    'msgid ""\n'
    '"// However, structs with private fields can be created using\\n"\n'
    '"    // public constructors\\n"\n',
    '"// Jednak struktury z prywatnymi polami można tworzyć\\n"\n'
    '"    // używając publicznych konstruktorów\\n"\n'
)

lit('classified information')

# struct_visibility:private fields of a public struct cannot be accessed
multi(
    'msgid ""\n'
    '"// and the private fields of a public struct cannot be accessed.\\n"\n'
    '"    // Error! The `contents` field is private\\n"\n'
    '"    //println!(\\"The closed box contains: {}\\", _closed_box.contents);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// a prywatnych pól publicznej struktury nie można dostępować.\\n"\n'
    '"    // Błąd! Pole `contents` jest prywatne\\n"\n'
    '"    //println!(\\"The closed box contains: {}\\", _closed_box.contents);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

prose('[generics](../generics.md) and [methods](../fn/methods.md)',
      '[typy ogólne](../generics.md) i [metody](../fn/methods.md)')

# ============================================================
# mod/use.md
# ============================================================

# use:3
multi(
    'msgid ""\n'
    '"The `use` declaration can be used to bind a full path to a new name, for "\n'
    '"easier access. It is often used like this:"\n',
    '"Deklaracja `use` może być używana do powiązania pełnej ścieżki z nową nazwą "\n'
    '"dla łatwiejszego dostępu. Często używa się jej tak:"\n'
)

prose('You can use the `as` keyword to bind imports to a different name:',
      'Słowa kluczowego `as` można użyć, aby powiązać importy z inną nazwą:')
comment('// Bind the `deeply::nested::function` path to `other_function`.\\n',
        '// Powiąż ścieżkę `deeply::nested::function` z `other_function`.\\n')
lit('called `deeply::nested::function()`')
comment('// Easier access to `deeply::nested::function`\\n',
        '// Łatwiejszy dostęp do `deeply::nested::function`\\n')
lit('Entering block')

# use:This is equivalent to use deeply::nested::function as function
multi(
    'msgid ""\n'
    '"// This is equivalent to `use deeply::nested::function as function`.\\n"\n'
    '"        // This `function()` will shadow the outer one.\\n"\n',
    '"// To jest równoważne `use deeply::nested::function as function`.\\n"\n'
    '"        // Ta `function()` przesłania zewnętrzną.\\n"\n'
)

# use:`use` bindings have a local scope
multi(
    'msgid ""\n'
    '"// `use` bindings have a local scope. In this case, the\\n"\n'
    '"        // shadowing of `function()` is only in this block.\\n"\n',
    '"// Wiązania `use` mają zasięg lokalny. W tym przypadku\\n"\n'
    '"        // przesłanianie `function()` dotyczy tylko tego bloku.\\n"\n'
)

lit('Leaving block')

# use:pub use to re-export
multi(
    'msgid ""\n'
    '"You can also use `pub use` to re-export an item from a module, so it can be "\n'
    '"accessed through the module\'s public interface:"\n',
    '"Można też użyć `pub use` do ponownego eksportu elementu z modułu, "\n'
    '"aby był dostępny przez publiczny interfejs modułu:"\n'
)

# ============================================================
# mod/super.md
# ============================================================

# super:3
multi(
    'msgid ""\n'
    '"The `super` and `self` keywords can be used in the path to remove ambiguity "\n'
    '"when accessing items and to prevent unnecessary hardcoding of paths."\n',
    '"Słowa kluczowe `super` i `self` mogą być używane w ścieżce, aby usunąć "\n'
    '"niejednoznaczność przy dostępie do elementów i zapobiec niepotrzebnemu "\n'
    '"zakodowaniu ścieżek na stałe."\n'
)

lit('called `cool::function()`')
lit('called `my::function()`')
lit('called `my::cool::function()`')
comment("// Let's access all the functions named `function` from this scope!\\n",
        '// Uzyskajmy dostęp do wszystkich funkcji o nazwie `function` z tego zasięgu!\\n')
lit('called `my::indirect_call()`, that\\\\n> ')

# super:self refers to current module
multi(
    'msgid ""\n'
    '"// The `self` keyword refers to the current module scope - in this case "\n'
    '"`my`.\\n"\n'
    '"        // Calling `self::function()` and calling `function()` directly both "\n'
    '"give\\n"\n'
    '"        // the same result, because they refer to the same function.\\n"\n',
    '"// Słowo `self` odnosi się do bieżącego zasięgu modułu — w tym przypadku "\n'
    '"`my`.\\n"\n'
    '"        // Wywołanie `self::function()` i bezpośrednie `function()` dają\\n"\n'
    '"        // ten sam wynik, bo odnoszą się do tej samej funkcji.\\n"\n'
)

comment('// We can also use `self` to access another module inside `my`:\\n',
        '// Możemy też użyć `self` do dostępu do innego modułu wewnątrz `my`:\\n')

# super:super keyword refers to the parent scope
multi(
    'msgid ""\n'
    '"// The `super` keyword refers to the parent scope (outside the `my` "\n'
    '"module).\\n"\n',
    '"// Słowo `super` odnosi się do zasięgu nadrzędnego (poza modułem `my`).\\n"\n'
)

# super:This will bind to the cool::function in the crate scope
multi(
    'msgid ""\n'
    '"// This will bind to the `cool::function` in the *crate* scope.\\n"\n'
    '"        // In this case the crate scope is the outermost scope.\\n"\n',
    '"// To powiąże z `cool::function` w zasięgu *skrzyni*.\\n"\n'
    '"        // W tym przypadku zasięg skrzyni jest zasięgiem najbardziej zewnętrznym.\\n"\n'
)

# ============================================================
# mod/split.md
# ============================================================

# split:3
multi(
    'msgid ""\n'
    '"Modules can be mapped to a file/directory hierarchy. Let\'s break down the "\n'
    '"[visibility example](visibility.md) in files:"\n',
    '"Moduły mogą być mapowane na hierarchię plików/katalogów. Rozłóżmy "\n'
    '"[przykład widoczności](visibility.md) na pliki:"\n'
)

prose('In `split.rs`:', 'W `split.rs`:')

# split:This declaration will look for a file named my.rs
multi(
    'msgid ""\n'
    '"// This declaration will look for a file named `my.rs` and will\\n"\n'
    '"// insert its contents inside a module named `my` under this scope\\n"\n',
    '"// Ta deklaracja poszuka pliku o nazwie `my.rs` i wstawi\\n"\n'
    '"// jego zawartość do modułu `my` w tym zasięgu\\n"\n'
)

prose('In `my.rs`:', 'W `my.rs`:')

# split:Similarly mod inaccessible and mod nested
multi(
    'msgid ""\n'
    '"// Similarly `mod inaccessible` and `mod nested` will locate the\\n"\n'
    '"// `inaccessible.rs` and `nested.rs` files and insert them here under their\\n"\n'
    '"// respective modules\\n"\n',
    '"// Podobnie `mod inaccessible` i `mod nested` zlokalizują pliki\\n"\n'
    '"// `inaccessible.rs` i `nested.rs` i wstawią je tutaj w odpowiednich modułach\\n"\n'
)

lit('called `my::private_function()`')
lit('called `my::indirect_access()`, that\\\\n> ')
prose('In `my/nested.rs`:', 'W `my/nested.rs`:')
lit('called `my::nested::function()`')
lit('called `my::nested::private_function()`')
prose('In `my/inaccessible.rs`:', 'W `my/inaccessible.rs`:')
lit('called `my::inaccessible::public_function()`')
prose("Let's check that things still work as before:", 'Sprawdźmy, że wszystko wciąż działa jak wcześniej:')

# ============================================================
# crates.md
# ============================================================

# crates:3
multi(
    'msgid ""\n'
    '"A crate is a compilation unit in Rust. Whenever `rustc some_file.rs` is "\n'
    '"called, `some_file.rs` is treated as the _crate file_. If `some_file.rs` has "\n'
    '"`mod` declarations in it, then the contents of the module files would be "\n'
    '"inserted in places where `mod` declarations in the crate file are found, "\n'
    '"_before_ running the compiler over it. In other words, modules do _not_ get "\n'
    '"compiled individually, only crates get compiled."\n',
    '"Skrzynia (crate) to jednostka kompilacji w Rust. Gdy wywoływane jest "\n'
    '"`rustc some_file.rs`, plik `some_file.rs` jest traktowany jako _plik skrzyni_. "\n'
    '"Jeśli `some_file.rs` zawiera deklaracje `mod`, zawartość plików modułów jest "\n'
    '"wstawiana w miejscach deklaracji `mod` w pliku skrzyni, _przed_ uruchomieniem "\n'
    '"kompilatora. Innymi słowy, moduły _nie_ są kompilowane osobno — kompilowane są tylko skrzynie."\n'
)

# crates:A crate can be compiled into a binary
multi(
    'msgid ""\n'
    '"A crate can be compiled into a binary or into a library. By default, `rustc` "\n'
    '"will produce a binary from a crate. This behavior can be overridden by "\n'
    '"passing the `--crate-type` flag to `lib`."\n',
    '"Skrzynię można skompilować do programu binarnego lub biblioteki. Domyślnie "\n'
    '"`rustc` tworzy program binarny. Zachowanie to można zmienić przekazując "\n'
    '"flagę `--crate-type` z wartością `lib`."\n'
)

prose("Let's create a library, and then see how to link it to another crate.",
      'Utwórzmy bibliotekę, a następnie zobaczmy jak połączyć ją z inną skrzynią.')
prose('In `rary.rs`:', 'W `rary.rs`:')
lit('called rary\'s `public_function()`')
lit('called rary\'s `private_function()`')
lit('called rary\'s `indirect_access()`, that\\\\n> ')

# crates/lib:Libraries get prefixed with lib
multi(
    'msgid ""\n'
    '"Libraries get prefixed with \\"lib\\", and by default they get named after "\n'
    '"their crate file, but this default name can be overridden by passing the `--"\n'
    '"crate-name` option to `rustc` or by using the [`crate_name` attribute](../"\n'
    '"attribute/crate.md)."\n',
    '"Biblioteki mają prefiks \\"lib\\" i domyślnie są nazywane jak plik skrzyni, "\n'
    '"ale tę domyślną nazwę można zmienić przekazując opcję `--crate-name` do `rustc` "\n'
    '"lub używając atrybutu [`crate_name`](../attribute/crate.md)."\n'
)

# crates/using_lib:To link a crate
multi(
    'msgid ""\n'
    '"To link a crate to this new library you may use `rustc`\'s `--extern` flag. "\n'
    '"All of its items will then be imported under a module named the same as the "\n'
    '"library. This module generally behaves the same way as any other module."\n',
    '"Aby połączyć skrzynię z tą nową biblioteką, użyj flagi `--extern` `rustc`. "\n'
    '"Wszystkie jej elementy zostaną zaimportowane do modułu o tej samej nazwie co "\n'
    '"biblioteka. Ten moduł ogólnie zachowuje się tak samo jak każdy inny moduł."\n'
)

# crates/using_lib:extern crate rary May be required
multi(
    'msgid ""\n'
    '"// extern crate rary; // May be required for Rust 2015 edition or earlier\\n"\n',
    '"// extern crate rary; // Może być wymagane dla edycji Rust 2015 lub wcześniejszej\\n"\n'
)

# crates/using_lib:Error! private_function is private (rary)
multi(
    'msgid ""\n'
    '"// Error! `private_function` is private\\n"\n'
    '"    //rary::private_function();\\n"\n',
    '"// Błąd! `private_function` jest prywatna\\n"\n'
    '"    //rary::private_function();\\n"\n'
)

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
