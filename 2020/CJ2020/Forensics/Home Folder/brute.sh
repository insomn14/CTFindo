#!/bin/bash
file="wordlist.txt"
while IFS= read -r line
do
    echo $line
done <"$file"
