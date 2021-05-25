#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "start end mem threads"
    exit
fi

for i in `seq $1 $2`
do
echo "Starting lane $i" &./lane.sh $3 $4 $i $i &
echo "..spawned .. now waiting.."
sleep 5m
done
