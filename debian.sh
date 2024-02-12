#!/bin/bash

# Menu
echo "Choose Your Option"
echo -e "\e[0;34m1. Pronounciation Similarity"
echo -e "2. Shape Similarity"
echo -e "3. Exit\e[0;m"
echo -n "- Your Option (Index): "
read option

# Conduct
if [ "$option" == "1" ]; then
    echo "Entering ./pronounciation_similarity/edit.py..."
    python ./pronounciation_similarity/edit.py
elif [ "$option" == "2" ]; then
    echo "Entering ./shape_similarity/edit.py..."
    python ./shape_similarity/edit.py
elif [ "$option" == "3" ]; then
    echo "Exit."
else
    echo "Undefined Option"
fi