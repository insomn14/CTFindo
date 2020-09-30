#!/usr/bin/bash

fname='code'

for i in {0..287}; do
	echo $fname$i
	objdump -d -M intel $fname$i | grep -A 1 6000c9;
done