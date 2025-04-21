#!/bin/sh

output_file="hh_concatenated_positions.csv"
rm -f "$output_file"

csv_files=$(ls *.csv | sort)

first=1
for file in $csv_files; do
    if [ "$first" -eq 1 ]; then
        cat "$file" > "$output_file"
        first=0
    else
        tail -n +2 "$file" >> "$output_file"
    fi
done
