#!/bin/zsh

# Menu
echo "Choose Your Option"
echo "1. Pronounciation Similarity"
echo "2. Shape Similarity"
echo -n "Your Option (Index): "
read option

# Conduct
if [ $option -eq 1 ]; then
    echo "Entering ./pronounciation_similarity/edit.py..."
    python ./pronounciation_similarity/edit.py
elif [ $option -eq 2 ]; then
    echo "Entering ./shape_similarity/edit.py..."
    python ./shape_similarity/edit.py
else
    echo "Undefined Option"
fi