chiaexec="/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon/chia"

rm /plot0/*

for i in 12 13 14 15 16 17 18 19 12 13 14 15
do
  while sleep 1
  do
    $chiaexec plots create -k 32 -n 1 -b $1 -r $2 -t /plot0 -d /farm$i --override-k > laneNvme$i.txt
    sleep 30m
  done
done &
