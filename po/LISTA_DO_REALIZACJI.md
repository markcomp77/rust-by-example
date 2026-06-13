# Lista do realizacji — tłumaczenie pl.po

Stan na 2026-06-07. Wszystkie 2959 wpisów mają wypełniony `msgstr`.
Poniżej zadania uszeregowane według priorytetu.

---

## Priorytet 1 — Błędy krytyczne (backtick-code w tekście)

**245 wpisów** ma backtick-code w msgid który nie występuje w msgstr.
Głównie tytuły w SUMMARY.md. Przykład: msgid `` `From` `` → msgstr `From` (bez backticków).

| Podzadanie | Opis | Szac. liczba |
|------------|------|:------------:|
| 1a | SUMMARY.md — przywrócić backticki w tytułach rozdziałów | ~80 |
| 1b | Pozostałe teksty — przywrócić backticki w nazwach typów/funkcji | ~165 |

**Weryfikacja:** `python3 -c skrypt` który wyciąga wpisy z różnymi backtickami.

---

## Priorytet 2 — Komentarze w kodzie po angielsku

**52 komentarze** mają `msgid == msgstr` (oba angielskie).
Głównie z apostrofami (`'a`, `don't`), cudzysłowami lub Unicode (znaki ramek).

| Podzadanie | Zakres | Liczba |
|------------|--------|:------:|
| 2a | scope/lifetime — znaki Unicode (─┐│ itp.) | ~10 |
| 2b | scope/borrow — apostrofy w `Can't`, `don't` | ~6 |
| 2c | trait, error — `'static`, `doesn't`, `can't` | ~12 |
| 2d | std — `don't`, `can't`, `"hello.txt"` itp. | ~15 |
| 2e | meta/doc — doc comments z ``` i `"name"` | ~3 |
| 2f | error/option — `\u{211D}` i SHIFT-JIS | ~2 |
| 2g | Pozostałe | ~4 |

**Weryfikacja:** `msgfmt --statistics` pokaże spadek `english_comments` z 52 do 0.

---

## Priorytet 3 — Tytuły rozdziałów

Wiele tytułów w SUMMARY.md i na stronach rozdziałów jest po angielsku.
Sekcja 1 (Hello World, Primitives) ma 66% kompletności tytułów.

| Podzadanie | Zakres | Etap |
|------------|--------|:----:|
| 3a | hello, primitives, custom_types | 1-2 |
| 3b | variable_bindings, types, conversion | 2-3 |
| 3c | flow_control, fn, mod | 3-4 |
| 3d | generics, scope | 5-6 |
| 3e | trait, macros, error, std | 7-9 |
| 3f | testing, unsafe, meta | 10 |

**Weryfikacja:** Przegląd wizualny z `MDBOOK_BOOK__LANGUAGE=pl mdbook serve`.

---

## Priorytet 4 — Czystość (issue #1)

Usunąć zbędny plik `po/pl.po.backup` i `po/pl.po.fixed*`, które powstały podczas napraw.

```
rm po/pl.po.backup po/pl.po.fixed* po/pl.po.new* 2>/dev/null
```

---

## Priorytet 5 — Automatyzacja (opcjonalnie)

Stworzyć skrypt `scripts/check-backticks.sh` który:
1. Znajduje wpisy z backtick-code w msgid
2. Sprawdza czy te same backticki są w msgstr
3. Raportuje różnice z numerami linii

---

## Podsumowanie czasowe

| Priorytet | Zadanie | Szac. czas |
|:---------:|---------|:----------:|
| 1 | Backticki w tekście | 30-45 min |
| 2 | 52 komentarze po angielsku | 15-20 min |
| 3 | Tytuły rozdziałów | 20-30 min |
| 4 | Sprzątanie plików | 1 min |
| 5 | Skrypt automatyzacji | 10 min |
| | **Razem** | **~1.5 godz.** |
