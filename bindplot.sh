#!/bin/bash

for i in `seq $2 $3`
do
  sudo mount /plot$1 /plot$i -B
  sudo chmod +777 /plot$1
done