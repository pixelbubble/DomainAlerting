#!/usr/bin/env python3

# Libraries
import re
import time
import requests
import os
import shutil
from urllib.request import urlopen
import zipfile
from datetime import datetime, timedelta

#Path directories
mainDirectory = os.path.dirname(os.path.realpath(__file__)) + '/'
otherDirectory = mainDirectory + 'database'

#Main function
def NDDRequest():
	html = urlopen("https://whoisds.com/newly-registered-domains")
	text = html.read()
	plaintext = text.decode('utf8')
	links = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
	r = re.compile("https:\/\/whoisds\.com\/\/whois-database\/newly-registered-domains\/.+=\/nrd")
	newlist = list(filter(r.match, links))
	url = newlist[1]
	request = requests.get(url, allow_redirects=True)
	open("database","wb").write(request.content)
	todayDate = datetime.today() - timedelta(days=1)
	yesterdayDate = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", str(todayDate))
	todayDate = yesterdayDate[0]
	dailyDirectory = mainDirectory + todayDate
	try:
		with zipfile.ZipFile(otherDirectory, 'r') as zip_ref:
			if not os.path.exists(dailyDirectory):
   				os.makedirs(dailyDirectory)
			zip_ref.extractall(dailyDirectory)
		if os.path.exists(otherDirectory):
	  		os.remove(otherDirectory)
		else:
			pass
	except:
		pass

NDDRequest()
