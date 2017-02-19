# web-scrapping
get data from bash.org, bashfr

Quick and dirty scripts to get quote datasets. 

import urllib2

# http://bash.org/?browse&p=420
for i in range(1, 420):
    response = urllib2.urlopen('http://bash.org/?browse&p=' + str(i))
    html = response.read()
    print "Reading html page " + str(i) + "/420"

    htmlfile = open("rawhtml/" + str(i) + ".html","w")
    htmlfile.write(html)
    htmlfile.close()
    print "File written on disk"
