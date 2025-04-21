#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Usage: $0 <vacancy_name>"
    exit 1
fi

VACANCY="$1"

VACANCY_ENCODED=$(echo "$VACANCY" | tr ' ' '+')

curl -s "https://api.hh.ru/vacancies?text=$VACANCY_ENCODED&per_page=20" | \
jq -r '.' > hh.json