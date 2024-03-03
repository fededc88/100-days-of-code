from bs4 import BeautifulSoup

import urllib
import urllib.request

url = 'https://raw.githubusercontent.com/BigDataGal/Data-Mania-Demos/master/IoT-2018.html'

with urllib.request.urlopen(url) as response:
    bs_obj = BeautifulSoup(response.read(), "lxml")

print(bs_obj)
