#!/usr/bin/env python3
# Etap 7: Zakresy — własność, pożyczanie, czasy życia
# Pokrywa: variable_bindings/scope.md, scope.md, scope/raii.md,
#          scope/move.md, scope/move/mut.md, scope/move/partial_move.md,
#          scope/borrow.md, scope/borrow/mut.md, scope/borrow/alias.md,
#          scope/borrow/ref.md, scope/lifetime.md, scope/lifetime/explicit.md,
#          scope/lifetime/fn.md, scope/lifetime/methods.md, scope/lifetime/struct.md,
#          scope/lifetime/trait.md, scope/lifetime/lifetime_bounds.md,
#          scope/lifetime/lifetime_coercion.md, scope/lifetime/static_lifetime.md,
#          scope/lifetime/elision.md

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

# ─── variable_bindings/scope.md ────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Variable bindings have a scope, and are constrained to live in a _block_. A "\n'
    '"block is a collection of statements enclosed by braces `{}`."'
    '\n',
    '"Powiązania zmiennych mają zakres i są ograniczone do życia w _bloku_. "\n'
    '"Blok to kolekcja instrukcji otoczonych nawiasami klamrowymi `{}`."'
    '\n'
)

multi(
    'msgid ""\n'
    '"Also, [variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing) "\n'
    '"is allowed."'
    '\n',
    '"Dozwolone jest również [przesłanianie zmiennych](https://en.wikipedia.org/wiki/Variable_shadowing)."'
    '\n'
)

# ─── scope.md ──────────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Scopes play an important part in ownership, borrowing, and lifetimes. That "\n'
    '"is, they indicate to the compiler when borrows are valid, when resources can "\n'
    '"be freed, and when variables are created or destroyed."'
    '\n',
    '"Zakresy odgrywają ważną rolę we własności, pożyczaniu i czasach życia. "\n'
    '"Wskazują kompilatorowi, kiedy pożyczenia są prawidłowe, kiedy zasoby mogą "\n'
    '"zostać zwolnione oraz kiedy zmienne są tworzone lub niszczone."'
    '\n'
)

# ─── scope/raii.md ─────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Variables in Rust do more than just hold data in the stack: they also _own_ "\n'
    '"resources, e.g. `Box<T>` owns memory in the heap. Rust enforces [RAII]"\n'
    '"(https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization) "\n'
    '"(Resource Acquisition Is Initialization), so whenever an object goes out of "\n'
    '"scope, its destructor is called and its owned resources are freed."'
    '\n',
    '"Zmienne w Rust nie tylko przechowują dane na stosie: _posiadają_ też zasoby, "\n'
    '"np. `Box<T>` posiada pamięć na stercie. Rust wymusza [RAII]"\n'
    '"(https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization) "\n'
    '"(ang. Resource Acquisition Is Initialization), więc gdy obiekt wychodzi poza "\n'
    '"zakres, wywoływany jest jego destruktor i zwalniane są posiadane zasoby."'
    '\n'
)

multi(
    'msgid ""\n'
    '"This behavior shields against _resource leak_ bugs, so you\'ll never have to "\n'
    '"manually free memory or worry about memory leaks again! Here\'s a quick "\n'
    '"showcase:"'
    '\n',
    '"To zachowanie chroni przed błędami _wycieku zasobów_, więc nigdy nie trzeba "\n'
    '"ręcznie zwalniać pamięci ani martwić się o wycieki pamięci! Oto krótki pokaz:"'
    '\n'
)

comment('// raii.rs\\n', '// raii.rs\\n')
comment('// Allocate an integer on the heap\\n', '// Alokuj liczbę całkowitą na stercie\\n')
comment('// `_box1` is destroyed here, and memory gets freed\\n',
        '// `_box1` jest tu niszczony, a pamięć zostaje zwolniona\\n')
comment('// A nested scope:\\n', '// Zagnieżdżony zakres:\\n')
comment('// `_box3` is destroyed here, and memory gets freed\\n',
        '// `_box3` jest tu niszczony, a pamięć zostaje zwolniona\\n')
comment('// `_box2` is destroyed here, and memory gets freed\\n',
        '// `_box2` jest tu niszczony, a pamięć zostaje zwolniona\\n')

multi(
    'msgid ""\n'
    '"// Creating lots of boxes just for fun\\n"\n'
    '"    // There\'s no need to manually free memory!\\n"'
    '\n',
    '"// Tworzymy mnóstwo pudełek dla zabawy\\n"\n'
    '"    // Nie trzeba ręcznie zwalniać pamięci!\\n"'
    '\n'
)

prose('No leaks here!', 'Żadnych wycieków!')
prose('Destructor', 'Destruktor')
verbatim('\\"ToDrop is being dropped\\"')
verbatim('\\"Made a ToDrop!\\"')
verbatim('[Box](../std/box.md)')

multi(
    'msgid ""\n'
    '"Of course, we can double check for memory errors using [`valgrind`](http://"\n'
    '"valgrind.org/info/):"'
    '\n',
    '"Oczywiście możemy sprawdzić błędy pamięci za pomocą [`valgrind`](http://"\n'
    '"valgrind.org/info/):"'
    '\n'
)

multi(
    'msgid ""\n'
    '"The notion of a destructor in Rust is provided through the [`Drop`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.Drop.html) trait. The destructor is called "\n'
    '"when the resource goes out of scope. This trait is not required to be "\n'
    '"implemented for every type, only implement it for your type if you require "\n'
    '"its own destructor logic."'
    '\n',
    '"Pojęcie destruktora w Rust jest zapewniane przez cechę [`Drop`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.Drop.html). Destruktor jest wywoływany, gdy "\n'
    '"zasób wychodzi poza zakres. Cecha ta nie musi być implementowana dla każdego "\n'
    '"typu — implementuj ją tylko wtedy, gdy typ wymaga własnej logiki destruktora."'
    '\n'
)

multi(
    'msgid ""\n'
    '"Run the below example to see how the [`Drop`](https://doc.rust-lang.org/std/"\n'
    '"ops/trait.Drop.html) trait works. When the variable in the `main` function "\n'
    '"goes out of scope the custom destructor will be invoked."'
    '\n',
    '"Uruchom poniższy przykład, aby zobaczyć, jak działa cecha [`Drop`](https://"\n'
    '"doc.rust-lang.org/std/ops/trait.Drop.html). Gdy zmienna w funkcji `main` "\n'
    '"wyjdzie poza zakres, zostanie wywołany własny destruktor."'
    '\n'
)

# ─── scope/move.md ─────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Because variables are in charge of freeing their own resources, **resources "\n'
    '"can only have one owner**. This prevents resources from being freed more "\n'
    '"than once. Note that not all variables own resources (e.g. [references](../"\n'
    '"flow_control/match/destructuring/destructure_pointers.md))."'
    '\n',
    '"Ponieważ zmienne są odpowiedzialne za zwalnianie własnych zasobów, **zasoby "\n'
    '"mogą mieć tylko jednego właściciela**. Zapobiega to wielokrotnemu zwalnianiu "\n'
    '"zasobów. Zauważ, że nie wszystkie zmienne posiadają zasoby "\n'
    '"(np. [referencje](../flow_control/match/destructuring/destructure_pointers.md))."'
    '\n'
)

