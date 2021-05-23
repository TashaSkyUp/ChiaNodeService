#!/bin/bash
for i in `seq 1 19`;do echo -n $i ; echo $(df /farm$i/.)| tail -n 1; done | grep $(df -P / | tail -n 1 | awk '/.*/ { print $1 }')
