#!/usr/bin/env python3
# Etap 8: Cechy (Traits)
# Pokrywa: trait.md, trait/derive.md, trait/dyn.md, trait/ops.md,
#          trait/drop.md, trait/iter.md, trait/impl_trait.md,
#          trait/clone.md, trait/supertraits.md, trait/disambiguating.md

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

# ─── trait.md ──────────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"A `trait` is a collection of methods defined for an unknown type: `Self`. "\n'
    '"They can access other methods declared in the same trait."\n',
    '"Cecha (`trait`) to zbiór metod zdefiniowanych dla nieznanego typu: `Self`. "\n'
    '"Mogą one uzyskiwać dostęp do innych metod zadeklarowanych w tej samej cesze."\n'
)

multi(
    'msgid ""\n'
    '"Traits can be implemented for any data type. In the example below, we define "\n'
    '"`Animal`, a group of methods. The `Animal` `trait` is then implemented for "\n'
    '"the `Sheep` data type, allowing the use of methods from `Animal` with a "\n'
    '"`Sheep` instance."\n',
    '"Cechy mogą być implementowane dla dowolnego typu danych. W poniższym przykładzie "\n'
    '"definiujemy `Animal`, grupę metod. Cecha `Animal` jest następnie implementowana "\n'
    '"dla typu danych `Sheep`, umożliwiając używanie metod z `Animal` z instancją `Sheep`."\n'
)

multi(
    'msgid ""\n'
    '"// Associated function signature; `Self` refers to the implementor type.\\n"\n',
    '"// Sygnatura funkcji skojarzonej; `Self` odnosi się do typu implementującego.\\n"\n'
)

comment('// Method signatures; these will return a string.\\n',
        '// Sygnatury metod; będą zwracać łańcuch znaków.\\n')
comment('// Traits can provide default method definitions.\\n',
        '// Cechy mogą dostarczać domyślne definicje metod.\\n')
verbatim('\\"{} says {}\\"')
comment('// Implementor methods can use the implementor\'s trait methods.\\n',
        '// Metody implementującego mogą używać metod cech implementującego.\\n')
verbatim('\\"{} is already naked...\\"')
verbatim('\\"{} gets a haircut!\\"')
comment('// Implement the `Animal` trait for `Sheep`.\\n',
        '// Implementuj cechę `Animal` dla `Sheep`.\\n')
comment('// `Self` is the implementor type: `Sheep`.\\n',
        '// `Self` to typ implementujący: `Sheep`.\\n')
verbatim('\\"baaaaah?\\"')
verbatim('\\"baaaaah!\\"')
comment('// Default trait methods can be overridden.\\n',
        '// Domyślne metody cech mogą być nadpisywane.\\n')
comment('// For example, we can add some quiet contemplation.\\n',
        '// Na przykład możemy dodać trochę cichej kontemplacji.\\n')
verbatim('\\"{} pauses briefly... {}\\"')
comment('// Type annotation is necessary in this case.\\n',
        '// W tym przypadku adnotacja typowa jest konieczna.\\n')
verbatim('\\"Dolly\\"')
comment('// TODO ^ Try removing the type annotations.\\n',
        '// TODO ^ Spróbuj usunąć adnotacje typowe.\\n')

# ─── trait/derive.md ───────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"The compiler is capable of providing basic implementations for some traits "\n'
    '"via the `#[derive]` [attribute](../attribute.md). These traits can still be "\n'
    '"manually implemented if a more complex behavior is required."\n',
    '"Kompilator jest w stanie dostarczyć podstawowe implementacje niektórych cech "\n'
    '"poprzez [atrybut](../attribute.md) `#[derive]`. Cechy te nadal mogą być "\n'
    '"implementowane ręcznie, jeśli wymagane jest bardziej złożone zachowanie."\n'
)

prose('The following is a list of derivable traits:',
      'Poniżej znajduje się lista cech, które można wyprowadzać:')

multi(
    'msgid ""\n'
    '"Comparison traits: [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html), "\n'
    '"[`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html), "\n'
    '"[`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html), [`PartialOrd`]"\n'
    '"(https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html)."\n',
    '"Cechy porównania: [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html), "\n'
    '"[`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html), "\n'
    '"[`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html), [`PartialOrd`]"\n'
    '"(https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html)."\n'
)

multi(
    'msgid ""\n'
    '"[`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html), to create "\n'
    '"`T` from `&T` via a copy."\n',
    '"[`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html), do tworzenia "\n'
    '"`T` z `&T` poprzez kopię."\n'
)

multi(
    'msgid ""\n'
    '"[`Copy`](https://doc.rust-lang.org/core/marker/trait.Copy.html), to give a "\n'
    '"type \'copy semantics\' instead of \'move semantics\'."\n',
    '"[`Copy`](https://doc.rust-lang.org/core/marker/trait.Copy.html), aby nadać "\n'
    '"typowi semantykę kopiowania zamiast semantyki przenoszenia."\n'
)

multi(
    'msgid ""\n'
    '"[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html), to compute a "\n'
    '"hash from `&T`."\n',
    '"[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html), do obliczenia "\n'
    '"skrótu z `&T`."\n'
)

multi(
    'msgid ""\n'
    '"[`Default`](https://doc.rust-lang.org/std/default/trait.Default.html), to "\n'
    '"create an empty instance of a data type."\n',
    '"[`Default`](https://doc.rust-lang.org/std/default/trait.Default.html), do "\n'
    '"tworzenia pustej instancji typu danych."\n'
)

