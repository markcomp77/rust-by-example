# Przewodnik tłumaczenia Rust by Example — język polski

Ten dokument opisuje:
1. Inwarianty poprawności — zasady, których naruszenie jest błędem, nie kwestią stylu.
2. Aksjomaty terminologiczne — konwencje przyjęte raz, stosowane bezwyjątkowo.
3. Szczegółowy plan tłumaczenia podzielony na 10 etapów.

Przed przystąpieniem do pracy przeczytaj też:
- [`TRANSLATING.md`](TRANSLATING.md) — ogólny workflow (narzędzia, komendy)
- [`po/GLOSSARY.md`](po/GLOSSARY.md) — kanoniczny glosariusz terminów

---

## Konfiguracja środowiska

```bash
# Wymagane narzędzia
cargo install mdbook mdbook-i18n-helpers
sudo apt install gettext   # lub brew install gettext

# Inicjalizacja pliku polskiego (tylko raz)
MDBOOK_OUTPUT='{"xgettext": {"pot-file": "messages.pot"}}' mdbook build -d po
msginit -i po/messages.pot -l pl -o po/pl.po

# Aktualizacja po zmianach w źródle angielskim
msgmerge --update po/pl.po po/messages.pot

# Podgląd tłumaczenia
MDBOOK_BOOK__LANGUAGE=pl mdbook serve

# Walidacja pliku przed commitem
./scripts/check-po.sh po/pl.po
```

---

## Część I — Inwarianty poprawności

Inwarianty są weryfikowalne automatycznie. Naruszenie każdego z nich to błąd, który `msgfmt --check` lub CI wykryje i zablokuje merge.

### Inwariant 1 — Białe znaki końcowe

Jeśli `msgid` kończy się `\n`, to `msgstr` **musi** kończyć się `\n`.
Jeśli `msgid` **nie** kończy się `\n`, to `msgstr` **nie może** kończyć się `\n`.

```po
# BŁĄD — brakuje \n w msgstr
msgid "// This is the main function.\n"
msgstr "// To jest funkcja główna."

# POPRAWNIE
msgid "// This is the main function.\n"
msgstr "// To jest funkcja główna.\n"
```

### Inwariant 2 — Bloki kodu pozostają bez zmian

Zawartość bloków ` ```rust ... ``` ` (kod Rusta) **nie jest tłumaczona**.
Wyjątek: komentarze `//` wewnątrz kodu można tłumaczyć — ale patrz Aksjomat 3.

```po
# POPRAWNIE — kod identyczny, komentarz przetłumaczony
msgid ""
"```rust\n"
"// This is the main function.\n"
"fn main() {\n"
"    println!(\"Hello World!\");\n"
"}\n"
"```\n"
msgstr ""
"```rust\n"
"// To jest funkcja główna.\n"
"fn main() {\n"
"    println!(\"Hello World!\");\n"
"}\n"
"```\n"
```

### Inwariant 3 — Struktura Markdown jest zachowana

- Liczba nagłówków (`#`, `##`, `###`) = identyczna jak w `msgid`.
- Liczba elementów list (`-`, `*`, `1.`) = identyczna.
- Pogrubienia `**tekst**` i kursywa `*tekst*` — można tłumaczyć tekst wewnątrz, ale delimitery muszą pozostać.
- Kod inline w backtickach `` `nazwa` `` — zawartość **nie jest tłumaczona** (identyfikatory, typy, makra).

```po
# POPRAWNIE
msgid "The `println!` macro **prints** to stdout."
msgstr "Makro `println!` **drukuje** na standardowe wyjście."

# BŁĄD — zmodyfikowano backtick-code
msgid "The `println!` macro prints."
msgstr "Makro `wydrukuj!` drukuje."
```

### Inwariant 4 — URL-e są nienaruszone

Format linków Markdown: `[tekst](url)`.
- `tekst` — można tłumaczyć.
- `url` — **absolutnie nie zmieniać**.

```po
# POPRAWNIE
msgid "See the [Rust book](https://doc.rust-lang.org/book/)."
msgstr "Zobacz [Rust book](https://doc.rust-lang.org/book/)."

# BŁĄD
msgid "See the [Rust book](https://doc.rust-lang.org/book/)."
msgstr "Zobacz [Książkę Rusta](https://pl.doc.rust-lang.org/book/)."
```

### Inwariant 5 — Znaki cudzysłowu w msgstr

