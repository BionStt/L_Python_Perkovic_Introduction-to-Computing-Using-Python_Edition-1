__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 11: The Web and Search           ####
##### PG 416 Ch 11 CS                   #####
#############################################

from urllib.request import urlopen, urlretrieve
from html.parser import HTMLParser
from urllib.parse import urljoin
from re import findall, search


class Collector(HTMLParser):
    """ Collects hyperlink URLs into a list
    """

    def __init__(self, url):
        """ Initializes parser, url, and the list
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
                if attr[0] == 'href':   # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':  # collect HTTP URLs
                        self.links.append(absolute)

    def handle_data(self, data):
        """ Collect text data
        """
        self.text += data

    def get_links(self):
        """ Return hyperlink URLs in their absolute format
        """
        return self.links

    def get_data(self):
        """ Return all text data in string format
        """
        return self.text

#################################################################### start of 11.6
### 11.6 ###
############
print('\nPP 11.6')


def frequency(s):
    """ Takes a sting as input and computes the frequency of
        every word in the string and returns a dictionary
        that maps words in the string to their frequency
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
#################################################################### end of 11.6


def analyze(url):
    """ Returns a list of HTTP links in their absolute format,
        in the web page with URL url
    """

    print('Visiting', url)      # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links()    # URLs in the list of links
    #
    # # compute word frequencies
    # content = collector.get_data()
    # freq = frequency(content)
    #
    # # print the frequency of every tet data word in the web page
    # print('\n{:50} {:10} {:5}'.format('URL', 'word', 'count'))
    # for word in freq:
    #     print('{:50} {:10} {:5}'.format(url, word, freq[word]))
    #
    # # print the http links found in web page
    # print('\n{:50} {:10}'.format('URL', 'link'))
    # for link in urls:
    #     print('{:50} {:10}'.format(url, link))
    #
    return urls


def crawl1(url):
    """ Recursive web crawler that calls analyze() on every web page
    """

    # analyze returns a list of hyperlink URLs in web page url
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        try:    # try block because link may not be valid HTML file
            crawl1(link)
        except:             # if an exception is thrown
            pass            # ignore an move on


# print(crawl1('http://reed.cs.depaul.edu/lperkovic/one.html'))
visited2 = set()


def crawl2(url):
    """ A recursive web crawler that calls analyze() on every web page visited,
        and stores pages visited to prevent re-crawling
    """

    # add url to set of visited pages
    global visited2          # while not necessary, warns the programmer
    visited2.add(url)

    # analyse() returns a list of hyperlink URLs in web page url
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited2:
            try:
                crawl2(link)
            except:
                pass

# print(crawl2('http://reed.cs.depaul.edu/lperkovic/one.html'))

#################################################################### start of 11.15
### 11.15 ###
#############
print('\nPP 11.15')

visited_15 = set()


def crawl_15(url, n=2):
    """ A recursive web crawler that calls analyze() on every web page visited,
        stores pages visited to prevent re-crawling,
        and stores crawl depth to prevent crawling deeper than initial n
    """

    if n == 0:
        print("Can't crawl more")
        return

    global visited_15
    visited_15.add(url)

    links = analyze(url)

    for link in links:
        if link not in visited_15:
            try:
                crawl_15(link, n - 1)
            except:
                pass

# print(crawl_15('http://reed.cs.depaul.edu/lperkovic/one.html'))

#################################################################### start of 11.17
### 11.17 ###
#############
print('\nPP 11.17')

visited_17 = set()


def crawl_17(url, host=''):
    """ A recursive web crawler that calls analyze() on every web page visited,
        stores pages visited to prevent re-crawling,
        and only follows links hosted on the same host as that starter page
    """

    if host not in url:
        return None
    if host == '':
        match = search('https?://[^/]+', url)
        host = match.string[match.start():match.end()]
        print(host)

    global visited_17
    visited_17.add(url)

    links = analyze(url)

    for link in links:
        if link not in visited_17:
            try:
                crawl_17(link, host)
            except:
                pass

# print(crawl_17('http://reed.cs.depaul.edu/lperkovic/one.html'))

#################################################################### start of 11.18
### 11.18 ###
#############
print('\nPP 11.18')

visited_18 = set()


def crawl_18(url, starter=''):
    """ A recursive web crawler that calls analyze() on every web page visited,
        stores pages visited to prevent re-crawling, and only follows links contained
        directly or indirectly in the web server file system folder containing the starting page
    """
    if starter not in url:
        return None
    if starter == '':
        starter = url
        print(starter)

    global visited_18
    visited_18.add(url)

    links = analyze(url)

    for link in links:
        if link not in visited_18:
            try:
                crawl_18(link, starter)
            except:
                pass

