#!/bin/bash
########################
echo "Unmounting"
unmdadm(){
    sudo mdadm --stop md0 md1
    sudo mdadm --remove /dev/md0
    sudo mdadm --remove /dev/md1

    sudo mdadm --stop md126 md127
    sudo mdadm --remove /dev/md126
    sudo mdadm --remove /dev/md127
}
for i in `seq 1 12`;
do
    echo item: $i
    sudo umount /plot$i

done
########################
echo "Partioning"

for value in b c d e f g h
do
sudo parted --script /dev/sd$value mklabel GPT
sudo parted  /dev/sd$value rm 1
sudo parted  /dev/sd$value rm 2
sudo parted  /dev/sd$value rm 3
sudo parted  /dev/sd$value rm 4
done

for value in b c d e f g h
do
sudo parted --script /dev/sd$value mkpart primary 2048s  500119551s
sudo parted --script /dev/sd$value mkpart primary 500119552s 4TB
sudo parted --script /dev/sd$value mkpart primary 500119552s 2TB
done

##########################
for value in b c d e f g h
do
echo "Formatting"
sudo partprobe /dev/sd$value
sudo mkfs.xfs /dev/sd$value$[1] -f -m crc=0 -i maxpct=1 -l size=853b
unmdadm
sudo mkfs.xfs /dev/sd$value$[2] -f -m crc=0 -i maxpct=1 -l size=853b
done
##########################
#sleep 10
#echo "spare space to raid 0 :sda+sdb"
#sudo mdadm --create /dev/md0 -l 0 -n 2 /dev/sda5 /dev/sdb2
#echo "spare space to raid 0 :remainder"
#sudo mdadm --create /dev/md1 -l 5 -n 7 /dev/md0 /dev/sdc2 /dev/sdd2 /dev/sde2 /dev/sdf2 /dev/sdg2 /dev/sdh2

echo "Mounting etc.."
for i in `seq 1 8`;
do
    echo item: $i
    sudo mkdir /plot$i
    sudo chmod +777 /plot$i
    sudo mkdir /farm$i
    sudo chmod +777 /farm$i
done

sudo mount /dev/sda4 /plot1
p=12

for drive in b c d e f g h
do
sudo mount /dev/sd$drive$[1] /plot$p
sudo mount /dev/sd$drive$[2] /farm$p
let "p=p+1"
done

for i in `seq 1 8`;

do
    echo item: $i
    sudo chmod +777 /plot$i
    sudo chmod +777 /farm$i
done

#sudo mkfs.ext4 /dev/md0
#sudo mkfs.ext4 /dev/md1
sudo mkdir /farm
sudo chmod +777 /farm
sudo mount /dev/md1 /farm