multi(
    'msgid ""\n'
    '"When doing assignments (`let x = y`) or passing function arguments by value "\n'
    '"(`foo(x)`), the _ownership_ of the resources is transferred. In Rust-speak, "\n'
    '"this is known as a _move_."'
    '\n',
    '"Przy przypisaniach (`let x = y`) lub przekazywaniu argumentów funkcji przez "\n'
    '"wartość (`foo(x)`) _własność_ zasobów jest przenoszona. W żargonie Rust-a "\n'
    '"nazywa się to _przeniesieniem_ (ang. move)."'
    '\n'
)

multi(
    'msgid ""\n'
    '"After moving resources, the previous owner can no longer be used. This "\n'
    '"avoids creating dangling pointers."'
    '\n',
    '"Po przeniesieniu zasobów poprzedni właściciel nie może już być używany. "\n'
    '"Zapobiega to tworzeniu wiszących wskaźników."'
    '\n'
)

comment('// This function takes ownership of the heap allocated memory\\n',
        '// Ta funkcja przejmuje własność pamięci zaalokowanej na stercie\\n')
verbatim('\\"Destroying a box that contains {}\\"')
comment('// `c` is destroyed and the memory freed\\n',
        '// `c` jest niszczony, a pamięć zwolniona\\n')
comment('// _Stack_ allocated integer\\n',
        '// Liczba całkowita zaalokowana na _stosie_\\n')
comment('// *Copy* `x` into `y` - no resources are moved\\n',
        '// *Kopiuj* `x` do `y` - żadne zasoby nie są przenoszone\\n')
comment('// Both values can be independently used\\n',
        '// Obie wartości mogą być niezależnie używane\\n')
verbatim('\\"x is {}, and y is {}\\"')
comment('// `a` is a pointer to a _heap_ allocated integer\\n',
        '// `a` jest wskaźnikiem do liczby całkowitej zaalokowanej na _stercie_\\n')
verbatim('\\"a contains: {}\\"')
comment('// *Move* `a` into `b`\\n',
        '// *Przenieś* `a` do `b`\\n')

multi(
    'msgid ""\n'
    '"// The pointer address of `a` is copied (not the data) into `b`.\\n"\n'
    '"    // Both are now pointers to the same heap allocated data, but\\n"\n'
    '"    // `b` now owns it.\\n"'
    '\n',
    '"// Adres wskaźnika `a` jest kopiowany (nie dane) do `b`.\\n"\n'
    '"    // Oba są teraz wskaźnikami do tych samych danych na stercie, ale\\n"\n'
    '"    // `b` teraz je posiada.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Error! `a` can no longer access the data, because it no longer owns the\\n"\n'
    '"    // heap memory\\n"\n'
    '"    //println!(\\\"a contains: {}\\\", a);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"'
    '\n',
    '"// Błąd! `a` nie może już uzyskać dostępu do danych, bo nie posiada już\\n"\n'
    '"    // pamięci na stercie\\n"\n'
    '"    //println!(\\\"a contains: {}\\\", a);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"'
    '\n'
)

comment('// This function takes ownership of the heap allocated memory from `b`\\n',
        '// Ta funkcja przejmuje własność pamięci na stercie od `b`\\n')

multi(
    'msgid ""\n'
    '"// Since the heap memory has been freed at this point, this action would\\n"\n'
    '"    // result in dereferencing freed memory, but it\'s forbidden by the compiler\\n"\n'
    '"    // Error! Same reason as the previous Error\\n"\n'
    '"    //println!(\\\"b contains: {}\\\", b);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n'
    '"    // destroy_box(b);\\n"'
    '\n',
    '"// Ponieważ pamięć na stercie została już w tym miejscu zwolniona,\\n"\n'
    '"    // ta akcja spowodowałaby wyłuskanie zwolnionej pamięci,\\n"\n'
    '"    // co jest zabronione przez kompilator\\n"\n'
    '"    // Błąd! Taki sam powód jak poprzedni błąd\\n"\n'
    '"    //println!(\\\"b contains: {}\\\", b);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
    '"    // destroy_box(b);\\n"'
    '\n'
)

# ─── scope/move/mut.md ─────────────────────────────────────────────────────

prose('Mutability of data can be changed when ownership is transferred.',
      'Mutowalność danych może zostać zmieniona przy przenoszeniu własności.')

verbatim('\\"immutable_box contains {}\\"')
comment('// *Move* the box, changing the ownership (and mutability)\\n',
        '// *Przenieś* pudełko, zmieniając własność (i mutowalność)\\n')
verbatim('\\"mutable_box contains {}\\"')
comment('// Modify the contents of the box\\n',
        '// Zmodyfikuj zawartość pudełka\\n')
verbatim('\\"mutable_box now contains {}\\"')

multi(
    'msgid ""\n'
    '"// Mutability error\\n"\n'
    '"    //*immutable_box = 4;\\n"'
    '\n',
    '"// Błąd mutowalności\\n"\n'
    '"    //*immutable_box = 4;\\n"'
    '\n'
)

# ─── scope/move/partial_move.md ────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Within the [destructuring](../../flow_control/match/destructuring.md) of a "\n'
    '"single variable, both `by-move` and `by-reference` pattern bindings can be "\n'
    '"used at the same time. Doing this will result in a _partial move_ of the "\n'
    '"variable, which means that parts of the variable will be moved while other "\n'
    '"parts remain. In such a case, the parent variable cannot be used afterwards "\n'
    '"as a whole, however the parts that are only referenced (and not moved) can "\n'
    '"still be used."'
    '\n',
    '"Podczas [destrukturyzacji](../../flow_control/match/destructuring.md) jednej "\n'
    '"zmiennej można jednocześnie użyć powiązań wzorców `by-move` i `by-reference`. "\n'
    '"Spowoduje to _częściowe przeniesienie_ zmiennej, co oznacza, że części "\n'
    '"zmiennej zostaną przeniesione, podczas gdy inne pozostaną. W takim przypadku "\n'
    '"zmienna nadrzędna nie może być później użyta jako całość, jednak części, do "\n'
    '"których tylko się odwołano (bez przenoszenia), mogą być nadal używane."'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Error! cannot move out of a type which implements the `Drop` trait\\n"\n'
    '"    //impl Drop for Person {\\n"\n'
    '"    //    fn drop(&mut self) {\\n"\n'
    '"    //        println!(\\\"Dropping the person struct {:?}\\\", self)\\n"\n'
    '"    //    }\\n"\n'
    '"    //}\\n"\n'
    '"    //\\n"'
    '\n',
    '"// Błąd! nie można przenieść z typu implementującego cechę `Drop`\\n"\n'
    '"    //impl Drop for Person {\\n"\n'
    '"    //    fn drop(&mut self) {\\n"\n'
    '"    //        println!(\\\"Dropping the person struct {:?}\\\", self)\\n"\n'
    '"    //    }\\n"\n'
    '"    //}\\n"\n'
    '"    //\\n"'
    '\n'
)

comment('// `name` is moved out of person, but `age` is referenced\\n',
        '// `name` jest przenoszone z person, ale `age` jest referencjonowane\\n')
