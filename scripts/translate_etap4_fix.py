#!/usr/bin/env python3
"""Poprawki do Etapu 4: wpisy, które nie zostały przetłumaczone w pierwszym przebiegu."""

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

# ============================================================
# 1. if_else.md:3 — backslash mismatch (\\\\- in file, \\\\\\\\- in script)
# ============================================================
old = 'msgid ""\n"Branching with `if`\\\\-`else` is similar to other languages. Unlike many of "\n"them, the boolean condition doesn\'t need to be surrounded by parentheses, "\n"and each condition is followed by a block. `if`\\\\-`else` conditionals are "\n"expressions, and, all branches must return the same type."\nmsgstr ""'
new = 'msgid ""\n"Branching with `if`\\\\-`else` is similar to other languages. Unlike many of "\n"them, the boolean condition doesn\'t need to be surrounded by parentheses, "\n"and each condition is followed by a block. `if`\\\\-`else` conditionals are "\n"expressions, and, all branches must return the same type."\nmsgstr ""\n"Rozgałęzianie z `if`\\\\-`else` jest podobne do innych języków. W odróżnieniu "\n"od wielu z nich, warunek logiczny nie musi być otoczony nawiasami, "\n"a każdy warunek jest poprzedzony blokiem. Wyrażenia `if`\\\\-`else` to "\n"wyrażenia, więc wszystkie gałęzie muszą zwracać ten sam typ."'
apply(old, new, 'if_else.md:3 Branching')

# ============================================================
# 2. for.md:14 — single-line comment (was tried as multi)
# ============================================================
old = 'msgid "// `n` will take the values: 1, 2, ..., 100 in each iteration\\n"\nmsgstr ""'
new = 'msgid "// `n` will take the values: 1, 2, ..., 100 in each iteration\\n"\nmsgstr "// `n` przyjmie wartości: 1, 2, ..., 100 w każdej iteracji\\n"'
apply(old, new, 'for.md:14 n will take values')

# ============================================================
# 3. match.md:23 — single-line comment (was tried as multi)
# ============================================================
old = 'msgid "// TODO ^ Try commenting out this catch-all arm\\n"\nmsgstr ""'
new = 'msgid "// TODO ^ Try commenting out this catch-all arm\\n"\nmsgstr "// TODO ^ Spróbuj zakomentować to ramię catch-all\\n"'
apply(old, new, 'match.md:23 TODO catch-all')

# ============================================================
# 4. destructuring.md:19 — multi-line link (was tried as prose/single-line)
# ============================================================
old = 'msgid ""\n"[The Rust Reference for Destructuring](https://doc.rust-lang.org/reference/"\n"patterns.html#r-patterns.destructure)"\nmsgstr ""'
new = 'msgid ""\n"[The Rust Reference for Destructuring](https://doc.rust-lang.org/reference/"\n"patterns.html#r-patterns.destructure)"\nmsgstr ""\n"[Dokumentacja Rust dla destrukturyzacji](https://doc.rust-lang.org/reference/"\n"patterns.html#r-patterns.destructure)"'
apply(old, new, 'destructuring.md:19 Rust Reference')

# ============================================================
# 5. destructure_slice.md — entries missing from script
# ============================================================

# :3 prose
old = 'msgid "Like tuples, arrays and slices can be destructured this way:"\nmsgstr ""'
new = 'msgid "Like tuples, arrays and slices can be destructured this way:"\nmsgstr "Podobnie jak krotki, tablice i wycinki można destrukturyzować w ten sposób:"'
apply(old, new, 'dslice:3 Like tuples')

# :7 comment
old = 'msgid "// Try changing the values in the array, or make it a slice!\\n"\nmsgstr ""'
new = 'msgid "// Try changing the values in the array, or make it a slice!\\n"\nmsgstr "// Spróbuj zmienić wartości w tablicy lub zamień ją na wycinek!\\n"'
apply(old, new, 'dslice:7 Try changing')

# :11 multi-line comment
old = 'msgid ""\n"// Binds the second and the third elements to the respective variables\\n"\nmsgstr ""'
new = 'msgid ""\n"// Binds the second and the third elements to the respective variables\\n"\nmsgstr ""\n"// Wiąże drugi i trzeci element z odpowiednimi zmiennymi\\n"'
apply(old, new, 'dslice:11 Binds second')

# :13 lit
old = 'msgid "\\"array[0] = 0, array[1] = {}, array[2] = {}\\""\nmsgstr ""'
new = 'msgid "\\"array[0] = 0, array[1] = {}, array[2] = {}\\""\nmsgstr "\\"array[0] = 0, array[1] = {}, array[2] = {}\\"'
apply(old, new, 'dslice:13 array[0]=0')

