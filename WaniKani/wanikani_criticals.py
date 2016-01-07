#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2

u = urllib2.urlopen('https://www.wanikani.com/api/user/<YOUR_API_KEY>/critical-items/85')
data = u.read()
data = json.loads(data)
data = [k for k in data['requested_information'] if k['character']][:5]

colors = {
  'radical': '#0093dd',
  'kanji': '#dd0093',
  'vocabulary': '#9300dd'
}

url_prefix = {
  'radical': 'radicals',
  'kanji': 'kanji',
  'vocabulary': 'vocabulary'
}

if not data:
  print "やった!"
else:
  print " ".join([k['character'] for k in data]).encode('utf-8')
  print "---"
  print "\n".join(["%s - %s%s | color=%s | href=https://www.wanikani.com/%s/%s" % (
    k['character'],
    k['meaning'],
    " - " + k[k.get('important_reading', 'kana')] if k['type'] in ('vocabulary', 'kanji') else '',
    colors[k['type']],
    url_prefix[k['type']],
    k['character'] if k['character'] else k['meaning']) for k in data]).encode('utf-8')
