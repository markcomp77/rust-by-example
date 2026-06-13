#!/usr/bin/env python3
"""Tłumaczenie Etapu 6: Cargo, Atrybuty, Typy ogólne."""

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
# cargo.md
# ============================================================

multi(
    'msgid ""\n'
    '"`cargo` is the official Rust package management tool. It has lots of really "\n'
    '"useful features to improve code quality and developer velocity! These include"\n',
    '"`cargo` to oficjalne narzędzie do zarządzania pakietami w Rust. Oferuje wiele "\n'
    '"użytecznych funkcji poprawiających jakość kodu i szybkość pracy deweloperskiej! Są to"\n'
)

multi(
    'msgid ""\n'
    '"Dependency management and integration with [crates.io](https://crates.io) "\n'
    '"(the official Rust package registry)"\n',
    '"Zarządzanie zależnościami i integracja z [crates.io](https://crates.io) "\n'
    '"(oficjalnym rejestrem pakietów Rusta)"\n'
)

prose('Awareness of unit tests', 'Obsługa testów jednostkowych')
prose('Awareness of benchmarks', 'Obsługa testów wydajnościowych')

multi(
    'msgid ""\n'
    '"This chapter will go through some quick basics, but you can find the "\n'
    '"comprehensive docs in [The Cargo Book](https://doc.rust-lang.org/cargo/)."\n',
    '"Ten rozdział omówi podstawy, a pełną dokumentację można znaleźć w "\n'
    '"[The Cargo Book](https://doc.rust-lang.org/cargo/)."\n'
)

# ============================================================
# cargo/deps.md
# ============================================================

multi(
    'msgid ""\n'
    '"Most programs have dependencies on some libraries. If you have ever managed "\n'
    '"dependencies by hand, you know how much of a pain this can be. Luckily, the "\n'
    '"Rust ecosystem comes standard with `cargo`! `cargo` can manage dependencies "\n'
    '"for a project."\n',
    '"Większość programów zależy od pewnych bibliotek. Jeśli kiedykolwiek zarządzano "\n'
    '"zależnościami ręcznie, wiadomo jak uciążliwe to może być. Na szczęście "\n'
    '"ekosystem Rusta jest standardowo wyposażony w `cargo`! `cargo` może zarządzać "\n'
    '"zależnościami projektu."\n'
)

prose('To create a new Rust project,', 'Aby utworzyć nowy projekt Rusta,')
comment('# A binary\\n', '# Binarny\\n')
comment('# A library\\n', '# Biblioteka\\n')

multi(
    'msgid ""\n'
    '"For the rest of this chapter, let\'s assume we are making a binary, rather "\n'
    '"than a library, but all of the concepts are the same."\n',
    '"W pozostałej części rozdziału zakładamy, że tworzymy program binarny, a nie "\n'
    '"bibliotekę, ale wszystkie koncepcje są takie same."\n'
)

prose('After the above commands, you should see a file hierarchy like this:',
      'Po powyższych poleceniach powinna być widoczna następująca hierarchia plików:')

multi(
    'msgid ""\n'
    '"The `main.rs` is the root source file for your new `foo` project -- nothing "\n'
    '"new there. The `Cargo.toml` is the config file for `cargo` for this project. "\n'
    '"If you look inside it, you should see something like this:"\n',
    '"Plik `main.rs` jest głównym plikiem źródłowym projektu `foo` — nic nowego. "\n'
    '"Plik `Cargo.toml` to plik konfiguracyjny `cargo` dla tego projektu. "\n'
    '"Jeśli zajrzeć do środka, powinien wyglądać mniej więcej tak:"\n'
)

# Code block — verbatim
multi(
    'msgid ""\n'
    '"```toml\\n"\n'
    '"[package]\\n"\n'
    '"name = \\"foo\\"\\n"\n'
    '"version = \\"0.1.0\\"\\n"\n'
    '"authors = [\\"mark\\"]\\n"\n'
    '"\\n"\n'
    '"[dependencies]\\n"\n'
    '"```"\n',
    '"```toml\\n"\n'
    '"[package]\\n"\n'
    '"name = \\"foo\\"\\n"\n'
    '"version = \\"0.1.0\\"\\n"\n'
    '"authors = [\\"mark\\"]\\n"\n'
    '"\\n"\n'
    '"[dependencies]\\n"\n'
    '"```"\n'
)

multi(
    'msgid ""\n'
    '"The `name` field under `[package]` determines the name of the project. This "\n'
    '"is used by `crates.io` if you publish the crate (more later). It is also the "\n'
    '"name of the output binary when you compile."\n',
    '"Pole `name` w sekcji `[package]` określa nazwę projektu. Jest ona używana "\n'
    '"przez `crates.io` przy publikowaniu skrzyni (więcej później). To też nazwa "\n'
    '"pliku binarnego generowanego podczas kompilacji."\n'
)

multi(
    'msgid ""\n'
    '"The `version` field is a crate version number using [Semantic Versioning]"\n'
    '"(http://semver.org/)."\n',
    '"Pole `version` to numer wersji skrzyni zgodny z "\n'
    '"[Wersjonowaniem Semantycznym](http://semver.org/)."\n'
)

multi(
    'msgid ""\n'
    '"The `authors` field is a list of authors used when publishing the crate."\n',
    '"Pole `authors` to lista autorów używana przy publikowaniu skrzyni."\n'
)

multi(
    'msgid ""\n'
    '"The `[dependencies]` section lets you add dependencies for your project."\n',
    '"Sekcja `[dependencies]` pozwala dodawać zależności do projektu."\n'
)

multi(
    'msgid ""\n'
    '"For example, suppose that we want our program to have a great CLI. You can "\n'
    '"find lots of great packages on [crates.io](https://crates.io) (the official "\n'
    '"Rust package registry). One popular choice is [clap](https://crates.io/"\n'
    '"crates/clap). As of this writing, the most recent published version of "\n'
    '"`clap` is `2.27.1`. To add a dependency to our program, we can simply add "\n'
    '"the following to our `Cargo.toml` under `[dependencies]`: `clap = "\n'
    '"\\"2.27.1\\"`. And that\'s it! You can start using `clap` in your program."\n',
    '"Na przykład, jeśli program ma mieć dobry interfejs CLI, można znaleźć wiele "\n'
    '"świetnych pakietów na [crates.io](https://crates.io) (oficjalny rejestr pakietów Rusta). "\n'
    '"Popularnym wyborem jest [clap](https://crates.io/crates/clap). W chwili pisania "\n'
    '"najnowsza opublikowana wersja `clap` to `2.27.1`. Aby dodać zależność, wystarczy "\n'
    '"dodać do `Cargo.toml` w sekcji `[dependencies]`: `clap = \\"2.27.1\\"`. "\n'
    '"I to wszystko! Można zacząć używać `clap` w programie."\n'
)

multi(
    'msgid ""\n'
    '"`cargo` also supports [other types of dependencies](https://doc.rust-lang."\n'
    '"org/cargo/reference/specifying-dependencies.html). Here is just a small "\n'
    '"sampling:"\n',
    '"`cargo` obsługuje też [inne typy zależności](https://doc.rust-lang."\n'
    '"org/cargo/reference/specifying-dependencies.html). Oto kilka przykładów:"\n'
)

# Code block — verbatim (TOML with inline comments)
multi(
    'msgid ""\n'
    '"```toml\\n"\n'
    '"[package]\\n"\n'
    '"name = \\"foo\\"\\n"\n'
    '"version = \\"0.1.0\\"\\n"\n'
    '"authors = [\\"mark\\"]\\n"\n'
    '"\\n"\n'
    '"[dependencies]\\n"\n'
    '"clap = \\"2.27.1\\" # from crates.io\\n"\n'
    '"rand = { git = \\"https://github.com/rust-lang-nursery/rand\\" } # from online "\n'
    '"repo\\n"\n'
    '"bar = { path = \\"../bar\\" } # from a path in the local filesystem\\n"\n'
    '"```"\n',
    '"```toml\\n"\n'
    '"[package]\\n"\n'
    '"name = \\"foo\\"\\n"\n'
    '"version = \\"0.1.0\\"\\n"\n'
    '"authors = [\\"mark\\"]\\n"\n'
    '"\\n"\n'
    '"[dependencies]\\n"\n'
    '"clap = \\"2.27.1\\" # from crates.io\\n"\n'
    '"rand = { git = \\"https://github.com/rust-lang-nursery/rand\\" } # from online "\n'
    '"repo\\n"\n'
    '"bar = { path = \\"../bar\\" } # from a path in the local filesystem\\n"\n'
    '"```"\n'
)

multi(
    'msgid ""\n'
    '"`cargo` is more than a dependency manager. All of the available "\n'
    '"configuration options are listed in the [format specification](https://doc."\n'
    '"rust-lang.org/cargo/reference/manifest.html) of `Cargo.toml`."\n',
    '"`cargo` to coś więcej niż zarządca zależności. Wszystkie dostępne opcje "\n'
    '"konfiguracji są wymienione w [specyfikacji formatu](https://doc."\n'
    '"rust-lang.org/cargo/reference/manifest.html) pliku `Cargo.toml`."\n'
)

multi(
    'msgid ""\n'
    '"To build our project we can execute `cargo build` anywhere in the project "\n'
    '"directory (including subdirectories!). We can also do `cargo run` to build "\n'
    '"and run. Notice that these commands will resolve all dependencies, download "\n'
    '"crates if needed, and build everything, including your crate. (Note that it "\n'
    '"only rebuilds what it has not already built, similar to `make`)."\n',
    '"Aby zbudować projekt, można wykonać `cargo build` z dowolnego miejsca w "\n'
    '"katalogu projektu (w tym podkatalogów!). Można też użyć `cargo run` do "\n'
    '"zbudowania i uruchomienia. Polecenia te rozwiązują wszystkie zależności, "\n'
    '"pobierają skrzynie jeśli potrzeba i budują wszystko, w tym twoją skrzynię. "\n'
    '"(Przebudowywane jest tylko to, co jeszcze nie zostało zbudowane, podobnie jak w `make`)."\n'
)

