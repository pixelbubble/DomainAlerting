#!/bin/bash

#To complete
keyword="google|amazon" #Keywords to complete
mail="hello@world.com" #Email to complete

sudo python3 domaindownload.py
cd  "$(\ls -1dt ./*/ | head -n 1)" 
egrep $keyword domain-names.txt > result.txt
mail -s "Domain Alerting $keyword" $mail < result.txt