# :15 comment
old = 'msgid "// Single values can be ignored with _\\n"\nmsgstr ""'
new = 'msgid "// Single values can be ignored with _\\n"\nmsgstr "// Pojedyncze wartości można pominąć za pomocą _\\n"'
apply(old, new, 'dslice:15 Single values')

# :17 lit
old = 'msgid "\\"array[0] = 1, array[2] = {} and array[1] was ignored\\""\nmsgstr ""'
new = 'msgid "\\"array[0] = 1, array[2] = {} and array[1] was ignored\\""\nmsgstr "\\"array[0] = 1, array[2] = {} and array[1] was ignored\\""'
apply(old, new, 'dslice:17 array[0]=1')

# :21 comment
old = 'msgid "// You can also bind some and ignore the rest\\n"\nmsgstr ""'
new = 'msgid "// You can also bind some and ignore the rest\\n"\nmsgstr "// Można też powiązać niektóre i zignorować resztę\\n"'
apply(old, new, 'dslice:21 bind some')

# :23 lit
old = 'msgid "\\"array[0] = -1, array[1] = {} and all the other ones were ignored\\""\nmsgstr ""'
new = 'msgid "\\"array[0] = -1, array[1] = {} and all the other ones were ignored\\""\nmsgstr "\\"array[0] = -1, array[1] = {} and all the other ones were ignored\\""'
apply(old, new, 'dslice:23 array[0]=-1')

# :26 multi
old = 'msgid ""\n"// The code below would not compile\\n"\n"        // [-1, second] => ...\\n"\nmsgstr ""'
new = 'msgid ""\n"// The code below would not compile\\n"\n"        // [-1, second] => ...\\n"\nmsgstr ""\n"// Poniższy kod się nie skompiluje\\n"\n"        // [-1, second] => ...\\n"'
apply(old, new, 'dslice:26 code below')

# :29 multi
old = 'msgid ""\n"// Or store them in another array/slice (the type depends on\\n"\n"        // that of the value that is being matched against)\\n"\nmsgstr ""'
new = 'msgid ""\n"// Or store them in another array/slice (the type depends on\\n"\n"        // that of the value that is being matched against)\\n"\nmsgstr ""\n"// Lub zapisz je w innej tablicy/wycinku (typ zależy od\\n"\n"        // wartości, która jest dopasowywana)\\n"'
apply(old, new, 'dslice:29 Or store')

# :32 lit
old = 'msgid "\\"array[0] = 3, array[1] = {} and the other elements were {:?}\\""\nmsgstr ""'
new = 'msgid "\\"array[0] = 3, array[1] = {} and the other elements were {:?}\\""\nmsgstr "\\"array[0] = 3, array[1] = {} and the other elements were {:?}\\""'
apply(old, new, 'dslice:32 array[0]=3')

# :36 multi
old = 'msgid ""\n"// Combining these patterns, we can, for example, bind the first and\\n"\n"        // last values, and store the rest of them in a single array\\n"\nmsgstr ""'
new = 'msgid ""\n"// Combining these patterns, we can, for example, bind the first and\\n"\n"        // last values, and store the rest of them in a single array\\n"\nmsgstr ""\n"// Łącząc te wzorce, możemy np. powiązać pierwszą i ostatnią wartość,\\n"\n"        // a resztę zapisać w jednej tablicy\\n"'
apply(old, new, 'dslice:36 Combining')

# :39 lit
old = 'msgid "\\"array[0] = {}, middle = {:?}, array[2] = {}\\""\nmsgstr ""'
new = 'msgid "\\"array[0] = {}, middle = {:?}, array[2] = {}\\""\nmsgstr "\\"array[0] = {}, middle = {:?}, array[2] = {}\\""'
apply(old, new, 'dslice:39 array[0]={}')

# :48 multi link
old = 'msgid ""\n"[Arrays and Slices](../../../primitives/array.md) and [Binding](../binding."\n"md) for `@` sigil"\nmsgstr ""'
new = 'msgid ""\n"[Arrays and Slices](../../../primitives/array.md) and [Binding](../binding."\n"md) for `@` sigil"\nmsgstr ""\n"[Tablice i wycinki](../../../primitives/array.md) i [Wiązanie](../binding."\n"md) dla operatora `@`"'
apply(old, new, 'dslice:48 Arrays and Slices')

# ============================================================
# 6. destructure_enum.md missing entries
# ============================================================

# :6 multi-line comment
old = 'msgid ""\n"// `allow` required to silence warnings because only\\n"\n"// one variant is used.\\n"\nmsgstr ""'
new = 'msgid ""\n"// `allow` required to silence warnings because only\\n"\n"// one variant is used.\\n"\nmsgstr ""\n"// `allow` wymagane, aby wyciszyć ostrzeżenia, bo tylko\\n"\n"// jeden wariant jest używany.\\n"'
apply(old, new, 'denum:6 allow required')

