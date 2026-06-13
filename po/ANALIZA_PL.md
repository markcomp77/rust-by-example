# Analiza tłumaczenia polskiego Rust by Example

**Data:** 2026-06-07 18:45
**Plik:** `po/pl.po`
**Całkowita liczba wpisów:** 2959
**Przetłumaczone:** 2959
**Nieprzetłumaczone:** 0
**Kompletność:** 100%
**Walidacja:** OK
**Budowa mdbook:** OK (tylko ostrzezenie HTML o <t>)

---
## 1. Rodzaje tłumaczeń

| Rodzaj | Liczba | Przetłumaczone | Kompletność |
|--------|------:|---------------:|------------:|
| title | 1067 | 322 | 30% |
| code_comment | 999 | 948 | 94% |
| text | 788 | 770 | 97% |
| link_list | 87 | 78 | 89% |
| code_block | 8 | 4 | 50% |
| terminal_block | 8 | 2 | 25% |
| heading | 3 | 1 | 33% |

### Opis kategorii

- **code_comment** — komentarze `//` i `///` w blokach kodu Rusta
- **code_block** — bloki kodu ```rust ... ``` (limitery + kod)
- **text** — akapity, zdania objaśniające, wieloliniowy tekst
- **title** — tytuły rozdziałów (krótkie, < 60 znaków)
- **heading** — nagłówki Markdown (`#`, `##`, `###`)
- **list_item** — elementy list (`*`, `-`, `1.`)
- **link_list** — listy linków z backtick-code
- **string_literal** — literały łańcuchowe w kodzie (np. `"Hello"`)
- **terminal_block** — bloki terminala (```bash, ```text)
- **other** — pozostałe

---
## 2. Komentarze w kodzie

| Status | Liczba |
|--------|------:|
| Komentarze ogółem | 1003 |
| Przetłumaczone na polski | 951 |
| Wciąż angielskie (msgid == msgstr) | 52 |
| Kompletność komentarzy | 94% |

---
## 3. Postęp według etapów

| Etap | Rozdział | Wpisy | Przetłum. | % | Ang. komentarze |
|------|----------|------:|----------:|--:|----------------:|
| **1** | | | | | |
| | hello | 181 | 121 | 66% | 0 |
| | primitives | 78 | 44 | 56% | 0 |
| **2** | | | | | |
| | custom_types | 115 | 80 | 69% | 0 |
| | types | 61 | 43 | 70% | 0 |
| | variable_bindings | 37 | 23 | 62% | 0 |
| **3** | | | | | |
| | conversion | 31 | 21 | 67% | 0 |
| | flow_control | 263 | 152 | 57% | 1 |
| **4** | | | | | |
| | crates | 9 | 6 | 66% | 0 |
| | fn | 190 | 132 | 69% | 0 |
| | mod | 83 | 52 | 62% | 0 |
| **5** | | | | | |
| | attribute | 29 | 20 | 68% | 0 |
| | cargo | 57 | 45 | 78% | 0 |
| | generics | 163 | 125 | 76% | 0 |
| **6** | | | | | |
| | scope | 237 | 156 | 65% | 21 |
| **7** | | | | | |
| | macros | 61 | 51 | 83% | 0 |
| | trait | 161 | 102 | 63% | 6 |
| **8** | | | | | |
| | error | 312 | 155 | 49% | 6 |
| **9** | | | | | |
| | std | 253 | 135 | 53% | 12 |
| | std_misc | 223 | 137 | 61% | 2 |
| **10** | | | | | |
| | compatibility | 4 | 4 | 100% | 0 |
| | meta | 44 | 33 | 75% | 2 |
| | testing | 56 | 51 | 91% | 0 |
| | unsafe | 126 | 81 | 64% | 0 |

---
## 4. Błędy i problemy

| Typ problemu | Liczba |
|--------------|------:|
| Nieprzetłumaczone wpisy (puste msgstr) | 0 |
| Komentarze angielskie (msgid == msgstr) | 52 |
| Niezgodność \\n w msgid/msgstr | 0 |
| Uszkodzone backtick-code w tłumaczeniu | 245 |
| Problemy terminologiczne | 0 (1 naprawiony) |

### Uwaga o backtick-code

245 wpisów ma backtick-code (`Foo`) w msgid, które nie pojawia się w msgstr.  
Głównie tytuły w `SUMMARY.md` —  np. `` `From` `` → brak backticków.  
Wymaga osobnej sesji naprawczej.

---
## 5. Walidacja strukturalna

```
=== Sprawdzam: po/pl.po ===
  Przetłumaczone:    2959 / 2959 (100%)
  OK.

Wszystkie pliki .po przeszły walidację.
```

---
## 6. Wnioski

**Wszystkie 2959 wpisy mają wypełniony msgstr.**
Pozostało 52 komentarzy w kodzie z msgid == msgstr (angielski → angielski).
Nie stanowią one błędu strukturalnego — msgfmt ich nie zgłasza.

### Liczniki inline

- total_entries=2959
- total_translated=2959
- total_untranslated=0
- english_comments=52
- polish_comments=951
- newline_issues=0
- backtick_issues=245
- terminology_issues=0 (1 naprawiony)