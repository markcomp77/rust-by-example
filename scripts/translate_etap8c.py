#!/usr/bin/env python3
# Etap 8c: pozostałe poprawki trait + partial_move

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

def verbatim(en):
    old = f'msgid "{en}"\nmsgstr ""'
    new = f'msgid "{en}"\nmsgstr "{en}"'
    apply(old, new, en[:40])

def multi(old_body, new_msgstr):
    old = old_body + 'msgstr ""'
    new = old_body + 'msgstr ""\n' + new_msgstr
    apply(old, new, old_body[8:48])

# scope/move/partial_move.md:3 — different text (longer, with Drop note)
multi(
    'msgid ""\n'
    '"Within the [destructuring](../../flow_control/match/destructuring.md) of a "\n'
    '"single variable, both `by-move` and `by-reference` pattern bindings can be "\n'
    '"used at the same time. Doing this will result in a _partial move_ of the "\n'
    '"variable, which means that parts of the variable will be moved while other "\n'
    '"parts stay. In such a case, the parent variable cannot be used afterwards as "\n'
    '"a whole, however the parts that are only referenced (and not moved) can "\n'
    '"still be used. Note that types that implement the [`Drop` trait](../../trait/"\n'
    '"drop.md) cannot be partially moved from, because its `drop` method would use "\n'
    '"it afterwards as a whole."\n',
    '"Podczas [destrukturyzacji](../../flow_control/match/destructuring.md) jednej "\n'
    '"zmiennej można jednocześnie użyć powiązań wzorców `by-move` i `by-reference`. "\n'
    '"Spowoduje to _częściowe przeniesienie_ zmiennej, co oznacza, że części "\n'
    '"zmiennej zostaną przeniesione, podczas gdy inne pozostaną. W takim przypadku "\n'
    '"zmienna nadrzędna nie może być później użyta jako całość, jednak części, do "\n'
    '"których tylko się odwołano (bez przenoszenia), mogą być nadal używane. "\n'
    '"Typy implementujące cechę [`Drop`](../../trait/drop.md) nie mogą być częściowo "\n'
    '"przenoszone, ponieważ ich metoda `drop` użyłaby ich później jako całości."\n'
)

# trait/derive.md:40 — "trait\\n" on continuation line
multi(
    'msgid ""\n'
    '"// Error: `Seconds` can\'t be printed; it doesn\'t implement the `Debug` "\n'
    '"trait\\n"\n'
    '"    //println!(\\"One second looks like: {:?}\\", _one_second);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd: `Seconds` nie może być drukowane; nie implementuje cechy `Debug`\\n"\n'
    '"    //println!(\\"One second looks like: {:?}\\", _one_second);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# trait/derive.md:44 — "trait\\n" on continuation line
multi(
    'msgid ""\n'
    '"// Error: `Seconds` can\'t be compared; it doesn\'t implement the `PartialEq` "\n'
    '"trait\\n"\n'
    '"    //let _this_is_true = (_one_second == _one_second);\\n"\n'
    '"    // TODO ^ Try uncommenting this line\\n"\n',
    '"// Błąd: `Seconds` nie może być porównywane; nie implementuje cechy `PartialEq`\\n"\n'
    '"    //let _this_is_true = (_one_second == _one_second);\\n"\n'
    '"    // TODO ^ Spróbuj odkomentować tę linię\\n"\n'
)

# trait/ops.md:55 — "See Also" (appears at multiple locations)
prose('See Also', 'Zobacz też')

# trait/drop.md:27 — verbatim "a" (at multiple locations)
verbatim('\\"a\\"')

# trait/iter.md:63 — verbatim "> {}" (at multiple locations)
verbatim('\\"> {}\\"')

# trait/impl_trait.md:109 — last line "can do this easily:"
multi(
    'msgid ""\n'
    '"You can also use `impl Trait` to return an iterator that uses `map` or "\n'
    '"`filter` closures! This makes using `map` and `filter` easier. Because "\n'
    '"closure types don\'t have names, you can\'t write out an explicit return type "\n'
    '"if your function returns iterators with closures. But with `impl Trait` you "\n'
    '"can do this easily:"\n',
    '"Możesz też używać `impl Trait` do zwracania iteratora, który używa domknięć `map` "\n'
    '"lub `filter`! Ułatwia to używanie `map` i `filter`. Ponieważ typy domknięć nie "\n'
    '"mają nazw, nie można zapisać jawnego typu zwracanego, jeśli funkcja zwraca "\n'
    '"iteratory z domknięciami. Ale z `impl Trait` możesz to zrobić łatwo:"\n'
)

# trait/clone.md:12 — "implicitly copy" ending
multi(
    'msgid ""\n'
    '"The [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html) trait "\n'
    '"allows a type to be duplicated simply by copying bits, with no additional "\n'
    '"logic required. When a type implements `Copy`, assignments and function "\n'
    '"calls will implicitly copy the value instead of moving it."\n',
    '"Cecha [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html) pozwala "\n'
    '"typowi być powielanym przez proste kopiowanie bitów, bez dodatkowej logiki. "\n'
    '"Gdy typ implementuje `Copy`, przypisania i wywołania funkcji niejawnie skopiują "\n'
    '"wartość zamiast ją przenosić."\n'
)

# ───────────────────────────────────────────────────────────────────────────

open('po/pl.po', 'w').write(text)
print(f'\nŁącznie zmian: {total}')
