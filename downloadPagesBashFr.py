import urllib2

for i in range(1, 723):
    response = urllib2.urlopen('https://danstonchat.com/browse/' + str(i) + '.html')
    html = response.read()
    print "Reading html page " + str(i) + "/723"

    htmlfile = open("rawdatasetsbashfr/" + str(i) + ".html","w")
    htmlfile.write(html)
    htmlfile.close()
    print "File written on disk"