W polskim tłumaczeniu używamy polskich cudzysłowów: `„tekst"` zamiast `"tekst"`.
Wyjątek: nie zmieniamy cudzysłowów wewnątrz bloków kodu ani gdy są częścią składni Markdown.

---

## Część II — Aksjomaty terminologiczne

Aksjomaty są konwencjami podjętymi jednorazowo przez społeczność tłumaczy.
Pełna lista z uzasadnieniem jest w [`po/GLOSSARY.md`](po/GLOSSARY.md).

### Aksjomat 1 — Bijektywność terminu

Każdy kluczowy termin Rusta ma **dokładnie jedno** polskie tłumaczenie.
Raz wybrany termin stosujemy we wszystkich 2912 wpisach — bez wyjątków.

```
ownership      → własność       (NIGDY: posiadanie, przynależność)
borrowing      → pożyczanie     (NIGDY: zapożyczenie, borrowing)
lifetime       → czas życia     (NIGDY: żywotność, lifetime)
trait          → cecha          (NIGDY: interfejs, właściwość)
closure        → domknięcie     (NIGDY: lambda, funkcja anonimowa)
crate          → skrzynia       (NIGDY: paczka, biblioteka, crate — samodzielnie)
scope          → zasięg         (NIGDY: zakres, przestrzeń)
pattern        → wzorzec        (NIGDY: szablon, deseń)
binding        → wiązanie       (NIGDY: przypisanie, powiązanie)
```

### Aksjomat 2 — Nazwy własne Rusta nie są tłumaczone

Nigdy nie tłumaczymy:
- Typów standardowych: `String`, `Vec`, `Option`, `Result`, `Box`, `Rc`, `Arc`, `HashMap`...
- Cech wbudowanych: `Display`, `Debug`, `Clone`, `Copy`, `Iterator`, `Drop`, `Fn`, `FnMut`, `FnOnce`...
- Makr: `println!`, `format!`, `vec!`, `assert!`, `panic!`, `todo!`...
- Słów kluczowych: `fn`, `let`, `mut`, `match`, `use`, `impl`, `trait`, `struct`, `enum`...

### Aksjomat 3 — Spójność tłumaczenia komentarzy w kodzie

Komentarze `//` wewnątrz bloków kodu **mogą** być tłumaczone — jest to pedagogicznie korzystne.
Ale: **albo tłumaczymy wszystkie komentarze w pliku .po, albo żadnego**.
Mieszanie jest gorsze niż konsekwentna decyzja w którąkolwiek stronę.

Decyzja dla `pl.po`: **tłumaczymy komentarze** w blokach kodu.

### Aksjomat 4 — Forma pierwszego wprowadzenia terminu

Przy pierwszym wystąpieniu trudnego terminu używamy formy: `polskie tłumaczenie (angielski oryginał)`.

```
własność (ownership)
pożyczanie (borrowing)
czas życia (lifetime)
skrzynia (crate)
domknięcie (closure)
```

Przy kolejnych wystąpieniach używamy **wyłącznie** polskiego tłumaczenia.

### Aksjomat 5 — Tryb formalny bez form osobowych

Tłumaczenie stosuje bezosobową formę formalną — jak w dokumentacji technicznej.
Nie używamy formy `ty` ani `Ty`. Zamiast „zobaczysz" piszemy „można zobaczyć" lub „widoczne jest".

```po
# BŁĄD — forma osobowa
msgid "You can run this code by clicking 'Run'."
msgstr "Możesz uruchomić ten kod klikając 'Run'."

# POPRAWNIE — forma bezosobowa
msgid "You can run this code by clicking 'Run'."
msgstr "Kod można uruchomić klikając przycisk 'Run'."
```

### Aksjomat 6 — Tytułów rozdziałów nie spolszczamy nadmiernie

Tytuły rozdziałów w SUMMARY.md tłumaczymy na polski, **ale** zachowujemy angielskie nazwy gdy są to:
- Koncepty ściśle techniczne (`RAII`, `FFI`)
- Nazwy cech (`Display`, `Debug`, `Drop`)
- Operator lub słowo kluczowe (`impl Trait`, `dyn`, `where`)

---

## Część III — Plan tłumaczenia

Całość to ~2912 wpisów PO. Plan podzielony jest na **10 etapów** pogrupowanych konceptualnie,
każdy obejmujący ~280–350 wpisów. Kolejność jest celowa: od trywialnego do złożonego,
tak żeby glosariusz krzepł zanim dotrzemy do najtrudniejszych konceptów (zasięg, czasy życia).

