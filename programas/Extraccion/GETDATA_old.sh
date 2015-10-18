#!/bin/bash
symbols=$1

###FECHAS###
#desde
A='00'
B='04'
C='2000'
#hasta
D='11'
E='28'
F='2001'
#############
path=$(pwd)
for line in `cat $symbols` 
do
  echo $line
  wget "http://real-chart.finance.yahoo.com/table.csv?s=%5E${line}&amp;a=${A}&amp;b=${B}&amp;c=${C}&amp;d=${D}&amp;e=${E}&amp;f=${F}&amp;g=d&amp;ignore=.csv";
  tac "table.csv?s=${line}&amp;a=${A}&amp;b=${B}&amp;c=${C}&amp;d=${D}&amp;e=${E}&amp;f=${F}&amp;g=d&amp;ignore=.csv" > ${line}.csv
  rm "table.csv?s=${line}&amp;a=${A}&amp;b=${B}&amp;c=${C}&amp;d=${D}&amp;e=${E}&amp;f=${F}&amp;g=d&amp;ignore=.csv"
done


