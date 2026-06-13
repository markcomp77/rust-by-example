# Glosariusz terminologii Rusta

Kanoniczne tłumaczenia kluczowych terminów dla poszczególnych języków.
Każdy tłumacz **musi** stosować te terminy spójnie w całym pliku `.po`.

---

## Zasady ogólne (wszystkie języki)

1. Nazwy typów standardowych (`String`, `Vec`, `Option`, `Result`, `Box`, `Rc`, `Arc`) — **nie tłumaczyć nigdy**.
2. Nazwy cech wbudowanych (`Display`, `Debug`, `Clone`, `Copy`, `Iterator`, `Drop`, `Fn`, `FnMut`, `FnOnce`) — **nie tłumaczyć nigdy**.
3. Makra (`println!`, `format!`, `vec!`, `assert!`, `panic!`) — **nie tłumaczyć nigdy**.
4. Słowa kluczowe języka (`fn`, `let`, `mut`, `match`, `use`, `impl`, `trait`, `struct`, `enum`, `pub`, `mod`, `crate`, `self`, `super`, `where`, `for`, `while`, `loop`, `if`, `else`, `return`, `unsafe`, `async`, `await`) — **nie tłumaczyć nigdy**.
5. Identyfikatory w kodzie (`main`, `x`, `my_struct` itd.) — **nie tłumaczyć nigdy**.
6. Zawartość bloków kodu (` ```rust ... ``` `) — **nie tłumaczyć**, wyjątek: komentarze `//` wewnątrz kodu *mogą* być tłumaczone, ale muszą być albo **wszystkie** przetłumaczone albo **żaden** w danym tłumaczeniu.
7. Adresy URL w linkach Markdown `[tekst](url)` — **nie tłumaczyć adresu URL**, tłumaczyć tylko tekst linku gdy sensowne.

---

## Polski (`pl`)

### Terminy rdzenne (własność/pożyczanie)

| Angielski               | Polski                        | Uwagi |
|-------------------------|-------------------------------|-------|
| ownership               | własność                      | nigdy "posiadanie" |
| owner                   | właściciel                    | |
| borrow / borrowing      | pożyczanie / pożyczyć         | |
| borrow checker          | analizator pożyczania         | dopuszczalne: "borrow checker" w nawiasie |
| move semantics          | semantyka przenoszenia        | |
| move                    | przeniesienie / przenieść     | jako rzeczownik i czasownik |
| copy                    | kopiowanie / skopiować        | |
| clone                   | klonowanie / sklonować        | |
| lifetime                | czas życia                    | nigdy "żywotność" |
| lifetime annotation     | adnotacja czasu życia         | |
| lifetime elision        | elizja czasu życia            | |
| scope                   | zasięg                        | |
| shadowing               | przesłanianie                 | |
| freeze / freezing       | zamrożenie                    | |
| drop                    | zrzucenie / zwolnienie        | (pamięci) |
| RAII                    | RAII                          | akronim — nie tłumaczyć |

### Typy i struktury

| Angielski               | Polski                        | Uwagi |
|-------------------------|-------------------------------|-------|
| trait                   | cecha                         | `trait` w kodzie bez zmian |
| supertrait              | supercecha                    | |
| struct / structure      | struktura                     | |
| enum / enumeration      | wyliczenie                    | |
| tuple                   | krotka                        | |
| array                   | tablica                       | |
| slice                   | wycinek                       | |
| reference               | referencja                    | |
| pointer                 | wskaźnik                      | |
| raw pointer             | surowy wskaźnik               | |
| smart pointer           | inteligentny wskaźnik         | |
| generic / generics      | ogólny / typy ogólne          | |
| type parameter          | parametr typu                 | |
| type alias              | alias typu                    | |
| associated type         | typ skojarzony                | |
| phantom type            | typ fantomowy                 | |
| newtype                 | nowotyp                       | |
| bounds                  | ograniczenia                  | |
| where clause            | klauzula where                | `where` w kodzie bez zmian |
| trait object            | obiekt cechy                  | |
| dynamic dispatch        | dynamiczne wysyłanie          | |
| monomorphization        | monomorfizacja                | |