verbatim('\\"The person\'s age is {}\\"')
verbatim('\\"The person\'s name is {}\\"')

multi(
    'msgid ""\n'
    '"// Error! borrow of partially moved value: `person` partial move occurs\\n"\n'
    '"    //println!(\\\"The person struct is {:?}\\\", person);\\n"'
    '\n',
    '"// Błąd! pożyczenie częściowo przeniesionej wartości: następuje częściowe przeniesienie `person`\\n"\n'
    '"    //println!(\\\"The person struct is {:?}\\\", person);\\n"'
    '\n'
)

comment('// `person` cannot be used but `person.age` can be used as it is not moved\\n',
        '// `person` nie można użyć, ale `person.age` można, bo nie zostało przeniesione\\n')

verbatim('\\"The person\'s age from person struct is {}\\"')

multi(
    'msgid ""\n'
    '"(In this example, we store the `age` variable on the heap to illustrate the "\n'
    '"partial move: deleting `ref` in the above code would give an error as the "\n'
    '"ownership of `person.age` would be moved to the variable `age`. If `Person."\n'
    '"age` were stored on the stack, `ref` would not be required as the definition "\n'
    '"of `age` would copy the data from the struct without moving it.)"'
    '\n',
    '"(W tym przykładzie przechowujemy zmienną `age` na stercie, aby zilustrować "\n'
    '"częściowe przeniesienie: usunięcie `ref` w powyższym kodzie spowodowałoby "\n'
    '"błąd, ponieważ własność `person.age` zostałaby przeniesiona do zmiennej "\n'
    '"`age`. Gdyby `Person.age` było przechowywane na stosie, `ref` nie byłoby "\n'
    '"wymagane, ponieważ definicja `age` skopiowałaby dane ze struktury bez przenoszenia.)"'
    '\n'
)

verbatim('[destructuring](../../flow_control/match/destructuring.md)')

# ─── scope/borrow.md ───────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Most of the time, we\'d like to access data without taking ownership over it. "\n'
    '"To accomplish this, Rust uses a _borrowing_ mechanism. Instead of passing "\n'
    '"objects by value (`T`), objects can be passed by reference (`&T`)."'
    '\n',
    '"Przez większość czasu chcemy uzyskać dostęp do danych bez przejmowania nad "\n'
    '"nimi własności. Aby to osiągnąć, Rust używa mechanizmu _pożyczania_. Zamiast "\n'
    '"przekazywać obiekty przez wartość (`T`), obiekty można przekazywać przez "\n'
    '"referencję (`&T`)."'
    '\n'
)

multi(
    'msgid ""\n'
    '"The compiler statically guarantees (via its borrow checker) that references "\n'
    '"_always_ point to valid objects. That is, while references to an object "\n'
    '"exist, the object cannot be destroyed."'
    '\n',
    '"Kompilator statycznie gwarantuje (poprzez analizator pożyczeń), że referencje "\n'
    '"_zawsze_ wskazują na prawidłowe obiekty. To znaczy, że dopóki istnieją "\n'
    '"referencje do obiektu, obiekt nie może zostać zniszczony."'
    '\n'
)

comment('// This function takes ownership of a box and destroys it\\n',
        '// Ta funkcja przejmuje własność pudełka i niszczy je\\n')
verbatim('\\"Destroying box that contains {}\\"')
comment('// This function borrows an i32\\n',
        '// Ta funkcja pożycza i32\\n')
verbatim('\\"This int is: {}\\"')

multi(
    'msgid ""\n'
    '"// Create a boxed i32 in the heap, and an i32 on the stack\\n"\n'
    '"    // Remember: numbers can have arbitrary underscores added for readability\\n"\n'
    '"    // 5_i32 is the same as 5i32\\n"'
    '\n',
    '"// Utwórz opakowane i32 na stercie i i32 na stosie\\n"\n'
    '"    // Pamiętaj: do liczb można dodawać podkreślenia dla czytelności\\n"\n'
    '"    // 5_i32 to to samo co 5i32\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Borrow the contents of the box. Ownership is not taken,\\n"\n'
    '"    // so the contents can be borrowed again.\\n"'
    '\n',
    '"// Pożycz zawartość pudełka. Własność nie jest przejmowana,\\n"\n'
    '"    // więc zawartość może być ponownie pożyczona.\\n"'
    '\n'
)

comment('// Take a reference to the data contained inside the box\\n',
        '// Pobierz referencję do danych zawartych w pudełku\\n')

multi(
    'msgid ""\n'
    '"// Error!\\n"\n'
    '"        // Can\'t destroy `boxed_i32` while the inner value is borrowed later in scope.\\n"'
    '\n',
    '"// Błąd!\\n"\n'
    '"        // Nie można zniszczyć `boxed_i32`, gdy wewnętrzna wartość jest pożyczona później w zakresie.\\n"'
    '\n'
)

comment('// Attempt to borrow `_ref_to_i32` after inner value is destroyed\\n',
        '// Próba pożyczenia `_ref_to_i32` po zniszczeniu wewnętrznej wartości\\n')
comment('// `_ref_to_i32` goes out of scope and is no longer borrowed.\\n',
        '// `_ref_to_i32` wychodzi poza zakres i nie jest już pożyczone.\\n')
comment('// `boxed_i32` can now give up ownership to `eat_box_i32` and be destroyed\\n',
        '// `boxed_i32` może teraz oddać własność do `eat_box_i32` i zostać zniszczone\\n')

# ─── scope/borrow/mut.md ───────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Mutable data can be mutably borrowed using `&mut T`. This is called a "\n'
    '"_mutable reference_ and gives read/write access to the borrower. In "\n'
    '"contrast, `&T` borrows the data via an immutable reference, and the borrower "\n'
    '"can read the data but not modify it:"'
    '\n',
    '"Mutowalne dane można pożyczać mutowalnie za pomocą `&mut T`. Nazywa się to "\n'
    '"_mutowalną referencją_ i daje pożyczkobiorcy dostęp do odczytu i zapisu. "\n'
    '"Dla porównania, `&T` pożycza dane przez niemutowalną referencję, a "\n'
    '"pożyczkobiorca może odczytać dane, ale nie modyfikować ich:"'
    '\n'
)

comment('// `&\'static str` is a reference to a string allocated in read only memory\\n',
        '// `&\'static str` to referencja do łańcucha znaków zaalokowanego w pamięci tylko do odczytu\\n')
comment('// This function takes a reference to a book\\n',
        '// Ta funkcja przyjmuje referencję do książki\\n')
verbatim('\\"I immutably borrowed {} - {} edition\\"')

comment('// This function takes a reference to a mutable book and changes `year` to 2014\\n',
        '// Ta funkcja przyjmuje referencję do mutowalnej książki i zmienia `year` na 2014\\n')

verbatim('\\"I mutably borrowed {} - {} edition\\"')
comment('// Create an immutable Book named `immutabook`\\n',
        '// Utwórz niemutowalną Book o nazwie `immutabook`\\n')
comment('// string literals have type `&\'static str`\\n',
        '// literały łańcuchowe mają typ `&\'static str`\\n')
verbatim('\\"Douglas Hofstadter\\"')
verbatim('\\"Gödel, Escher, Bach\\"')
comment('// Create a mutable copy of `immutabook` and call it `mutabook`\\n',
        '// Utwórz mutowalną kopię `immutabook` i nazwij ją `mutabook`\\n')