prose("Voila! That's all there is to it!", 'Voilà! To wszystko, co trzeba wiedzieć!')

# ============================================================
# cargo/conventions.md
# ============================================================

prose('In the previous chapter, we saw the following directory hierarchy:',
      'W poprzednim rozdziale widzieliśmy następującą hierarchię katalogów:')

multi(
    'msgid ""\n'
    '"Suppose that we wanted to have two binaries in the same project, though. "\n'
    '"What then?"\n',
    '"Załóżmy jednak, że chcemy mieć dwa programy binarne w tym samym projekcie. "\n'
    '"Co wtedy?"\n'
)

multi(
    'msgid ""\n'
    '"It turns out that `cargo` supports this. The default binary name is `main`, "\n'
    '"as we saw before, but you can add additional binaries by placing them in a "\n'
    '"`bin/` directory:"\n',
    '"Okazuje się, że `cargo` to obsługuje. Domyślna nazwa programu binarnego to `main`, "\n'
    '"jak widzieliśmy wcześniej, ale można dodawać kolejne binaria umieszczając je "\n'
    '"w katalogu `bin/`:"\n'
)

multi(
    'msgid ""\n'
    '"To tell `cargo` to only compile or run this binary, we just pass `cargo` the "\n'
    '"`--bin my_other_bin` flag, where `my_other_bin` is the name of the binary we "\n'
    '"want to work with."\n',
    '"Aby powiedzieć `cargo`, żeby skompilował lub uruchomił tylko ten binarny, "\n'
    '"przekazujemy flagę `--bin my_other_bin`, gdzie `my_other_bin` to nazwa "\n'
    '"binarium, z którym chcemy pracować."\n'
)

multi(
    'msgid ""\n'
    '"In addition to extra binaries, `cargo` supports [more features](https://doc."\n'
    '"rust-lang.org/cargo/guide/project-layout.html) such as benchmarks, tests, "\n'
    '"and examples."\n',
    '"Oprócz dodatkowych plików binarnych, `cargo` obsługuje [więcej funkcji]"\n'
    '"(https://doc.rust-lang.org/cargo/guide/project-layout.html), takich jak "\n'
    '"testy wydajnościowe, testy i przykłady."\n'
)

prose('In the next chapter, we will look more closely at tests.',
      'W następnym rozdziale przyjrzymy się bliżej testom.')

# ============================================================
# cargo/test.md
# ============================================================

multi(
    'msgid ""\n'
    '"As we know testing is integral to any piece of software! Rust has first-"\n'
    '"class support for unit and integration testing ([see this chapter](https://"\n'
    '"doc.rust-lang.org/book/ch11-00-testing.html) in TRPL)."\n',
    '"Testowanie jest nieodłączną częścią każdego oprogramowania! Rust ma "\n'
    '"wbudowane wsparcie dla testów jednostkowych i integracyjnych "\n'
    '"([patrz ten rozdział](https://doc.rust-lang.org/book/ch11-00-testing.html) w TRPL)."\n'
)

multi(
    'msgid ""\n'
    '"From the testing chapters linked above, we see how to write unit tests and "\n'
    '"integration tests. Organizationally, we can place unit tests in the modules "\n'
    '"they test and integration tests in their own `tests/` directory:"\n',
    '"Z rozdziałów o testowaniu widzieliśmy jak pisać testy jednostkowe i "\n'
    '"integracyjne. Organizacyjnie: testy jednostkowe umieszcza się w modułach, "\n'
    '"które testują, a testy integracyjne w osobnym katalogu `tests/`:"\n'
)

multi(
    'msgid ""\n'
    '"Each file in `tests` is a separate [integration test](https://doc.rust-lang."\n'
    '"org/book/ch11-03-test-organization.html#integration-tests), i.e. a test that "\n'
    '"is meant to test your library as if it were being called from a dependent "\n'
    '"crate."\n',
    '"Każdy plik w `tests` to osobny [test integracyjny](https://doc.rust-lang."\n'
    '"org/book/ch11-03-test-organization.html#integration-tests), czyli test "\n'
    '"sprawdzający bibliotekę tak, jakby była wywoływana z zależnej skrzyni."\n'
)

multi(
    'msgid ""\n'
    '"The [Testing](../testing.md) chapter elaborates on the three different "\n'
    '"testing styles: [Unit](../testing/unit_testing.md), [Doc](../testing/"\n'
    '"doc_testing.md), and [Integration](../testing/integration_testing.md)."\n',
    '"Rozdział [Testowanie](../testing.md) opisuje trzy style testowania: "\n'
    '"[Jednostkowe](../testing/unit_testing.md), [Dokumentacyjne](../testing/"\n'
    '"doc_testing.md) i [Integracyjne](../testing/integration_testing.md)."\n'
)

prose('`cargo` naturally provides an easy way to run all of your tests!',
      '`cargo` naturalnie zapewnia prosty sposób uruchamiania wszystkich testów!')

prose('You should see output like this:', 'Powinny pojawić się dane wyjściowe podobne do tych:')

# Shell output block — verbatim
multi(
    'msgid ""\n'
    '"```shell\\n"\n'
    '"$ cargo test\\n"\n'
    '"   Compiling blah v0.1.0 (file:///nobackup/blah)\\n"\n'
    '"    Finished dev [unoptimized + debuginfo] target(s) in 0.89 secs\\n"\n'
    '"     Running target/debug/deps/blah-d3b32b97275ec472\\n"\n'
    '"\\n"\n'
    '"running 4 tests\\n"\n'
    '"test test_bar ... ok\\n"\n'
    '"test test_baz ... ok\\n"\n'
    '"test test_foo_bar ... ok\\n"\n'
    '"test test_foo ... ok\\n"\n'
    '"\\n"\n'
    '"test result: ok. 4 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out\\n"\n'
    '"```"\n',
    '"```shell\\n"\n'
    '"$ cargo test\\n"\n'
    '"   Compiling blah v0.1.0 (file:///nobackup/blah)\\n"\n'
    '"    Finished dev [unoptimized + debuginfo] target(s) in 0.89 secs\\n"\n'
    '"     Running target/debug/deps/blah-d3b32b97275ec472\\n"\n'
    '"\\n"\n'
    '"running 4 tests\\n"\n'
    '"test test_bar ... ok\\n"\n'
    '"test test_baz ... ok\\n"\n'
    '"test test_foo_bar ... ok\\n"\n'
    '"test test_foo ... ok\\n"\n'
    '"\\n"\n'
    '"test result: ok. 4 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out\\n"\n'
    '"```"\n'
)

prose('You can also run tests whose name matches a pattern:',
      'Można też uruchamiać testy, których nazwa pasuje do wzorca:')

# Shell output block — verbatim
multi(
    'msgid ""\n'
    '"```shell\\n"\n'
    '"$ cargo test test_foo\\n"\n'
    '"   Compiling blah v0.1.0 (file:///nobackup/blah)\\n"\n'
    '"    Finished dev [unoptimized + debuginfo] target(s) in 0.35 secs\\n"\n'
    '"     Running target/debug/deps/blah-d3b32b97275ec472\\n"\n'
    '"\\n"\n'
    '"running 2 tests\\n"\n'
    '"test test_foo ... ok\\n"\n'
    '"test test_foo_bar ... ok\\n"\n'
    '"\\n"\n'
    '"test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 2 filtered out\\n"\n'
    '"```"\n',
    '"```shell\\n"\n'
    '"$ cargo test test_foo\\n"\n'
    '"   Compiling blah v0.1.0 (file:///nobackup/blah)\\n"\n'
    '"    Finished dev [unoptimized + debuginfo] target(s) in 0.35 secs\\n"\n'
    '"     Running target/debug/deps/blah-d3b32b97275ec472\\n"\n'
    '"\\n"\n'
    '"running 2 tests\\n"\n'
    '"test test_foo ... ok\\n"\n'
    '"test test_foo_bar ... ok\\n"\n'
    '"\\n"\n'
    '"test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 2 filtered out\\n"\n'
    '"```"\n'
)

multi(
    'msgid ""\n'
    '"One word of caution: Cargo may run multiple tests concurrently, so make sure "\n'
    '"that they don\'t race with each other."\n',
    '"Uwaga: Cargo może uruchamiać wiele testów współbieżnie, więc należy upewnić się, "\n'
    '"że nie rywalizują ze sobą o zasoby."\n'
)

multi(
    'msgid ""\n'
    '"One example of this concurrency causing issues is if two tests output to a "\n'
    '"file, such as below:"\n',
    '"Przykładem problemów ze współbieżnością jest sytuacja, gdy dwa testy zapisują "\n'
    '"do tego samego pliku, jak poniżej:"\n'
)

comment('// Import the necessary modules\\n', '// Zaimportuj niezbędne moduły\\n')
comment('// This test writes to a file\\n', '// Ten test zapisuje do pliku\\n')
comment("// Opens the file ferris.txt or creates one if it doesn't exist.\\n",
        '// Otwiera plik ferris.txt lub tworzy go jeśli nie istnieje.\\n')
lit('ferris.txt')
lit('Failed to open ferris.txt')
comment('// Print \\"Ferris\\" 5 times.\\n', '// Drukuj \\"Ferris\\" 5 razy.\\n')
lit('Ferris\\\\n')
lit('Could not write to ferris.txt')
comment('// This test tries to write to the same file\\n',
        '// Ten test próbuje zapisywać do tego samego pliku\\n')
comment('// Print \\"Corro\\" 5 times.\\n', '// Drukuj \\"Corro\\" 5 razy.\\n')
lit('Corro\\\\n')

prose('Although the intent is to get the following:',
      'Choć intencją jest uzyskanie następujących danych:')
prose('What actually gets put into `ferris.txt` is this:',
      'To co faktycznie trafia do `ferris.txt` wygląda tak:')

# ============================================================
# cargo/build_scripts.md
# ============================================================

