#!/usr/bin/env python3
# Etap 8b: poprawki NIE z etap8

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

def multi(old_body, new_msgstr):
    old = old_body + 'msgstr ""'
    new = old_body + 'msgstr ""\n' + new_msgstr
    apply(old, new, old_body[8:48])

# trait.md:6 — ends with "`Sheep`." not "`Sheep` instance."
multi(
    'msgid ""\n'
    '"Traits can be implemented for any data type. In the example below, we define "\n'
    '"`Animal`, a group of methods. The `Animal` `trait` is then implemented for "\n'
    '"the `Sheep` data type, allowing the use of methods from `Animal` with a "\n'
    '"`Sheep`."\n',
    '"Cechy mogą być implementowane dla dowolnego typu danych. W poniższym przykładzie "\n'
    '"definiujemy `Animal`, grupę metod. Cecha `Animal` jest następnie implementowana "\n'
    '"dla typu danych `Sheep`, umożliwiając używanie metod z `Animal` z instancją `Sheep`."\n'
)

# trait/derive.md:67 — single-line format
prose('[`derive`](https://doc.rust-lang.org/reference/attributes.html#derive)',
      '[`derive`](https://doc.rust-lang.org/reference/attributes.html#derive)')

# trait/dyn.md:39 — "at compile time.\\n" on continuation line
multi(
    'msgid ""\n'
    '"// Returns some struct that implements Animal, but we don\'t know which one "\n'
    '"at compile time.\\n"\n',
    '"// Zwraca jakąś strukturę implementującą Animal, ale nie wiemy którą w czasie kompilacji.\\n"\n'
)

# trait/ops.md:3 — different line breaks
multi(
    'msgid ""\n'
    '"In Rust, many of the operators can be overloaded via traits. That is, some "\n'
    '"operators can be used to accomplish different tasks based on their input "\n'
    '"arguments. This is possible because operators are syntactic sugar for method "\n'
    '"calls. For example, the `+` operator in `a + b` calls the `add` method (as "\n'
    '"in `a.add(b)`). This `add` method is part of the `Add` trait. Hence, the `+` "\n'
    '"operator can be used by any implementor of the `Add` trait."\n',
    '"W Rust wiele operatorów można przeciążać za pomocą cech. To znaczy, że niektóre "\n'
    '"operatory mogą być używane do różnych zadań w zależności od argumentów wejściowych. "\n'
    '"Jest to możliwe, ponieważ operatory są lukrem składniowym dla wywołań metod. Na "\n'
    '"przykład operator `+` w `a + b` wywołuje metodę `add` (jak w `a.add(b)`). Ta "\n'
    '"metoda `add` jest częścią cechy `Add`. Dlatego operator `+` może być używany "\n'
    '"przez każdego implementującego cechę `Add`."\n'
)

# trait/ops.md:22 — "`Bar`.\\n" on continuation + extra line
multi(
    'msgid ""\n'
    '"// The `std::ops::Add` trait is used to specify the functionality of `+`.\\n"\n'
    '"// Here, we make `Add<Bar>` - the trait for addition with a RHS of type "\n'
    '"`Bar`.\\n"\n'
    '"// The following block implements the operation: Foo + Bar = FooBar\\n"\n',
    '"// Cecha `std::ops::Add` służy do określania funkcjonalności `+`.\\n"\n'
    '"// Tu tworzymy `Add<Bar>` - cechę dodawania z prawym operandem typu `Bar`.\\n"\n'
    '"// Poniższy blok implementuje operację: Foo + Bar = FooBar\\n"\n'
)

# trait/ops.md:35 — "`Foo`.\\n" on continuation + extra line
multi(
    'msgid ""\n'
    '"// By reversing the types, we end up implementing non-commutative addition.\\n"\n'
    '"// Here, we make `Add<Foo>` - the trait for addition with a RHS of type "\n'
    '"`Foo`.\\n"\n'
    '"// This block implements the operation: Bar + Foo = BarFoo\\n"\n',
    '"// Odwracając typy, implementujemy nieprzemienne dodawanie.\\n"\n'
    '"// Tu tworzymy `Add<Foo>` - cechę dodawania z prawym operandem typu `Foo`.\\n"\n'
    '"// Ten blok implementuje operację: Bar + Foo = BarFoo\\n"\n'
)

