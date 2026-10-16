#!/bin/bash
n=$1; shift; s=$(date +%s%N); bash -c "$*" >/tmp/tm_$n.log 2>&1; r=$?; e=$(( ($(date +%s%N)-s)/1000000 )); echo -e "$n\t${e}ms\texit=$r" | tee -a times.tsv