multi(
    'msgid ""\n'
    '"Sometimes a normal build from `cargo` is not enough. Perhaps your crate "\n'
    '"needs some pre-requisites before `cargo` will successfully compile, things "\n'
    '"like code generation, or some native code that needs to be compiled. To "\n'
    '"solve this problem we have build scripts that Cargo can run."\n',
    '"Czasem zwykła budowa z `cargo` nie wystarczy. Być może skrzynia wymaga "\n'
    '"pewnych wstępnych kroków przed udaną kompilacją, takich jak generowanie kodu "\n'
    '"lub kompilacja kodu natywnego. Do rozwiązania tego problemu służą skrypty "\n'
    '"budowania, które Cargo może uruchamiać."\n'
)

multi(
    'msgid ""\n'
    '"To add a build script to your package it can either be specified in the "\n'
    '"`Cargo.toml` as follows:"\n',
    '"Aby dodać skrypt budowania do pakietu, można go określić w "\n'
    '"`Cargo.toml` w następujący sposób:"\n'
)

# TOML code block — verbatim
multi(
    'msgid ""\n'
    '"```toml\\n"\n'
    '"[package]\\n"\n'
    '"...\\n"\n'
    '"build = \\"build.rs\\"\\n"\n'
    '"```"\n',
    '"```toml\\n"\n'
    '"[package]\\n"\n'
    '"...\\n"\n'
    '"build = \\"build.rs\\"\\n"\n'
    '"```"\n'
)

multi(
    'msgid ""\n'
    '"Otherwise Cargo will look for a `build.rs` file in the project directory by "\n'
    '"default."\n',
    '"W przeciwnym razie Cargo domyślnie szuka pliku `build.rs` w katalogu projektu."\n'
)

prose('How to use a build script', 'Jak używać skryptu budowania')

multi(
    'msgid ""\n'
    '"The build script is simply another Rust file that will be compiled and "\n'
    '"invoked prior to compiling anything else in the package. Hence it can be "\n'
    '"used to fulfill pre-requisites of your crate."\n',
    '"Skrypt budowania to zwykły plik Rusta, który jest kompilowany i wywoływany "\n'
    '"przed skompilowaniem czegokolwiek innego w pakiecie. Może więc być używany "\n'
    '"do spełnienia wymagań wstępnych skrzyni."\n'
)

multi(
    'msgid ""\n'
    '"Cargo provides the script with inputs via environment variables [specified "\n'
    '"here](https://doc.rust-lang.org/cargo/reference/environment-variables."\n'
    '"html#environment-variables-cargo-sets-for-build-scripts) that can be used."\n',
    '"Cargo dostarcza skryptowi dane wejściowe przez zmienne środowiskowe "\n'
    '"[opisane tutaj](https://doc.rust-lang.org/cargo/reference/environment-variables."\n'
    '"html#environment-variables-cargo-sets-for-build-scripts)."\n'
)

multi(
    'msgid ""\n'
    '"The script provides output via stdout. All lines printed are written to "\n'
    '"`target/debug/build/<pkg>/output`. Further, lines prefixed with `cargo:` "\n'
    '"will be interpreted by Cargo directly and hence can be used to define "\n'
    '"parameters for the package\'s compilation."\n',
    '"Skrypt przekazuje dane wyjściowe przez stdout. Wszystkie wydrukowane linie "\n'
    '"są zapisywane do `target/debug/build/<pkg>/output`. Linie z prefiksem `cargo:` "\n'
    '"są interpretowane bezpośrednio przez Cargo i mogą definiować parametry "\n'
    '"kompilacji pakietu."\n'
)

multi(
    'msgid ""\n'
    '"For further specification and examples have a read of the [Cargo "\n'
    '"specification](https://doc.rust-lang.org/cargo/reference/build-scripts.html)."\n',
    '"Więcej szczegółów i przykładów można znaleźć w "\n'
    '"[specyfikacji Cargo](https://doc.rust-lang.org/cargo/reference/build-scripts.html)."\n'
)

# ============================================================
# attribute.md
# ============================================================

multi(
    'msgid ""\n'
    '"An attribute is metadata applied to some module, crate or item. This "\n'
    '"metadata can be used to/for:"\n',
    '"Atrybut to metadane stosowane do modułu, skrzyni lub elementu. Metadane te "\n'
    '"mogą być używane do:"\n'
)

prose('[conditional compilation of code](attribute/cfg.md)',
      '[kompilacji warunkowej kodu](attribute/cfg.md)')

multi(
    'msgid ""\n'
    '"[set crate name, version and type (binary or library)](attribute/crate.md)"\n',
    '"[ustawiania nazwy, wersji i typu skrzyni (binarny lub biblioteka)](attribute/crate.md)"\n'
)

multi(
    'msgid ""\n'
    '"disable [lints](https://en.wikipedia.org/wiki/Lint_%28software%29) (warnings)"\n',
    '"wyłączania [lintów](https://en.wikipedia.org/wiki/Lint_%28software%29) (ostrzeżeń)"\n'
)

prose('enable compiler features (macros, glob imports, etc.)',
      'włączania funkcji kompilatora (makra, importy glob itp.)')
prose('link to a foreign library', 'łączenia z zewnętrzną biblioteką')
prose('mark functions as unit tests', 'oznaczania funkcji jako testy jednostkowe')
prose('mark functions that will be part of a benchmark',
      'oznaczania funkcji wchodzących w skład testów wydajnościowych')

multi(
    'msgid ""\n'
    '"[attribute like macros](https://doc.rust-lang.org/book/ch19-06-macros."\n'
    '"html#attribute-like-macros)"\n',
    '"[makra podobne do atrybutów](https://doc.rust-lang.org/book/ch19-06-macros."\n'
    '"html#attribute-like-macros)"\n'
)

multi(
    'msgid ""\n'
    '"Attributes look like `#[outer_attribute]` or `#![inner_attribute]`, with the "\n'
    '"difference between them being where they apply."\n',
    '"Atrybuty mają postać `#[outer_attribute]` lub `#![inner_attribute]`, a różnica "\n'
    '"między nimi polega na tym, do czego się stosują."\n'
)

multi(
    'msgid ""\n'
    '"`#[outer_attribute]` applies to the [item](https://doc.rust-lang.org/stable/"\n'
    '"reference/items.html) immediately following it. Some examples of items are: "\n'
    '"a function, a module declaration, a constant, a structure, an enum. Here is "\n'
    '"an example where attribute `#[derive(Debug)]` applies to the struct "\n'
    '"`Rectangle`:"\n',
    '"`#[outer_attribute]` stosuje się do [elementu](https://doc.rust-lang.org/stable/"\n'
    '"reference/items.html) bezpośrednio po nim następującego. Przykładami elementów są: "\n'
    '"funkcja, deklaracja modułu, stała, struktura, wyliczenie. Oto przykład, w którym "\n'
    '"atrybut `#[derive(Debug)]` stosuje się do struktury `Rectangle`:"\n'
)

multi(
    'msgid ""\n'
    '"`#![inner_attribute]` applies to the enclosing [item](https://doc.rust-lang."\n'
    '"org/stable/reference/items.html) (typically a module or a crate). In other "\n'
    '"words, this attribute is interpreted as applying to the entire scope in "\n'
    '"which it\'s placed. Here is an example where `#![allow(unused_variables)]` "\n'
    '"applies to the whole crate (if placed in `main.rs`):"\n',
    '"`#![inner_attribute]` stosuje się do otaczającego [elementu](https://doc.rust-lang."\n'
    '"org/stable/reference/items.html) (zazwyczaj modułu lub skrzyni). Innymi słowy, "\n'
    '"atrybut ten jest interpretowany jako stosowany do całego zasięgu, w którym jest "\n'
    '"umieszczony. Oto przykład, w którym `#![allow(unused_variables)]` stosuje się "\n'
    '"do całej skrzyni (jeśli umieszczony w `main.rs`):"\n'
)

comment('// This would normally warn about an unused variable.\\n',
        '// Normalnie spowodowałoby to ostrzeżenie o nieużywanej zmiennej.\\n')

prose('Attributes can take arguments with different syntaxes:',
      'Atrybuty mogą przyjmować argumenty w różnych składniach:')

prose('`#[attribute = \\"value\\"]`', '`#[attribute = \\"value\\"]`')
prose('`#[attribute(key = \\"value\\")]`', '`#[attribute(key = \\"value\\")]`')
prose('`#[attribute(value)]`', '`#[attribute(value)]`')

multi(
    'msgid ""\n'
    '"Attributes can have multiple values and can be separated over multiple "\n'
    '"lines, too:"\n',
    '"Atrybuty mogą mieć wiele wartości i mogą być rozdzielone na wiele linii:"\n'
)

# ============================================================
# attribute/unused.md
# ============================================================

multi(
    'msgid ""\n'
    '"The compiler provides a `dead_code` [_lint_](https://en.wikipedia.org/wiki/"\n'
    '"Lint_%28software%29) that will warn about unused functions. An _attribute_ "\n'
    '"can be used to disable the lint."\n',
    '"Kompilator dostarcza lint `dead_code` [_lint_](https://en.wikipedia.org/wiki/"\n'
    '"Lint_%28software%29), który ostrzega o nieużywanych funkcjach. _Atrybut_ "\n'
    '"może być użyty do wyłączenia tego lintu."\n'
)

multi(
    'msgid ""\n'
    '"// `#[allow(dead_code)]` is an attribute that disables the `dead_code` lint\\n"\n',
    '"// `#[allow(dead_code)]` to atrybut wyłączający lint `dead_code`\\n"\n'
)

comment('// FIXME ^ Add an attribute to suppress the warning\\n',
        '// FIXME ^ Dodaj atrybut, aby wyciszyć ostrzeżenie\\n')

multi(
    'msgid ""\n'
    '"Note that in real programs, you should eliminate dead code. In these "\n'
    '"examples we\'ll allow dead code in some places because of the interactive "\n'
    '"nature of the examples."\n',
    '"W prawdziwych programach należy eliminować martwy kod. W tych przykładach "\n'
    '"dopuszczamy martwy kod w niektórych miejscach ze względu na interaktywny "\n'
    '"charakter przykładów."\n'
)