comment('// Immutably borrow an immutable object\\n',
        '// Niemutowalnie pożycz niemutowalny obiekt\\n')
comment('// Immutably borrow a mutable object\\n',
        '// Niemutowalnie pożycz mutowalny obiekt\\n')
comment('// Borrow a mutable object as mutable\\n',
        '// Pożycz mutowalny obiekt jako mutowalny\\n')
comment('// Error! Cannot borrow an immutable object as mutable\\n',
        '// Błąd! Nie można pożyczyć niemutowalnego obiektu jako mutowalnego\\n')
verbatim('[`static`](../lifetime/static_lifetime.md)')

# ─── scope/borrow/alias.md ─────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Data can be immutably borrowed any number of times, but while immutably "\n'
    '"borrowed, the original data can\'t be mutably borrowed. On the other hand, "\n'
    '"only _one_ mutable borrow is allowed at a time. The original data can be "\n'
    '"borrowed again only _after_ the mutable reference has been used for the last "\n'
    '"time."'
    '\n',
    '"Dane można pożyczać niemutowalnie dowolną liczbę razy, ale gdy są pożyczane "\n'
    '"niemutowalnie, oryginalne dane nie mogą być pożyczane mutowalnie. Z drugiej "\n'
    '"strony, dozwolone jest tylko _jedno_ mutowalne pożyczenie naraz. Oryginalne "\n'
    '"dane można ponownie pożyczyć dopiero _po_ ostatnim użyciu mutowalnej referencji."'
    '\n'
)

comment('// Data can be accessed via the references and the original owner\\n',
        '// Dane mogą być dostępne przez referencje i oryginalnego właściciela\\n')

multi(
    'msgid ""\n'
    '"// Error! Can\'t borrow `point` as mutable because it\'s currently\\n"\n'
    '"    // borrowed as immutable.\\n"\n'
    '"    // let mutable_borrow = &mut point;\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"'
    '\n',
    '"// Błąd! Nie można pożyczyć `point` mutowalnie, bo jest aktualnie\\n"\n'
    '"    // pożyczone niemutowalnie.\\n"\n'
    '"    // let mutable_borrow = &mut point;\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"'
    '\n'
)

comment('// The borrowed values are used again here\\n',
        '// Pożyczone wartości są tu ponownie używane\\n')

multi(
    'msgid ""\n'
    '"// The immutable references are no longer used for the rest of the code so\\n"\n'
    '"    // it is possible to reborrow with a mutable reference.\\n"'
    '\n',
    '"// Niemutowalne referencje nie są już używane w pozostałej części kodu,\\n"\n'
    '"    // więc można ponownie pożyczyć z mutowalną referencją.\\n"'
    '\n'
)

comment('// Change data via mutable reference\\n',
        '// Zmień dane przez mutowalną referencję\\n')

multi(
    'msgid ""\n'
    '"// Error! Can\'t borrow `point` as immutable because it\'s currently\\n"\n'
    '"    // borrowed as mutable.\\n"\n'
    '"    // let y = &point.y;\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"'
    '\n',
    '"// Błąd! Nie można pożyczyć `point` niemutowalnie, bo jest aktualnie\\n"\n'
    '"    // pożyczone mutowalnie.\\n"\n'
    '"    // let y = &point.y;\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Error! Can\'t print because `println!` takes an immutable reference.\\n"\n'
    '"    // println!(\\\"Point Z coordinate is {}\\\", point.z);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"'
    '\n',
    '"// Błąd! Nie można drukować, bo `println!` przyjmuje niemutowalną referencję.\\n"\n'
    '"    // println!(\\\"Point Z coordinate is {}\\\", point.z);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"'
    '\n'
)

comment('// Ok! Mutable references can be passed as immutable to `println!`\\n',
        '// Ok! Mutowalne referencje mogą być przekazane jako niemutowalne do `println!`\\n')

multi(
    'msgid ""\n'
    '"// The mutable reference is no longer used for the rest of the code so it\\n"\n'
    '"    // is possible to reborrow\\n"'
    '\n',
    '"// Mutowalna referencja nie jest już używana w pozostałej części kodu,\\n"\n'
    '"    // więc można ponownie pożyczyć\\n"'
    '\n'
)

verbatim('\\"Point has coordinates: ({}, {}, {})\\"')
verbatim('\\"Point now has coordinates: ({}, {}, {})\\"')

# ─── scope/borrow/ref.md ───────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"When doing pattern matching or destructuring via the `let` binding, the "\n'
    '"`ref` keyword can be used to take references to the fields of a struct/"\n'
    '"tuple. The example below shows a few instances where this can be useful:"'
    '\n',
    '"Podczas dopasowywania wzorców lub destrukturyzacji przez powiązanie `let`, "\n'
    '"słowo kluczowe `ref` może być użyte do pobrania referencji do pól struktury/"\n'
    '"krotki. Poniższy przykład pokazuje kilka przypadków, gdy może to być przydatne:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// A `ref` borrow on the left side of an assignment is equivalent to\\n"\n'
    '"    // an `&` borrow on the right side.\\n"'
    '\n',
    '"// Pożyczenie `ref` po lewej stronie przypisania jest równoważne\\n"\n'
    '"    // pożyczeniu `&` po prawej stronie.\\n"'
    '\n'
)

verbatim('\\"ref_c1 equals ref_c2: {}\\"')
comment('// `ref` is also valid when destructuring a struct.\\n',
        '// `ref` jest również prawidłowe przy destrukturyzacji struktury.\\n')
comment('// `ref_to_x` is a reference to the `x` field of `point`.\\n',
        '// `ref_to_x` to referencja do pola `x` w `point`.\\n')
comment('// Return a copy of the `x` field of `point`.\\n',
        '// Zwróć kopię pola `x` z `point`.\\n')
comment('// A mutable copy of `point`\\n',
        '// Mutowalna kopia `point`\\n')
comment('// `ref` can be paired with `mut` to take mutable references.\\n',
        '// `ref` można łączyć z `mut`, aby pobierać mutowalne referencje.\\n')
comment('// Mutate the `y` field of `mutable_point` via a mutable reference.\\n',
        '// Mutuj pole `y` w `mutable_point` przez mutowalną referencję.\\n')
verbatim('\\"point is ({}, {})\\"')
verbatim('\\"mutable_point is ({}, {})\\"')
comment('// A mutable tuple that includes a pointer\\n',
        '// Mutowalna krotka zawierająca wskaźnik\\n')
comment('// Destructure `mutable_tuple` to change the value of `last`.\\n',
        '// Destrukturyzuj `mutable_tuple`, aby zmienić wartość `last`.\\n')
verbatim('\\"tuple is {:?}\\"')

# ─── scope/lifetime.md ─────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"A _lifetime_ is a construct the compiler (or more specifically, its _borrow "\n'
    '"checker_) uses to ensure all borrows are valid. Specifically, a variable\'s "\n'
    '"lifetime begins when it is created and ends when it is destroyed. While "\n'
    '"lifetimes and scopes are often referred to together, they are not the same."'
    '\n',
    '"_Czas życia_ to konstrukt używany przez kompilator (dokładniej: jego _analizator "\n'
    '"pożyczeń_) do zapewnienia, że wszystkie pożyczenia są prawidłowe. Konkretnie, "\n'
    '"czas życia zmiennej zaczyna się, gdy jest tworzona, a kończy, gdy jest niszczona. "\n'
    '"Choć czasy życia i zakresy są często wymieniane razem, nie są tym samym."'
    '\n'
)