multi(
    'msgid ""\n'
    '"[`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html), to format a "\n'
    '"value using the `{:?}` formatter."\n',
    '"[`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html), do formatowania "\n'
    '"wartości za pomocą formatera `{:?}`."\n'
)

comment('// `Centimeters`, a tuple struct that can be compared\\n',
        '// `Centimeters`, krotka-struktury, którą można porównywać\\n')
comment('// `Inches`, a tuple struct that can be printed\\n',
        '// `Inches`, krotka-struktury, którą można drukować\\n')
comment('// `Seconds`, a tuple struct with no additional attributes\\n',
        '// `Seconds`, krotka-struktury bez dodatkowych atrybutów\\n')

multi(
    'msgid ""\n'
    '"// Error: `Seconds` can\'t be printed; it doesn\'t implement the `Debug` trait\\n"\n'
    '"    //println!(\\\"One second looks like: {:?}\\\", _one_second);\\n"\n'
    '"    // TODO ^ Try enabling this line.\\n"\n',
    '"// Błąd: `Seconds` nie może być drukowane; nie implementuje cechy `Debug`\\n"\n'
    '"    //println!(\\\"One second looks like: {:?}\\\", _one_second);\\n"\n'
    '"    // TODO ^ Spróbuj włączyć tę linię.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Error: `Seconds` can\'t be compared; it doesn\'t implement the `PartialEq` trait\\n"\n'
    '"    //let _this_is_true = (_one_second == _one_second);\\n"\n'
    '"    // TODO ^ Try enabling this line.\\n"\n',
    '"// Błąd: `Seconds` nie może być porównywane; nie implementuje cechy `PartialEq`\\n"\n'
    '"    //let _this_is_true = (_one_second == _one_second);\\n"\n'
    '"    // TODO ^ Spróbuj włączyć tę linię.\\n"\n'
)

verbatim('\\"One foot equals {:?}\\"')
verbatim('\\"smaller\\"')
verbatim('\\"bigger\\"')
verbatim('\\"One foot is {} than one meter.\\"')

multi(
    'msgid ""\n'
    '"[`derive`](https://doc.rust-lang.org/reference/attributes.html#derive)"\n',
    '"[`derive`](https://doc.rust-lang.org/reference/attributes.html#derive)"\n'
)

# ─── trait/dyn.md ──────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"The Rust compiler needs to know how much space every function\'s return type "\n'
    '"requires. This means all your functions have to return a concrete type. "\n'
    '"Unlike other languages, if you have a trait like `Animal`, you can\'t write a "\n'
    '"function that returns `Animal`, because its different implementations will "\n'
    '"need different amounts of memory."\n',
    '"Kompilator Rust musi wiedzieć, ile miejsca wymaga typ zwracany każdej funkcji. "\n'
    '"Oznacza to, że wszystkie funkcje muszą zwracać konkretny typ. W przeciwieństwie "\n'
    '"do innych języków, jeśli masz cechę taką jak `Animal`, nie możesz napisać funkcji "\n'
    '"zwracającej `Animal`, ponieważ różne implementacje wymagają różnych ilości pamięci."\n'
)

multi(
    'msgid ""\n'
    '"However, there\'s an easy workaround. Instead of returning a trait object "\n'
    '"directly, our functions return a `Box` which _contains_ some `Animal`. A "\n'
    '"`box` is just a reference to some memory in the heap. Because a reference "\n'
    '"has a statically-known size, and the compiler can guarantee it points to a "\n'
    '"heap-allocated `Animal`, we can return a trait from our function!"\n',
    '"Istnieje jednak proste obejście. Zamiast zwracać obiekt cechy bezpośrednio, "\n'
    '"nasze funkcje zwracają `Box` _zawierający_ jakiegoś `Animal`. `box` to po prostu "\n'
    '"referencja do pewnej pamięci na stercie. Ponieważ referencja ma statycznie znany "\n'
    '"rozmiar, a kompilator może zagwarantować, że wskazuje na zaalokowany na stercie "\n'
    '"`Animal`, możemy zwrócić cechę z naszej funkcji!"\n'
)

multi(
    'msgid ""\n'
    '"Rust tries to be as explicit as possible whenever it allocates memory on the "\n'
    '"heap. So if your function returns a pointer-to-trait-on-heap in this way, "\n'
    '"you need to write the return type with the `dyn` keyword, e.g. `Box<dyn "\n'
    '"Animal>`."\n',
    '"Rust stara się być jak najbardziej jawny, gdy alokuje pamięć na stercie. Więc "\n'
    '"jeśli twoja funkcja zwraca wskaźnik-do-cechy-na-stercie w ten sposób, musisz "\n'
    '"napisać typ zwracany ze słowem kluczowym `dyn`, np. `Box<dyn Animal>`."\n'
)

comment('// Instance method signature\\n',
        '// Sygnatura metody instancji\\n')
comment('// Implement the `Animal` trait for `Cow`.\\n',
        '// Implementuj cechę `Animal` dla `Cow`.\\n')
verbatim('\\"moooooo!\\"')

multi(
    'msgid ""\n'
    '"// Returns some struct that implements Animal, but we don\'t know which one at compile time.\\n"\n',
    '"// Zwraca jakąś strukturę implementującą Animal, ale nie wiemy którą w czasie kompilacji.\\n"\n'
)

verbatim('\\"You\'ve randomly chosen an animal, and it says {}\\"')