# ============================================================
# attribute/crate.md
# ============================================================

multi(
    'msgid ""\n'
    '"The `crate_type` attribute can be used to tell the compiler whether a crate "\n'
    '"is a binary or a library (and even which type of library), and the "\n'
    '"`crate_name` attribute can be used to set the name of the crate."\n',
    '"Atrybut `crate_type` może być użyty do poinformowania kompilatora, czy skrzynia "\n'
    '"jest programem binarnym czy biblioteką (a nawet jakim rodzajem biblioteki), a "\n'
    '"atrybut `crate_name` może być użyty do ustawienia nazwy skrzyni."\n'
)

multi(
    'msgid ""\n'
    '"However, it is important to note that both the `crate_type` and `crate_name` "\n'
    '"attributes have **no** effect whatsoever when using Cargo, the Rust package "\n'
    '"manager. Since Cargo is used for the majority of Rust projects, this means "\n'
    '"real-world uses of `crate_type` and `crate_name` are relatively limited."\n',
    '"Ważne jest jednak, że atrybuty `crate_type` i `crate_name` nie mają **żadnego** "\n'
    '"efektu przy używaniu Cargo, zarządcy pakietów Rusta. Ponieważ Cargo jest używany "\n'
    '"w większości projektów Rusta, praktyczne zastosowanie `crate_type` i `crate_name` "\n'
    '"jest stosunkowo ograniczone."\n'
)

comment('// This crate is a library\\n', '// Ta skrzynia jest biblioteką\\n')
lit('lib')
comment('// The library is named \\"rary\\"\\n', '// Biblioteka nazywa się \\"rary\\"\\n')
lit('rary')

multi(
    'msgid ""\n'
    '"When the `crate_type` attribute is used, we no longer need to pass the `--"\n'
    '"crate-type` flag to `rustc`."\n',
    '"Gdy atrybut `crate_type` jest używany, nie trzeba już przekazywać flagi "\n'
    '"`--crate-type` do `rustc`."\n'
)

# ============================================================
# attribute/cfg.md
# ============================================================

multi(
    'msgid ""\n'
    '"Configuration conditional checks are possible through two different "\n'
    '"operators:"\n',
    '"Warunkowe sprawdzenia konfiguracji są możliwe przez dwa różne operatory:"\n'
)

prose('the `cfg` attribute: `#[cfg(...)]` in attribute position',
      'atrybut `cfg`: `#[cfg(...)]` w pozycji atrybutu')
prose('the `cfg!` macro: `cfg!(...)` in boolean expressions',
      'makro `cfg!`: `cfg!(...)` w wyrażeniach logicznych')

multi(
    'msgid ""\n'
    '"While the former enables conditional compilation, the latter conditionally "\n'
    '"evaluates to `true` or `false` literals allowing for checks at run-time. "\n'
    '"Both utilize identical argument syntax."\n',
    '"Pierwsza włącza kompilację warunkową, druga warunkowo ewaluuje do `true` lub "\n'
    '"`false`, umożliwiając sprawdzenia w czasie wykonania. Obie używają identycznej "\n'
    '"składni argumentów."\n'
)

multi(
    'msgid ""\n'
    '"`cfg!`, unlike `#[cfg]`, does not remove any code and only evaluates to true "\n'
    '"or false. For example, all blocks in an if/else expression need to be valid "\n'
    '"when `cfg!` is used for the condition, regardless of what `cfg!` is "\n'
    '"evaluating."\n',
    '"`cfg!`, w odróżnieniu od `#[cfg]`, nie usuwa żadnego kodu i jedynie ewaluuje "\n'
    '"do true lub false. Na przykład, wszystkie bloki wyrażenia if/else muszą być "\n'
    '"poprawne gdy `cfg!` jest używane jako warunek, niezależnie od tego co `cfg!` ewaluuje."\n'
)

comment('// This function only gets compiled if the target OS is linux\\n',
        '// Ta funkcja jest kompilowana tylko jeśli docelowy OS to linux\\n')
lit('linux')
lit('You are running linux!')

multi(
    'msgid ""\n'
    '"// And this function only gets compiled if the target OS is *not* linux\\n"\n',
    '"// A ta funkcja jest kompilowana tylko jeśli docelowy OS to *nie* linux\\n"\n'
)

lit('You are *not* running linux!')
lit('Are you sure?')
lit("Yes. It's definitely linux!")
lit("Yes. It's definitely *not* linux!")

multi(
    'msgid ""\n'
    '"[the reference](https://doc.rust-lang.org/reference/attributes."\n'
    '"html#conditional-compilation), [`cfg!`](https://doc.rust-lang.org/std/macro."\n'
    '"cfg!.html), and [macros](../macros.md)."\n',
    '"[the reference](https://doc.rust-lang.org/reference/attributes."\n'
    '"html#conditional-compilation), [`cfg!`](https://doc.rust-lang.org/std/macro."\n'
    '"cfg!.html) i [makra](../macros.md)."\n'
)

# ============================================================
# attribute/cfg/custom.md
# ============================================================

multi(
    'msgid ""\n'
    '"Some conditionals like `target_os` are implicitly provided by `rustc`, but "\n'
    '"custom conditionals must be passed to `rustc` using the `--cfg` flag."\n',
    '"Niektóre warunki jak `target_os` są dostarczane niejawnie przez `rustc`, ale "\n'
    '"własne warunki muszą być przekazywane do `rustc` za pomocą flagi `--cfg`."\n'
)

lit('condition met!')
prose('Try to run this to see what happens without the custom `cfg` flag.',
      'Spróbuj uruchomić to, aby zobaczyć co się stanie bez własnej flagi `cfg`.')
prose('With the custom `cfg` flag:', 'Z własną flagą `cfg`:')

# ============================================================
# generics.md
# ============================================================

multi(
    'msgid ""\n'
    '"_Generics_ is the topic of generalizing types and functionalities to broader "\n'
    '"cases. This is extremely useful for reducing code duplication in many ways, "\n'
    '"but can call for rather involved syntax. Namely, being generic requires "\n'
    '"taking great care to specify over which types a generic type is actually "\n'
    '"considered valid. The simplest and most common use of generics is for type "\n'
    '"parameters."\n',
    '"_Typy ogólne_ (generics) to temat uogólniania typów i funkcjonalności do "\n'
    '"szerszych przypadków. Jest to niezwykle przydatne do redukcji duplikacji kodu "\n'
    '"na wiele sposobów, ale może wymagać złożonej składni. Bycie ogólnym wymaga "\n'
    '"precyzyjnego określenia, dla jakich typów dany typ ogólny jest uznawany za "\n'
    '"poprawny. Najprostszym i najczęstszym zastosowaniem typów ogólnych są parametry typowe."\n'
)

multi(
    'msgid ""\n'
    '"A type parameter is specified as generic by the use of angle brackets and "\n'
    '"upper [camel case](https://en.wikipedia.org/wiki/CamelCase): `<Aaa, Bbb, ..."\n'
    '">`. \\"Generic type parameters\\" are typically represented as `<T>`. In Rust, "\n'
    '"\\"generic\\" also describes anything that accepts one or more generic type "\n'
    '"parameters `<T>`. Any type specified as a generic type parameter is generic, "\n'
    '"and everything else is concrete (non-generic)."\n',
    '"Parametr typowy jest oznaczany jako ogólny przez użycie nawiasów kątowych i "\n'
    '"notacji [camelCase](https://en.wikipedia.org/wiki/CamelCase): `<Aaa, Bbb, ..."\n'
    '">`. \\"Ogólne parametry typowe\\" są zazwyczaj reprezentowane jako `<T>`. W Rust, "\n'
    '"\\"ogólny\\" opisuje też wszystko, co przyjmuje jeden lub więcej parametrów typowych `<T>`. "\n'
    '"Każdy typ podany jako ogólny parametr typowy jest ogólny, a wszystko inne jest konkretne."\n'
)

multi(
    'msgid ""\n'
    '"For example, defining a _generic function_ named `foo` that takes an "\n'
    '"argument `T` of any type:"\n',
    '"Na przykład definiowanie _funkcji ogólnej_ o nazwie `foo` przyjmującej "\n'
    '"argument `T` dowolnego typu:"\n'
)

multi(
    'msgid ""\n'
    '"Because `T` has been specified as a generic type parameter using `<T>`, it "\n'
    '"is considered generic when used here as `(arg: T)`. This is the case even if "\n'
    '"`T` has previously been defined as a `struct`."\n',
    '"Ponieważ `T` zostało określone jako ogólny parametr typowy za pomocą `<T>`, "\n'
    '"jest uważane za ogólne gdy użyte jako `(arg: T)`. Dotyczy to nawet gdy "\n'
    '"`T` zostało wcześniej zdefiniowane jako `struct`."\n'
)

prose('This example shows some of the syntax in action:',
      'Ten przykład pokazuje część składni w działaniu:')

comment('// A concrete type `A`.\\n', '// Konkretny typ `A`.\\n')

multi(
    'msgid ""\n'
    '"// In defining the type `Single`, the first use of `A` is not preceded by "\n'
    '"`<A>`.\\n"\n'
    '"// Therefore, `Single` is a concrete type, and `A` is defined as above.\\n"\n',
    '"// Definiując typ `Single`, pierwsze użycie `A` nie jest poprzedzone `<A>`.\\n"\n'
    '"// Dlatego `Single` jest typem konkretnym, a `A` jest zdefiniowane jak wyżej.\\n"\n'
)

comment("//            ^ Here is `Single`s first use of the type `A`.\\n",
        '//            ^ Tu jest pierwsze użycie typu `A` w `Single`.\\n')

multi(
    'msgid ""\n'
    '"// Here, `<T>` precedes the first use of `T`, so `SingleGen` is a generic "\n'
    '"type.\\n"\n'
    '"// Because the type parameter `T` is generic, it could be anything, "\n'
    '"including\\n"\n'
    '"// the concrete type `A` defined at the top.\\n"\n',
    '"// Tu `<T>` poprzedza pierwsze użycie `T`, więc `SingleGen` jest typem ogólnym.\\n"\n'
    '"// Ponieważ parametr typowy `T` jest ogólny, może być czymkolwiek, w tym\\n"\n'
    '"// konkretnym typem `A` zdefiniowanym na górze.\\n"\n'
)