### Funkcje i kontrola przepływu

| Angielski               | Polski                        | Uwagi |
|-------------------------|-------------------------------|-------|
| closure                 | domknięcie                    | |
| higher-order function   | funkcja wyższego rzędu        | |
| diverging function      | funkcja rozbieżna             | |
| pattern matching        | dopasowanie wzorca            | |
| destructuring           | destrukturyzacja              | |
| guard                   | strażnik                      | |
| binding                 | wiązanie / powiązanie         | |
| capture                 | przechwytywanie               | |
| iterator                | iterator                      | |
| combinator              | kombinator                    | |

### Zarządzanie projektem

| Angielski               | Polski                        | Uwagi |
|-------------------------|-------------------------------|-------|
| crate                   | skrzynia                      | dopuszczalne "crate" + nawiasem |
| module                  | moduł                         | |
| package                 | pakiet                        | |
| workspace               | przestrzeń robocza            | |
| dependency              | zależność                     | |
| attribute               | atrybut                       | |
| macro                   | makro                         | |
| visibility              | widoczność                    | |

### Obsługa błędów

| Angielski               | Polski                        | Uwagi |
|-------------------------|-------------------------------|-------|
| error handling          | obsługa błędów                | |
| panic                   | panika                        | `panic!` w kodzie bez zmian |
| unwrap                  | rozwinięcie                   | `unwrap()` w kodzie bez zmian |
| propagate               | propagować / przekazać        | (błąd) |
| early return            | wczesny powrót                | |
| boxing errors           | pakowanie błędów w Box        | |
| wrapping errors         | owijanie błędów               | |

### Pozostałe

| Angielski               | Polski                        | Uwagi |
|-------------------------|-------------------------------|-------|
| unsafe                  | niebezpieczny                 | `unsafe` w kodzie bez zmian |
| inline assembly         | wbudowany asembler            | |
| formatted print         | formatowane drukowanie        | |
| literal                 | literał                       | |
| casting                 | rzutowanie                    | |
| inference               | wnioskowanie (o typach)       | |
| aliasing                | aliasowanie                   | |
| operator overloading    | przeciążanie operatorów       | |
| testcase                | przykład testowy              | |
| playground              | plac zabaw                    | |
| FFI (Foreign Function Interface) | FFI (Interfejs Funkcji Zewnętrznych) | akronim zachować |

---

## Terminy sporne — uzasadnienie wyboru (PL)

**`trait` → cecha**: Słowo "cecha" jest bezpośrednim tłumaczeniem "trait" i funkcjonuje dobrze w polskiej literaturze programistycznej. Alternatywa "interfejs" jest myląca (trait ≠ interface w Javie).

**`ownership` → własność**: "Własność" dokładnie oddaje semantykę — wartość *należy* do jednego właściciela. "Posiadanie" brzmi bardziej abstrakcyjnie.

**`lifetime` → czas życia**: Kalka dosłowna, ale powszechnie używana. "Żywotność" jest poprawna językowo, ale mniej używana w społeczności.

**`crate` → skrzynia**: Oficjalne polskie tłumaczenie stosowane w dokumentacji Rust. W tekście można użyć "skrzynia (crate)" przy pierwszym wprowadzeniu.

**`closure` → domknięcie**: Matematyczny termin, prawidłowy. Nie "lambda" (to inny koncept), nie "zamknięcie".

---

## Japońskie (`ja`) — wybrane terminy referencyjne

| Angielski  | Japoński      |
|------------|---------------|
| ownership  | 所有権        |
| borrowing  | 借用          |
| lifetime   | ライフタイム  |
| closure    | クロージャ    |
| trait      | トレイト      |

## Chińskie (`zh`) — wybrane terminy referencyjne

| Angielski  | Chiński  |
|------------|----------|
| ownership  | 所有权   |
| borrowing  | 借用     |
| lifetime   | 生命周期 |
| closure    | 闭包     |
| trait      | trait    |
