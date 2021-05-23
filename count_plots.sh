#!/bin/bash
for file in /*/*.plot; do echo $file| grep -o '[-][0-9a-z]\+[.]'|grep -o '[0-9a-z]\+'; done | sort | uniq --count | wc -l