multi(
    'msgid ""\n'
    '"Take, for example, the case where we borrow a variable via `&`. The borrow "\n'
    '"has a lifetime that is determined by where it is declared. As a result, the "\n'
    '"borrow is valid as long as it ends before the lender is destroyed. However, "\n'
    '"the scope of the borrow is determined by where the reference is used."'
    '\n',
    '"Weźmy na przykład przypadek, gdy pożyczamy zmienną przez `&`. Pożyczenie ma "\n'
    '"czas życia określony przez miejsce jego deklaracji. W rezultacie pożyczenie "\n'
    '"jest prawidłowe, dopóki kończy się przed zniszczeniem pożyczającego. Jednak "\n'
    '"zakres pożyczenia jest określony przez miejsce użycia referencji."'
    '\n'
)

multi(
    'msgid ""\n'
    '"In the following example and in the rest of this section, we will see how "\n'
    '"lifetimes relate to scopes, as well as how the two differ."'
    '\n',
    '"W poniższym przykładzie i w pozostałej części tej sekcji zobaczymy, jak czasy "\n'
    '"życia odnoszą się do zakresów oraz czym się od siebie różnią."'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Lifetimes are annotated below with lines denoting the creation\\n"\n'
    '"// and destruction of each variable.\\n"\n'
    '"// `i` has the longest lifetime because its scope entirely encloses\\n"\n'
    '"// both `borrow1` and `borrow2`. The duration of `borrow1` compared\\n"\n'
    '"// to `borrow2` is irrelevant since they are disjoint.\\n"'
    '\n',
    '"// Czasy życia są adnotowane poniżej liniami oznaczającymi tworzenie\\n"\n'
    '"// i niszczenie każdej zmiennej.\\n"\n'
    '"// `i` ma najdłuższy czas życia, bo jego zakres całkowicie obejmuje\\n"\n'
    '"// zarówno `borrow1`, jak i `borrow2`. Czas trwania `borrow1` względem\\n"\n'
    '"// `borrow2` jest nieistotny, bo są rozłączne.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Lifetime for `i` starts. ────────────────┐\\n"\n'
    '"    //                                                     │\\n"'
    '\n',
    '"// Czas życia `i` zaczyna się. ────────────────┐\\n"\n'
    '"    //                                                     │\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// `borrow1` lifetime starts. ──┐│\\n"\n'
    '"        //                                                ││\\n"'
    '\n',
    '"// Czas życia `borrow1` zaczyna się. ──┐│\\n"\n'
    '"        //                                                ││\\n"'
    '\n'
)

verbatim('\\"borrow1: {}\\"')
verbatim('//                                                   │\\n')
verbatim('//              ││\\n')

multi(
    'msgid ""\n'
    '"// `borrow1` ends. ─────────────────────────────────┘│\\n"\n'
    '"    //                                                     │\\n"\n'
    '"    //                                                     │\\n"'
    '\n',
    '"// `borrow1` kończy się. ─────────────────────────────────┘│\\n"\n'
    '"    //                                                     │\\n"\n'
    '"    //                                                     │\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// `borrow2` lifetime starts. ──┐│\\n"\n'
    '"        //                                                ││\\n"'
    '\n',
    '"// Czas życia `borrow2` zaczyna się. ──┐│\\n"\n'
    '"        //                                                ││\\n"'
    '\n'
)

verbatim('\\"borrow2: {}\\"')

multi(
    'msgid ""\n'
    '"// `borrow2` ends. ─────────────────────────────────┘│\\n"\n'
    '"    //                                                     │\\n"'
    '\n',
    '"// `borrow2` kończy się. ─────────────────────────────────┘│\\n"\n'
    '"    //                                                     │\\n"'
    '\n'
)

comment('// Lifetime ends. ─────────────────────────────────────┘\\n',
        '// Czas życia kończy się. ─────────────────────────────────────┘\\n')

multi(
    'msgid ""\n'
    '"Note that no names or types are assigned to label lifetimes. This restricts "\n'
    '"how lifetimes will be able to be used as we will see."'
    '\n',
    '"Zauważ, że żadne nazwy ani typy nie są przypisywane do etykiet czasów życia. "\n'
    '"Ogranicza to sposób, w jaki czasy życia będą mogły być używane, jak zobaczymy."'
    '\n'
)

# ─── scope/lifetime/explicit.md ────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"The borrow checker uses explicit lifetime annotations to determine how long "\n'
    '"references should be valid. In cases where lifetimes are not elided[^1], "\n'
    '"Rust requires explicit annotations to determine what the lifetime of a "\n'
    '"reference should be. The syntax for explicitly annotating a lifetime uses an "\n'
    '"apostrophe character as follows:"'
    '\n',
    '"Analizator pożyczeń używa jawnych adnotacji czasu życia, aby określić, jak "\n'
    '"długo referencje powinny być prawidłowe. W przypadkach, gdy czasy życia nie "\n'
    '"są elizowane[^1], Rust wymaga jawnych adnotacji, aby określić, jaki powinien "\n'
    '"być czas życia referencji. Składnia jawnej adnotacji czasu życia używa znaku "\n'
    '"apostrofu w następujący sposób:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"Similar to [closures](../../fn/closures/anonymity.md), using lifetimes "\n'
    '"requires generics. Additionally, this lifetime syntax indicates that the "\n'
    '"lifetime of `foo` may not exceed that of `\'a`. Explicit annotation of a type "\n'
    '"has the form `&\'a T` where `\'a` has already been introduced."'
    '\n',
    '"Podobnie jak [domknięcia](../../fn/closures/anonymity.md), używanie czasów "\n'
    '"życia wymaga typów ogólnych. Ponadto ta składnia czasu życia wskazuje, że "\n'
    '"czas życia `foo` nie może przekroczyć czasu życia `\'a`. Jawna adnotacja "\n'
    '"typu ma postać `&\'a T`, gdzie `\'a` zostało już wprowadzone."'
    '\n'
)

comment('// `foo` has a lifetime parameter `\'a`\\n',
        '// `foo` ma parametr czasu życia `\'a`\\n')

prose('In cases with multiple lifetimes, the syntax is similar:',
      'W przypadku wielu czasów życia składnia jest podobna:')

comment('// `foo` has lifetime parameters `\'a` and `\'b`\\n',
        '// `foo` ma parametry czasu życia `\'a` i `\'b`\\n')

multi(
    'msgid ""\n'
    '"In this case, the lifetime of `foo` cannot exceed that of either `\'a` _or_ "\n'
    '"`\'b`."'
    '\n',
    '"W tym przypadku czas życia `foo` nie może przekroczyć czasu życia `\'a` _ani_ `\'b`."'
    '\n'
)

prose('See the following example for explicit lifetime annotation in use:',
      'Zobacz poniższy przykład jawnej adnotacji czasu życia w użyciu:')

