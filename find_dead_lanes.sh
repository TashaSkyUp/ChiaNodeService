#!/bin/bash
find lane*.txt -mmin +60
echo would you like restart some?
read yesno
if [ "$yesno" == "y" ]; then

for line in $( echo $(find lane*.txt -mmin +60)):
do
  echo $line
  num="$(echo $line | grep -o '[0-9]\+')"
  echo $num
  echo restart?

  read del
  if [ "$del" == "y" ]; then

    echo killing $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')
    kill $(ps -ef |grep "/plot$num "| grep chia |awk '{print $3}')

  fi
  done
fi