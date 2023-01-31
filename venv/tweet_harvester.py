import tweepy
import json
import re
import pdflatex as pdl
from datetime import datetime, timedelta
import pandas as pd
from collections import OrderedDict
from APIKeys import *

auth = tweepy.OAuthHandler(TweepyKeys.consumer_key, TweepyKeys.consumer_secret)
auth.set_access_token(TweepyKeys.access_token, TweepyKeys.access_token_secret)
api = tweepy.API(auth)

now = datetime.today().now()
prev = now - timedelta(hours = 24)
url_exp = re.compile(r"https:\/\/\S*")

with open("list_of_users.txt", 'r') as f:
    user_list = f.read().split(',')

def search_tweets_for_username(users):
    output = ''
    formatting = []
    formatting2 = []
    for user in users:
        for tweet in api.user_timeline(screen_name=user, include_rts=False, tweet_mode='extended', count=50):
                url = f"{'https://twitter.com'}/{tweet.author.screen_name}/status/{tweet.id}"

                another_way_to_get_url_from_the_text = url_exp.findall(tweet.full_text)
                text = tweet.full_text
                name = tweet.author.screen_name
                if another_way_to_get_url_from_the_text:
                    another_way_to_get_url_from_the_text = another_way_to_get_url_from_the_text[-1]
                    text = tweet.full_text[:-len(another_way_to_get_url_from_the_text)]
                tweet_export = f"""
    {name}
    {text}
    {url} """
                output += tweet_export +'\n'
                tweet_export2 = text
                formatting2.append(tweet_export2)
                formatting.append(tweet_export)
    return formatting2