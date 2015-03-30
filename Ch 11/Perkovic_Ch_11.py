__author__ = 'Rolando'

#############################################
### Perkovic Intro to Python              ###
#### CH 11: The Web and Search           ####
##### PG 395 Ch 11                      #####
#############################################

from urllib.request import urlopen

response1 = urlopen('http://www.w3c.org/Consortium/facts.html')
print(type(response1))
print(response1.geturl())

for header in response1.getheaders():
    print(header)

html1 = response1.read()
print(type(html1))
html1 = html1.decode()
print(html1)
print(html1.count('Web'))


def get_source(url):
    """ Returns the content of resource specified by url as a string
    """

    response = urlopen(url)
    html = response.read()
    return html.decode()

print(get_source('http://www.google.com'))

from html.parser import HTMLParser

infile = open('w3c.html')
content = infile.read()
infile.close()
parser1 = HTMLParser()
parser1.feed(content)

############
### 11.1 ###
############
print('\nPP 11.1')


def news(url, keywords):
    """ Takes a URL of a news web site and a list of news topics
        and computes the number of occurences of each topic in teh news
    """

    response = urlopen(url)
    html = response.read()
    html = html.decode().lower()

    for key in keywords:
        key_count = html.count(key)
        print('{} appears {} times.'.format(key, key_count))

print(news('http://bbc.co.uk', ['economy', 'climate', 'education', 'news']))