# ─── trait/ops.md ──────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"In Rust, many of the operators can be overloaded via traits. That is, some "\n'
    '"operators can be used to accomplish different tasks based on their input "\n'
    '"arguments. This is possible because operators are syntactic sugar for method "\n'
    '"calls. For example, the `+` operator in `a + b` calls the `add` method "\n'
    '"(as in `a.add(b)`). This `add` method is part of the `Add` trait. Hence, "\n'
    '"the `+` operator can be used by any implementor of the `Add` trait."\n',
    '"W Rust wiele operatorów można przeciążać za pomocą cech. To znaczy, że niektóre "\n'
    '"operatory mogą być używane do różnych zadań w zależności od argumentów wejściowych. "\n'
    '"Jest to możliwe, ponieważ operatory są lukrem składniowym dla wywołań metod. Na "\n'
    '"przykład operator `+` w `a + b` wywołuje metodę `add` (jak w `a.add(b)`). Ta "\n'
    '"metoda `add` jest częścią cechy `Add`. Dlatego operator `+` może być używany "\n'
    '"przez każdego implementującego cechę `Add`."\n'
)

multi(
    'msgid ""\n'
    '"A list of the traits, such as `Add`, that overload operators can be found in "\n'
    '"[`core::ops`](https://doc.rust-lang.org/core/ops/)."\n',
    '"Listę cech, takich jak `Add`, które przeciążają operatory, można znaleźć w "\n'
    '"[`core::ops`](https://doc.rust-lang.org/core/ops/)."\n'
)

multi(
    'msgid ""\n'
    '"// The `std::ops::Add` trait is used to specify the functionality of `+`.\\n"\n'
    '"// Here, we make `Add<Bar>` - the trait for addition with a RHS of type `Bar`.\\n"\n',
    '"// Cecha `std::ops::Add` służy do określania funkcjonalności `+`.\\n"\n'
    '"// Tu tworzymy `Add<Bar>` - cechę dodawania z prawym operandem typu `Bar`.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// By reversing the types, we end up implementing non-commutative addition.\\n"\n'
    '"// Here, we make `Add<Foo>` - the trait for addition with a RHS of type `Foo`.\\n"\n',
    '"// Odwracając typy, implementujemy nieprzemienne dodawanie.\\n"\n'
    '"// Tu tworzymy `Add<Foo>` - cechę dodawania z prawym operandem typu `Foo`.\\n"\n'
)

verbatim('\\"> Foo.add(Bar) was called\\"')
verbatim('\\"> Bar.add(Foo) was called\\"')
verbatim('\\"Foo + Bar = {:?}\\"')
verbatim('\\"Bar + Foo = {:?}\\"')

multi(
    'msgid ""\n'
    '"[Add](https://doc.rust-lang.org/core/ops/trait.Add.html), [Syntax Index]"\n'
    '"(https://doc.rust-lang.org/book/appendix-02-operators.html)"\n',
    '"[Add](https://doc.rust-lang.org/core/ops/trait.Add.html), [Indeks składni]"\n'
    '"(https://doc.rust-lang.org/book/appendix-02-operators.html)"\n'
)

# ─── trait/drop.md ─────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"The [`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html) trait only "\n'
    '"has one method: `drop`, which is called automatically when an object goes "\n'
    '"out of scope. The main use of the `Drop` trait is to free the resources that "\n'
    '"the implementor instance owns."\n',
    '"Cecha [`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html) ma tylko "\n'
    '"jedną metodę: `drop`, wywoływaną automatycznie gdy obiekt wychodzi poza zakres. "\n'
    '"Głównym zastosowaniem cechy `Drop` jest zwalnianie zasobów posiadanych przez "\n'
    '"instancję implementującą."\n'
)

multi(
    'msgid ""\n'
    '"`Box`, `Vec`, `String`, `File`, and `Process` are some examples of types "\n'
    '"that implement the `Drop` trait to free resources. The `Drop` trait can also "\n'
    '"be manually implemented for any custom data type."\n',
    '"`Box`, `Vec`, `String`, `File` i `Process` to przykłady typów implementujących "\n'
    '"cechę `Drop` w celu zwalniania zasobów. Cechę `Drop` można też ręcznie "\n'
    '"zaimplementować dla dowolnego własnego typu danych."\n'
)

multi(
    'msgid ""\n'
    '"The following example adds a print to console to the `drop` function to "\n'
    '"announce when it is called."\n',
    '"Poniższy przykład dodaje wydruk na konsolę do funkcji `drop`, aby ogłaszać, "\n'
    '"kiedy jest wywoływana."\n'
)

comment('// This trivial implementation of `drop` adds a print to console.\\n',
        '// Ta trywialna implementacja `drop` dodaje wydruk na konsolę.\\n')
verbatim('\\"> Dropping {}\\"')
comment('// block A\\n', '// blok A\\n')
verbatim('\\"b\\"')
comment('// block B\\n', '// blok B\\n')
verbatim('\\"c\\"')
verbatim('\\"d\\"')
verbatim('\\"Exiting block B\\"')
verbatim('\\"Just exited block B\\"')
verbatim('\\"Exiting block A\\"')
verbatim('\\"Just exited block A\\"')
comment('// Variable can be manually dropped using the `drop` function\\n',
        '// Zmienna może być ręcznie upuszczona za pomocą funkcji `drop`\\n')
