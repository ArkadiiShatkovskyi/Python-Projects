import urllib.request
from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.error import URLError
import copy
import sys


first_arg = sys.argv[1]

global_url = sys.argv[1]

key = 'href'
result = dict()
 
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.isTitle = 0
		self.links = []
		self.title = ''

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			attr = dict(attrs)
			self.links.append(attr)
		elif tag == 'title':
			self.isTitle = 1
		else:
			return
	def handle_endtag(self, tag):
		if tag == 'title':
			self.isTitle = 0

	def handle_data(self, data):
		if self.isTitle:
			self.title = data
	
def getWeb(url):
	html = openUrl(url)
	parser = MyHTMLParser()
	parser.links = []
	parser.feed(str(html))
	tempLinks = copy.deepcopy(parser.links)
	parser.links = []
	tempLinks = correctUrls(copy.deepcopy(tempLinks))
	if html is not '':
		addResult(url, tempLinks, parser.title)
		parser.title = ''

	for link in tempLinks:
		if link.get(key) not in result:
			getWeb(link.get(key))
	return result

def openUrl(url):
	try:
		with urllib.request.urlopen(url) as response:
			html = response.read()
			return html
	except URLError:
		removeWrongURL(url)
		sys.stderr.write("Server do not deployed or exist!")
	return ''

def removeWrongURL(url):
	for k in result.keys():
		helpDict = []
		t = result[k]['Title']
		for link in result[k]['Links']:
			if link != url:
				helpDict.append(link)
		sub = result.get(k)
		del sub['Links']
		result[k] = {'Title': t, 'Links': {x for x in helpDict}}
				

def checkUrl(page):
	for ulr in result:
		if page == url.get(page):
			return true
	return false

def correctUrls(linksTemp):
	for l in linksTemp:
		if global_url not in l[key]:
			l[key] = global_url + l.get(key)
	return linksTemp

def addResult(page, urlLinks, title):
	result[page] = {'Title': title,
			'Links': {x[key] for x in urlLinks},
			}

if __name__ == "__main__":
	getWeb(first_arg)
	print(result)