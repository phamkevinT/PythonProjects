import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)
user = api.me()


# Prevent the program from spamming the Twitter API
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(500)


"""
Bot to follow back follwers
"""
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()

"""
Favorite tweets with the keyword 'python'
"""
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break