comment('// `Single` is concrete and explicitly takes `A`.\\n',
        '// `Single` jest konkretny i jawnie przyjmuje `A`.\\n')

multi(
    'msgid ""\n'
    '"// Create a variable `_char` of type `SingleGen<char>`\\n"\n'
    '"    // and give it the value `SingleGen(\'a\')`.\\n"\n'
    '"    // Here, `SingleGen` has a type parameter explicitly specified.\\n"\n',
    '"// Utwórz zmienną `_char` typu `SingleGen<char>`\\n"\n'
    '"    // i nadaj jej wartość `SingleGen(\'a\')`.\\n"\n'
    '"    // Tu `SingleGen` ma jawnie podany parametr typowy.\\n"\n'
)

comment('// `SingleGen` can also have a type parameter implicitly specified:\\n',
        '// `SingleGen` może też mieć niejawnie podany parametr typowy:\\n')
comment('// Uses `A` defined at the top.\\n', '// Używa `A` zdefiniowanego na górze.\\n')
comment('// Uses `i32`.\\n', '// Używa `i32`.\\n')
comment('// Uses `char`.\\n', '// Używa `char`.\\n')

prose('[`structs`](custom_types/structs.md)', '[`structs`](custom_types/structs.md)')

# ============================================================
# generics/gen_fn.md
# ============================================================

multi(
    'msgid ""\n'
    '"The same set of rules can be applied to functions: a type `T` becomes "\n'
    '"generic when preceded by `<T>`."\n',
    '"Ten sam zestaw zasad można zastosować do funkcji: typ `T` staje się ogólny "\n'
    '"gdy jest poprzedzony `<T>`."\n'
)

multi(
    'msgid ""\n'
    '"Using generic functions sometimes requires explicitly specifying type "\n'
    '"parameters. This may be the case if the function is called where the return "\n'
    '"type is generic, or if the compiler doesn\'t have enough information to infer "\n'
    '"the necessary type parameters."\n',
    '"Używanie funkcji ogólnych czasem wymaga jawnego podania parametrów typowych. "\n'
    '"Może to być konieczne gdy funkcja jest wywoływana w miejscu, gdzie typ zwracany "\n'
    '"jest ogólny, lub gdy kompilator nie ma wystarczających informacji do wnioskowania "\n'
    '"o niezbędnych parametrach typowych."\n'
)

multi(
    'msgid ""\n'
    '"A function call with explicitly specified type parameters looks like: `fun::"\n'
    '"<A, B, ...>()`."\n',
    '"Wywołanie funkcji z jawnie podanymi parametrami typowymi wygląda tak: `fun::"\n'
    '"<A, B, ...>()`."\n'
)

comment('// Concrete type `A`.\\n', '// Konkretny typ `A`.\\n')
comment('// Concrete type `S`.\\n', '// Konkretny typ `S`.\\n')
comment('// Generic type `SGen`.\\n', '// Ogólny typ `SGen`.\\n')

multi(
    'msgid ""\n'
    '"// The following functions all take ownership of the variable passed into\\n"\n'
    '"// them and immediately go out of scope, freeing the variable.\\n"\n',
    '"// Poniższe funkcje przejmują własność przekazanej zmiennej\\n"\n'
    '"// i natychmiast wychodzą z zasięgu, zwalniając zmienną.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Define a function `reg_fn` that takes an argument `_s` of type `S`.\\n"\n'
    '"// This has no `<T>` so this is not a generic function.\\n"\n',
    '"// Zdefiniuj funkcję `reg_fn` przyjmującą argument `_s` typu `S`.\\n"\n'
    '"// Brak `<T>` oznacza, że to nie jest funkcja ogólna.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Define a function `gen_spec_t` that takes an argument `_s` of type "\n'
    '"`SGen<T>`.\\n"\n'
    '"// It has been explicitly given the type parameter `A`, but because `A` has "\n'
    '"not\\n"\n'
    '"// been specified as a generic type parameter for `gen_spec_t`, it is not "\n'
    '"generic.\\n"\n',
    '"// Zdefiniuj funkcję `gen_spec_t` przyjmującą argument `_s` typu `SGen<T>`.\\n"\n'
    '"// Jawnie podano parametr typowy `A`, ale ponieważ `A` nie jest\\n"\n'
    '"// ogólnym parametrem typowym `gen_spec_t`, funkcja nie jest ogólna.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Define a function `gen_spec_i32` that takes an argument `_s` of type "\n'
    '"`SGen<i32>`.\\n"\n'
    '"// It has been explicitly given the type parameter `i32`, which is a "\n'
    '"specific type.\\n"\n'
    '"// Because `i32` is not a generic type, this function is also not generic.\\n"\n',
    '"// Zdefiniuj funkcję `gen_spec_i32` przyjmującą argument `_s` typu `SGen<i32>`.\\n"\n'
    '"// Jawnie podano parametr typowy `i32`, który jest konkretnym typem.\\n"\n'
    '"// Ponieważ `i32` nie jest typem ogólnym, ta funkcja też nie jest ogólna.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Define a function `generic` that takes an argument `_s` of type "\n'
    '"`SGen<T>`.\\n"\n'
    '"// Because `SGen<T>` is preceded by `<T>`, this function is generic over "\n'
    '"`T`.\\n"\n',
    '"// Zdefiniuj funkcję `generic` przyjmującą argument `_s` typu `SGen<T>`.\\n"\n'
    '"// Ponieważ `SGen<T>` jest poprzedzone `<T>`, funkcja jest ogólna względem `T`.\\n"\n'
)

comment('// Using the non-generic functions\\n', '// Używanie funkcji nieogólnych\\n')
comment('// Concrete type.\\n', '// Konkretny typ.\\n')
comment('// Implicitly specified type parameter `A`.\\n',
        '// Niejawnie podany parametr typowy `A`.\\n')
comment('// Implicitly specified type parameter `i32`.\\n',
        '// Niejawnie podany parametr typowy `i32`.\\n')
comment('// Explicitly specified type parameter `char` to `generic()`.\\n',
        '// Jawnie podany parametr typowy `char` dla `generic()`.\\n')
comment('// Implicitly specified type parameter `char` to `generic()`.\\n',
        '// Niejawnie podany parametr typowy `char` dla `generic()`.\\n')

prose("'c'", "'c'")

prose('[functions](../fn.md) and [`struct`s](../custom_types/structs.md)',
      '[funkcje](../fn.md) i [`struct`s](../custom_types/structs.md)')

# ============================================================
# generics/impl.md
# ============================================================

prose('Similar to functions, implementations require care to remain generic.',
      'Podobnie jak funkcje, implementacje wymagają uwagi, aby pozostały ogólne.')

comment('// Concrete type `S`\\n', '// Konkretny typ `S`\\n')
comment('// Generic type `GenericVal`\\n', '// Ogólny typ `GenericVal`\\n')
comment('// impl of GenericVal where we explicitly specify type parameters:\\n',
        '// implementacja GenericVal z jawnie podanymi parametrami typowymi:\\n')
comment('// Specify `f32`\\n', '// Podaj `f32`\\n')
comment('// Specify `S` as defined above\\n', '// Podaj `S` zdefiniowane wyżej\\n')
comment('// `<T>` Must precede the type to remain generic\\n',
        '// `<T>` musi poprzedzać typ, aby pozostał ogólny\\n')
comment('// impl of Val\\n', '// implementacja Val\\n')
comment('// impl of GenVal for a generic type `T`\\n',
        '// implementacja GenVal dla ogólnego typu `T`\\n')

multi(
    'msgid ""\n'
    '"[functions returning references](../scope/lifetime/fn.md), [`impl`](../fn/"\n'
    '"methods.md), and [`struct`](../custom_types/structs.md)"\n',
    '"[funkcje zwracające referencje](../scope/lifetime/fn.md), [`impl`](../fn/"\n'
    '"methods.md) i [`struct`](../custom_types/structs.md)"\n'
)

# ============================================================
# generics/gen_trait.md
# ============================================================

multi(
    'msgid ""\n'
    '"Of course `trait`s can also be generic. Here we define one which "\n'
    '"reimplements the `Drop` `trait` as a generic method to `drop` itself and an "\n'
    '"input."\n',
    '"Oczywiście cechy (`trait`s) też mogą być ogólne. Tutaj definiujemy jedną, "\n'
    '"która reimplementuje cechę `Drop` jako ogólną metodę do upuszczenia siebie "\n'
    '"i wejścia."\n'
)

comment('// Non-copyable types.\\n', '// Typy nie-kopiujące.\\n')
comment('// A trait generic over `T`.\\n', '// Cecha ogólna względem `T`.\\n')

multi(
    'msgid ""\n'
    '"// Define a method on the caller type which takes an\\n"\n'
    '"    // additional single parameter `T` and does nothing with it.\\n"\n',
    '"// Zdefiniuj metodę na typie wywołującym, przyjmującą\\n"\n'
    '"    // dodatkowy parametr `T` i nic z nim nie robiącą.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Implement `DoubleDrop<T>` for any generic parameter `T` and\\n"\n'
    '"// caller `U`.\\n"\n',
    '"// Zaimplementuj `DoubleDrop<T>` dla dowolnego ogólnego parametru `T`\\n"\n'
    '"// i wywołującego `U`.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// This method takes ownership of both passed arguments,\\n"\n'
    '"    // deallocating both.\\n"\n',
    '"// Ta metoda przejmuje własność obu przekazanych argumentów\\n"\n'
    '"    // i dealokuje oba.\\n"\n'
)

comment('// Deallocate `empty` and `null`.\\n', '// Dealokuj `empty` i `null`.\\n')

