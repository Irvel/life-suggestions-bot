import json
import tweepy
import random

# The access keys for the Twitter API are in access_keys.py
from access_keys import *
from tweepy.streaming import StreamListener
from time import sleep
from user_manager import UserManager


class TwitterAPI:
    def __init__(self):
        consumer_key = C_KEY
        consumer_secret = C_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = A_TOKEN
        access_token_secret = A_TOKEN_SECRET
        auth.set_access_token(access_token, access_token_secret)
        self.auth = auth
        self.api = tweepy.API(auth)

    def start_listening(self, listener):
        return tweepy.Stream(self.auth, listener)

    def tweet(self, message):
        self.api.update_status(status=message)


class TweetListener(StreamListener):
    def __init__(self, configured_api):
        self.twitterApi = configured_api
        self.manager = UserManager(configured_api)

    def on_data(self, data):
        tweet = json.loads(data.strip())

        retweeted = tweet.get('retweeted')
        from_self = tweet.get('user',{}).get('screen_name','') == "BotExistencial"

        if retweeted is not None and not retweeted and not from_self:

            tweetId = tweet.get('id_str')
            screen_name = tweet.get('user',{}).get('screen_name')
            tweetText = tweet.get('text')

            response = self.manager.get_response(screen_name)

            replyText = '@' + screen_name + ' ' + response

            #check if repsonse is over 140 char
            if len(replyText) > 140:
                replyText = replyText[0:139] + '…'

            print('Tweet ID: ' + tweetId)
            print('From: ' + screen_name)
            print('Tweet Text: ' + tweetText)
            print('Reply Text: ' + replyText)

            # If rate limited, the status posts should be queued up and sent on an interval
            self.twitterApi.api.update_status(status=replyText, in_reply_to_status_id=tweetId)
            sleep(95)

    def on_error(self, status):
        print (status)


if __name__ == "__main__":
    twitter = TwitterAPI()
    listener = TweetListener(twitter)
    stream = twitter.start_listening(listener)
    stream.filter(track=["@BotExistencial"])
