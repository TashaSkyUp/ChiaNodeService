#!/bin/bash

for nvme in  /dev/nvme???
do
  echo $nvme
  sudo umount $nvme
  for part in p1 p2 p3 p4
  do
    sudo umount $nvme$part
  done

  sudo parted --script $nvme mklabel GPT
  sudo parted  $nvme rm 1
  sudo parted  $nvme rm 2
  sudo parted  $nvme rm 3
  sudo parted  $nvme rm 4
done

for nvme in  /dev/nvme???
do
  sudo parted --script $nvme mkpart primary 1024s  500106752s
  sudo parted --script $nvme mkpart primary 500106753s 1000213504s
done

for nvme in  /dev/nvme???
do
  sudo ./format_xfs.sh $nvme"p1"
  sudo ./format_xfs.sh $nvme"p2"
done
i=0
for nvme in  /dev/nvme???
do
  sudo mkdir /plot$i
  sudo  mount $nvme"p1" /plot$i
  sudo chmod +777 /plot$i
  let "i=i+1"

  sudo mkdir /plot$i
  sudo  mount $nvme"p2" /plot$i
  sudo chmod +777 /plot$i
  let "i=i+1"

done
