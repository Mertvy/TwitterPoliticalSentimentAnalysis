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

def few_shotted2(tweet_text):
  co = cohere.Client(CohereKeys.mk) # This is your trial API key
  response = co.classify(
    model='large',
    inputs=tweet_text,
    examples=[Example("Arabs are not welcome", "Hate Speech"), Example("bananas are for black people", "Hate Speech"), Example("the thought of a world free of blacks makes me so happy", "Hate Speech"), Example("There is a new shop on my block with the sign of the swastika on its door. Customer on the way!", "Hate Speech"), Example("I don\'t want Indians on my street", "Hate Speech"), Example("Immigrants have a culture of rape", "Hate Speech"), Example("mornin all! have to go to nans for her birthday  boringgggg", "Random"), Example("But I was so busy with the growing line I couldn\'t ask his name.  &lt;/3 He talked about  backpacking through europe!", "Random"), Example("I haven\'t forgotten about sending the Maxwell single to you guys - my internet isn\'t active til tomorrow  g\'night tweeps!", "Random"), Example("Tummy all better. I think I should be working on my English SAC plan. arrggg. and wishing I had more pokemon ", "Random"), Example("@nickyy123  ooooo no Nicky  who\'s gonna make me laugh in English!", "Random"), Example("I like Bagels", "Random"), Example("@POTUS Y'all should really stop with the propaganda. Seems Americans aren't buying it anymore.","Random")])

  return response.classifications

def few_shotted(tweet):
  co = cohere.Client('NnJpUuXLJ3XPdtoT0FZUmD10P9UJzRZB3HJI53n1') # This is your trial API key
  response = co.classify(
    model='large',
    inputs=[tweet[1]],
    examples=[Example("Arabs are not welcome", "Hate Speech"), Example("bananas are for black people", "Hate Speech"), Example("the thought of a world free of blacks makes me so happy", "Hate Speech"), Example("There is a new shop on my block with the sign of the swastika on its door. Customer on the way!", "Hate Speech"), Example("I don\'t want Indians on my street", "Hate Speech"), Example("Immigrants have a culture of rape", "Hate Speech"), Example("mornin all! have to go to nans for her birthday  boringgggg", "Random"), Example("But I was so busy with the growing line I couldn\'t ask his name.  &lt;/3 He talked about  backpacking through europe!", "Random"), Example("I haven\'t forgotten about sending the Maxwell single to you guys - my internet isn\'t active til tomorrow  g\'night tweeps!", "Random"), Example("Tummy all better. I think I should be working on my English SAC plan. arrggg. and wishing I had more pokemon ", "Random"), Example("@nickyy123  ooooo no Nicky  who\'s gonna make me laugh in English!", "Random"), Example("I like Bagels", "Random"), Example("@POTUS Y'all should really stop with the propaganda. Seems Americans aren't buying it anymore.","Random","Black democrat  Americans are the most racist people in the world next to white democrats.","Hate Speech")])
  print('The confidence levels of the labels are: {}'.format(response.classifications))
  return tweet, response.classifications, right_left_classify(tweet)

few_shotted(clean_slate())

'''input = []


with open("TrainingData/RandomTweets"):
  

co = cohere.Client(CohereKeys.key) # This is your trial API key
response = co.classify(
  model='a659de31-e4d1-4500-8857-30ff656ad9ca-ft',
  inputs=)

print('The confidence levels of the labels are: {}'.format(response.classifications))
'''
