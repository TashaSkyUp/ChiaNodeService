#memory, threads ,/plot num ,/farm num
chiaexec="/usr/lib/chia-blockchain/resources/app.asar.unpacked/daemon/chia"

while sleep 1; do sleep 10s &&
kill $(ps -ef |grep /plot$3| grep chia |awk '{print $3}')
rm /plot$3/*
nohup $chiaexec plots create -k 32 -n 1 -b $1 -r $2 -t /plot$3 -d /farm$4 --override-k > lane$3.txt; done &
