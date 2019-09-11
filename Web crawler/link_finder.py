from urllib import parse            # to parse
from html.parser import HTMLParser   # for html parser


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url     # home page
        self.page_url = page_url     # links in the homepage 
        self.links = set()            # storing links in the form of sets

    def error(self, message):     # function for error response
        pass

    def handle_starttag(self, tag, attrs):  # inbuilt function to handle the start tag in the html
        # print(tag)
        if tag == 'a':   # identifying the link tag in html
            for (attribute, value) in attrs:
                if attribute == 'href':   # href is the link attribute in the html
                    url = parse.urljoin(self.base_url, value)  # join the value of link with baseurl to get complete url
                    self.links.add(url)

    def page_links(self):
        return self.links
