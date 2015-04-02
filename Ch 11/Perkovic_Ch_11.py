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

infile1 = open('w3c.html')
content1 = infile1.read()
infile1.close()
parser1 = HTMLParser()
parser1.feed(content1)


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

from re import search

match1 = search('e+', 'beetbtbelt?bet, best')
print(type(match1))
print(match1.start())
print(match1.end())
print(match1.string)
print(match1.string[match1.start():match1.end()])

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

# print(news('http://bbc.co.uk', ['economy', 'climate', 'education', 'news']))

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
for link1 in collector1.get_links():
    print(link1)
print(collector1.get_data())

############
### 11.4 ###
############
print('\nPP 11.4')

# 11.4 does not ask for code

############
### 11.5 ###
############
print('\nPP 11.5')

# pattern_a5 = 'a[abc]c'
# pattern_b5 = 'abc|xyz'
# pattern_c5 = 'a[b]*'
# pattern_d5 = '[a-z]+'
# pattern_e5 = '[a-zA-Z]*oe[a-zA-Z]*'
# pattern_f5 = '<[^>]*>'

############
### 11.6 ###
############
print('\nPP 11.6')

# 11.6 done in Ch_11_CS

############
### 11.7 ###
############
print('\nPP 11.7')

# 11.7 done in CH_11_CS

############
### 11.8 ###
############
print('\nPP 11.8')

# 11.8 does not ask for code

############
### 11.9 ###
############
print('\nPP 11.9')

# pattern_a = '[a-zA-Z]*'[a-zA-Z]*'
# pattern_b = '[a-z]+[a-z]+[a-z]+'
# pattern_c = '^0[0-9]+'
# pattern_d = '[0-9]+'
# pattern_e = '\-[0-9]+'
# pattern_f = '\-?[0-9]+
# pattern_g = '\-?[0-9]+\.[0-9]+

#############
### 11.10 ###
#############
print('\nPP 11.10')

infile1 = open('frankenstein.txt')
content1 = infile1.read()
infile1.close()

# a
print(findall('Frankenstein', content1))
# b
print(findall('[0-9]+', content1))
# c
print(findall('[a-zA-Z]*ible', content1))
# d
print(findall('[A-Z][a-zA-Z]*y', content1))
# e
print(findall('horror of[ a-z]*[ a-z]*', content1))
# f
print(findall('[a-zA-Z]+ death', content1))
# g
# print(findall('[^.?!]*?laboratory[^.?!]*\.', content1))

#############
### 11.11 ###
#############
print('\nPP 11.11')

print(findall('[^@\s]+@[^@]+\.[^@\s]+', 'hi im john99@yahoo.com suck my dick'))

#############
### 11.12 ###
#############
print('\nPP 11.12')

google = get_source('http://www.google.com')

print(findall('href="[^"]+"', google))

#############
### 11.13 ###
#############
print('\nPP 11.13')

print(findall('\$[0-9,]*\.[0-9][0-9]', 'He paid a total of $1,099.29, and received $13.29 as change.'))

#############
### 11.14 ###
#############
print('\nPP 11.14')

print(findall('"https?://[^"]+"', google))

#############
### 11.15 ###
#############
print('\nPP 11.15')

# 11.15 done in Ch_11_CS

#############
### 11.16 ###
#############
print('\nPP 11.16')

# 11.16 does not ask for code

#############
### 11.17 ###
#############
print('\nPP 11.17')

# 11.17 done in Ch_11_CS

#############
### 11.18 ###
#############
print('\nPP 11.18')

# 11.18 done in Ch_11_CS

#############
### 11.19 ###
#############
print('\nPP 11.19')

infile1 = open('frankenstein.txt')
content1 = infile1.read()
infile1.close()

import time


def timing(func, n1, n2):
    """ Runs func on input returned by build_input
    """

    start = time.time()
    func(n1, n2)
    end = time.time()

    return end - start


def timing_analysis(func, n1, n2, runs):
    """ Prints average runtime of function func on input of
        size start, start+inc, start+(inc*2), ..., up to stop
    """

    acc = 0.0

    for i in range(runs):
        acc += timing(func, n1, n2)

    format_str = 'Run time of {}(\'{}\', \'{}\') is {:.7f} seconds.'
    print(format_str.format(func.__name__, n1, n2, acc / runs))


# replace


def test_replace(n1, n2):
    """ Removes periods
    """

    global content1

    return content1.replace(n1, n2)


print(timing_analysis(test_replace, '.', ' ', 10))

# translate


def test_translate(n1, n2):
    """ Translates content to remove periods
    """

    global content1

    table = str.maketrans(n1, n2)
    result = content1.translate(table)

    return result


# print(timing_analysis(test_translate, '.', ' ', 10))

# regex


def test_regex(n1, n2):
    """ Use regex to remove periods
    """

    global content1

    pattern = '[^\\' + n1 + ']*\\' + n1
    strings = findall(pattern, content1)

    return n2.join(strings)


print(timing_analysis(test_regex, '.', ' ', 10))

#############
### 11.20 ###
#############
print('\nPP 11.20')


def scary(file):
    """ Takes a text file as input and returns a dictionary
        of all the words in the file using regex
    """

    infile = open(file)
    content = infile.read()
    infile.close()

    strings = sorted(list(set(findall('[a-z]+', content.lower()))))

    outfile = open('scary_dictionary.txt', 'w')
    for i in strings:
        outfile.write(i + '\n')
    outfile.close()


scary('frankenstein.txt')


#############
### 11.21 ###
#############
print('\nPP 11.21')


def get_content(url):
    """ Takes a URL as input and prints only the text data content of the
        associated web page (no tags).
    """

    response = urlopen(url)
    html = response.read()
    html = html.decode()

    collector = Collector(url)
    collector.feed(html)
    content = collector.get_data()

    content = content.split('\n')
    for i in content:
        content[content.index(i)] = i.strip()

    counter = 0
    while counter < len(content) - 1:
        if content[counter] == content[counter + 1]:
            content.pop(counter)
        else:
            counter += 1

    content = '\n'.join(content)

    return content

print(get_content('http://www.nytimes.com/'))