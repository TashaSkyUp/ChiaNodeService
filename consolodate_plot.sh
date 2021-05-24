#!/bin/bash
if [ "$1" == "" ]; then
  echo "consolidate_plot /targetfarm"
  out_farm=/farm2
fi

echo "continuing with $out_farm"

dest_free=$(df -Ph $out_farm | tail -1 | awk '{print $4}')

# get one file name in farm dir with path

file="$(stat -f -c "%n" $out_farm/*.plot |tail -n 1)"

echo $file
