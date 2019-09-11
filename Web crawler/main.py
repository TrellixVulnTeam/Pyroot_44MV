from demo import *   # demo file contents
from domain import *  # domain file contents
from spyder import Spyder # spyder class contents
import threading  # for multi threading
from queue import Queue

PROJECT_NAME = 'thesite'
HOMEPAGE = 'https://www.catalysts.cc/en/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()   # in built data structure
Spyder(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# functions crawl and multi threading are interlinked


def crawl():   # crawling implementation
    queued_links = file_to_set(QUEUE_FILE)   # func returns a set and is stored in queued_links
    if len(queued_links) > 0:
        print(str(len(queued_links)) + '-Links in the queue file')
        create_jobs()  # multi threading


def create_jobs():  # multi threading implementation
    for link in file_to_set(QUEUE_FILE):  # file_to_set(queue.txt) returns a set
        queue.put(link)
        queue.join()
        crawl()     # links/urls to be crawled


def create_workers():  # threads
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)   # assigning the work function to the threads
        t.daemon = True   # daemon process
        t.start()         # starts the thread


def work():
    while True:
        url = queue.get()          # gets the url from the queue
        Spyder.crawl_page(threading.current_thread().name, url)  # crawl_page from spyder file
        queue.task_done()


create_workers()   # function call to threads
crawl()            # function call to crawl the links

