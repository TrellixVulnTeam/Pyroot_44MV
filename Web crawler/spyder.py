from urllib.request import urlopen
from link_finder import LinkFinder # accessing LinkFinder class
from demo import *      # accessing demo file
from domain import *    # accessing domain file


class Spyder():
    # variables declared here instead of init - these variables will be shared by multiple instances of the spyder class
    # Multithreading

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        # intializing the variables declared above
        Spyder.project_name = project_name
        Spyder.base_url = base_url
        Spyder.domain_name = domain_name
        Spyder.queue_file = Spyder.project_name + '/queue.txt'     # file name
        Spyder.crawled_file = Spyder.project_name + '/crawled.txt' # file name
        self.boot()                          # function to boot up to create the text files and project
        self.crawl_page('First spyder', Spyder.base_url)  # function to crawl the given base url(homepage)

    @staticmethod     # no need of the class to be instantiated while calling this method
    def boot():       # boot function definition - boots the creation of basics for the webcrawler

        create_project_directory(Spyder.project_name)  # create the directory
        create_data_files(Spyder.project_name, Spyder.base_url)  # creates the file queue and crawled.txt
        Spyder.queue = file_to_set(Spyder.queue_file)            # file_to_set(Spyder.project_name + '/queue.txt')
        Spyder.crawled = file_to_set(Spyder.crawled_file)        # Nothing would be written on this call in the func

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spyder.crawled:     # validate if the page is already crawled
            print(thread_name + '-Now crawling-' + page_url)
            print('Queue-' + str(len(Spyder.queue)) +
                  '|Crawled-' + str(len(Spyder.crawled)))  # printing the length of the sets
            Spyder.add_links_to_queue(Spyder.gather_links(page_url)) # gather the links first and then add them to queue
            Spyder.queue.remove(page_url)   # removes the link from queue and add to be crawled
            Spyder.crawled.add(page_url)    # add the link to be crawled from queue
            Spyder.update_files()           # update the text files with new sets of links

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        # validate data contains only html and text
        try:
            response = urlopen(page_url)    # open the page url
            if 'text/html' in response.getheader('Content-Type'):  # validates the response header has only text/html
                html_bytes = response.read()   # reads the page url
                html_string = html_bytes.decode("utf-8")  # decodes the bytes into string
            finder = LinkFinder(Spyder.base_url, page_url)  # arguements for the LinkFinder class
            finder.feed(html_string)      # feeds and segregates start tag, attribute, value etc in the link passed
        except Exception as e:   # exception block
            print(str(e))
            return set()
        return finder.page_links()  # return the found links

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spyder.queue) or (url in Spyder.crawled):  # validates if the links are in queue or crawled
                continue
            if Spyder.domain_name != get_domain_name(url):     # validates the domain name
                continue
            Spyder.queue.add(url)      # adds to the set - Spyder.queue = file_to_set(Spyder.queue_file)

    @staticmethod
    def update_files():
        set_to_file(Spyder.queue, Spyder.queue_file)   # queue=file_to_set(Spyder.queue_file)returns set queue_file= txt
        set_to_file(Spyder.crawled, Spyder.crawled_file)  # the crawled file










