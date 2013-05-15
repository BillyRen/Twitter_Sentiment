import urllib2 as urllib
import json

#proxy_support = urllib.ProxyHandler({'http':'http://127.0.0.1:8087'})
#opener = urllib.build_opener(proxy_support,urllib.HTTPHandler)
#urllib.install_opener(opener)

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
print json.load(response)