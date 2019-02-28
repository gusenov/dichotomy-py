#!/bin/bash

# Usage:
#  $ "./tree.sh" "tree_0-10.gv" "tree_0-10.png"
#  $ "./tree.sh" "tree_1-10.gv" "tree_1-10.png"

input_file="$1"
output_file="$2"

#while inotifywait -e close_write "$input_file"; do dot -Tpng "$input_file" -o "$output_file"; done
echo "$input_file" | entr -s "clear; dot -Tpng \"$input_file\" -o \"$output_file\""