Szacunkowy nakład pracy: 20–30 wpisów na sesję = 10–15 sesji na etap.

---

### Etap 1 — Wejście i pierwsze kroki (≈280 wpisów)

**Rozdziały:**
- Introduction (`src/index.md`)
- Hello World (`src/hello.md`)
  - Comments (`src/hello/comment.md`)
  - Formatted print (`src/hello/print.md`)
    - Debug (`src/hello/print/print_debug.md`)
    - Display (`src/hello/print/print_display.md`)
      - Testcase: List (`src/hello/print/print_display/testcase_list.md`)
    - Formatting (`src/hello/print/fmt.md`)
- Primitives (`src/primitives.md`)
  - Literals and operators (`src/primitives/literals.md`)
  - Tuples (`src/primitives/tuples.md`)
  - Arrays and Slices (`src/primitives/array.md`)

**Dlaczego zaczynamy tu:** Hello World i Primitives są najbardziej samodzielne,
mają mało terminologii specyficznej dla Rusta i dają poczucie progresu.
Przy tym etapie ustala się styl tłumaczenia komentarzy w kodzie (Aksjomat 3).

**Kluczowe decyzje terminologiczne do podjęcia:**
- `formatted print` → „formatowane drukowanie" (ustalić i zapisać w GLOSSARY)
- `macro` → „makro" (nie zmieniamy nazwy `println!`)
- `literal` → „literał"

**Kontrola jakości po etapie:**
```bash
./scripts/check-po.sh po/pl.po
MDBOOK_BOOK__LANGUAGE=pl mdbook serve
# Sprawdź wizualnie: strona tytułowa, Hello World, sekcje Primitives
```

---

### Etap 2 — Typy niestandardowe i wiązania (≈290 wpisów)

**Rozdziały:**
- Custom Types (`src/custom_types.md`)
  - Structures (`src/custom_types/structs.md`)
  - Enums (`src/custom_types/enum.md`)
    - use (`src/custom_types/enum/enum_use.md`)
    - C-like (`src/custom_types/enum/c_like.md`)
    - Testcase: linked-list (`src/custom_types/enum/testcase_linked_list.md`)
  - constants (`src/custom_types/constants.md`)
- Variable Bindings (`src/variable_bindings.md`)
  - Mutability (`src/variable_bindings/mut.md`)
  - Scope and Shadowing (`src/variable_bindings/scope.md`)
  - Declare first (`src/variable_bindings/declare.md`)
  - Freezing (`src/variable_bindings/freeze.md`)
- Types (`src/types.md`)
  - Casting (`src/types/cast.md`)
  - Literals (`src/types/literals.md`)
  - Inference (`src/types/inference.md`)
  - Aliasing (`src/types/alias.md`)

**Kluczowe terminy do ustalenia:**
- `struct` / `structure` → „struktura" (termin wchodzi glosariusz)
- `enum` → „wyliczenie"
- `scope` → „zasięg" ← **ważne**, pojawi się setki razy
- `shadowing` → „przesłanianie"
- `mutability` → „zmienność" lub „mutowalność" — wybrać jedno
- `inference` → „wnioskowanie (o typach)"
- `casting` → „rzutowanie"
- `aliasing` → „aliasowanie"
- `freezing` → „zamrożenie"

---

### Etap 3 — Konwersja i sterowanie przepływem (≈320 wpisów)

**Rozdziały:**
- Conversion (`src/conversion.md`)
  - `From` and `Into` (`src/conversion/from_into.md`)
  - `TryFrom` and `TryInto` (`src/conversion/try_from_try_into.md`)
  - To and from `String`s (`src/conversion/string.md`)