comment('// TODO ^ Try commenting this line\\n',
        '// TODO ^ Spróbuj zakomentować tę linię\\n')
verbatim('\\"end of the main function\\"')

multi(
    'msgid ""\n'
    '"// `_a` *won\'t* be `drop`ed again here, because it already has been\\n"\n'
    '"    // (manually) `drop`ed\\n"\n',
    '"// `_a` *nie* zostanie tu ponownie `drop`owana, bo już była\\n"\n'
    '"    // (ręcznie) `drop`owana\\n"\n'
)

multi(
    'msgid ""\n'
    '"For a more practical example, here\'s how the `Drop` trait can be used to "\n'
    '"automatically clean up temporary files when they\'re no longer needed:"\n',
    '"Dla bardziej praktycznego przykładu, oto jak cecha `Drop` może być używana do "\n'
    '"automatycznego usuwania plików tymczasowych, gdy nie są już potrzebne:"\n'
)

comment('// Note: File::create() will overwrite existing files\\n',
        '// Uwaga: File::create() nadpisze istniejące pliki\\n')

multi(
    'msgid ""\n'
    '"// When TempFile is dropped:\\n"\n'
    '"// 1. First, our custom drop implementation runs. The file is still open at this point,\\n"\n'
    '"//    so we can attempt to delete it.\\n"\n'
    '"// 2. After our code runs, Rust automatically drops each field in order.\\n"\n'
    '"//    This will drop `file` (a File), which closes the file handle.\\n"\n'
    '"// The file handle is closed *after* our drop code runs!\\n"\n',
    '"// Gdy TempFile jest upuszczany:\\n"\n'
    '"// 1. Najpierw uruchamia się nasza własna implementacja drop. Plik jest nadal otwarty,\\n"\n'
    '"//    więc możemy spróbować go usunąć.\\n"\n'
    '"// 2. Po uruchomieniu naszego kodu, Rust automatycznie upuszcza każde pole po kolei.\\n"\n'
    '"//    To spowoduje upuszczenie `file` (File), co zamknie uchwyt do pliku.\\n"\n'
    '"// Uchwyt do pliku jest zamykany *po* uruchomieniu naszego kodu drop!\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Note: the File is still open here — field destructors run after this method.\\n"\n',
    '"// Uwaga: plik jest nadal otwarty tutaj — destruktory pól uruchamiają się po tej metodzie.\\n"\n'
)

verbatim('\\"Failed to remove temporary file: {}\\"')
verbatim('\\"> Dropped temporary file: {:?}\\"')

multi(
    'msgid ""\n'
    '"// After this method returns, Rust will drop each field (including `file`),\\n"\n'
    '"        // which closes the underlying file handle.\\n"\n',
    '"// Po powrocie tej metody Rust upuści każde pole (w tym `file`),\\n"\n'
    '"        // co zamknie bazowy uchwyt do pliku.\\n"\n'
)

comment('// Create a new scope to demonstrate drop behavior\\n',
        '// Utwórz nowy zakres, aby zademonstrować zachowanie drop\\n')
verbatim('\\"test.txt\\"')
verbatim('\\"Temporary file created\\"')
comment('// File will be automatically cleaned up when temp goes out of scope\\n',
        '// Plik zostanie automatycznie wyczyszczony gdy temp wyjdzie poza zakres\\n')
verbatim('\\"End of scope - file should be cleaned up\\"')
comment('// We can also manually drop if needed\\n',
        '// Możemy też ręcznie upuścić, jeśli potrzeba\\n')
verbatim('\\"another_test.txt\\"')
comment('// Explicitly drop the file\\n',
        '// Jawnie upuść plik\\n')
verbatim('\\"Manually dropped file\\"')

# ─── trait/iter.md ─────────────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"The [`Iterator`](https://doc.rust-lang.org/core/iter/trait.Iterator.html) "\n'
    '"trait is used to implement iterators over collections such as arrays."\n',
    '"Cecha [`Iterator`](https://doc.rust-lang.org/core/iter/trait.Iterator.html) "\n'
    '"służy do implementowania iteratorów po kolekcjach, takich jak tablice."\n'
)

multi(
    'msgid ""\n'
    '"The trait requires only a method to be defined for the `next` element, which "\n'
    '"may be manually defined in an `impl` block or automatically defined (as in "\n'
    '"arrays and ranges)."\n',
    '"Cecha wymaga zdefiniowania tylko jednej metody dla elementu `next`, która może "\n'
    '"być zdefiniowana ręcznie w bloku `impl` lub automatycznie (jak w tablicach i zakresach)."\n'
)

multi(
    'msgid ""\n'
    '"As a point of convenience for common situations, the `for` construct turns "\n'
    '"some collections into iterators using the [`.into_iter()`](https://doc.rust-"\n'
    '"lang.org/std/iter/trait.IntoIterator.html) method."\n',
    '"Dla wygody w typowych sytuacjach, konstrukcja `for` zamienia niektóre kolekcje "\n'
    '"w iteratory za pomocą metody [`.into_iter()`](https://doc.rust-"\n'
    '"lang.org/std/iter/trait.IntoIterator.html)."\n'
)

comment('// We can refer to this type using Self::Item\\n',
        '// Możemy odwoływać się do tego typu używając Self::Item\\n')

