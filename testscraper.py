import requests
import time
from bs4 import BeautifulSoup

webpage = "http://www.styleforum.net/t/164384/the-waywt-discussion-thread/117645"

r = requests.get(webpage)
soup = BeautifulSoup(r.content)

imageURLs = soup.find_all('a')

for link in imageURLs:
	print link

def check_valid_url(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content)

	divs = soup.find_all( 'div', { "class" : "post-header shazam" })

	# code can be simplified and print statements can be removed
	if (len(divs) != 0):
		print("returning true")
		return True

	print("returning false")
	return False



check_valid_url(webpage)




