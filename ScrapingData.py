import requests
from bs4 import BeautifulSoup
import pprint


response = requests.get('https://news.ycombinator.com/show')
response2 = requests.get('https://news.ycombinator.com/show?p=2')

soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

links = soup.select(".titleline")
subtext = soup.select(".subtext")
links2 = soup2.select(".titleline")
subtext2 = soup2.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hackerNewslist):
    return sorted(hackerNewslist, key=lambda k: k['votes'], reverse=True)

def create_custom_HackerNews(links, subtext):
    hackerNwes_list = []
    for index ,item in enumerate(links):
        title = item.get_text()
        href = item.get('href', None)
        votes = subtext[index].select('.score')
        if len(votes):
            points = int(votes[0].get_text().replace(' points', ''))
            if points > 20:
                hackerNwes_list.append({'title':title,'href':href,'votes':points}) 
    return sort_stories_by_votes(hackerNwes_list)

pprint.pprint(create_custom_HackerNews(mega_links, mega_subtext))
