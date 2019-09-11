from urllib.request import urlopen    # module for opening the url
from bs4 import BeautifulSoup
import os                             # creating the directory

# html = urlopen("http://wikipedia.org")    # open the url of wikipedia

# print(html.read())                        # read the contents of the page

# bsobj = BeautifulSoup(html.read(), "html.parser")   # read the html and type html parser - store in an obj variable
# print(bsobj.h1)   # filters the h1 tags in the html content


# function for creating directory
def create_project_directory(directory):
    if not os.path.exists(directory):
        print('creating directory ' + directory)
        os.makedirs(directory)

# function for creating queue and crawled


def create_data_files(project_name, base_url):   # creates the file under specific proj and base url- homepage
    queue = os.path.join(project_name, 'queue.txt')   # create file location  path for queue
    crawled = os.path.join(project_name, 'crawled.txt')  # create file location path for crawled
    # validate if the files exist
    if not os.path.isfile(queue):
        write_file(queue, base_url)                      # writes the file with filename and base url(homepage)
    if not os.path.isfile(crawled):
        write_file(crawled, '')       # very first time there everything should be only queue wont have anything crawled


def write_file(path, data):              # path= projname+queue.txt, data=baseurl where to write and what data to write
    with open(path, 'w') as f:           # open the file path in write mode - with keyword ensures closing files easily
        f.write(data)                    # writes the data - deletes the previous content in w mode


def append_to_file(path, data):          # append function for the queue
    with open(path, 'a') as f:
        f.write(data, '\n')              # appends data and moves to next line - no need to close


def delete_file_contents(path):          # delete the file contents
    f = open(path, 'w')
    f.write()                            # w mode empty will erase the contents
    f.close()

# functions to improve the performance rather than searching for the file


def file_to_set(file_name):     # func creating sets - copy contents into set first and then into file
    results = set()             # creating a set
    with open(file_name, 'rt') as f:   # rt - read text mode
        for line in f:                 # for lines in the file operator
            results.add(line.replace('\n', ''))  # add lines to set and replace next line with spaces - since its set
    return results                               # return the set


def set_to_file(links, file_name):  # func to copy set into the text file - links is the set
    with open(file_name, 'w') as f:
        for lin in sorted(links):   # sorts the links passed into the func
            f.write(lin+'\n')       # writes the line to the file



