import requests

from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
news_links = soup.select('.titleline')
news_subtext = soup.select('.subtext')


def sort_news_by_votes(news_list):
    return sorted(news_list, key=lambda k: k['votes'], reverse=True)


def create_custom_feed(links, subtext):
    news_feed = []
    for index, item in enumerate(links):
        # Grab title of each news link
        title = links[index].getText()
        # Grab the URL of each news link
        href = links[index].find('a').get('href')
        # Get the subtext and check if news post has votes
        vote = subtext[index].select('.score')
        if len(vote):
            # Get the news points as string, drop extra wordings and convert to integer
            points = int(vote[0].getText().replace(' points', ''))
            # Add to list if votes are at least 100
            if points > 99:
                news_feed.append({'title': title, 'link': href, 'votes': points})
    return sort_news_by_votes(news_feed)


pprint.pprint(create_custom_feed(news_links, news_subtext))