multi(
    'msgid ""\n'
    '"// Implement `Iterator` for `Fibonacci`.\\n"\n'
    '"// The `Iterator` trait only requires a method to be defined for the `next` element,\\n"\n'
    '"// and the `Fibonacci` sequence is infinite, so we can use the unit value `()` to\\n"\n'
    '"// indicate no iteration is finished.\\n"\n',
    '"// Implementuj `Iterator` dla `Fibonacci`.\\n"\n'
    '"// Cecha `Iterator` wymaga zdefiniowania tylko metody dla elementu `next`,\\n"\n'
    '"// a sekwencja Fibonacciego jest nieskończona, więc możemy użyć wartości jednostkowej\\n"\n'
    '"// `()`, aby wskazać, że żadna iteracja nie jest zakończona.\\n"\n'
)

comment('// Returns a Fibonacci sequence generator\\n',
        '// Zwraca generator sekwencji Fibonacciego\\n')

multi(
    'msgid ""\n'
    '"// Here, we define the sequence using `.curr` and `.next`.\\n"\n'
    '"    // The return type is `Option<T>`:\\n"\n'
    '"    //     * When the `Iterator` is finished, `None` is returned.\\n"\n'
    '"    //     * Otherwise, the next value is wrapped in `Some` and returned.\\n"\n'
    '"    // We use Self::Item in the return type, so we can change\\n"\n'
    '"    // the type without having to update the function signatures.\\n"\n',
    '"// Tu definiujemy sekwencję za pomocą `.curr` i `.next`.\\n"\n'
    '"    // Typ zwracany to `Option<T>`:\\n"\n'
    '"    //     * Gdy `Iterator` jest zakończony, zwracane jest `None`.\\n"\n'
    '"    //     * W przeciwnym razie następna wartość jest opakowana w `Some` i zwracana.\\n"\n'
    '"    // Używamy Self::Item w typie zwracanym, aby móc zmienić\\n"\n'
    '"    // typ bez konieczności aktualizowania sygnatur funkcji.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Since there\'s no endpoint to a Fibonacci sequence, the `Iterator`\\n"\n'
    '"        // will never return `None`, and `Some` is always returned.\\n"\n',
    '"// Ponieważ sekwencja Fibonacciego nie ma końca, `Iterator`\\n"\n'
    '"        // nigdy nie zwróci `None` i zawsze jest zwracane `Some`.\\n"\n'
)

comment('// `0..3` is an `Iterator` that generates: 0, 1, and 2.\\n',
        '// `0..3` to `Iterator` generujący: 0, 1 i 2.\\n')
verbatim('\\"Four consecutive `next` calls on 0..3\\"')
verbatim('\\"> {:?}\\"')
verbatim('\\"Iterate through 0..3 using `for`\\"')

multi(
    'msgid ""\n'
    '"// `for` works through an `Iterator` until it returns `None`.\\n"\n'
    '"    // Each `Some` value is unwrapped and bound to a variable (here, `i`).\\n"\n',
    '"// `for` przechodzi przez `Iterator` dopóki nie zwróci `None`.\\n"\n'
    '"    // Każda wartość `Some` jest rozpakowywana i wiązana ze zmienną (tu `i`).\\n"\n'
)

comment('// The `take(n)` method reduces an `Iterator` to its first `n` terms.\\n',
        '// Metoda `take(n)` redukuje `Iterator` do pierwszych `n` elementów.\\n')
verbatim('\\"The first four terms of the Fibonacci sequence are: \\"')

multi(
    'msgid ""\n'
    '"// The `skip(n)` method shortens an `Iterator` by dropping its first `n` terms.\\n"\n',
    '"// Metoda `skip(n)` skraca `Iterator` pomijając jego pierwsze `n` elementów.\\n"\n'
)

verbatim('\\"The next four terms of the Fibonacci sequence are: \\"')
comment('// The `iter` method produces an `Iterator` over an array/slice.\\n',
        '// Metoda `iter` tworzy `Iterator` po tablicy/wycinku.\\n')
verbatim('\\"Iterate the following array {:?}\\"')

# ─── trait/impl_trait.md ───────────────────────────────────────────────────

prose('`impl Trait` can be used in two locations:',
      '`impl Trait` można użyć w dwóch miejscach:')
prose('as an argument type', 'jako typ argumentu')
prose('as a return type', 'jako typ zwracany')
prose('As an argument type', 'Jako typ argumentu')
prose('For example, consider the following code:', 'Na przykład rozważ poniższy kod:')

multi(
    'msgid ""\n'
    '"If your function is generic over a trait but you don\'t mind the specific "\n'
    '"type, you can simplify the function declaration using `impl Trait` as the "\n'
    '"type of the argument."\n',
    '"Jeśli twoja funkcja jest ogólna dla cechy, ale nie zależy ci na konkretnym "\n'
    '"typie, możesz uprościć deklarację funkcji używając `impl Trait` jako typu argumentu."\n'
)

comment('// For each line in the source\\n',
        '// Dla każdej linii w źródle\\n')
verbatim("','")
comment('// Split the line separated by commas\\n',
        '// Podziel linię oddzieloną przecinkami\\n')
comment('// Remove leading and trailing whitespace\\n',
        '// Usuń wiodące i końcowe białe znaki\\n')
comment('// Collect all strings in a row into a Vec<String>\\n',
        '// Zbierz wszystkie łańcuchy w wierszu do Vec<String>\\n')
comment('// Collect all lines into a Vec<Vec<String>>\\n',
        '// Zbierz wszystkie linie do Vec<Vec<String>>\\n')

