'''
Created on 01.02.2012

@author: kapitan Nemo
'''
import urllib2, re

log = open("c:\\User\\Shu\\arjlover.log", "r")
log2= open("c:\\User\\Shu\\arjlover2.log", "w")
"""
req = urllib2.Request('http://film.arjlover.net/film/') 
req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; windows NT 5.1; en-GB; rv:1.9.0.3 Gecko/2008092417 Firefox/3.0.3)')
response = urllib2.urlopen(req)
page = response.read()
"""

page = log.read()
page = page.replace("\n", "")

links = re.compile("class=l(.*?)>torrent<").findall(page)

for link in links:
    name = link[link.find("avi.html")+11 :]
    name = name[: name.find("</a>")]
    
    link_http = link[link.find("<td><a href")+13 :]
    link_http = link_http[: link_http.find('"') ]
    
    link_torrent = link[ :]
    link_torrent = link_torrent[: ]
    
    log2.write(name + " http://film.arjlover.net" + link_http +"\n")
