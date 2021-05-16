#!/bin/bash
for i in `seq $1 $2`
do
./lane.sh $1 $2 $i
done