# trait/drop.md:77 — different content
multi(
    'msgid ""\n'
    '"// When TempFile is dropped:\\n"\n'
    '"// 1. First, our custom drop implementation runs. The file is still open at "\n'
    '"this point,\\n"\n'
    '"//    but we can remove it from the filesystem by path.\\n"\n'
    '"// 2. Then, after our drop returns, Rust automatically drops each field,\\n"\n'
    '"//    so File\'s drop runs and closes the file handle.\\n"\n',
    '"// Gdy TempFile jest upuszczany:\\n"\n'
    '"// 1. Najpierw uruchamia się nasza własna implementacja drop. Plik jest nadal otwarty,\\n"\n'
    '"//    ale możemy go usunąć z systemu plików po ścieżce.\\n"\n'
    '"// 2. Następnie, po powrocie naszego drop, Rust automatycznie upuszcza każde pole,\\n"\n'
    '"//    więc drop File uruchamia się i zamyka uchwyt pliku.\\n"\n'
)

# trait/drop.md:85 — "method.\\n" on continuation line
multi(
    'msgid ""\n'
    '"// Note: the File is still open here — field destructors run after this "\n'
    '"method.\\n"\n',
    '"// Uwaga: plik jest nadal otwarty tutaj — destruktory pól uruchamiają się po tej metodzie.\\n"\n'
)

# trait/iter.md:18 — different 4th line
multi(
    'msgid ""\n'
    '"// Implement `Iterator` for `Fibonacci`.\\n"\n'
    '"// The `Iterator` trait only requires a method to be defined for the `next` "\n'
    '"element,\\n"\n'
    '"// and an `associated type` to declare the return type of the iterator.\\n"\n',
    '"// Implementuj `Iterator` dla `Fibonacci`.\\n"\n'
    '"// Cecha `Iterator` wymaga zdefiniowania tylko metody dla elementu `next`,\\n"\n'
    '"// i `skojarzonego typu` do deklarowania typu zwracanego przez iterator.\\n"\n'
)

# trait/iter.md:72 — "terms.\\n" on continuation line
multi(
    'msgid ""\n'
    '"// The `skip(n)` method shortens an `Iterator` by dropping its first `n` "\n'
    '"terms.\\n"\n',
    '"// Metoda `skip(n)` skraca `Iterator` pomijając jego pierwsze `n` elementów.\\n"\n'
)

# trait/impl_trait.md:30 — different last line: "`src`, so the function can also be written as:"
multi(
    'msgid ""\n'
    '"`parse_csv_document` is generic, allowing it to take any type which "\n'
    '"implements BufRead, such as `BufReader<File>` or `[u8]`, but it\'s not "\n'
    '"important what type `R` is, and `R` is only used to declare the type of "\n'
    '"`src`, so the function can also be written as:"\n',
    '"`parse_csv_document` jest ogólne, pozwalając przyjmować dowolny typ implementujący "\n'
    '"BufRead, taki jak `BufReader<File>` lub `[u8]`, ale nie jest ważne, jaki typ ma `R`, "\n'
    '"i `R` jest używane tylko do deklarowania typu `src`, więc funkcja może być też zapisana jako:"\n'
)

# trait/impl_trait.md:49 — different last line: "the second example."
multi(
    'msgid ""\n'
    '"Note that using `impl Trait` as an argument type means that you cannot "\n'
    '"explicitly state what form of the function you use, i.e. "\n'
    '"`parse_csv_document::<std::io::Empty>(std::io::empty())` will not work with "\n'
    '"the second example."\n',
    '"Należy zauważyć, że używanie `impl Trait` jako typu argumentu oznacza, że nie można "\n'
    '"jawnie podać, której formy funkcji się używa, tzn. "\n'
    '"`parse_csv_document::<std::io::Empty>(std::io::empty())` nie zadziała z "\n'
    '"drugim przykładem."\n'
)

