#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-serve}"

case "$MODE" in
    serve)
        echo "Uruchamianie polskiego tłumaczenia Rust by Example..."
        echo "→ http://localhost:3000"
        MDBOOK_BOOK__LANGUAGE=pl mdbook serve
        ;;
    build)
        echo "Budowanie polskiego tłumaczenia Rust by Example..."
        MDBOOK_BOOK__LANGUAGE=pl mdbook build
        echo "Gotowe. Wynik w book/pl/"
        ;;
    check)
        echo "Walidacja pl.po..."
        ./scripts/check-po.sh po/pl.po
        ;;
    *)
        echo "Użycie: $0 {serve|build|check}"
        echo "  serve  (domyślnie) — uruchom serwer deweloperski na :3000"
        echo "  build             — zbuduj wersję statyczną"
        echo "  check             — sprawdź poprawność pl.po"
        exit 1
        ;;
esac
