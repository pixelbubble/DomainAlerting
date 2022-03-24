#!/bin/bash

#To complete
export keyword="google|amazon" #Keywords to complete
mail="hello@world.com" #Email to complete

python3 domaindownload.py | mail -E -s "Domain Alerting $keyword" $mail
