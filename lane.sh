#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "memory, threads ,/plot num ,/farm num, plot prefix, farm prefex"
    exit
fi

chiaexec="/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon/chia"

f_pfx=/farm

if [ -z $5 ]
  then
    p_pfx=/plot
  else
    p_pfx=$5
  fi
echo $p_pfx

if [ -z $6 ]
  then
    f_pfx=/farm
  else
    f_pfx=$6
  fi
echo $f_pfx

chiaexec2="$chiaexec plots create -k 32 -n 1 -b $1 -r $2 -t /plot$3 -d /farm$4 --override-k"

#while sleep 1; do sleep 10s &&
#kill $(ps -ef |grep "/plot$3 "| grep chia |awk '{print $3}')
#rm /plot$3/*.tmp
$chiaexec2 > lane$[$3]-$[$4].txt & echo $! > lane$[$3]-$[$4].dat
#done