multi(
    'msgid ""\n'
    '"//empty;\\n"\n'
    '"    //null;\\n"\n'
    '"    // ^ TODO: Try uncommenting these lines.\\n"\n',
    '"//empty;\\n"\n'
    '"    //null;\\n"\n'
    '"    // ^ TODO: Spróbuj odkomentować te linie.\\n"\n'
)

multi(
    'msgid ""\n'
    '"[`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html), [`struct`](../"\n'
    '"custom_types/structs.md), and [`trait`](../trait.md)"\n',
    '"[`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html), [`struct`](../"\n'
    '"custom_types/structs.md) i [`trait`](../trait.md)"\n'
)

# ============================================================
# generics/bounds.md
# ============================================================

multi(
    'msgid ""\n'
    '"When working with generics, the type parameters often must use traits as "\n'
    '"_bounds_ to stipulate what functionality a type implements. For example, the "\n'
    '"following example uses the trait `Display` to print and so it requires `T` "\n'
    '"to be bound by `Display`; that is, `T` _must_ implement `Display`."\n',
    '"Przy pracy z typami ogólnymi, parametry typowe często muszą używać cech jako "\n'
    '"_ograniczeń_ określających jaką funkcjonalność typ implementuje. Na przykład, "\n'
    '"poniższy przykład używa cechy `Display` do drukowania, więc wymaga by `T` "\n'
    '"było ograniczone przez `Display`; czyli `T` _musi_ implementować `Display`."\n'
)

multi(
    'msgid ""\n'
    '"// Define a function `printer` that takes a generic type `T` which\\n"\n'
    '"// must implement trait `Display`.\\n"\n',
    '"// Zdefiniuj funkcję `printer` przyjmującą ogólny typ `T`, który\\n"\n'
    '"// musi implementować cechę `Display`.\\n"\n'
)

multi(
    'msgid ""\n'
    '"Bounding restricts the generic to types that conform to the bounds. That is:"\n',
    '"Ograniczanie zawęża typy ogólne do tych, które spełniają ograniczenia. Mianowicie:"\n'
)

multi(
    'msgid ""\n'
    '"// Error! `Vec<T>` does not implement `Display`. This\\n"\n'
    '"// specialization will fail.\\n"\n',
    '"// Błąd! `Vec<T>` nie implementuje `Display`. Ta\\n"\n'
    '"// specjalizacja zawiedzie.\\n"\n'
)

multi(
    'msgid ""\n'
    '"Another effect of bounding is that generic instances are allowed to access "\n'
    '"the [methods](../fn/methods.md) of traits specified in the bounds. For "\n'
    '"example:"\n',
    '"Innym efektem ograniczania jest to, że instancje ogólne mogą dostępować "\n'
    '"[metody](../fn/methods.md) cech podanych w ograniczeniach. Na przykład:"\n'
)

comment('// A trait which implements the print marker: `{:?}`.\\n',
        '// Cecha implementująca znacznik drukowania: `{:?}`.\\n')

multi(
    'msgid ""\n'
    '"// The generic `T` must implement `Debug`. Regardless\\n"\n'
    '"// of the type, this will work properly.\\n"\n',
    '"// Ogólny typ `T` musi implementować `Debug`. Niezależnie\\n"\n'
    '"// od typu, to będzie działać poprawnie.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// `T` must implement `HasArea`. Any type which meets\\n"\n'
    '"// the bound can access `HasArea`\'s function `area`.\\n"\n',
    '"// `T` musi implementować `HasArea`. Każdy typ spełniający\\n"\n'
    '"// ograniczenie może dostępować funkcję `area` cechy `HasArea`.\\n"\n'
)

lit('Area: {}')

multi(
    'msgid ""\n'
    '"//print_debug(&_triangle);\\n"\n'
    '"    //println!(\\"Area: {}\\", area(&_triangle));\\n"\n'
    '"    // ^ TODO: Try uncommenting these.\\n"\n'
    '"    // | Error: Does not implement either `Debug` or `HasArea`.\\n"\n',
    '"//print_debug(&_triangle);\\n"\n'
    '"    //println!(\\"Area: {}\\", area(&_triangle));\\n"\n'
    '"    // ^ TODO: Spróbuj odkomentować te linie.\\n"\n'
    '"    // | Błąd: Nie implementuje ani `Debug` ani `HasArea`.\\n"\n'
)

multi(
    'msgid ""\n'
    '"As an additional note, [`where`](../generics/where.md) clauses can also be "\n'
    '"used to apply bounds in some cases to be more expressive."\n',
    '"Dodatkowo, klauzule [`where`](../generics/where.md) mogą też być używane do "\n'
    '"stosowania ograniczeń w niektórych przypadkach dla lepszej czytelności."\n'
)

multi(
    'msgid ""\n'
    '"[`std::fmt`](../hello/print.md), [`struct`s](../custom_types/structs.md), "\n'
    '"and [`trait`s](../trait.md)"\n',
    '"[`std::fmt`](../hello/print.md), [`struct`s](../custom_types/structs.md) "\n'
    '"i [`trait`s](../trait.md)"\n'
)

# ============================================================
# generics/bounds/testcase_empty.md
# ============================================================

multi(
    'msgid ""\n'
    '"A consequence of how bounds work is that even if a `trait` doesn\'t include "\n'
    '"any functionality, you can still use it as a bound. `Eq` and `Copy` are "\n'
    '"examples of such `trait`s from the `std` library."\n',
    '"Konsekwencją działania ograniczeń jest to, że nawet jeśli cecha nie zawiera "\n'
    '"żadnej funkcjonalności, można jej używać jako ograniczenia. `Eq` i `Copy` są "\n'
    '"przykładami takich cech z biblioteki `std`."\n'
)

multi(
    'msgid ""\n'
    '"// These functions are only valid for types which implement these\\n"\n'
    '"// traits. The fact that the traits are empty is irrelevant.\\n"\n',
    '"// Te funkcje są poprawne tylko dla typów implementujących te cechy.\\n"\n'
    '"// Fakt, że cechy są puste, jest nieistotny.\\n"\n'
)

lit('red')
lit('blue')

multi(
    'msgid ""\n'
    '"// `red()` won\'t work on a blue jay nor vice versa\\n"\n'
    '"    // because of the bounds.\\n"\n',
    '"// `red()` nie zadziała na sójce błękitnej ani odwrotnie\\n"\n'
    '"    // ze względu na ograniczenia.\\n"\n'
)

lit('A cardinal is {}')
lit('A blue jay is {}')

multi(
    'msgid ""\n'
    '"//println!(\\"A turkey is {}\\", red(&_turkey));\\n"\n'
    '"    // ^ TODO: Try uncommenting this line.\\n"\n',
    '"//println!(\\"A turkey is {}\\", red(&_turkey));\\n"\n'
    '"    // ^ TODO: Spróbuj odkomentować tę linię.\\n"\n'
)

multi(
    'msgid ""\n'
    '"[`std::cmp::Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html), [`std::"\n'
    '"marker::Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html), and "\n'
    '"[`trait`s](../../trait.md)"\n',
    '"[`std::cmp::Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html), [`std::"\n'
    '"marker::Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html) i "\n'
    '"[`trait`s](../../trait.md)"\n'
)

# ============================================================
# generics/multi_bounds.md
# ============================================================

multi(
    'msgid ""\n'
    '"Multiple bounds for a single type can be applied with a `+`. Like normal, "\n'
    '"different types are separated with `,`."\n',
    '"Wiele ograniczeń dla jednego typu można zastosować za pomocą `+`. Jak zwykle, "\n'
    '"różne typy są oddzielane przecinkiem `,`."\n'
)

lit('Debug: `{:?}`')
lit('Display: `{}`')
lit('t: `{:?}`')
lit('u: `{:?}`')
lit('words')

multi(
    'msgid ""\n'
    '"//compare_prints(&array);\\n"\n'
    '"    // TODO ^ Try uncommenting this.\\n"\n',
    '"//compare_prints(&array);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować to.\\n"\n'
)

prose('[`std::fmt`](../hello/print.md) and [`trait`s](../trait.md)',
      '[`std::fmt`](../hello/print.md) i [`trait`s](../trait.md)')

# ============================================================
# generics/where.md
# ============================================================

multi(
    'msgid ""\n'
    '"A bound can also be expressed using a `where` clause immediately before the "\n'
    '"opening `{`, rather than at the type\'s first mention. Additionally, `where` "\n'
    '"clauses can apply bounds to arbitrary types, rather than just to type "\n'
    '"parameters."\n',
    '"Ograniczenie można też wyrazić za pomocą klauzuli `where` bezpośrednio przed "\n'
    '"otwierającym `{`, zamiast przy pierwszym wspomnieniu typu. Ponadto klauzule "\n'
    '"`where` mogą stosować ograniczenia do dowolnych typów, nie tylko parametrów typowych."\n'
)

prose('Some cases that a `where` clause is useful:',
      'Przypadki, w których klauzula `where` jest użyteczna:')
prose('When specifying generic types and bounds separately is clearer:',
      'Gdy osobne określenie typów ogólnych i ograniczeń jest czytelniejsze:')
comment('// Expressing bounds with a `where` clause\\n',
        '// Wyrażanie ograniczeń za pomocą klauzuli `where`\\n')

multi(
    'msgid ""\n'
    '"When using a `where` clause is more expressive than using normal syntax. The "\n'
    '"`impl` in this example cannot be directly expressed without a `where` clause:"\n',
    '"Gdy użycie klauzuli `where` jest bardziej ekspresyjne niż normalna składnia. "\n'
    '"`impl` w tym przykładzie nie może być bezpośrednio wyrażone bez klauzuli `where`:"\n'
)

multi(
    'msgid ""\n'
    '"// Because we would otherwise have to express this as `T: Debug` or\\n"\n'
    '"// use another method of indirect approach, this requires a `where` clause:\\n"\n',
    '"// Ponieważ w przeciwnym razie musielibyśmy wyrazić to jako `T: Debug` lub\\n"\n'
    '"// użyć innej pośredniej metody, wymagana jest klauzula `where`:\\n"\n'
)