# :10 single-line comment
old = 'msgid "// These 3 are specified solely by their name.\\n"\nmsgstr ""'
new = 'msgid "// These 3 are specified solely by their name.\\n"\nmsgstr "// Te 3 są określone wyłącznie przez nazwę.\\n"'
apply(old, new, 'denum:10 These 3')

# :14 single-line comment
old = 'msgid "// These likewise tie `u32` tuples to different names: color models.\\n"\nmsgstr ""'
new = 'msgid "// These likewise tie `u32` tuples to different names: color models.\\n"\nmsgstr "// Te podobnie wiążą krotki `u32` z różnymi nazwami: modele kolorów.\\n"'
apply(old, new, 'denum:14 These likewise')

# :50 multi-line link (wrong backtick placement in original script)
old = 'msgid ""\n"[`#[allow(...)]`](../../../attribute/unused.md), [color models](https://en."\n"wikipedia.org/wiki/Color_model) and [`enum`](../../../custom_types/enum.md)"\nmsgstr ""'
new = 'msgid ""\n"[`#[allow(...)]`](../../../attribute/unused.md), [color models](https://en."\n"wikipedia.org/wiki/Color_model) and [`enum`](../../../custom_types/enum.md)"\nmsgstr ""\n"[`#[allow(...)]`](../../../attribute/unused.md), [modele kolorów](https://en."\n"wikipedia.org/wiki/Color_model) i [`enum`](../../../custom_types/enum.md)"'
apply(old, new, 'denum:50 allow color models')

# ============================================================
# 7. destructure_structures.md:22 — single-line (was tried as multi)
# ============================================================
old = 'msgid "// and you can also ignore some variables:\\n"\nmsgstr ""'
new = 'msgid "// and you can also ignore some variables:\\n"\nmsgstr "// można też pominąć niektóre zmienne:\\n"'
apply(old, new, 'dstruct:22 ignore some variables')

# ============================================================
# 8. binding.md:28 — single-line (was tried as multi)
# ============================================================
old = 'msgid "// A similar binding can be done when matching several values.\\n"\nmsgstr ""'
new = 'msgid "// A similar binding can be done when matching several values.\\n"\nmsgstr "// Podobne wiązanie można zastosować przy dopasowaniu kilku wartości.\\n"'
apply(old, new, 'binding:28 similar binding')

# ============================================================
# 9. binding.md:45 — PO splits line after {n}!  (second cont: "\"` \n")
# ============================================================
# Extract old exactly from file to avoid space/backslash confusion
import re as _re
with open(PO_FILE, 'r', encoding='utf-8') as _f:
    _raw = _f.read()
_idx45 = _raw.find('#: src/flow_control/match/binding.md:45\n')
_end45 = _raw.find('\n\n', _idx45)
_block45 = _raw[_idx45:_end45]
_old45 = _block45[_block45.find('msgid '):]
_new45 = (_old45[:_old45.rfind('msgstr ""')] +
          'msgstr ""\n'
          '"// Mamy wariant `Some`, dopasuj jeśli jego wartość powiązana z `n`,\\n"\n'
          '"        // jest równa 42.\\n"\n'
          '"        // Można użyć `Some(42)` i drukować `\\"The Answer: 42!\\"`,\\n"\n'
          '"        // ale to wymagałoby zmiany `42` w 2 miejscach.\\n"\n'
          '"        // Można użyć `Some(n) if n == 42` i drukować `\\"The Answer: {n}!\\"`,\\n"\n'
          '"        // ale to nie przyczyni się do sprawdzania wyczerpania.\\n"\n'
          '"        // (Choć w tym przypadku to nie ma znaczenia, bo\\n"\n'
          '"        // następne ramię jest wzorcem \\"catch-all\\")\\n"')
apply(_old45, _new45, 'binding:45 Got Some variant')

# ============================================================
# 10. binding.md:65 — wrong backtick placement in original script
# ============================================================
old = ('msgid ""\n'
       '"[`functions`](../../fn.md), [`enums`](../../custom_types/enum.md) and "\n'
       '"[`Option`](../../std/option.md)"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"[`functions`](../../fn.md), [`enums`](../../custom_types/enum.md) and "\n'
       '"[`Option`](../../std/option.md)"\n'
       'msgstr ""\n'
       '"[`funkcje`](../../fn.md), [`wyliczenia`](../../custom_types/enum.md) i "\n'
       '"[`Option`](../../std/option.md)"')
apply(old, new, 'binding:65 functions enums Option')

