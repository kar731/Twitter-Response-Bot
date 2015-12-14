import tweepy
import time
import sys
from random import randint

CONSUMER_KEY = "enter key here"
CONSUMER_SECRET = "enter key here"
ACCESS_KEY = "enter key here"
ACCESS_SECRET = "enter key here"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class streamListener(tweepy.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        #sets user to the username of the poster
        user = status.user.screen_name
        #chooses a random quote
        randNumb = randint(1, len(quoteList))     
        randNumb -= 1
        #sets it to randquote
        randQuote = quoteList[randNumb]
        #gets their tweetid so you can reply to it
        tweetId = status.id
        #prints the user and tweet.
        print("User:" + user + "\n    Message: " + status.text)
        message = "@{username} {quotation}".format(username=user, quotation=randQuote)
        api.update_status(message, tweetId)
		#prints what tweet was sent
        print("    Sent Tweet: {0}".format(message))
		
        return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
 
    def on_timeout(self):
        print('Timeout...')
        return True
 
if __name__ == '__main__':
    file = raw_input("Filename:")
    argfile = file

    #opens argfile into read mode
    filename=open(argfile,"r")
    #reads the lines in argfile
    quoteList=filename.readlines()
    #closes the file
    filename.close()

    print("File loaded. Program initialized. Ready.")
    listener = streamListener()
 
    stream = tweepy.Stream(auth, listener)
	#checks for whatever you want. #seanrandomness was unused so i used it
    stream.filter(track=['#seanrandomness'])