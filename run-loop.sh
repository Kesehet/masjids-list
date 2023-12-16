#!/bin/bash

# Starting value
start=1100

# Increment value
increment=100

# Number of iterations
iterations=10

for (( i=0; i<$iterations; i++ ))
do
    # Run your Python script
    python main.py $((start + i * increment))

    # Git add, commit, and push
    git add .
    git commit -m "Update: iteration $i with start value $((start + i * increment))"
    git push origin main
    clear
done
