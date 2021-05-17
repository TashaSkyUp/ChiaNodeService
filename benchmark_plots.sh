#!/bin/bash

p=13

for i in `seq 12 20`
do
if=/dev/zero of=/plot$((i))/tmp.tmp bs=1G count=1 oflag=dsync
done