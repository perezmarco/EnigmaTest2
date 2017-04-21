from bs4 import BeautifulSoup
import requests

#url = raw_input("Enter a website to extract the URL's from:")
#r = requests.get('http://' + url)
#data = r.text
r2 = requests.get('http://data-interview.enigmalabs.org/companies/West,%20Reichel%20and%20Keebler')
data2 =  r2.text
print data2

class WebScraper(object):

  def __init__(self):
    self.visited = set()
    
  def parse_page(self, url):
    pass

  def _create_json(self, html):
    pass

  def set_root(self, url):
    pass
"""
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
  print url + link.get('href')




idea:
  maintain a set of visited websites
  do BFS starting at the root
    for each page that is not the root
      parse html create json dict
      and write to file
  




"""  