- Expressions (`src/expression.md`)
- Flow of Control (`src/flow_control.md`)
  - if/else (`src/flow_control/if_else.md`)
  - loop (`src/flow_control/loop.md`)
    - Nesting and labels (`src/flow_control/loop/nested.md`)
    - Returning from loops (`src/flow_control/loop/return.md`)
  - while (`src/flow_control/while.md`)
  - for and range (`src/flow_control/for.md`)
  - match (`src/flow_control/match.md`)
    - Destructuring (`src/flow_control/match/destructuring.md`)
      - tuples (`src/flow_control/match/destructuring/destructure_tuple.md`)
      - arrays/slices (`src/flow_control/match/destructuring/destructure_slice.md`)
      - enums (`src/flow_control/match/destructuring/destructure_enum.md`)
      - pointers/ref (`src/flow_control/match/destructuring/destructure_pointers.md`)
      - structs (`src/flow_control/match/destructuring/destructure_structures.md`)
    - Guards (`src/flow_control/match/guard.md`)
    - Binding (`src/flow_control/match/binding.md`)
  - if let (`src/flow_control/if_let.md`)
  - let-else (`src/flow_control/let_else.md`)
  - while let (`src/flow_control/while_let.md`)

**Kluczowe terminy:**
- `pattern matching` → „dopasowanie wzorca"
- `destructuring` → „destrukturyzacja"
- `guard` → „strażnik"
- `binding` → „wiązanie" ← **pilnować spójności z Etapem 2**
- `label` → „etykieta"
- `range` → „zakres" (tu wyjątek — `range` w kontekście `for..in` to „zakres")

**Uwaga:** `match` i `if let` to fundamentalne wzorce Rusta.
Tłumaczenie tych sekcji wymaga szczególnej precyzji — czytelnik będzie wracał do nich wielokrotnie.

---

### Etap 4 — Funkcje i moduły (≈300 wpisów)

**Rozdziały:**
- Functions (`src/fn.md`)
  - Methods (`src/fn/methods.md`)
  - Closures (`src/fn/closures.md`)
    - Capturing (`src/fn/closures/capture.md`)
    - As input parameters (`src/fn/closures/input_parameters.md`)
    - Type anonymity (`src/fn/closures/anonymity.md`)
    - Input functions (`src/fn/closures/input_functions.md`)
    - As output parameters (`src/fn/closures/output_parameters.md`)
    - Examples in `std` (`src/fn/closures/closure_examples.md`)
      - Iterator::any (`src/fn/closures/closure_examples/iter_any.md`)
      - Searching through iterators (`src/fn/closures/closure_examples/iter_find.md`)
  - Higher Order Functions (`src/fn/hof.md`)
  - Diverging functions (`src/fn/diverging.md`)
- Modules (`src/mod.md`)
  - Visibility (`src/mod/visibility.md`)
  - Struct visibility (`src/mod/struct_visibility.md`)
  - The `use` declaration (`src/mod/use.md`)
  - `super` and `self` (`src/mod/super.md`)
  - File hierarchy (`src/mod/split.md`)
- Crates (`src/crates.md`)
  - Creating a Library (`src/crates/lib.md`)
  - Using a Library (`src/crates/using_lib.md`)

**Kluczowe terminy:**
- `closure` → „domknięcie" ← **krytyczne, pojawi się dziesiątki razy w tym etapie**
- `capturing` → „przechwytywanie"
- `higher-order function` → „funkcja wyższego rzędu"
- `diverging function` → „funkcja rozbieżna"
- `visibility` → „widoczność"
- `crate` → „skrzynia (crate)" przy pierwszym użyciu, potem „skrzynia"

**Uwaga do domknięć:** Sekcja Closures jest jedną z bardziej rozbudowanych.
`Fn`, `FnMut`, `FnOnce` — to nazwy cech, **nie tłumaczymy ich**, ale tłumaczymy objaśnienia.

---

### Etap 5 — Cargo, Atrybuty i Generyki (≈340 wpisów)

**Rozdziały:**
- Cargo (`src/cargo.md`)
  - Dependencies (`src/cargo/deps.md`)
  - Conventions (`src/cargo/conventions.md`)
  - Tests (`src/cargo/test.md`)
  - Build Scripts (`src/cargo/build_scripts.md`)
- Attributes (`src/attribute.md`)
  - `dead_code` (`src/attribute/unused.md`)
  - Crates (`src/attribute/crate.md`)
  - `cfg` (`src/attribute/cfg.md`)
    - Custom (`src/attribute/cfg/custom.md`)
