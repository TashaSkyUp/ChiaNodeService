#!/bin/bash
for i in `seq $1 $2`
do
  echo $i
  testfile=/plot$((i))/tmp.tmp
  dd if=/dev/zero of=/$testfile$((1)) bs=$((1))G count=1 oflag=dsync &
  dd if=/dev/zero of=/$testfile$((1)) bs=$((1))G count=1 oflag=dsync &
  dd if=/dev/zero of=/$testfile$((1)) bs=$((1))G count=1 oflag=dsync
  rm $testfile$((1))
  rm $testfile$((2))
  rm $testfile$((3))

done