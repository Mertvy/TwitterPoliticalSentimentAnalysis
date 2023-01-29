from APIKeys import *
import cohere
from cohere.classify import Example
# from YeTweets import kanye_tweet
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from filtered_stream import clean_slate


def classify_tweet(tweet_list):
    for tweet in tweet_list:
        co = cohere.Client('NnJpUuXLJ3XPdtoT0FZUmD10P9UJzRZB3HJI53n1')  # This is your trial API key
        response = co.classify(
            model='4b14f0dc-6e46-45c9-b3a6-3f82f48bd5ca-ft',
            inputs=[tweet])
        # print(tweet + '\nThe confidence levels of the labels are: {}'.format(response.classifications))
        tweet_classifications = str(
            tweet + '\nThe confidence levels of the labels are: {}'.format(response.classifications))
        print(tweet_classifications)


def single_classifier(tweet):
    co = cohere.Client(CohereKeys.key)  # This is your trial API key
    response = co.classify(
        model='7b69120b-9daf-4139-8ba6-bf609aba963f-ft',
        inputs=[tweet[1]])
    # print(tweet + '\nThe confidence levels of the labels are: {}'.format(response.classifications))
    return tweet, response.classifications, right_left_classify(tweet)

def right_left_classify(tweet):
    co = cohere.Client(CohereKeys.mk)  # This is your trial API key
    response = co.classify(
        model='b9bdd6cc-6333-4c48-ab91-92391ce3b8b0-ft',
        inputs=[tweet[1]])
    # print(tweet + '\nThe confidence levels of the labels are: {}'.format(response.classifications))
    return response.classifications

single_classifier(clean_slate())
'''input = []

with open("TrainingData/RandomTweets"):
  

co = cohere.Client(CohereKeys.key) # This is your trial API key
response = co.classify(
  model='a659de31-e4d1-4500-8857-30ff656ad9ca-ft',
  inputs=)

print('The confidence levels of the labels are: {}'.format(response.classifications))
'''
