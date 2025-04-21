#!/bin/sh
head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n +2 ../ex02/hh_sorted.csv | awk -F ',' 'BEGIN{OFS=","} {level = "-"
if ($3 ~/Junior/) { level = "Junior"}
if ($3 ~/Middle/) { level =  "Middle"}
if ($3 ~/Senior/) { level = "Senior"}
print $1, $2, level, $4, $5}' >> hh_positions.csv