# trait/impl_trait.md:91 — different last line: "it all statically, like this:"
multi(
    'msgid ""\n'
    '"More importantly, some Rust types can\'t be written out. For example, every "\n'
    '"closure has its own unnamed concrete type. Before `impl Trait` syntax, you "\n'
    '"had to allocate on the heap in order to return a closure. But now you can do "\n'
    '"it all statically, like this:"\n',
    '"Co ważniejsze, niektórych typów Rust nie można zapisać. Na przykład każde domknięcie "\n'
    '"ma swój własny nienazwany konkretny typ. Przed składnią `impl Trait` trzeba było "\n'
    '"alokować na stercie, aby zwrócić domknięcie. Ale teraz można to wszystko robić statycznie:"\n'
)

# trait/clone.md:16 — different last line: "types simply copies the bits."
multi(
    'msgid ""\n'
    '"**Important:** `Copy` requires `Clone` - any type that implements `Copy` "\n'
    '"must also implement `Clone`. This is because `Copy` is defined as a "\n'
    '"subtrait: `trait Copy: Clone {}`. The `Clone` implementation for `Copy` "\n'
    '"types simply copies the bits."\n',
    '"**Ważne:** `Copy` wymaga `Clone` - każdy typ implementujący `Copy` musi też "\n'
    '"implementować `Clone`. Wynika to z faktu, że `Copy` jest zdefiniowane jako "\n'
    '"podcecha: `trait Copy: Clone {}`. Implementacja `Clone` dla typów `Copy` "\n'
    '"po prostu kopiuje bity."\n'
)

# trait/clone.md:23 — multi-line format
multi(
    'msgid ""\n'
    '"It doesn\'t manage external resources (like heap memory, file handles, etc.)"\n',
    '"Nie zarządza zasobami zewnętrznymi (jak pamięć sterty, uchwyty do plików itp.)"\n'
)

# trait/supertraits.md:20 — "Programmer\\n" on continuation line
multi(
    'msgid ""\n'
    '"// CompSciStudent (computer science student) is a subtrait of both "\n'
    '"Programmer\\n"\n'
    '"// and Student. Implementing CompSciStudent requires you to impl both "\n'
    '"supertraits.\\n"\n',
    '"// CompSciStudent (student informatyki) jest podcechą zarówno Programmer\\n"\n'
    '"// jak i Student. Implementacja CompSciStudent wymaga impl obu nadcech.\\n"\n'
)

# trait/supertraits.md:29 — "is {}\\"" on continuation line
multi(
    'msgid ""\n'
    '"\\"My name is {} and I attend {}. My favorite language is {}. My Git username "\n'
    '"is {}\\""\n',
    '"\\"Mam na imię {} i uczęszczam do {}. Moim ulubionym językiem jest {}. Mój login Git to {}\\""\n'
)

# trait/disambiguating.md:48 — "methods\\n" on continuation, different content
multi(
    'msgid ""\n'
    '"// If you uncomment this line, you\'ll get an error saying\\n"\n'
    '"    // \\"multiple `get` found\\". Because, after all, there are multiple "\n'
    '"methods\\n"\n'
    '"    // named `get`.\\n"\n'
    '"    // println!(\\"{}\\", form.get());\\n"\n',
    '"// Jeśli odkomentowasz tę linię, otrzymasz błąd mówiący\\n"\n'
    '"    // \\"multiple `get` found\\". Bo w końcu istnieje wiele metod\\n"\n'
    '"    // o nazwie `get`.\\n"\n'
    '"    // println!(\\"{}\\", form.get());\\n"\n'
)

# ───────────────────────────────────────────────────────────────────────────

open('po/pl.po', 'w').write(text)
print(f'\nŁącznie zmian: {total}')
