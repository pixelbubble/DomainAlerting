#!/usr/bin/env python3

import base64
import os
import re
import requests

from datetime import datetime, timedelta
from io import BytesIO
from zipfile import ZipFile

if 'keyword' not in os.environ:
    exit('ERROR: Missing \'keyword\' Environment Variable')

keywords = re.split(r'[^a-z0-9-]', os.environ['keyword'])

for i in range(4):
    f = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') + '.zip'
    try:
        r = requests.get(f'https://www.whoisds.com/whois-database/newly-registered-domains/{base64.b64encode(f.encode()).decode()}/nrd')
        z = ZipFile(BytesIO(r.content))
        for l in z.open('domain-names.txt').readlines():
            if not re.search('({})'.format('|'.join(keywords)), l.decode()):
                continue
            print(l.decode().strip())
        break
    except:
        pass
