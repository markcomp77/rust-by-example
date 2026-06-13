# Status tłumaczenia Rust by Example na język polski

**Data:** 2026-06-13
**Ostatnia aktualizacja:** synchronizacja `pl.po` z aktualnym `po/messages.pot`

---

## 1. Ogólne statystyki

| Metryka | Wartość |
|---|---:|
| Pliki Markdown w `src/` | 198 |
| Pliki objęte katalogiem gettext | 198 |
| Łącznie wpisów w `pl.po` | 2959 |
| Przetłumaczone wpisy | 2959 (100%) |
| Nieprzetłumaczone wpisy | 0 |
| Wpisy `fuzzy` | 0 |
| Błędy `msgfmt --check` | 0 |
| Braki względem `po/messages.pot` (`msgcmp`) | 0 |

---

## 2. Wyniki walidacji

```text
$ ./scripts/check-po.sh po/pl.po
=== Sprawdzam: po/pl.po ===
  Przetłumaczone:    2959 / 2959 (100%)
  OK.

Wszystkie pliki .po przeszły walidację.
```

```text
$ msgfmt --statistics --check -o /tmp/pl.mo po/pl.po
2959 przetłumaczonych komunikatów.
```

```text
$ msgcmp po/pl.po po/messages.pot
# brak wyjścia, brak błędów
```

```text
$ MDBOOK_BOOK__LANGUAGE=pl mdbook build -d /tmp/rbe-book-pl
INFO Book building has started
INFO Running the html backend
INFO HTML book written to `/tmp/rbe-book-pl`
```

Polski build HTML kończy się bez ostrzeżeń.

---

## 3. Zakres kompletności

Wszystkie rozdziały i podrozdziały znajdujące się w `src/` są objęte tłumaczeniem gettext. Nie ma obecnie rozdziałów w trakcie tłumaczenia ani plików pominiętych przez katalog POT.

Ostatnio uzupełnione wpisy dotyczyły:

- `src/scope/borrow/mut.md` - komentarze i komunikaty `println!` dla pożyczania mutowalnego i niemutowalnego,
- `src/scope/lifetime.md` - komunikat `"borrow1: {}"`,
- `src/error/option_unwrap.md` - akapit i lista o `Option<T>`, poprawione również pod kątem ostrzeżenia Markdown o tagu `<T>`.

---

## 4. Słownik i spójność

Tłumaczenie powinno pozostać zgodne z `po/GLOSSARY.md`. Kluczowe terminy:

- `ownership` → **własność**
- `borrowing` → **pożyczanie**
- `lifetime` → **czas życia**
- `trait` → **cecha**
- `crate` → **skrzynia**
- `enum` → **wyliczenie**

Nazwy typów, cech, makr, słów kluczowych i identyfikatorów Rusta powinny pozostawać w backtickach oraz bez tłumaczenia, np. `Option<T>`, `Result`, `Vec`, `println!`, `match`.

---

## 5. Pozostałe prace

Stan kompletności tłumaczenia wynosi 100%. Dalsze prace powinny koncentrować się na audycie jakościowym:

1. Sprawdzenie brakujących backticków w `msgstr` względem `msgid`.
2. Przegląd komentarzy w blokach kodu pod kątem naturalnego języka polskiego.
3. Ujednolicenie starszych fragmentów tłumaczonych automatycznie, zwłaszcza tam, gdzie zachowano angielską składnię zdań.
4. Okresowe uruchamianie `msgmerge --update po/pl.po po/messages.pot` po zmianach w źródłach.

---

## 6. Wniosek

Polskie tłumaczenie Rust by Example jest kompletne na poziomie katalogu gettext i poprawnie buduje się jako książka HTML. Aktualny stan nie zawiera brakujących wpisów, wpisów `fuzzy`, błędów `msgfmt`, różnic względem POT ani ostrzeżeń podczas budowania polskiej wersji.