multi(
    'msgid ""\n'
    '"// If the line was read successfully, process it, if not, return the error\\n"\n',
    '"// Jeśli linia została odczytana pomyślnie, przetwórz ją, jeśli nie, zwróć błąd\\n"\n'
)

multi(
    'msgid ""\n'
    '"`parse_csv_document` is generic, allowing it to take any type which "\n'
    '"implements BufRead, such as `BufReader<File>` or `[u8]`, but it\'s not "\n'
    '"important what type `R` is, and `R` is only used to declare the type of "\n'
    '"the argument `source`."\n',
    '"`parse_csv_document` jest ogólne, pozwalając przyjmować dowolny typ implementujący "\n'
    '"BufRead, taki jak `BufReader<File>` lub `[u8]`, ale nie jest ważne, jaki typ ma `R`, "\n'
    '"i `R` jest używane tylko do deklarowania typu argumentu `source`."\n'
)

prose('As a return type', 'Jako typ zwracany')

multi(
    'msgid ""\n'
    '"Note that using `impl Trait` as an argument type means that you cannot "\n'
    '"explicitly state what form of the function you use, i.e. "\n'
    '"`parse_csv_document::<std::io::Empty>(std::io::empty())` will not work with "\n'
    '"the `impl Trait` version."\n',
    '"Należy zauważyć, że używanie `impl Trait` jako typu argumentu oznacza, że nie można "\n'
    '"jawnie podać, której formy funkcji się używa, tzn. "\n'
    '"`parse_csv_document::<std::io::Empty>(std::io::empty())` nie zadziała z "\n'
    '"wersją `impl Trait`."\n'
)

multi(
    'msgid ""\n'
    '"If your function returns a type that implements `MyTrait`, you can write its "\n'
    '"return type as `-> impl MyTrait`. This can help simplify your type "\n'
    '"signatures quite a lot!"\n',
    '"Jeśli twoja funkcja zwraca typ implementujący `MyTrait`, możesz zapisać jej "\n'
    '"typ zwracany jako `-> impl MyTrait`. Może to znacznie uprościć sygnatury typów!"\n'
)

multi(
    'msgid ""\n'
    '"// This function combines two `Vec<i32>` and returns an iterator over it.\\n"\n'
    '"// Look how complicated its return type is!\\n"\n',
    '"// Ta funkcja łączy dwa `Vec<i32>` i zwraca iterator po nich.\\n"\n'
    '"// Spójrz, jak skomplikowany jest jej typ zwracany!\\n"\n'
)

multi(
    'msgid ""\n'
    '"// This is the exact same function, but its return type uses `impl Trait`.\\n"\n'
    '"// Look how much simpler it is!\\n"\n',
    '"// To dokładnie ta sama funkcja, ale jej typ zwracany używa `impl Trait`.\\n"\n'
    '"// Spójrz, jak dużo prostszy jest!\\n"\n'
)

verbatim('\\"all done\\"')

multi(
    'msgid ""\n'
    '"More importantly, some Rust types can\'t be written out. For example, every "\n'
    '"closure has its own unnamed concrete type. Before `impl Trait` syntax, you "\n'
    '"had to allocate on the heap in order to return a closure. But now you can do "\n'
    '"it all on the stack:"\n',
    '"Co ważniejsze, niektórych typów Rust nie można zapisać. Na przykład każde domknięcie "\n'
    '"ma swój własny nienazwany konkretny typ. Przed składnią `impl Trait` trzeba było "\n'
    '"alokować na stercie, aby zwrócić domknięcie. Ale teraz można to wszystko robić na stosie:"\n'
)

comment('// Returns a function that adds `y` to its input\\n',
        '// Zwraca funkcję, która dodaje `y` do swojego wejścia\\n')

multi(
    'msgid ""\n'
    '"You can also use `impl Trait` to return an iterator that uses `map` or "\n'
    '"`filter` closures! This makes using `map` and `filter` easier. Because "\n'
    '"closure types don\'t have names, you can\'t write out an explicit return type "\n'
    '"if your function returns iterators with closures."\n',
    '"Możesz też używać `impl Trait` do zwracania iteratora, który używa domknięć `map` "\n'
    '"lub `filter`! Ułatwia to używanie `map` i `filter`. Ponieważ typy domknięć nie "\n'
    '"mają nazw, nie można zapisać jawnego typu zwracanego, jeśli funkcja zwraca iteratory "\n'
    '"z domknięciami."\n'
)

# ─── trait/clone.md ────────────────────────────────────────────────────────

prose('Clone and Copy', 'Clone i Copy')
prose('Copy: Implicit Cloning', 'Copy: niejawne klonowanie')

multi(
    'msgid ""\n'
    '"When dealing with resources, the default behavior is to transfer them during "\n'
    '"assignments or function calls. However, sometimes we need to make a copy of "\n'
    '"the resource as well."\n',
    '"Podczas pracy z zasobami domyślnym zachowaniem jest przenoszenie ich podczas "\n'
    '"przypisań lub wywołań funkcji. Jednak czasami potrzebujemy też wykonać kopię zasobu."\n'
)

multi(
    'msgid ""\n'
    '"The [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html) trait "\n'
    '"helps us do exactly this. Most commonly, we can use the `.clone()` method "\n'
    '"defined by the `Clone` trait."\n',
    '"Cecha [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html) pomaga "\n'
    '"nam zrobić dokładnie to. Najczęściej możemy używać metody `.clone()` zdefiniowanej "\n'
    '"przez cechę `Clone`."\n'
)

