# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
import urllib2
import json
import simplejson


#html = urllib2.urlopen("http://cinerama.com.pe")

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print 'DATA', repr(data)
data_string = json.dumps(data)
print 'JSON:', data_string