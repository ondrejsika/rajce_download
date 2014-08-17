#!/usr/bin/python

import sys
import os
import urllib
import requests
from pyquery import PyQuery as pq


print 'Rajce download'
print '(c) Ondrej Sika, ondrej@ondrejsika.com'

if len(sys.argv) < 2:
    url = raw_input('Gallery url: ')
else:
    url = sys.argv[1]
    print 'Gallery url: %s' % url

print ''

html = requests.get(url).text
d = pq(html)

images = []
for link in d('a.photoThumb'):
    images.append(pq(link).attr('href'))


downloader = urllib.URLopener()

output = '/tmp/rajce_download/%s' % url.replace('https://', '').replace('http://', '')
os.system('mkdir -p %s' % output)

i = 1
total = len(images)
for img in images:
    to = os.path.join(output, img.rsplit('/', 1)[1])
    print '%s / %s' % (i, total)
    print 'from: %s' % img
    print 'to:   %s' % to
    print ''
    downloader.retrieve(img, to)
    i += 1

