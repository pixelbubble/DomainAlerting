sudo python3 domaindownload.py
sudo chown -R ubuntu:ubuntu "$(\ls -1dt ./*/ | head -n 1)" #Your username:username
cd  "$(\ls -1dt ./*/ | head -n 1)" 
egrep "google|amazon" domain-names.txt > result.txt #Keywords to complete
mail -s "Domain Alerting" my@email.com < result.txt #Email to complete
