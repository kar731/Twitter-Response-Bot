"""
    Automatically responds to tweets containing '#seanrandomness' with a random response
        from a provided file.
"""
from random import randint
import credentials
import tweepy


CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_SECRET
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(AUTH)

class StreamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        #sets user to the username of the poster
        user = status.user.screen_name
        #chooses a random quote
        rand_numb = randint(1, len(QUOTE_LIST))
        #sets it to randquote
        rand_quote = QUOTE_LIST[rand_numb-1]
        #gets their tweetid so you can reply to it
        tweet_id = status.id
        print("User:" + user + "\n    Message: " + status.text)
        message = "@{0} {1}".format(user, rand_quote)
        API.update_status(message, tweet_id)
        print("    Sent Tweet: {0}".format(message))
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

if __name__ == '__main__':
    ARGFILE = input("Filename:")

    with open(ARGFILE, "r") as f:
        #reads the lines in argfile
        QUOTE_LIST = f.readlines()

    print("File loaded. Program initialized. Ready.")
    LISTENER = StreamListener()
    STREAM = tweepy.Stream(AUTH, LISTENER)
    STREAM.filter(track=['#seanrandomness'])
    