- Generics (`src/generics.md`)
  - Functions (`src/generics/gen_fn.md`)
  - Implementation (`src/generics/impl.md`)
  - Traits (`src/generics/gen_trait.md`)
  - Bounds (`src/generics/bounds.md`)
    - Testcase: empty bounds (`src/generics/bounds/testcase_empty.md`)
  - Multiple bounds (`src/generics/multi_bounds.md`)
  - Where clauses (`src/generics/where.md`)
  - New Type Idiom (`src/generics/new_types.md`)
  - Associated items (`src/generics/assoc_items.md`)
    - The Problem (`src/generics/assoc_items/the_problem.md`)
    - Associated types (`src/generics/assoc_items/types.md`)
  - Phantom type parameters (`src/generics/phantom.md`)
    - Testcase: unit clarification (`src/generics/phantom/testcase_units.md`)

**Kluczowe terminy:**
- `generic` → „ogólny" / `generics` → „typy ogólne"
- `bounds` → „ograniczenia"
- `where clause` → „klauzula where" (`where` w kodzie bez zmian)
- `associated type` → „typ skojarzony"
- `phantom type` → „typ fantomowy"
- `newtype idiom` → „idiom nowotypu"
- `dependency` → „zależność"
- `attribute` → „atrybut"
- `build script` → „skrypt budowania"

**Uwaga do Generics:** To najtrudniejszy etap konceptualnie przed Etapem 6.
`PhantomData` — nazwa własna, nie tłumaczymy.
Sekcja „The Problem" i „Associated types" wymaga szczególnie precyzyjnych tłumaczeń —
to miejsce gdzie czytelnik po raz pierwszy rozumie, po co są typy skojarzone.

---

### Etap 6 — Reguły zasięgu: własność, pożyczanie, czasy życia (≈310 wpisów)

**To jest najtrudniejszy etap. Stanowi serce Rusta.**

**Rozdziały:**
- Scoping rules (`src/scope.md`)
  - RAII (`src/scope/raii.md`)
  - Ownership and moves (`src/scope/move.md`)
    - Mutability (`src/scope/move/mut.md`)
    - Partial moves (`src/scope/move/partial_move.md`)
  - Borrowing (`src/scope/borrow.md`)
    - Mutability (`src/scope/borrow/mut.md`)
    - Aliasing (`src/scope/borrow/alias.md`)
    - The ref pattern (`src/scope/borrow/ref.md`)
  - Lifetimes (`src/scope/lifetime.md`)
    - Explicit annotation (`src/scope/lifetime/explicit.md`)
    - Functions (`src/scope/lifetime/fn.md`)
    - Methods (`src/scope/lifetime/methods.md`)
    - Structs (`src/scope/lifetime/struct.md`)
    - Traits (`src/scope/lifetime/trait.md`)
    - Bounds (`src/scope/lifetime/lifetime_bounds.md`)
    - Coercion (`src/scope/lifetime/lifetime_coercion.md`)
    - Static (`src/scope/lifetime/static_lifetime.md`)
    - Elision (`src/scope/lifetime/elision.md`)

**Kluczowe terminy — tu terminologia jest najważniejsza:**
- `ownership` → „własność" ← w tym etapie pojawi się kilkadziesiąt razy
- `move` → „przeniesienie" (rzeczownik) / „przenosić" (czasownik)
- `partial move` → „częściowe przeniesienie"
- `borrow` → „pożyczać" / `borrowing` → „pożyczanie"
- `lifetime` → „czas życia"
- `lifetime annotation` → „adnotacja czasu życia"
- `lifetime elision` → „elizja czasu życia"
- `coercion` → „koercja" lub „wymuszenie" — wybrać jedno
- `static lifetime` → „statyczny czas życia"
- `RAII` → RAII (akronim, bez tłumaczenia — można wyjaśnić rozwinięcie)

**Protokół kontroli jakości dla tego etapu:**
Każde zdanie opisujące zasadę dotyczącą ownership/borrowing/lifetimes przeczytaj dwukrotnie —
raz po angielsku, raz po polsku — i sprawdź czy zachowuje pełną precyzję semantyczną.
Niepoprawne tłumaczenie reguł Rusta może wprowadzać czytelnika w błąd co do działania języka.

---

### Etap 7 — Cechy i makra (≈290 wpisów)

**Rozdziały:**
- Traits (`src/trait.md`)
  - Derive (`src/trait/derive.md`)
  - Returning Traits with `dyn` (`src/trait/dyn.md`)
  - Operator Overloading (`src/trait/ops.md`)
  - Drop (`src/trait/drop.md`)
  - Iterators (`src/trait/iter.md`)
  - `impl Trait` (`src/trait/impl_trait.md`)
  - Clone (`src/trait/clone.md`)
  - Supertraits (`src/trait/supertraits.md`)
  - Disambiguating overlapping traits (`src/trait/disambiguating.md`)