multi(
    'msgid ""\n'
    '"The [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html) trait "\n'
    '"allows a type to be duplicated simply by copying bits, with no additional "\n'
    '"logic required. When a type implements `Copy`, assignments and function "\n'
    '"calls will copy the value instead of moving it."\n',
    '"Cecha [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html) pozwala "\n'
    '"typowi być powielanym przez proste kopiowanie bitów, bez dodatkowej logiki. "\n'
    '"Gdy typ implementuje `Copy`, przypisania i wywołania funkcji skopiują wartość "\n'
    '"zamiast ją przenosić."\n'
)

multi(
    'msgid ""\n'
    '"**Important:** `Copy` requires `Clone` - any type that implements `Copy` "\n'
    '"must also implement `Clone`. This is because `Copy` is defined as a "\n'
    '"subtrait: `trait Copy: Clone {}`. The `Clone` implementation for `Copy` "\n'
    '"types is typically trivial."\n',
    '"**Ważne:** `Copy` wymaga `Clone` - każdy typ implementujący `Copy` musi też "\n'
    '"implementować `Clone`. Wynika to z faktu, że `Copy` jest zdefiniowane jako "\n'
    '"podcecha: `trait Copy: Clone {}`. Implementacja `Clone` dla typów `Copy` "\n'
    '"jest zazwyczaj trywialna."\n'
)

prose('Not all types can implement `Copy`. A type can only be `Copy` if:',
      'Nie wszystkie typy mogą implementować `Copy`. Typ może być `Copy` tylko jeśli:')
prose('All of its components are `Copy`',
      'Wszystkie jego składniki są `Copy`')
prose('It doesn\'t manage external resources (like heap memory, file handles, etc.)',
      'Nie zarządza zasobami zewnętrznymi (jak pamięć sterty, uchwyty do plików itp.)')

multi(
    'msgid ""\n'
    '"// A unit struct without resources\\n"\n'
    '"// Note: Copy requires Clone, so we must derive both\\n"\n',
    '"// Struktura jednostkowa bez zasobów\\n"\n'
    '"// Uwaga: Copy wymaga Clone, więc musimy wyprowadzić oba\\n"\n'
)

multi(
    'msgid ""\n'
    '"// A tuple struct with resources that implements the `Clone` trait\\n"\n'
    '"// This CANNOT be Copy because Box<T> is not Copy\\n"\n',
    '"// Krotka-struktura z zasobami implementująca cechę `Clone`\\n"\n'
    '"// NIE MOŻE być Copy, bo Box<T> nie jest Copy\\n"\n'
)

comment('// Instantiate `Unit`\\n', '// Utwórz instancję `Unit`\\n')

multi(
    'msgid ""\n'
    '"// Copy `Unit` - this is an implicit copy, not a move!\\n"\n'
    '"    // Because Unit implements Copy, the value is duplicated automatically\\n"\n',
    '"// Kopiuj `Unit` - to jest niejawna kopia, nie przeniesienie!\\n"\n'
    '"    // Ponieważ Unit implementuje Copy, wartość jest automatycznie powielana\\n"\n'
)

comment('// Both `Unit`s can be used independently\\n',
        '// Obie instancje `Unit` mogą być używane niezależnie\\n')
verbatim('\\"original: {:?}\\"')
verbatim('\\"copy: {:?}\\"')
comment('// Instantiate `Pair`\\n', '// Utwórz instancję `Pair`\\n')

multi(
    'msgid ""\n'
    '"// Move `pair` into `moved_pair`, moves resources\\n"\n'
    '"    // Pair does not implement Copy, so this is a move\\n"\n',
    '"// Przenieś `pair` do `moved_pair`, przenosi zasoby\\n"\n'
    '"    // Pair nie implementuje Copy, więc to jest przeniesienie\\n"\n'
)

verbatim('\\"moved: {:?}\\"')

multi(
    'msgid ""\n'
    '"// Error! `pair` has lost its resources\\n"\n'
    '"    //println!(\\\"original: {:?}\\\", pair);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `pair` utraciło swoje zasoby\\n"\n'
    '"    //println!(\\\"original: {:?}\\\", pair);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Clone `moved_pair` into `cloned_pair` (resources are included)\\n"\n'
    '"    // Unlike Copy, Clone is explicit - we must call .clone()\\n"\n',
    '"// Klonuj `moved_pair` do `cloned_pair` (zasoby są zawarte)\\n"\n'
    '"    // W przeciwieństwie do Copy, Clone jest jawne - musimy wywołać .clone()\\n"\n'
)

comment('// Drop the moved original pair using std::mem::drop\\n',
        '// Upuść przeniesioną oryginalną parę używając std::mem::drop\\n')

multi(
    'msgid ""\n'
    '"// Error! `moved_pair` has been dropped\\n"\n'
    '"    //println!(\\\"moved and dropped: {:?}\\\", moved_pair);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd! `moved_pair` zostało upuszczone\\n"\n'
    '"    //println!(\\\"moved and dropped: {:?}\\\", moved_pair);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

comment('// The result from .clone() can still be used!\\n',
        '// Wynik z .clone() nadal może być używany!\\n')
verbatim('\\"clone: {:?}\\"')

# ─── trait/supertraits.md ──────────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"Rust doesn\'t have \\"inheritance\\", but you can define a trait as being a "\n'
    '"superset of another trait. For example:"\n',
    '"Rust nie ma \\"dziedziczenia\\", ale można zdefiniować cechę jako nadzbiór "\n'
    '"innej cechy. Na przykład:"\n'
)

