import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
import random

query = "what is a python module"

user_agents = ['Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
               'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
               'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36']

r = requests.get('https://www.duckduckgo.com/html/?q=site:stackoverflow.com%20what is a {0}'.format(query),
                 headers={'user-agent': random.choice(user_agents)})
page_html = r.text

soup = BeautifulSoup(page_html)

links = soup.find_all('a')

def pick_first_answer(links):
    so_links = OrderedDict()
    so_regex = re.compile('questions/\d+/')
    for link in links:
        if not link.has_attr('href'):
            pass
        else:
            if so_regex.search(link['href']):
                    so_links[link.text] = link
    first_link = so_links.keys()[0]

    return so_links[first_link]

print pick_first_answer(links)
