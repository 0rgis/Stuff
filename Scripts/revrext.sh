#!/bin/bash
set -euo pipefail
input="${1:?Error please add a string}"
reverse=""
 
len=${#input}
for (( i=$len-1; i>=0; i-- ))
do 
	reverse="$reverse${input:$i:1}"
done
 
echo "Input (original): $input"
echo "Output (reversed): $reverse"