multi(
    'msgid ""\n'
    '"// `print_refs` takes two references to `i32` which have different\\n"\n'
    '"// lifetimes `\'a` and `\'b`. These two lifetimes must both be at\\n"\n'
    '"// least as long as the function `print_refs`.\\n"'
    '\n',
    '"// `print_refs` przyjmuje dwie referencje do `i32` o różnych\\n"\n'
    '"// czasach życia `\'a` i `\'b`. Oba czasy życia muszą być co najmniej\\n"\n'
    '"// tak długie jak funkcja `print_refs`.\\n"'
    '\n'
)

verbatim('\\"x is {} and y is {}\\"')

comment('// A function which takes no arguments, but has a lifetime parameter `\'a`.\\n',
        '// Funkcja, która nie przyjmuje argumentów, ale ma parametr czasu życia `\'a`.\\n')

comment('// ERROR: `_x` does not live long enough\\n',
        '// BŁĄD: `_x` nie żyje wystarczająco długo\\n')

multi(
    'msgid ""\n'
    '"// Attempting to use the lifetime `\'a` as an explicit type annotation\\n"\n'
    '"    // inside the function will fail because the lifetime of `&_x` is shorter\\n"\n'
    '"    // than that of `_y`. A short lifetime cannot be coerced into a longer\\n"\n'
    '"    // one.\\n"\n'
    '"    // let _z = longest(x, s);\\n"'
    '\n',
    '"// Próba użycia czasu życia `\'a` jako jawnej adnotacji typowej wewnątrz\\n"\n'
    '"    // funkcji się nie powiedzie, bo czas życia `&_x` jest krótszy niż\\n"\n'
    '"    // `_y`. Krótki czas życia nie może być przekształcony na dłuższy.\\n"\n'
    '"    // let _z = longest(x, s);\\n"'
    '\n'
)

comment('// Create variables to be borrowed below.\\n',
        '// Utwórz zmienne do pożyczenia poniżej.\\n')
comment('// Borrows (`&`) of both variables are passed into the function.\\n',
        '// Pożyczenia (`&`) obu zmiennych są przekazywane do funkcji.\\n')

multi(
    'msgid ""\n'
    '"// Any input which is borrowed must outlive the borrower.\\n"\n'
    '"    // In other words, the lifetime of `four` and `nine` must\\n"\n'
    '"    // be longer than that of `print_refs`.\\n"'
    '\n',
    '"// Każde wejście, które jest pożyczone, musi przeżyć pożyczającego.\\n"\n'
    '"    // Innymi słowy, czas życia `four` i `nine` musi\\n"\n'
    '"    // być dłuższy niż czas życia `print_refs`.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// `failed_borrow` contains no references to force `\'a` to be\\n"\n'
    '"    // longer than the lifetime of the function, but `\'a` is longer.\\n"\n'
    '"    // Because the lifetime is never constrained, it defaults to `\'static`.\\n"'
    '\n',
    '"// `failed_borrow` nie zawiera referencji wymuszających, aby `\'a` było\\n"\n'
    '"    // dłuższe niż czas życia funkcji, ale `\'a` jest dłuższe.\\n"\n'
    '"    // Ponieważ czas życia nigdy nie jest ograniczany, domyślnie przyjmuje `\'static`.\\n"'
    '\n'
)

prose('[elision](elision.md) implicitly annotates lifetimes and so is different.',
      '[Elizja](elision.md) niejawnie adnotuje czasy życia i dlatego jest inna.')

verbatim('[generics](../../generics.md) and [closures](../../fn/closures.md)')

# ─── scope/lifetime/fn.md ──────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Ignoring [elision](elision.md), function signatures with lifetimes have a "\n'
    '"few constraints:"'
    '\n',
    '"Pomijając [elizję](elision.md), sygnatury funkcji z czasami życia mają kilka ograniczeń:"'
    '\n'
)

prose('any reference _must_ have an annotated lifetime.',
      'każda referencja _musi_ mieć adnotowany czas życia.')

prose('any reference being returned _must_ have the same lifetime as an input or be `static`.',
      'każda zwracana referencja _musi_ mieć ten sam czas życia co wejście lub być `static`.')

multi(
    'msgid ""\n'
    '"Additionally, note that returning references without input is banned if it "\n'
    '"would result in returning references to invalid data. The following example "\n'
    '"shows off some valid forms of functions with lifetimes:"'
    '\n',
    '"Ponadto należy zauważyć, że zwracanie referencji bez wejścia jest zabronione, "\n'
    '"jeśli skutkowałoby to zwróceniem referencji do nieprawidłowych danych. "\n'
    '"Poniższy przykład pokazuje kilka prawidłowych form funkcji z czasami życia:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// One input reference with lifetime `\'a` which must live\\n"\n'
    '"// at least as long as the function.\\n"'
    '\n',
    '"// Jedna wejściowa referencja z czasem życia `\'a`, która musi żyć\\n"\n'
    '"// co najmniej tak długo jak funkcja.\\n"'
    '\n'
)

verbatim('\\"`print_one`: x is {}\\"')

comment('// Mutable references are possible with lifetimes as well.\\n',
        '// Mutowalne referencje są możliwe z czasami życia również.\\n')

multi(
    'msgid ""\n'
    '"// Multiple elements with different lifetimes. In this case, it\\n"\n'
    '"// would be fine for both to have the same lifetime `\'a`, but\\n"\n'
    '"// in more complex cases, different lifetimes may be required.\\n"'
    '\n',
    '"// Wiele elementów o różnych czasach życia. W tym przypadku oba mogłyby\\n"\n'
    '"// mieć ten sam czas życia `\'a`, ale w bardziej złożonych przypadkach\\n"\n'
    '"// mogą być wymagane różne czasy życia.\\n"'
    '\n'
)

verbatim('\\"`print_multi`: x is {}, y is {}\\"')

multi(
    'msgid ""\n'
    '"// Returning references that have been passed in is acceptable.\\n"\n'
    '"// However, the correct lifetime must be returned.\\n"'
    '\n',
    '"// Zwracanie przekazanych referencji jest akceptowalne.\\n"\n'
    '"// Jednak musi być zwrócony prawidłowy czas życia.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"//fn invalid_output<\'a>() -> &\'a String { &String::from(\\"foo\\") }\\n"\n'
    '"// The above is invalid: `\'a` must live longer than the function.\\n"\n'
    '"// Here, `&String::from(\\"foo\\")` would create a `String`, followed by a\\n"\n'
    '"// reference. Then the data is dropped upon exiting the scope, leaving\\n"\n'
    '"// a reference pointing to invalid data: a dangling pointer!\\n"'
    '\n',
    '"//fn invalid_output<\'a>() -> &\'a String { &String::from(\\"foo\\") }\\n"\n'
    '"// Powyższe jest nieprawidłowe: `\'a` musi żyć dłużej niż funkcja.\\n"\n'
    '"// Tu `&String::from(\\"foo\\")` tworzy `String`, a następnie referencję.\\n"\n'
    '"// Dane są upuszczane po wyjściu z zakresu, pozostawiając referencję\\n"\n'
    '"// wskazującą na nieprawidłowe dane: wiszący wskaźnik!\\n"'
    '\n'
)

