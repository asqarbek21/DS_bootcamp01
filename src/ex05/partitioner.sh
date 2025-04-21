#!/bin/sh

input_file="../ex03/hh_positions.csv"

header=$(head -n 1 "$input_file")

tail -n +2 "$input_file" | while IFS=, read -r id created_at name has_test alternate_url; do
    date=$(echo "$created_at" | tr -d '"' | cut -d'T' -f1)

    filename="${date}.csv"

    if [ ! -f "$filename" ]; then
        echo "$header" > "$filename"
    fi

    echo "$id,$created_at,$name,$has_test,$alternate_url" >> "$filename"
done
