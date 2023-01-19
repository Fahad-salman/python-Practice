import tweepy
import time

auth = tweepy.OAuth1UserHandler(
   '', # Consumer key
   '', # Consumer secret
   '', # Access token
   '' # Access token secret
)

api = tweepy.API(auth)

# print(api.get_favorites())

# for folowers in tweepy.Cursor(api.get_followers).items():
#     print(folowers.name)


# this will function will follow back 
def limit_followers(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.TooManyRequests:
        time.sleep(100)
        
for i in limit_followers(tweepy.Cursor(api.get_followers).items()):
    if i.name == 'Fahad':
        i.follow()
        print('done')
        break
    print(i.name)


# this function for searching and will add to favorite
search_str = 'python' # your search keyword
numberOfTweets = 2 # How many tweets will liked

for tweet in tweepy.Cursor(api.search_tweets,search_str).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked this tweet')
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
        