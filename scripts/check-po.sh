#!/usr/bin/env bash
# Waliduje pliki .po: sprawdza błędy formatowania i próg kompletności.
# Użycie: ./scripts/check-po.sh [plik.po ...]
# Bez argumentów: sprawdza wszystkie po/*.po

set -euo pipefail

COMPLETENESS_THRESHOLD=30  # minimalny % przetłumaczonych, poniżej którego jest błąd
ERRORS=0

po_files=("${@:-po/*.po}")

check_file() {
    local po="$1"
    local lang
    lang=$(basename "$po" .po)
    echo "=== Sprawdzam: $po ==="

    # 1. Weryfikacja strukturalna (newline mismatch, nieprawidłowy format)
    if ! msgfmt --check -o /dev/null "$po" 2>/tmp/msgfmt_out_$$; then
        echo "BŁĄD [$lang]: msgfmt --check zgłosił błędy:"
        cat /tmp/msgfmt_out_$$
        ERRORS=$((ERRORS + 1))
        rm -f /tmp/msgfmt_out_$$
        return
    fi
    rm -f /tmp/msgfmt_out_$$

    # 2. Statystyki kompletności
    local stats
    stats=$(msgfmt --statistics -o /dev/null "$po" 2>&1 || true)

    local translated fuzzy untranslated total pct
    translated=$(echo "$stats" | grep -oP '\d+(?= przetłumaczon)' | head -1 || echo "0")
    fuzzy=$(echo "$stats" | grep -oP '\d+(?= tłumacze)' | head -1 || echo "0")
    untranslated=$(echo "$stats" | grep -oP '\d+(?= nieprzetłumaczon)' | head -1 || echo "0")
    total=$((translated + fuzzy + untranslated))

    if [ "$total" -eq 0 ]; then
        echo "OSTRZEŻENIE [$lang]: brak wpisów w pliku."
        return
    fi

    pct=$(( (translated * 100) / total ))
    echo "  Przetłumaczone:    $translated / $total ($pct%)"
    [ "$fuzzy" -gt 0 ]       && echo "  Wątpliwe (fuzzy):  $fuzzy — wymagają przeglądu"
    [ "$untranslated" -gt 0 ] && echo "  Nieprzetłumaczone: $untranslated"

    if [ "$pct" -lt "$COMPLETENESS_THRESHOLD" ]; then
        echo "BŁĄD [$lang]: kompletność $pct% poniżej progu $COMPLETENESS_THRESHOLD%."
        ERRORS=$((ERRORS + 1))
    else
        echo "  OK."
    fi
    echo ""
}

for po in "${po_files[@]}"; do
    check_file "$po"
done

if [ "$ERRORS" -gt 0 ]; then
    echo "Łącznie błędów: $ERRORS"
    exit 1
fi

echo "Wszystkie pliki .po przeszły walidację."
