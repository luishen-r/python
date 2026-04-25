import urllib.request
import urllib
try:
    site = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
except urllib.error.URLError:
    print('O site não está acessível')
else:
    print(site.read().decode('utf-8'))
    print('O site está acessível')
