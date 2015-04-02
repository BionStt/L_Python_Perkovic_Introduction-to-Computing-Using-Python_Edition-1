__author__ = 'Rolando'

from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin
from re import findall


class Collector(HTMLParser):
    """ Collects hyperlink URLs into a list
    """

    def __init__(self, url):
        """ Initialize parser, url, list, and data
        """
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = ''

    def handle_starttag(self, tag, attrs):
        """ Collect hyperlink URLs in their absolute format
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

# this is only the skeleton for the price match function


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

# This is an example of the fleshed out version of a Newegg price match


# def price_match_newegg(urls, prices):
#     """ Price matches links on Newegg
#     """
#
#     for url in urls:
#         if 'http://www.newegg.com/' in url:
#             resource = urlopen(url)
#             content = resource.read().decode()
#             collector = Collector(url)
#             collector.feed(content)
#             priced = findall('"price":[0-9,]*\.[0-9][0-9]', collector.get_data())
#             for i in range(len(priced)):
#                 priced[i] = eval(priced[i][8:])
#             priced = min(priced)
#             if priced <= prices[urls.index(url)]:
#                 print(url)
#
# links = ['http://www.newegg.com/Product/Product.aspx?'
#          'Item=N82E16824009656&cm_sp=Homepage_HD-_-P2_24-009-656-_-04022015',
#          'http://www.newegg.com/Product/Product.aspx?'
#          'Item=N82E16826106514&cm_sp=Homepage_HD-_-P3_26-106-514-_-04022015',
#          'http://www.newegg.com/Product/Product.aspx?'
#          'Item=N82E16883266608&cm_sp=Homepage_HD-_-P4_83-266-608-_-04022015']
# money = [140.00, 130.00, 400.00]
# print(price_match_newegg(links, money))