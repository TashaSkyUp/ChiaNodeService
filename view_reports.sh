for file in $(find "." -name "lane*.txt" -size +205900c);
 do
   plotnum=$(echo $file |grep -o '[0-9]\+'| head -n 1)
   echo $plotnum
   df /plot$plotnum | tail -n 1 | grep -o '[0-9a-z]\+ ' | tail -n 1
   #plot=$(cat $file |head -n 10| grep "/plot"|grep -o '/plot[0-9]\+': head -n 1)
   #echo $plot
   cat $file |head -n 10| grep "threads"
   cat $file |head -n 10| grep "Buffer"
   cat $file |tail -n 10| grep "Total time"
   echo ""
 done
