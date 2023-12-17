#!/bin/bash

# Starting value
start=0

# Increment value
increment=100

# Number of iterations
iterations=99999999

for (( i=0; i<$iterations; i++ ))
do
    # Run your Python script
    python main.py $((start + i * increment)) >> logs/output_$((start + i * increment)).txt

    # Git add, commit, and push
    git add .
    git commit -m "Update: iteration $i with start value $((start + i * increment))"
    git push origin main
    clear
done
