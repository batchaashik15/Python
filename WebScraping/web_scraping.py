''''
A simple web scraping script to understand how it works
'''

import requests
import bs4

# CODE HERE
author_list = []
base_url = "https://quotes.toscrape.com/page/{}/"
page = 1
first_page = base_url.format(1)
req = requests.get(first_page)
soup = bs4.BeautifulSoup(req.text, "lxml")
author_scrap = soup.select('.author')
pager = soup.select('.next')[0].text
author_list.extend(author.text for author in author_scrap)

while "Next" in pager:
    print("Scraping the page number: "+str(page))
    page += 1
    webpage = base_url.format(page)
    req = requests.get(webpage)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    author_scrap = soup.select('.author')
    author_list.extend(author.text for author in author_scrap)
    try:
        pager = soup.select('.next')[0].text
    except:
        print("Scraping done. No more pages to scrap")
        break

unique_authors = set(author_list)
print(unique_authors)
