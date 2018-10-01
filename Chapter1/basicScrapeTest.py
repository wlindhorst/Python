from urllib.request import urlopen
html = urlopen('http://somewebsite.com')
print(html.read())