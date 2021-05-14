#!/bin/bash
for i in `seq 1 12`;
do
    echo item: $i
    sudo umount /plot$i

done

for value in b c d e f
do
sudo sfdisk /dev/sd$value <<EOF
,500115871
,500115871
,
write
EOF
sudo partprobe /dev/sd$value
sudo mkfs.xfs /dev/sd$value$[1] -f -m crc=0 -i maxpct=1 -l size=853b
sudo mkfs.xfs /dev/sd$value$[2] -f -m crc=0 -i maxpct=1 -l size=853b
sudo mkfs.xfs /dev/sd$value$[3] -f -m crc=0 -i maxpct=1 -l size=853b

done

for i in `seq 1 12`;
do
    echo item: $i
    sudo mkdir /plot$i
    sudo chmod +777 /plot$i

done
p=2
for drive in b c d e f
do
let "p=p+1"
sudo mount /dev/sd$drive$[1] /plot$p
let "p=p+1"
sudo mount /dev/sd$drive$[2] /plot$p
done
for i in `seq 1 12`;

do
    echo item: $i
    sudo mkdir /plot$i
    sudo chmod +777 /plot$i

done