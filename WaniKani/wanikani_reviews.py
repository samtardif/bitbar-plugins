#!/usr/bin/env python

import json
import urllib2

u = urllib2.urlopen('https://www.wanikani.com/api/user/<YOUR_API_KEY>/study-queue')
data = u.read()
data = json.loads(data)

notifications = data['requested_information']['lessons_available'] + data['requested_information']['reviews_available']
print "WK [%s]|color=#e74c3c" % ("-" if notifications == 0 else str(notifications),)
print "---"
print "Lessons: %d | href=https://www.wanikani.com/lesson/session" % data['requested_information']['lessons_available']
print "Reviews: %d | href=https://www.wanikani.com/review/session" % data['requested_information']['reviews_available']
