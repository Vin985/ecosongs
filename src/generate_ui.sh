#!/bin/bash


# ECOSONGS_MAIN="./ecosongs.ui"
# ECOSONGS_MAIN_DEST="../"




# cd gui;

for f in `find . -name "*.ui"`; do
    # echo $f
    # if [[ $f == $ECOSONGS_MAIN ]]; then
    echo $(echo $f | sed s/.ui/_ui.py/);
    # fi 
done

# for f in *.ui; do pyside2-uic "$f" -o $(echo $f | sed s/.ui/_ui.py/); done