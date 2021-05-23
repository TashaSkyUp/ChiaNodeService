#!/bin/bash
find lane*.txt -mmin +60
echo would you like restart some?
read yesno
if [ "$yesno" == "y" ]; then

for line in $( echo $(find lane*.txt -mmin +60)):
do
  echo $line
  num="$(echo $line | grep -o '[0-9]\+')"
  num="$(echo $line |grep -o  'lane[0-9]\+' | grep -o '[0-9]\+')"
  echo $num

  echo $(df /plot$num)
  echo $(df /farm$num)
  echo restart?
  read del
  if [ "$del" == "y" ]; then

    echo killing $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    kill $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    rm $line
    sleep 5
    echo result: $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    if [ "$(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')" == "" ]; then
      echo "lane.sh full params"
      read params
      ./lane.sh $params > null
    fi

  fi
  done
fi