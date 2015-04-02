__author__ = 'Rolando'

from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin
from re import findall

class Collector(HTMLParser):
    """ Collects hyperlink URLs into a list
    """

