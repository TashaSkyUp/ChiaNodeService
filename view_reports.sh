for file in $(find "." -name "lane*.txt" -size +205900c);
 do
   plotnum=$(echo $file |grep -o '[0-9]\+'| head -n 1)
   echo $plotnum
   df /plot$plotnum | tail -n 1 | grep -o '[0-9a-z]\+ ' | head -n 1
   cat $file |head -n 7| tail -n 3
   cat $file |tail -n 5|head -n 2
   echo ""
 done