verbatim('[Functions](../../fn.md)')

# ─── scope/lifetime/methods.md ─────────────────────────────────────────────

prose('Methods are annotated similarly to functions:',
      'Metody są adnotowane podobnie jak funkcje:')

comment('// Annotate lifetimes as in a standalone function.\\n',
        '// Adnotuj czasy życia jak w samodzielnej funkcji.\\n')

verbatim('\\"`print`: {}\\"')

verbatim('[methods](../../fn/methods.md)')

# ─── scope/lifetime/struct.md ──────────────────────────────────────────────

prose('Annotation of lifetimes in structures are also similar to functions:',
      'Adnotacja czasów życia w strukturach jest również podobna do funkcji:')

multi(
    'msgid ""\n'
    '"// A type `Borrowed` which houses a reference to an\\n"\n'
    '"// `i32`. The reference to `i32` must outlive `Borrowed`.\\n"'
    '\n',
    '"// Typ `Borrowed` przechowujący referencję do\\n"\n'
    '"// `i32`. Referencja do `i32` musi przeżyć `Borrowed`.\\n"'
    '\n'
)

comment('// Similarly, both references here must outlive this structure.\\n',
        '// Podobnie, obie referencje tu muszą przeżyć tę strukturę.\\n')

comment('// An enum which is either an `i32` or a reference to one.\\n',
        '// Enum będące albo `i32`, albo referencją do niego.\\n')

verbatim('\\"x is borrowed in {:?}\\"')
verbatim('\\"x and y are borrowed in {:?}\\"')
verbatim('\\"y is *not* borrowed in {:?}\\"')

# ─── scope/lifetime/trait.md ───────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Annotation of lifetimes in trait methods basically are similar to functions. "\n'
    '"Note that `impl` may have annotation of lifetimes too."'
    '\n',
    '"Adnotacja czasów życia w metodach cech jest zasadniczo podobna do funkcji. "\n'
    '"Zauważ, że `impl` może również mieć adnotacje czasów życia."'
    '\n'
)

# ─── scope/lifetime/lifetime_bounds.md ────────────────────────────────────

multi(
    'msgid ""\n'
    '"Just like generic types can be bounded, lifetimes (themselves generic) use "\n'
    '"bounds as well. The `:` character has a slightly different meaning here, but "\n'
    '"`+` is the same. Note how the following read:"'
    '\n',
    '"Podobnie jak typy ogólne mogą mieć ograniczenia, czasy życia (same będące ogólnymi) "\n'
    '"również używają ograniczeń. Znak `:` ma tu nieco inne znaczenie, ale `+` jest takie "\n'
    '"samo. Zauważ, jak należy rozumieć poniższe:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"`T: \'a`: All references in `T` must outlive lifetime `\'a`."'
    '\n',
    '"`T: \'a`: Wszystkie referencje w `T` muszą przeżyć czas życia `\'a`."'
    '\n'
)

multi(
    'msgid ""\n'
    '"`T: Trait + \'a`: Type `T` must implement trait `Trait` and _all_ references "\n'
    '"in `T` must outlive `\'a`."'
    '\n',
    '"`T: Trait + \'a`: Typ `T` musi implementować cechę `Trait`, a _wszystkie_ "\n'
    '"referencje w `T` muszą przeżyć `\'a`."'
    '\n'
)

multi(
    'msgid ""\n'
    '"The example below shows the above syntax in action used after keyword "\n'
    '"`where`:"'
    '\n',
    '"Poniższy przykład pokazuje powyższą składnię w działaniu użytą po słowie kluczowym `where`:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// `Ref` contains a reference to a generic type `T` that has\\n"\n'
    '"// some lifetime `\'a` unknown by `Ref`. `T` is bounded such that any\\n"\n'
    '"// *references* in `T` must outlive `\'a`. Additionally, the lifetime\\n"\n'
    '"// of `Ref` may not exceed `\'a`.\\n"'
    '\n',
    '"// `Ref` zawiera referencję do ogólnego typu `T` z jakimś czasem życia\\n"\n'
    '"// `\'a` nieznanym przez `Ref`. `T` jest ograniczone tak, że wszelkie\\n"\n'
    '"// *referencje* w `T` muszą przeżyć `\'a`. Ponadto czas życia `Ref`\\n"\n'
    '"// nie może przekroczyć `\'a`.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Here a reference to `T` is taken where `T` implements\\n"\n'
    '"// `Debug` and all *references* in `T` outlive `\'a`. In\\n"\n'
    '"// addition, `\'a` must outlive the function.\\n"'
    '\n',
    '"// Tu pobierana jest referencja do `T`, gdzie `T` implementuje\\n"\n'
    '"// `Debug`, a wszystkie *referencje* w `T` przeżywają `\'a`. Ponadto\\n"\n'
    '"// `\'a` musi przeżyć funkcję.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"[generics](../../generics.md), [bounds in generics](../../generics/bounds."\n'
    '"md), and [multiple bounds in generics](../../generics/multi_bounds.md)"'
    '\n',
    '"[typy ogólne](../../generics.md), [ograniczenia w typach ogólnych](../../generics/bounds."\n'
    '"md) oraz [wiele ograniczeń w typach ogólnych](../../generics/multi_bounds.md)"'
    '\n'
)

# ─── scope/lifetime/lifetime_coercion.md ──────────────────────────────────

multi(
    'msgid ""\n'
    '"A longer lifetime can be coerced into a shorter one so that it works inside "\n'
    '"a scope it normally wouldn\'t work in. This comes in the form of inferred "\n'
    '"coercion by the Rust compiler, and also in the form of declaring a lifetime "\n'
    '"difference:"'
    '\n',
    '"Dłuższy czas życia może być przekształcony w krótszy, aby działał wewnątrz "\n'
    '"zakresu, w którym normalnie by nie działał. Dzieje się to w formie wnioskowanej "\n'
    '"koercji przez kompilator Rust, a także w formie deklarowania różnicy czasów życia:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Here, Rust infers a lifetime that is as short as possible.\\n"\n'
    '"// The two references are then coerced to that lifetime.\\n"'
    '\n',
    '"// Tu Rust wnioskuje czas życia tak krótki, jak to możliwe.\\n"\n'
    '"// Dwie referencje są następnie przekształcane do tego czasu życia.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// `<\'a: \'b, \'b>` reads as lifetime `\'a` is at least as long as `\'b`.\\n"\n'
    '"// Here, we take in an `&\'a i32` and return a `&\'b i32` as a result of coercion.\\n"'
    '\n',
    '"// `<\'a: \'b, \'b>` czytamy: czas życia `\'a` jest co najmniej tak długi jak `\'b`.\\n"\n'
    '"// Tu przyjmujemy `&\'a i32` i zwracamy `&\'b i32` w wyniku koercji.\\n"'
    '\n'
)

# ─── scope/lifetime/static_lifetime.md ────────────────────────────────────

