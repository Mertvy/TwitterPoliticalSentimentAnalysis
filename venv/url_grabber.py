import tweepy
import json
from APIKeys import *

auth = tweepy.OAuthHandler(TweepyKeys.consumer_key, TweepyKeys.consumer_secret)
auth.set_access_token(TweepyKeys.access_token, TweepyKeys.access_token_secret)
api = tweepy.API(auth)

def convertDateAndTime(created_at):
    monthDict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    (date, time) = created_at.split()
    date = date.split("-")
    date = monthDict[int(date[1])] + " " + date[2] + ", " + date[0]
    time = time.split("+")[0].split(":")
    time = str((int(time[0]) - 5) % 24) + ":" + time[1]
    return (date, time)


def fetch_from_url(url):
    tweet = str(url)
    tweetid = tweet.strip().split('status/')[1]
    tweet = api.get_status(tweetid,tweet_mode='extended')
    tw_client = tweet.source
    print(tweet.created_at)
    return (tweet.user.name, tweet.full_text, tw_client, convertDateAndTime(str(tweet.created_at)))

def get_tweet_from_id(id):
    tweet = api.get_status(id, tweet_mode='extended')
    tw_client = tweet.source
    return (tweet.user.screen_name, tweet.user.name, tweet.full_text, tw_client, convertDateAndTime(str(tweet.created_at)))