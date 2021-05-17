#!/bin/bash

p=13

for i in `seq 12 20`
do
dd if=/dev/zero of=/plot$((i))/tmp.tmp bs=$((1))G count=1 oflag=dsync
dd if=/dev/zero of=/farm$((i))/tmp.tmp bs=$((1))G count=1 oflag=dsync
done