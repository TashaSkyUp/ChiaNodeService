#!/bin/bash
if [ "$1" == "" ]; then
  out_farm=/farm2
fi
file="$(stat -f -c "%n" $out_farm/*.plot |tail -n 1)"
echo $file
