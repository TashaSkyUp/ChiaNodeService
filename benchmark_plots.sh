#!/bin/bash
for i in `seq $1 $2`
do
  echo $i
  for t in `seq 1 $3`
  do
    for tt in `seq 1 $4`
    do
      testfile=/plot$i/tmp.tmp$t
      dd if=/dev/zero of=$testfile bs=2G count=1 oflag=dsync && rm $testfile &
    done
  done
  #sleep 10
  #for t in `seq 1 $3`
  #do
    #testfile=/plot$i/tmp.tmp$t
    #rm $testfile$t
  #done



done