# print(crawl_18('http://reed.cs.depaul.edu/lperkovic/one.html'))

#################################################################### start of 11.22
### 11.22 ###
#############
print('\nPP 11.22')


def emails(s):
    """ Takes a string as input and returns the set of email addresses appearing in it
    """

    return set(findall('[^@:"><\?\s]+@+[^@:"<>\?\s]+', s))

url1 = 'http://www.cdm.depaul.edu/'
content2 = urlopen(url1).read().decode()
print(emails(content2))

#################################################################### start of 11.23
### 11.23 ###
#############
print('\nPP 11.23')


def price_match_general(urls, prices):
    """ Takes a list of web page addresses and a list of target prices of
        the same list size then prints web page addresses that correspond
        to products whose price was less than the target price
    """

    for url in urls:
        resource = urlopen(url)                     # open url
        content = resource.read().decode()          # read and decode url
        collector = Collector(url)                  # create Parser object
        collector.feed(content)                     # feed content to parser
        priced = findall('\$[0-9,]*\.[0-9][0-9]', collector.get_data())     # filter out price numbers into a list
        for i in range(len(priced)):
            priced[i] = eval(priced[i])             # make price string into a number
        priced = min(priced)                        # get the lowest price
        if priced <= prices[urls.inde(url)]:        # if price on site lower than price on input
            print(url)                              # print price

#################################################################### start of 11.24
### 11.24 ###
#############
print('\nPP 11.24')

visited_email = set()
emails_x = set()


def crawl_email(url, host=''):
    """ A recursive crawler that collects email addresses in the visited
        web pages. The crawler only follows links with the same host as
        the starter page.
    """

    if host not in url:
        return None
    if host == '':
        match = search('https?://[^/]+', url)
        host = match.string[match.start():match.end()]
        print(host)

    global visited_email, emails_x
    visited_email.add(url)

    content = urlopen(url).read().decode()
    found_emails = emails(content)
    emails_x = emails_x.union(found_emails)

    links = analyze(url)

    for link in links:
        if link not in visited_email:
            try:
                crawl_email(link, host)
            except:
                pass

    return emails_x

# print(crawl_email('http://britevisuals.com/'))

#################################################################### start of 11.25
### 11.25 ###
#############
print('\nPP 11.25')

visited_retrieve = set()
base_names = set()

def crawl_retrieve(url, host=''):
    """ Takes a URL and a filename and uses urlretrieve() to copy all the web pages from a
        website, starting from the main web page, to a local folder on the computer
    """

    if host not in url:
        return None
    if host == '':
        match = search('https?://[^/]+', url)
        host = match.string[match.start():match.end()]
        print(host)

    global visited_retrieve, base_names
    visited_retrieve.add(url)

    links = analyze(url)

    filename = search(host + '.+\.', url)
    filename = filename.string[filename.start() + len(host) + 1:filename.end() - 1].replace('/', '+')
    urlretrieve(url, '{}{}'.format(filename, '.html'))
    base_names.add(filename)

    for link in links:
        if link not in visited_retrieve:
            try:
                crawl_retrieve(link, host)
            except:
                pass

    return base_names

print(crawl_retrieve('http://reed.cs.depaul.edu/lperkovic/one.html'))

#################################################################### start of 11.7
### 11.7 ###
############
print('\nPP 11.7')


class Crawler2():
    """ Recursively crawls through HTML links
    """

    def __init__(self):
        """ Initializes set of visited websites
        """
        self.visited = set()

    def analyze(self, url):
        """ Returns a list of links in their absolute format
            in the web page URL
        """
        print('Visiting', url)

        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.get_links()

        content = collector.get_data()
        freq = self.frequency(content)

        # print the frequency of every tet data word in the web page
        print('\n{:50} {:10} {:5}'.format('URL', 'word', 'count'))
        for word in freq:
            print('{:50} {:10} {:5}'.format(url, word, freq[word]))

        # print the http links found in web page
        print('\n{:50} {:10}'.format('URL', 'link'))
        for link in urls:
            print('{:50} {:10}'.format(url, link))

        return urls

    def crawl(self, url):
        """ Recursive web crawler that calls analyze() on every web page visited
        """
        self.visited.add(url)

        links = self.analyze(url)

        for link in links:
            if link not in self.visited:
                try:
                    self.crawl(link)
                except:
                    pass

    def frequency(self, s):
        """ Takes a sting as input and computes the frequency of
            every word in the string and returns a dictionary
            that maps words in the string to their frequency
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

# crawler2 = Crawler2()
# crawler2.crawl('http://reed.cs.depaul.edu/lperkovic/one.html')