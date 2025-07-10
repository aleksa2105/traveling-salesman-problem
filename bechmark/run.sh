#!/bin/bash


# Testing average fitness value for TSP problem

N=15 # number of runs
SUM=0
EXEC="main.py"

echo "Running test..."

for i in $(seq 1 $N); do
	echo "Run #$i"

	VALUE=$(python3 $EXEC | tail -n 1)
	
	echo "Result: $VALUE"
	SUM=$(echo "$SUM + $VALUE" | bc -l)
	echo ""
done

AVG=$(echo "$SUM / $N" | bc -l)

echo "==========================="
echo "Average: $AVG"
