import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
position = input('Enter position: ')
position = int(position)
count = int(count)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
links = list()
tags = soup('a')
for tag in tags:
    # you need to convert it into string so that it can be appended in to links
    links.append(str(tag.get('href', None)))
print('Retrieving:', url)
print('Retrieving:', links[position-1])
nextlink = links[position-1]

counter = 1
# when the counter is equal to 4 it will break from the body of the loop
while counter < count:
    # we need to repeate the same process as above but with the newlink
    html = urllib.request.urlopen(nextlink, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    links = list()

    tags = soup('a')
    for tag in tags:
        links.append(str(tag.get('href', None)))
    print('Retrieving:', links[position-1])
    nextlink = links[position-1]
    counter = counter + 1