multi(
    'msgid ""\n'
    '"// We want `Option<T>: Debug` as our bound because that is what\'s\\n"\n'
    '"    // being printed. Doing otherwise would be using the wrong bound.\\n"\n',
    '"// Chcemy `Option<T>: Debug` jako ograniczenie, bo to jest drukowane.\\n"\n'
    '"    // Użycie czegoś innego byłoby błędnym ograniczeniem.\\n"\n'
)

multi(
    'msgid ""\n'
    '"[RFC](https://github.com/rust-lang/rfcs/blob/master/text/0135-where.md), "\n'
    '"[`struct`](../custom_types/structs.md), and [`trait`](../trait.md)"\n',
    '"[RFC](https://github.com/rust-lang/rfcs/blob/master/text/0135-where.md), "\n'
    '"[`struct`](../custom_types/structs.md) i [`trait`](../trait.md)"\n'
)

# ============================================================
# generics/new_types.md
# ============================================================

multi(
    'msgid ""\n'
    '"The `newtype` idiom gives compile time guarantees that the right type of "\n'
    '"value is supplied to a program."\n',
    '"Idiom nowotypu (`newtype`) daje gwarancje czasu kompilacji, że do programu "\n'
    '"przekazywany jest właściwy typ wartości."\n'
)

multi(
    'msgid ""\n'
    '"For example, a function that measures distance in miles, _must_ be given a "\n'
    '"value of type `Miles`."\n',
    '"Na przykład funkcja mierząca odległość w milach _musi_ otrzymać wartość "\n'
    '"typu `Miles`."\n'
)

lit('Is a marathon? {}')

comment('// println!(\\"Is a marathon? {}\\", is_a_marathon(&distance_km));\\n',
        '// println!(\\"Is a marathon? {}\\", is_a_marathon(&distance_km));\\n')

multi(
    'msgid ""\n'
    '"Uncomment the last print statement to observe that the type supplied must be "\n'
    '"`Miles`."\n',
    '"Odkomentuj ostatnią instrukcję print, aby zobaczyć, że podany typ musi być "\n'
    '"`Miles`."\n'
)

multi(
    'msgid ""\n'
    '"To obtain the `newtype`\'s value as the base type, you may use the tuple or "\n'
    '"destructuring syntax like so:"\n',
    '"Aby uzyskać wartość nowotypu jako typ bazowy, można użyć składni krotki lub "\n'
    '"destrukturyzacji w następujący sposób:"\n'
)

comment('// Tuple\\n', '// Krotka\\n')
comment('// Destructuring\\n', '// Destrukturyzacja\\n')
prose('[`structs`](../custom_types/structs.md)', '[`structs`](../custom_types/structs.md)')

# ============================================================
# generics/assoc_items.md
# ============================================================

multi(
    'msgid ""\n'
    '"\\"Associated Items\\" refers to a set of rules pertaining to [`item`](https://"\n'
    '"doc.rust-lang.org/reference/items.html)s of various types. It is an "\n'
    '"extension to `trait` generics, and allows `trait`s to internally define new "\n'
    '"items."\n',
    '"\\"Elementy skojarzone\\" (Associated Items) odnoszą się do zbioru reguł "\n'
    '"dotyczących [`item`](https://doc.rust-lang.org/reference/items.html)ów różnych typów. "\n'
    '"Jest to rozszerzenie typów ogólnych dla cech, pozwalające cechom wewnętrznie "\n'
    '"definiować nowe elementy."\n'
)

multi(
    'msgid ""\n'
    '"One such item is called an _associated type_, providing simpler usage "\n'
    '"patterns when the `trait` is generic over its container type."\n',
    '"Jednym z takich elementów jest _typ skojarzony_, zapewniający prostsze wzorce "\n'
    '"użycia gdy cecha jest ogólna względem swojego typu kontenera."\n'
)

multi(
    'msgid ""\n'
    '"[RFC](https://github.com/rust-lang/rfcs/blob/master/text/0195-associated-"\n'
    '"items.md)"\n',
    '"[RFC](https://github.com/rust-lang/rfcs/blob/master/text/0195-associated-"\n'
    '"items.md)"\n'
)

# ============================================================
# generics/assoc_items/the_problem.md
# ============================================================

multi(
    'msgid ""\n'
    '"A `trait` that is generic over its container type has type specification "\n'
    '"requirements - users of the `trait` _must_ specify all of its generic types."\n',
    '"Cecha ogólna względem swojego typu kontenera ma wymagania dotyczące podania typów — "\n'
    '"użytkownicy cechy _muszą_ podać wszystkie jej typy ogólne."\n'
)

multi(
    'msgid ""\n'
    '"In the example below, the `Contains` `trait` allows the use of the generic "\n'
    '"types `A` and `B`. The trait is then implemented for the `Container` type, "\n'
    '"specifying `i32` for `A` and `B` so that it can be used with `fn "\n'
    '"difference()`."\n',
    '"W poniższym przykładzie cecha `Contains` pozwala na użycie ogólnych typów `A` i `B`. "\n'
    '"Cecha jest następnie zaimplementowana dla typu `Container`, podając `i32` dla `A` i `B` "\n'
    '"aby móc użyć jej z `fn difference()`."\n'
)

multi(
    'msgid ""\n'
    '"Because `Contains` is generic, we are forced to explicitly state _all_ of "\n'
    '"the generic types for `fn difference()`. In practice, we want a way to "\n'
    '"express that `A` and `B` are determined by the _input_ `C`. As you will see "\n'
    '"in the next section, associated types provide exactly that capability."\n',
    '"Ponieważ `Contains` jest ogólna, jesteśmy zmuszeni jawnie podać _wszystkie_ "\n'
    '"typy ogólne dla `fn difference()`. W praktyce chcemy wyrazić, że `A` i `B` są "\n'
    '"wyznaczane przez _wejście_ `C`. Jak zobaczymy w następnej sekcji, typy skojarzone "\n'
    '"dają dokładnie tę możliwość."\n'
)

multi(
    'msgid ""\n'
    '"// A trait which checks if 2 items are stored inside of container.\\n"\n'
    '"// Also retrieves first or last value.\\n"\n',
    '"// Cecha sprawdzająca czy 2 elementy są przechowywane w kontenerze.\\n"\n'
    '"// Pobiera też pierwszą lub ostatnią wartość.\\n"\n'
)

comment('// Explicitly requires `A` and `B`.\\n', '// Jawnie wymaga `A` i `B`.\\n')
comment("// Doesn't explicitly require `A` or `B`.\\n",
        '// Nie wymaga jawnie `A` ani `B`.\\n')
comment('// True if the numbers stored are equal.\\n',
        '// Prawda jeśli przechowywane liczby są równe.\\n')
comment('// Grab the first number.\\n', '// Pobierz pierwszą liczbę.\\n')
comment('// Grab the last number.\\n', '// Pobierz ostatnią liczbę.\\n')

multi(
    'msgid ""\n'
    '"// `C` contains `A` and `B`. In light of that, having to express `A` and\\n"\n'
    '"// `B` again is a nuisance.\\n"\n',
    '"// `C` zawiera `A` i `B`. W związku z tym, konieczność ponownego wyrażania\\n"\n'
    '"// `A` i `B` jest uciążliwa.\\n"\n'
)

lit('Does container contain {} and {}: {}')
lit('First number: {}')
lit('Last number: {}')
lit('The difference is: {}')

multi(
    'msgid ""\n'
    '"[`struct`s](../../custom_types/structs.md), and [`trait`s](../../trait.md)"\n',
    '"[`struct`s](../../custom_types/structs.md) i [`trait`s](../../trait.md)"\n'
)

# ============================================================
# generics/assoc_items/types.md
# ============================================================

multi(
    'msgid ""\n'
    '"The use of \\"Associated types\\" improves the overall readability of code by "\n'
    '"moving inner types locally into a trait as _output_ types. Syntax for the "\n'
    '"`trait` definition is as follows:"\n',
    '"Użycie \\"typów skojarzonych\\" poprawia ogólną czytelność kodu przez przeniesienie "\n'
    '"wewnętrznych typów lokalnie do cechy jako typy _wyjściowe_. Składnia definicji cechy:"\n'
)

multi(
    'msgid ""\n'
    '"// `A` and `B` are defined in the trait via the `type` keyword.\\n"\n'
    '"// (Note: `type` in this context is different from `type` when used for\\n"\n'
    '"// aliases).\\n"\n',
    '"// `A` i `B` są zdefiniowane w cesze za pomocą słowa kluczowego `type`.\\n"\n'
    '"// (Uwaga: `type` w tym kontekście różni się od `type` używanego dla aliasów).\\n"\n'
)

comment('// Updated syntax to refer to these new types generically.\\n',
        '// Zaktualizowana składnia do ogólnego odwoływania się do tych nowych typów.\\n')

multi(
    'msgid ""\n'
    '"Note that functions that use the `trait` `Contains` are no longer required "\n'
    '"to express `A` or `B` at all:"\n',
    '"Zauważ, że funkcje używające cechy `Contains` nie muszą już podawać `A` ani `B`:"\n'
)

comment('// Without using associated types\\n', '// Bez użycia typów skojarzonych\\n')
comment('// Using associated types\\n', '// Z użyciem typów skojarzonych\\n')

multi(
    'msgid ""\n'
    '"Let\'s rewrite the example from the previous section using associated types:"\n',
    '"Przepiszmy przykład z poprzedniej sekcji używając typów skojarzonych:"\n'
)

comment('// Define generic types here which methods will be able to utilize.\\n',
        '// Zdefiniuj tu typy ogólne, z których metody będą mogły korzystać.\\n')

multi(
    'msgid ""\n'
    '"// Specify what types `A` and `B` are. If the `input` type\\n"\n'
    '"    // is `Container(i32, i32)`, the `output` types are determined\\n"\n'
    '"    // as `i32` and `i32`.\\n"\n',
    '"// Podaj co to są typy `A` i `B`. Jeśli typ `input`\\n"\n'
    '"    // to `Container(i32, i32)`, typy `output` są wyznaczane\\n"\n'
    '"    // jako `i32` i `i32`.\\n"\n'
)

