#!/bin/bash
sudo apt intsall lvm2 -y
sudo apt install f2fs -y

sudo umount /dev/NVMEPLOTS/nvme1
for i in `seq 0 11`
do
  sudo umount /plot$i
done
sudo umount /dev/NVMEPLOTS/nvme1
for i in `seq 0 11`
do
  sudo umount /plot$i
done
sudo vgremove NVMEPLOTS
sudo pvremove  /dev/nvme*

sudo pvcreate /dev/nvme0n1
sudo vgcreate NVMEPLOTS /dev/nvme0n1
sudo lvcreate -l +100%FREE NVMEPLOTS -n nvme1

for i in `seq 1 10`
do
  sudo echo nvme"$i"n1
  sudo pvcreate /dev/nvme"$i"n1
  sudo vgextend /dev/NVMEPLOTS /dev/nvme"$i"n1
  sudo lvextend -l +100%FREE /dev/NVMEPLOTS/nvme1 /dev/nvme"$i"n1
done

sudo rm /plot0 -R
sudo mkdir /plot0
sudo umount /plot0

sudo mkfs.xfs /dev/NVMEPLOTS/nvme1 -f
sudo mount /dev/NVMEPLOTS/nvme1 /plot0
sudo chmod +777 /plot0
