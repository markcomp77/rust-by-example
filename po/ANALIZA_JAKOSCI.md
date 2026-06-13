# Analiza jakosciowa tlumaczenia polskiego Rust by Example

**Data:** 2026-06-11 00:57
**Plik:** `po/pl.po`

---
## 1. Slabosci krytyczne

### 1a. Przetlumaczone nazwy typow/cech (NIE powinny byc)

Brak.

### 1b. Backticki w tekscie niezgodne z msgid

Znaleziono: **163** wystapien

Najczestsze brakujace backticki:
- `trait`: 12x
- `Option`: 12x
- `panic`: 8x
- `match`: 7x
- `traits`: 5x
- `panic!`: 5x
- `'static`: 4x
- `struct`: 3x
- `Result`: 3x
- `impl Trait`: 3x
- `Add`: 3x
- `unwrap`: 3x
- `dead_code`: 2x
- `write!`: 2x
- `primitives`: 2x

---
## 2. Slabosci srednie

### 2a. Angielskie komentarze `//` w kodzie

Brak.

### 2b. Forma osobowa zamiast bezosobowej

Brak.

### 2c. Niespojna terminologia (ASCII vs Unicode)

Brak.

---
## 3. Slabosci niskie

### 3a. Tytuly SUMMARY.md po angielsku

19 tytulow, wszystkie to nazwy wlasne Rusta (RAII, Drop, `impl Trait`, `Option`, itp.)
Zgodnie z Aksjomatem 6 nie wymagaja tlumaczenia.

### 3b. Doslowny tekst z dwoch ostatnich sesji (9 cofnietych komentarzy)

9 komentarzy z `println!("...")` cofnieto do angielskiego z powodu bledow escapowania.
Wymagaja recznej naprawy z poprawnym `\"` w pliku .po.

---
## 4. Podsumowanie

| Kategoria | Liczba | Waga |
|-----------|-------:|:----:|
| Przetlumaczone typy/cechy | 0 | krytyczna |
| Brakujace backticki | 163 | krytyczna |
| Komentarze po angielsku | 0 | srednia |
| Forma osobowa "mozesz" | 0 | niska |
| Niespojna terminologia | 0 | niska |
| **Laczenie** | **163** | |

### Interpretacja

Na 2953 wpisy, 163 ma jakies niedoskonalosci (5%).
Walidacja strukturalna przechodzi w 100%.
Jakosc tlumaczenia jest dobra, ale wymaga poprawek w 3 obszarach:
1. **Backticki** (163) — najwiekszy pojedynczy problem