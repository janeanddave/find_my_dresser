#!/usr/bin/python

import sys
from xml.dom import minidom
import urllib2

if len(sys.argv) == 1:
    print 'You must enter a search string!'
    sys.exit()

def gettext(node):
    nodelist = node.childNodes
    rc = []
    for n in nodelist:
        if n.nodeType == n.TEXT_NODE:
            rc.append(n.data)
    return ''.join(rc)

def search(search_string):
    print 'You searched for "%s"!' % (search_string)
    url = 'http://sfbay.craigslist.org/search/sss?format=rss&query=%s' % (search_string)
    print url

    response = urllib2.urlopen(url)

    if response.getcode() != 200:
        print 'Request failed with %s' % (response.getcode())
        return

    xml = response.read()

    results = minidom.parseString(xml)

    print results

    items = results.getElementsByTagName('item')

    print len(items)

    for item in items:
        item_url = item.getElementsByTagName('link')
        print gettext(item_url[0])

        # import pdb; pdb.set_trace()

search(sys.argv[1])