# ============================================================
# 11. if_let.md:3 — multi-line (was tried as prose/single-line)
# ============================================================
old = ('msgid ""\n'
       '"For some use cases, when matching enums, `match` is awkward. For example:"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"For some use cases, when matching enums, `match` is awkward. For example:"\n'
       'msgstr ""\n'
       '"W niektórych przypadkach, gdy dopasowujemy enum, `match` jest niezgrabny. Na przykład:"')
apply(old, new, 'if_let:3 For some use cases')

# ============================================================
# 12. if_let.md:120 — wrong backtick placement in original script
# ============================================================
old = ('msgid ""\n'
       '"[`enum`](../custom_types/enum.md), [`Option`](../std/option.md), and the "\n'
       '"[RFC](https://github.com/rust-lang/rfcs/pull/160)"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"[`enum`](../custom_types/enum.md), [`Option`](../std/option.md), and the "\n'
       '"[RFC](https://github.com/rust-lang/rfcs/pull/160)"\n'
       'msgstr ""\n'
       '"[`enum`](../custom_types/enum.md), [`Option`](../std/option.md) i "\n'
       '"[RFC](https://github.com/rust-lang/rfcs/pull/160)"')
apply(old, new, 'if_let:120 enum Option RFC')

# ============================================================
# 13. let_else.md:5 — multi-line (was tried as prose/single-line)
# ============================================================
old = ('msgid ""\n'
       '"🛈 you can target specific edition by compiling like this `rustc --"\n'
       '"edition=2021 main.rs`"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"🛈 you can target specific edition by compiling like this `rustc --"\n'
       '"edition=2021 main.rs`"\n'
       'msgstr ""\n'
       '"🛈 możesz targetować konkretną edycję kompilując tak: `rustc --"\n'
       '"edition=2021 main.rs`"')
apply(old, new, 'let_else:5 target specific edition')

# ============================================================
# 14. let_else.md:8 — backslash mismatch (\\\\- in file)
# ============================================================
old = ('msgid ""\n'
       '"With `let`\\\\-`else`, a refutable pattern can match and bind variables in the "\n'
       '"surrounding scope like a normal `let`, or else diverge (e.g. `break`, "\n'
       '"`return`, `panic!`) when the pattern doesn\'t match."\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"With `let`\\\\-`else`, a refutable pattern can match and bind variables in the "\n'
       '"surrounding scope like a normal `let`, or else diverge (e.g. `break`, "\n'
       '"`return`, `panic!`) when the pattern doesn\'t match."\n'
       'msgstr ""\n'
       '"Dzięki `let`\\\\-`else` wzorzec obalający może dopasować i powiązać zmienne w "\n'
       '"otaczającym zasięgu jak normalne `let`, lub rozejść się (np. `break`, "\n'
       '"`return`, `panic!`) gdy wzorzec nie pasuje."')
apply(old, new, 'let_else:8 refutable pattern')

# ============================================================
# 15. let_else.md:31 — backslash mismatch
# ============================================================
old = ('msgid ""\n'
       '"The scope of name bindings is the main thing that makes this different from "\n'
       '"`match` or `if let`\\\\-`else` expressions. You could previously approximate "\n'
       '"these patterns with an unfortunate bit of repetition and an outer `let`:"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"The scope of name bindings is the main thing that makes this different from "\n'
       '"`match` or `if let`\\\\-`else` expressions. You could previously approximate "\n'
       '"these patterns with an unfortunate bit of repetition and an outer `let`:"\n'
       'msgstr ""\n'
       '"Zasięg wiązań nazw to główna różnica w stosunku do wyrażeń `match` lub "\n'
       '"`if let`\\\\-`else`. Wcześniej można było przybliżyć te wzorce niefortunnymi "\n'
       '"powtórzeniami i zewnętrznym `let`:"')
apply(old, new, 'let_else:31 scope of name bindings')

# ============================================================
# 16. while_let.md:58 — wrong backtick placement
# ============================================================
old = ('msgid ""\n'
       '"[`enum`](../custom_types/enum.md), [`Option`](../std/option.md), and the "\n'
       '"[RFC](https://github.com/rust-lang/rfcs/pull/214)"\n'
       'msgstr ""')
new = ('msgid ""\n'
       '"[`enum`](../custom_types/enum.md), [`Option`](../std/option.md), and the "\n'
       '"[RFC](https://github.com/rust-lang/rfcs/pull/214)"\n'
       'msgstr ""\n'
       '"[`enum`](../custom_types/enum.md), [`Option`](../std/option.md) i "\n'
       '"[RFC](https://github.com/rust-lang/rfcs/pull/214)"')
apply(old, new, 'while_let:58 enum Option RFC')

with open(PO_FILE, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\nŁącznie zmian: {total}')
