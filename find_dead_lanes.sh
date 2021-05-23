#!/bin/bash
find lane*.txt -mmin +60
echo would you like restart some?
read yesno
if [ "$yesno" == "y" ]; then

# full lane
#if [ "Error 1" == "$(cat lane17.txt | tail -n 1 | grep -o 'Error 1')" ]; then echo crap; fi

for line in $( echo $(find lane*.txt -mmin +60)):
do
  echo $line
  num="$(echo $line | grep -o '[0-9]\+')"
  num="$(echo $line |grep -o  'lane[0-9]\+' | grep -o '[0-9]\+')"
  echo $num

  echo $(df /plot$num)
  echo $(df /farm$num)
  echo "$(cat $line | tail -n 1)"
  echo "pids of lane = "$(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
  echo restart?
  read del
  if [ "$del" == "y" ]; then

    echo killing $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    kill $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    rm $line
    sleep 2
    echo result: $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    if [ "$(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')" == "" ]; then
      echo "lane.sh full params"
      read params
      echo starting & ./lane.sh $params > what.txt &
    fi

  fi
  done
fi