#!/bin/bash
# Create advent of code files for next day
# must be in working directory
# read in arg for day from ENV ADVENT_DAY
# run . ./create_files.sh  to make ensure ADVENT_DAY is updated (or source ./)

echo "Day $ADVENT_DAY"
PRIORDAY=$(($ADVENT_DAY-1))
echo "Prior Day $PRIORDAY"
echo "Create puzzle and input files"
cp "day${PRIORDAY}_puzzles.py" "day${ADVENT_DAY}_puzzles.py"
touch "day${ADVENT_DAY}_example.txt"
touch "day${ADVENT_DAY}_input.txt"
echo "Increment Advent day"
export ADVENT_DAY=$(($ADVENT_DAY+1))
echo "ADVENT_DAY=$ADVENT_DAY"
echo "Done."
