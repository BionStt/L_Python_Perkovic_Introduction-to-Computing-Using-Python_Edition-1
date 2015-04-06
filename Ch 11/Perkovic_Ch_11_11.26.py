__author__ = 'Rolando'

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

class Queue:
    """ A basic Queue class
    """

    def __init__(self, q=list()):
        """ Initialize Queue based on input q, default is empty queue
        """
        self.q = q

    def is_empty(self):
        """ Returns True if queue is empty, false otherwise
        """
        return len(self.q) == 0

    def enqueue(self, item):
        """ Insert item at end of queue
        """
        if type(item) is list:
            return self.q.extend(item)
        else:
            return self.q.append(item)

    def dequeue(self):
        """ Remove and return item at front of queue
        """
        return self.q.pop(0)

    def __eq__(self, other):
        """ Returns True if queues self and other contain the
            same items on the same order, false otherwise
        """
        return self.q == other.q

    def __len__(self):
        """ Returns the number of items in queue
        """
        return len(self.q)

    def __repr__(self):
        """ Return canonical string representation of self
        """
        return 'Queue({})'.format(self.q)


class Collector(HTMLParser):
    """ Collects hyperlink URLs into a list
    """

    def __init__(self, url):
        """ Initializes parser, url, list, and data
        """
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = ''

    def handle_starttag(self, tag, attrs):
        """ Collects hyperlink URLs in their absolute format
        """
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def handle_data(self, data):
        """ Collect text data
        """
        self.data += data

    def get_links(self):
        """ Return hyperlink URLs in their absolute format
        """
        return self.links

    def get_data(self):
        """ Return all text data in string format
        """
        return self.data


def analyze(url):
    """ Returns a list of HTTP links in their absolute format
        in the web page with the url
    """

    print('visiting', url)                      # test
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links()

    return urls


def crawl_queue(url):
    """ A web crawler that uses a breadth-first traversal method to crawl
        through links hosted by the same web server
    """

    visited = set()
    q = Queue([url])

    while len(q) > 0:
        current = q.dequeue()
        if current in visited:
            continue
        visited.add(current)
        links = analyze(current)
        for link in links:
            if link in visited:
                links.remove(link)
        q.enqueue(links)

print(crawl_queue('http://reed.cs.depaul.edu/lperkovic/one.html'))