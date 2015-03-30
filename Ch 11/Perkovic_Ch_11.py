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


class LinkParser(HTMLParser):
    """ HTML doc parser that prints values of
        href attributes in anchor start tags
    """

    def handle_starttag(self, tag, attrs):
        """ Print value of href attribute if any
        """
        if tag == 'a':
            # search for href attribute and print its value
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])


infile1 = open('links.html')
content1 = infile1.read()
infile1.close()
linkparser1 = LinkParser()
linkparser1.feed(content1)

rsrcel = urlopen('http://www.w3.org/Consortium/mission.html')
content1 = rsrcel.read().decode()
linkparser1 = LinkParser()
linkparser1.feed(content1)

from urllib.parse import urljoin

url1 = 'http://www.w3.org/Consortium/mission.html'
relative1 = '/Consortium/contact.html'
print(urljoin(url1, relative1))

from re import findall

print(findall('best', 'beetbtbelt?bet, best'))
print(findall('be.t', 'beetbtbelt?bet, best'))
print(findall('be?t', 'beetbtbelt?bet, best'))
print(findall('be*t', 'beetbtbelt?bet, best'))
print(findall('be+t', 'beetbtbelt?bet, best'))

print(findall('e+', 'beeeetbet bt'))  # if the regular expression matches 2 sub-strings
                                      # such that one is contained within the other, the
                                      # function will match  the longer substring only

print(findall('[^bt]+', 'beetbtbelt?bet, best'))
print(findall('[bt]+', 'beetbtbelt?bet, best'))

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

############
### 11.2 ###
############
print('\nPP 11.2')


class MyHTMLParser(HTMLParser):
    """ HTML doc parser that prints only start and end
        tags of html files with appropriate indentation
    """

    def __init__(self):
        """ Initializes parser and indentation
        """
        HTMLParser.__init__(self)
        self.indent = 0
        self.excluded_tags = {'p', 'br'}

    def handle_starttag(self, tag, attrs):
        """ Print start tag if any
        """
        if tag not in self.excluded_tags:
            print('{}{} start'.format(' ' * self.indent, tag))
            self.indent += 4

    def handle_endtag(self, tag):
        """ Print the end tag if any
        """
        if tag not in self.excluded_tags:
            self.indent -= 4
            print('{}{} end'.format(' ' * self.indent, tag))

infile1 = open('w3c.html')
content1 = infile1.read()
infile1.close()
myparser1 = MyHTMLParser()
myparser1.feed(content1)

############
### 11.3 ###
############
print('\nPP 11.3')


class Collector(HTMLParser):
    """ Collects hyperlink URLs into a list
    """

    def __init__(self, url):
        """ Initializes parser, the url, and a list
        """
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

        self.text = ''

    def handle_starttag(self, tag, attrs):
        """ Collects hyperlink URLs in their absolute format
        """
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':  # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':  # collect HTTP URLs
                        self.links.append(absolute)

    def handle_data(self, data):
        """ Collect data
        """
        self.text += data

    def get_links(self):
        """ Return hyperlinks URLs in their absolute format
        """
        return self.links

    def get_data(self):
        """ Return all text data in a string
        """
        return self.text

url1 = 'http://www.w3.org/Consortium/mission.html'
resource1 = urlopen(url1)
content1 = resource1.read().decode()
collector1 = Collector(url1)
collector1.feed(content1)
for link in collector1.get_links():
    print(link)
print(collector1.get_data())

############
### 11.4 ###
############
print('\nPP 11.4')


def frequency(s):
    """ Takes a string as input, compute the frequency if every word
        in the string, and returns a dictionary that maps words in
        the string to their frequency
    """
    pattern = '[a-zA-Z]+'
    words = findall(pattern, s)
    dictionary = {}

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary

content1 = 'The pure and simple truth is\
            rarely pure and never simple'

print(frequency(content1))