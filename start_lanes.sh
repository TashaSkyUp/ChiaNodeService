#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "start end mem threads"
    exit
fi

for i in `seq $1 $2`
do
./lane.sh $3 $4 $i $i
sleep 5m
done