- macro_rules! (`src/macros.md`)
  - Syntax (`src/macros/syntax.md`)
    - Designators (`src/macros/designators.md`)
    - Overload (`src/macros/overload.md`)
    - Repeat (`src/macros/repeat.md`)
  - DRY (Don't Repeat Yourself) (`src/macros/dry.md`)
  - DSL (Domain Specific Languages) (`src/macros/dsl.md`)
  - Variadics (`src/macros/variadics.md`)

**Kluczowe terminy:**
- `trait` → „cecha" ← spójne z całą resztą
- `supertrait` → „supercecha"
- `derive` → „wyprowadzenie" lub zostawić `derive` z objaśnieniem
- `operator overloading` → „przeciążanie operatorów"
- `iterator` → „iterator"
- `designator` → „oznacznik"
- `variadic` → „wariadyczny" / `variadics` → „wariadyki"
- `DSL` → DSL (akronim zachować, można rozwinąć)

**Uwaga:** `dyn Trait` i `impl Trait` to składnia Rusta — w kodzie bez zmian,
ale w tekście objaśniającym tłumaczymy otaczające zdania.

---

### Etap 8 — Obsługa błędów (≈310 wpisów)

**Rozdziały:**
- Error handling (`src/error.md`)
  - `panic` (`src/error/panic.md`)
  - `abort` & `unwind` (`src/error/abort_unwind.md`)
  - `Option` & `unwrap` (`src/error/option_unwrap.md`)
    - Unpacking options with `?` (`src/error/option_unwrap/question_mark.md`)
    - Combinators: `map` (`src/error/option_unwrap/map.md`)
    - Combinators: `and_then` (`src/error/option_unwrap/and_then.md`)
    - Defaults: `or`, `or_else`, `get_or_insert`, `get_or_insert_with` (`src/error/option_unwrap/defaults.md`)
  - `Result` (`src/error/result.md`)
    - `map` for `Result` (`src/error/result/result_map.md`)
    - aliases for `Result` (`src/error/result/result_alias.md`)
    - Early returns (`src/error/result/early_returns.md`)
    - Introducing `?` (`src/error/result/enter_question_mark.md`)
  - Multiple error types (`src/error/multiple_error_types.md`)
    - Pulling `Result`s out of `Option`s (`src/error/multiple_error_types/option_result.md`)
    - Defining an error type (`src/error/multiple_error_types/define_error_type.md`)
    - `Box`ing errors (`src/error/multiple_error_types/boxing_errors.md`)
    - Other uses of `?` (`src/error/multiple_error_types/reenter_question_mark.md`)
    - Wrapping errors (`src/error/multiple_error_types/wrap_error.md`)
  - Iterating over `Result`s (`src/error/iter_result.md`)

**Kluczowe terminy:**
- `error handling` → „obsługa błędów"
- `panic` → „panika" (`panic!` w kodzie bez zmian)
- `unwind` → „rozwijanie stosu"
- `abort` → „przerwanie"
- `unwrap` → „rozwinięcie" (`unwrap()` w kodzie bez zmian)
- `combinator` → „kombinator"
- `early return` → „wczesny powrót"
- `propagate` → „propagować" (błąd)
- `boxing errors` → „pakowanie błędów w Box"
- `wrapping errors` → „owijanie błędów"

---

### Etap 9 — Biblioteka standardowa (≈340 wpisów)

**Rozdziały:**
- Std library types (`src/std.md`)
  - Box, stack and heap (`src/std/box.md`)
  - Vectors (`src/std/vec.md`)
  - Strings (`src/std/str.md`)
  - `Option` (`src/std/option.md`)
  - `Result` (`src/std/result.md`)
    - `?` (`src/std/result/question_mark.md`)
  - `panic!` (`src/std/panic.md`)
  - HashMap (`src/std/hash.md`)
    - Alternate/custom key types (`src/std/hash/alt_key_types.md`)
    - HashSet (`src/std/hash/hashset.md`)
  - `Rc` (`src/std/rc.md`)
  - `Arc` (`src/std/arc.md`)
- Std misc (`src/std_misc.md`)
  - Threads (`src/std_misc/threads.md`)
    - Testcase: map-reduce (`src/std_misc/threads/testcase_mapreduce.md`)
  - Channels (`src/std_misc/channels.md`)
  - Path (`src/std_misc/path.md`)
  - File I/O (`src/std_misc/file.md`)
    - `open` (`src/std_misc/file/open.md`)
    - `create` (`src/std_misc/file/create.md`)
    - `read_lines` (`src/std_misc/file/read_lines.md`)
  - Child processes (`src/std_misc/process.md`)
    - Pipes (`src/std_misc/process/pipe.md`)
    - Wait (`src/std_misc/process/wait.md`)
  - Filesystem Operations (`src/std_misc/fs.md`)
  - Program arguments (`src/std_misc/arg.md`)
    - Argument parsing (`src/std_misc/arg/matching.md`)
  - Foreign Function Interface (`src/std_misc/ffi.md`)

**Kluczowe terminy:**
- `stack` → „stos"
- `heap` → „sterta"
- `thread` → „wątek"
- `channel` → „kanał"
- `pipe` → „potok"
- `filesystem` → „system plików"
- `FFI` → FFI (akronim, rozwinąć: „Interfejs Funkcji Zewnętrznych" przy pierwszym użyciu)
- `smart pointer` → „inteligentny wskaźnik"
- `reference counting` → „zliczanie referencji"

---

### Etap 10 — Finalizacja (≈200 wpisów)

**Rozdziały:**
- Testing (`src/testing.md`)
  - Unit testing (`src/testing/unit_testing.md`)
  - Documentation testing (`src/testing/doc_testing.md`)
  - Integration testing (`src/testing/integration_testing.md`)
  - Dev-dependencies (`src/testing/dev_dependencies.md`)
- Unsafe Operations (`src/unsafe.md`)
  - Inline assembly (`src/unsafe/asm.md`)
- Compatibility (`src/compatibility.md`)
  - Raw identifiers (`src/compatibility/raw_identifiers.md`)
- Meta (`src/meta.md`)
  - Documentation (`src/meta/doc.md`)
  - Playground (`src/meta/playground.md`)

**Kluczowe terminy:**
- `unit testing` → „testy jednostkowe"
- `integration testing` → „testy integracyjne"
- `documentation testing` → „testy dokumentacji"
- `unsafe` → „niebezpieczny" (`unsafe` w kodzie bez zmian)
- `inline assembly` → „wbudowany asembler"
- `raw identifier` → „surowy identyfikator"
- `playground` → „plac zabaw"

**Po tym etapie:**
```bash
msgfmt --statistics po/pl.po
# Powinno pokazać: 2912 przetłumaczonych komunikatów, 0 nieprzetłumaczonych.
./scripts/check-po.sh po/pl.po
MDBOOK_BOOK__LANGUAGE=pl mdbook build
```

---

## Część IV — Protokół przeglądu przed commitem

Przed każdym commitem zawierającym zmiany w `pl.po`:

```bash
# 1. Walidacja strukturalna
./scripts/check-po.sh po/pl.po

# 2. Sprawdzenie spójności terminologii (kluczowe terminy)
grep -n 'msgstr.*ownership\|msgstr.*posiadanie\|msgstr.*przynależność' po/pl.po
grep -n 'msgstr.*borrowing\|msgstr.*zapożyczenie' po/pl.po
grep -n 'msgstr.*lifetime\|msgstr.*żywotność' po/pl.po
# Powyższe komendy powinny zwrócić puste wyniki — błąd jeśli cokolwiek znajdą

# 3. Sprawdzenie backtick-code
# Każde 'msgstr' zawierające zmienione backtick-code to błąd
# (weryfikacja manualna dla nowych wpisów)

# 4. Podgląd wizualny zmienionych sekcji
MDBOOK_BOOK__LANGUAGE=pl mdbook serve
```

---

## Część V — Lista kontrolna dla nowego tłumacza

- [ ] Przeczytałem `TRANSLATING.md` (ogólny workflow)
- [ ] Przeczytałem `po/GLOSSARY.md` (terminologia)
- [ ] Zainstalowałem `gettext` i `mdbook-i18n-helpers`
- [ ] Rozumiem wszystkie 5 inwariantów z Części I
- [ ] Rozumiem wszystkie 6 aksjomatów z Części II
- [ ] Pierwsza sesja: tłumaczę **maksymalnie 30 wpisów** i puszczam `./scripts/check-po.sh`
- [ ] Przed każdym PR: pełna walidacja + wizualny podgląd zmienionych stron