multi(
    'msgid ""\n'
    '"Rust has a few reserved lifetime names. One of those is `\'static`. You might "\n'
    '"encounter it in two situations:"'
    '\n',
    '"Rust ma kilka zarezerwowanych nazw czasów życia. Jedną z nich jest `\'static`. "\n'
    '"Możesz napotkać ją w dwóch sytuacjach:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"A reference with `\'static` lifetime:"'
    '\n',
    '"Referencja z czasem życia `\'static`:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"A trait bound:"'
    '\n',
    '"Ograniczenie cechy:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"Both are related but subtly different and this is a common source for "\n'
    '"confusion when learning Rust. Here are some examples for each situation:"'
    '\n',
    '"Obie sytuacje są powiązane, ale subtelnie różne, i jest to częste źródło "\n'
    '"zamieszania przy nauce Rust. Oto kilka przykładów dla każdej sytuacji:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"As a reference lifetime `\'static` indicates that the data pointed to by the "\n'
    '"reference lives for the remaining lifetime of the running program. It can "\n'
    '"still be coerced to a shorter lifetime."'
    '\n',
    '"Jako czas życia referencji `\'static` wskazuje, że dane wskazywane przez "\n'
    '"referencję żyją przez pozostały czas działania programu. Nadal można je "\n'
    '"przekształcić do krótszego czasu życia."'
    '\n'
)

multi(
    'msgid ""\n'
    '"There are two common ways to make a variable with `\'static` lifetime, and "\n'
    '"both are stored in the read-only memory of the binary:"'
    '\n',
    '"Istnieją dwa powszechne sposoby tworzenia zmiennej z czasem życia `\'static`, "\n'
    '"i oba są przechowywane w pamięci binarnej tylko do odczytu:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"Make a constant with the `static` declaration."'
    '\n',
    '"Utwórz stałą z deklaracją `static`."'
    '\n'
)

multi(
    'msgid ""\n'
    '"Make a `string` literal which has type `&\'static str`."'
    '\n',
    '"Utwórz literał `string` o typie `&\'static str`."'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Returns a reference to `NUM` where its `\'static`\\n"\n'
    '"// lifetime is coerced to that of the input argument.\\n"'
    '\n',
    '"// Zwraca referencję do `NUM`, gdzie jej czas życia `\'static`\\n"\n'
    '"// jest przekształcany do czasu życia argumentu wejściowego.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// When `static_string` goes out of scope, the reference\\n"\n'
    '"        // can no longer be used, but the data remains in the binary.\\n"'
    '\n',
    '"// Gdy `static_string` wychodzi poza zakres, referencja\\n"\n'
    '"        // nie może być już używana, ale dane pozostają w pliku binarnym.\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"Since `\'static` references only need to be valid for the _remainder_ of a "\n'
    '"program\'s life, they can be created while the program is executed. Just to "\n'
    '"demonstrate, the below example uses [`Box::leak`](https://doc.rust-lang.org/"\n'
    '"std/boxed/struct.Box.html#method.leak) to dynamically create `\'static` "\n'
    '"references, which is one method for getting a `\'static` reference at "\n'
    '"runtime."'
    '\n',
    '"Ponieważ referencje `\'static` muszą być prawidłowe tylko przez _pozostały_ "\n'
    '"czas działania programu, mogą być tworzone podczas jego wykonywania. Dla "\n'
    '"demonstracji poniższy przykład używa [`Box::leak`](https://doc.rust-lang.org/"\n'
    '"std/boxed/struct.Box.html#method.leak) do dynamicznego tworzenia referencji "\n'
    '"`\'static`, co jest jedną metodą uzyskiwania referencji `\'static` w czasie wykonania."'
    '\n'
)

multi(
    'msgid ""\n'
    '"As a trait bound, it means the type does not contain any non-static "\n'
    '"references. Eg. the receiver can hold on to the type for as long as they "\n'
    '"want and it will never become invalid until they drop it."'
    '\n',
    '"Jako ograniczenie cechy oznacza, że typ nie zawiera żadnych niestatycznych "\n'
    '"referencji. Np. odbiorca może trzymać się typu tak długo, jak chce, i nie "\n'
    '"stanie się on nieprawidłowy, dopóki go nie upuści."'
    '\n'
)

multi(
    'msgid ""\n'
    '"It\'s important to understand this means that any owned data always passes a "\n'
    '"`\'static` lifetime bound, but a reference to that owned data generally does "\n'
    '"not:"'
    '\n',
    '"Ważne jest, aby zrozumieć, że oznacza to, iż wszelkie posiadane dane zawsze "\n'
    '"spełniają ograniczenie czasu życia `\'static`, ale referencja do tych "\n'
    '"posiadanych danych generalnie nie:"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// oops, &i only has the lifetime defined by the scope of\\n"\n'
    '"    // main(), so it\'s not \'static:\\n"'
    '\n',
    '"// ups, &i ma tylko czas życia zdefiniowany przez zakres\\n"\n'
    '"    // main(), więc nie jest \'static:\\n"'
    '\n'
)

# ─── scope/lifetime/elision.md ─────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Some lifetime patterns are overwhelmingly common and so the borrow checker "\n'
    '"will allow you to omit them to save typing and to improve readability. This "\n'
    '"is known as elision. Elision exists in Rust solely because these patterns "\n'
    '"are common."'
    '\n',
    '"Niektóre wzorce czasów życia są niezwykle powszechne, więc analizator pożyczeń "\n'
    '"pozwala je pominąć, aby zaoszczędzić pisania i poprawić czytelność. Nazywa "\n'
    '"się to elizją. Elizja istnieje w Rust wyłącznie dlatego, że te wzorce są powszechne."'
    '\n'
)

multi(
    'msgid ""\n'
    '"The following code shows a few examples of elision. For a more comprehensive "\n'
    '"description of elision, see [lifetime elision](https://doc.rust-lang.org/"\n'
    '"book/ch10-03-lifetime-syntax.html#lifetime-elision) in the book."'
    '\n',
    '"Poniższy kod pokazuje kilka przykładów elizji. Bardziej wyczerpujący opis "\n'
    '"elizji można znaleźć w [elizja czasu życia](https://doc.rust-lang.org/"\n'
    '"book/ch10-03-lifetime-syntax.html#lifetime-elision) w książce."'
    '\n'
)

multi(
    'msgid ""\n'
    '"// `elided_input` and `annotated_input` essentially have identical signatures\\n"\n'
    '"// because the lifetime of `elided_input` is inferred by the compiler:\\n"'
    '\n',
    '"// `elided_input` i `annotated_input` mają zasadniczo identyczne sygnatury,\\n"\n'
    '"// bo czas życia `elided_input` jest wnioskowany przez kompilator:\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"// Similarly, `elided_pass` and `annotated_pass` have identical signatures\\n"\n'
    '"// because the lifetime is added implicitly to `elided_pass`:\\n"'
    '\n',
    '"// Podobnie, `elided_pass` i `annotated_pass` mają identyczne sygnatury,\\n"\n'
    '"// bo czas życia jest niejawnie dodawany do `elided_pass`:\\n"'
    '\n'
)

multi(
    'msgid ""\n'
    '"[elision](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax."\n'
    '"html#lifetime-elision)"'
    '\n',
    '"[elizja](https://doc.rust-lang.org/book/ch10-03-lifetime-syntax."\n'
    '"html#lifetime-elision)"'
    '\n'
)

# ───────────────────────────────────────────────────────────────────────────

open('po/pl.po', 'w').write(text)
print(f'\nŁącznie zmian: {total}')