comment('// `&Self::A` and `&Self::B` are also valid here.\\n',
        '// `&Self::A` i `&Self::B` są tu też poprawne.\\n')

# ============================================================
# generics/phantom.md
# ============================================================

multi(
    'msgid ""\n'
    '"A phantom type parameter is one that doesn\'t show up at runtime, but is "\n'
    '"checked statically (and only) at compile time."\n',
    '"Fantomowy parametr typowy to taki, który nie pojawia się w czasie wykonania, "\n'
    '"ale jest sprawdzany statycznie (i tylko) w czasie kompilacji."\n'
)

multi(
    'msgid ""\n'
    '"Data types can use extra generic type parameters to act as markers or to "\n'
    '"perform type checking at compile time. These extra parameters hold no "\n'
    '"storage values, and have no runtime behavior."\n',
    '"Typy danych mogą używać dodatkowych ogólnych parametrów typowych jako znaczników "\n'
    '"lub do sprawdzania typów w czasie kompilacji. Te dodatkowe parametry nie przechowują "\n'
    '"żadnych wartości i nie mają zachowania w czasie wykonania."\n'
)

multi(
    'msgid ""\n'
    '"In the following example, we combine [std::marker::PhantomData](https://doc."\n'
    '"rust-lang.org/std/marker/struct.PhantomData.html) with the phantom type "\n'
    '"parameter concept to create tuples containing different data types."\n',
    '"W poniższym przykładzie łączymy [std::marker::PhantomData](https://doc."\n'
    '"rust-lang.org/std/marker/struct.PhantomData.html) z konceptem fantomowego "\n'
    '"parametru typowego, aby tworzyć krotki zawierające różne typy danych."\n'
)

multi(
    'msgid ""\n'
    '"// A phantom tuple struct which is generic over `A` with hidden parameter "\n'
    '"`B`.\\n"\n',
    '"// Fantomowa struktura krotkowa ogólna względem `A` z ukrytym parametrem `B`.\\n"\n'
)

comment('// Allow equality test for this type.\\n',
        '// Zezwól na test równości dla tego typu.\\n')

multi(
    'msgid ""\n'
    '"// A phantom type struct which is generic over `A` with hidden parameter "\n'
    '"`B`.\\n"\n',
    '"// Fantomowa struktura typowa ogólna względem `A` z ukrytym parametrem `B`.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Note: Storage is allocated for generic type `A`, but not for `B`.\\n"\n'
    '"//       Therefore, `B` cannot be used in computations.\\n"\n',
    '"// Uwaga: Pamięć jest przydzielana dla ogólnego typu `A`, ale nie dla `B`.\\n"\n'
    '"//       Dlatego `B` nie może być używane w obliczeniach.\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Here, `f32` and `f64` are the hidden parameters.\\n"\n'
    '"    // PhantomTuple type specified as `<char, f32>`.\\n"\n',
    '"// Tu `f32` i `f64` są ukrytymi parametrami.\\n"\n'
    '"    // Typ PhantomTuple podany jako `<char, f32>`.\\n"\n'
)

prose("'Q'", "'Q'")
comment('// PhantomTuple type specified as `<char, f64>`.\\n',
        '// Typ PhantomTuple podany jako `<char, f64>`.\\n')
comment('// Type specified as `<char, f32>`.\\n', '// Typ podany jako `<char, f32>`.\\n')
comment('// Type specified as `<char, f64>`.\\n', '// Typ podany jako `<char, f64>`.\\n')

multi(
    'msgid ""\n'
    '"// Compile-time Error! Type mismatch so these cannot be compared:\\n"\n'
    '"    // println!(\\"_tuple1 == _tuple2 yields: {}\\",\\n"\n'
    '"    //           _tuple1 == _tuple2);\\n"\n',
    '"// Błąd kompilacji! Niezgodność typów, więc nie można ich porównać:\\n"\n'
    '"    // println!(\\"_tuple1 == _tuple2 yields: {}\\",\\n"\n'
    '"    //           _tuple1 == _tuple2);\\n"\n'
)

multi(
    'msgid ""\n'
    '"// Compile-time Error! Type mismatch so these cannot be compared:\\n"\n'
    '"    // println!(\\"_struct1 == _struct2 yields: {}\\",\\n"\n'
    '"    //           _struct1 == _struct2);\\n"\n',
    '"// Błąd kompilacji! Niezgodność typów, więc nie można ich porównać:\\n"\n'
    '"    // println!(\\"_struct1 == _struct2 yields: {}\\",\\n"\n'
    '"    //           _struct1 == _struct2);\\n"\n'
)

multi(
    'msgid ""\n'
    '"[Derive](../trait/derive.md), [struct](../custom_types/structs.md), and "\n'
    '"[tuple](../primitives/tuples.html)."\n',
    '"[Derive](../trait/derive.md), [struct](../custom_types/structs.md) i "\n'
    '"[tuple](../primitives/tuples.html)."\n'
)

# ============================================================
# generics/phantom/testcase_units.md
# ============================================================

multi(
    'msgid ""\n'
    '"A useful method of unit conversions can be examined by implementing `Add` "\n'
    '"with a phantom type parameter. The `Add` `trait` is examined below:"\n',
    '"Użyteczną metodę konwersji jednostek można zbadać implementując `Add` "\n'
    '"z fantomowym parametrem typowym. Cecha `Add` jest opisana poniżej:"\n'
)

multi(
    'msgid ""\n'
    '"// This construction would impose: `Self + RHS = Output`\\n"\n'
    '"// where RHS defaults to Self if not specified in the implementation.\\n"\n',
    '"// Ta konstrukcja narzuca: `Self + RHS = Output`\\n"\n'
    '"// gdzie RHS domyślnie to Self, jeśli nie podano w implementacji.\\n"\n'
)

comment('// `Output` must be `T<U>` so that `T<U> + T<U> = T<U>`.\\n',
        '// `Output` musi być `T<U>` tak aby `T<U> + T<U> = T<U>`.\\n')

prose('The whole implementation:', 'Pełna implementacja:')

comment('/// Create void enumerations to define unit types.\\n',
        '/// Utwórz puste wyliczenia definiujące typy jednostek.\\n')

multi(
    'msgid ""\n'
    '"/// `Length` is a type with phantom type parameter `Unit`,\\n"\n'
    '"/// and is not generic over the length type (that is `f64`).\\n"\n'
    '"///\\n"\n'
    '"/// `f64` already implements the `Clone` and `Copy` traits.\\n"\n',
    '"/// `Length` to typ z fantomowym parametrem typowym `Unit`,\\n"\n'
    '"/// nie jest ogólny względem typu długości (którym jest `f64`).\\n"\n'
    '"///\\n"\n'
    '"/// `f64` już implementuje cechy `Clone` i `Copy`.\\n"\n'
)

comment('/// The `Add` trait defines the behavior of the `+` operator.\\n',
        '/// Cecha `Add` definiuje zachowanie operatora `+`.\\n')
comment('// add() returns a new `Length` struct containing the sum.\\n',
        '// add() zwraca nową strukturę `Length` zawierającą sumę.\\n')
comment('// `+` calls the `Add` implementation for `f64`.\\n',
        '// `+` wywołuje implementację `Add` dla `f64`.\\n')
comment('// Specifies `one_foot` to have phantom type parameter `Inch`.\\n',
        '// Określa `one_foot` z fantomowym parametrem typowym `Inch`.\\n')
comment('// `one_meter` has phantom type parameter `Mm`.\\n',
        '// `one_meter` ma fantomowy parametr typowy `Mm`.\\n')

multi(
    'msgid ""\n'
    '"// `+` calls the `add()` method we implemented for `Length<Unit>`.\\n"\n'
    '"    //\\n"\n'
    '"    // Since `Length` implements `Copy`, `add()` does not consume\\n"\n'
    '"    // `one_foot` and `one_meter` but copies them into `self` and `rhs`.\\n"\n',
    '"// `+` wywołuje metodę `add()` zaimplementowaną dla `Length<Unit>`.\\n"\n'
    '"    //\\n"\n'
    '"    // Ponieważ `Length` implementuje `Copy`, `add()` nie konsumuje\\n"\n'
    '"    // `one_foot` i `one_meter`, lecz kopiuje je do `self` i `rhs`.\\n"\n'
)

comment('// Addition works.\\n', '// Dodawanie działa.\\n')
lit('one foot + one_foot = {:?} in')
lit('one meter + one_meter = {:?} mm')

multi(
    'msgid ""\n'
    '"// Nonsensical operations fail as they should:\\n"\n'
    '"    // Compile-time Error: type mismatch.\\n"\n'
    '"    //let one_feter = one_foot + one_meter;\\n"\n',
    '"// Bezsensowne operacje zawodzą tak jak powinny:\\n"\n'
    '"    // Błąd kompilacji: niezgodność typów.\\n"\n'
    '"    //let one_feter = one_foot + one_meter;\\n"\n'
)

multi(
    'msgid ""\n'
    '"[Borrowing (`&`)](../../scope/borrow.md), [Bounds (`X: Y`)](../../generics/"\n'
    '"bounds.md), [enum](../../custom_types/enum.md), [impl & self](../../fn/"\n'
    '"methods.md), [Overloading](../../trait/ops.md), [ref](../../scope/borrow/ref."\n'
    '"md), [Traits (`X for Y`)](../../trait.md), and [TupleStructs](../../"\n'
    '"custom_types/structs.md)."\n',
    '"[Pożyczanie (`&`)](../../scope/borrow.md), [Ograniczenia (`X: Y`)](../../generics/"\n'
    '"bounds.md), [enum](../../custom_types/enum.md), [impl & self](../../fn/"\n'
    '"methods.md), [Przeciążanie](../../trait/ops.md), [ref](../../scope/borrow/ref."\n'
    '"md), [Cechy (`X for Y`)](../../trait.md) i [TupleStructs](../../"\n'
    '"custom_types/structs.md)."\n'
)

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
