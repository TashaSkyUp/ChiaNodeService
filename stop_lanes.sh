#!/bin/bash
for i in `seq $1 $2`
do
kill $(ps -ef |grep "/plot$i"| grep chia |awk '{print $3}')
rm /plot$i/*
done