multi(
    'msgid ""\n'
    '"// Person is a supertrait of Student.\\n"\n'
    '"// Implementing Student requires you to also impl Person.\\n"\n',
    '"// Person jest nadcechą Student.\\n"\n'
    '"// Implementacja Student wymaga też impl Person.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// CompSciStudent (computer science student) is a subtrait of both Programmer\\n"\n'
    '"// and Student. Implementing CompSciStudent requires you to impl both supertraits.\\n"\n',
    '"// CompSciStudent (student informatyki) jest podcechą zarówno Programmer\\n"\n'
    '"// jak i Student. Implementacja CompSciStudent wymaga impl obu nadcech.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// CompSciStudent (computer science student) is a subtrait of both Programmer\\n"\n'
    '"// and Student. Implementing CompSciStudent requires you to impl both supertraits.\\n"\n',
    '"// CompSciStudent (student informatyki) jest podcechą zarówno Programmer\\n"\n'
    '"// jak i Student. Implementacja CompSciStudent wymaga impl obu nadcech.\\n"\n'
)

multi(
    'msgid ""\n'
    '"\\\"My name is {} and I attend {}. My favorite language is {}. My Git username is {}\\\""\n',
    '"\\\"Mam na imię {} i uczęszczam do {}. Moim ulubionym językiem jest {}. Mój login Git to {}\\\""\n'
)

verbatim('\\"MIT\\"')
verbatim('\\"alice_codes\\"')

multi(
    'msgid ""\n'
    '"[The Rust Programming Language chapter on supertraits](https://doc.rust-lang."\n'
    '"org/book/ch19-03-advanced-traits.html#using-supertraits-to-require-one-"\n'
    '"traits-functionality-within-another-trait)"\n',
    '"[Rozdział Rust Programming Language o nadcechach](https://doc.rust-lang."\n'
    '"org/book/ch19-03-advanced-traits.html#using-supertraits-to-require-one-"\n'
    '"traits-functionality-within-another-trait)"\n'
)

# ─── trait/disambiguating.md ───────────────────────────────────────────────

multi(
    'msgid ""\n'
    '"A type can implement many different traits. What if two traits both require "\n'
    '"the same name for a function? For example, many traits might have a method "\n'
    '"named `get()`. They might even have different return types!"\n',
    '"Typ może implementować wiele różnych cech. Co jeśli dwie cechy wymagają tej samej "\n'
    '"nazwy dla funkcji? Na przykład wiele cech może mieć metodę o nazwie `get()`. "\n'
    '"Mogą nawet mieć różne typy zwracane!"\n'
)

multi(
    'msgid ""\n'
    '"Good news: because each trait implementation gets its own `impl` block, it\'s "\n'
    '"clear which trait\'s `get` method you\'re implementing."\n',
    '"Dobra wiadomość: ponieważ każda implementacja cechy ma własny blok `impl`, "\n'
    '"jasne jest, której metody `get` cechy się implementuje."\n'
)

multi(
    'msgid ""\n'
    '"What about when it comes time to _call_ those methods? To disambiguate "\n'
    '"between them, we have to use Fully Qualified Syntax."\n',
    '"A co gdy przychodzi czas na _wywołanie_ tych metod? Aby je rozróżnić, "\n'
    '"musimy użyć w pełni kwalifikowanej składni."\n'
)

comment('// Get the selected username out of this widget\\n',
        '// Pobierz wybraną nazwę użytkownika z tego widżetu\\n')
comment('// Get the selected age out of this widget\\n',
        '// Pobierz wybrany wiek z tego widżetu\\n')
comment('// A form with both a UsernameWidget and an AgeWidget\\n',
        '// Formularz z UsernameWidget i AgeWidget\\n')

multi(
    'msgid ""\n'
    '"// If you uncomment this line, you\'ll get an error saying\\n"\n'
    '"    // \\"multiple `get` found\\". Because, after all, there are multiple methods\\n"\n'
    '"    // named `get` in scope.\\n"\n'
    '"    // form.get()\\n"\n'
    '"    // TODO ^ try uncommenting this line\\n"\n',
    '"// Jeśli odkomentowasz tę linię, otrzymasz błąd mówiący\\n"\n'
    '"    // \\"multiple `get` found\\". Bo w końcu istnieje wiele metod\\n"\n'
    '"    // o nazwie `get` w zakresie.\\n"\n'
    '"    // form.get()\\n"\n'
    '"    // TODO ^ spróbuj odkomentować tę linię\\n"\n'
)

verbatim('\\"rustacean\\"')

multi(
    'msgid ""\n'
    '"[The Rust Programming Language chapter on Fully Qualified syntax](https://"\n'
    '"doc.rust-lang.org/book/ch19-03-advanced-traits.html#fully-qualified-syntax-"\n'
    '"for-disambiguation-calling-methods-with-the-same-name)"\n',
    '"[Rozdział Rust Programming Language o w pełni kwalifikowanej składni](https://"\n'
    '"doc.rust-lang.org/book/ch19-03-advanced-traits.html#fully-qualified-syntax-"\n'
    '"for-disambiguation-calling-methods-with-the-same-name)"\n'
)

# ───────────────────────────────────────────────────────────────────────────

open('po/pl.po', 'w').write(text)
print(f'\nŁącznie zmian: {total}')
