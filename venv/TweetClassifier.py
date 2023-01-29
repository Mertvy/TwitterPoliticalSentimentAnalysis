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
        model='large',
        inputs=[tweet[1]],
        examples=[Example('Gas prices are at a 7 year high, Thanks Joe Biden!','Dem'), Example("It used to be that Dems’ ignorance of economics was a talking point for conservatives. Conservatives now trying to take over the mantle for not understanding how economics works.", "Dem"), Example("""Insurrection and sedition were a at two hundred year high on January 6th
Thank the former president for that

If I have to choose between gas prices or dictatorship, I’ll go with our Constitution

Many Americans have paid the ultimate price 4 our democracy

& you care about gas""", "Dem"), Example("Have you ever noticed how Democrats NEVER talk about how they are going to get the illegal guns out of the hands of the criminals?", "Rep"), Example("Every dark chapter in the US is always because of the Democrats", "Rep"), Example("Why are Democrats obsessed with taking away guns from law-abiding Americans?", "Rep"), Example("""Every single House Republican just voted to block President Biden from selling oil to lower gas prices.

They want you to pay higher prices.""", "Dem"), Example("And what do Republicans do? Vote against all real solutions, against veterans, against children, against raising minimum wage, as well as against price gouging! So who do they support? Themselves and their mega donors! ", "Dem")])

    # print(tweet + '\nThe confidence levels of the labels are: {}'.format(response.classifications))
    return response.classifications

def few_shotted(tweet):
  co = cohere.Client('NnJpUuXLJ3XPdtoT0FZUmD10P9UJzRZB3HJI53n1') # This is your trial API key
  response = co.classify(
    model='large',
    inputs=[tweet[1]],
    examples=[Example("Arabs are not welcome", "Hate Speech"), Example("bananas are for black people", "Hate Speech"), Example("the thought of a world free of blacks makes me so happy", "Hate Speech"), Example("There is a new shop on my block with the sign of the swastika on its door. Customer on the way!", "Hate Speech"), Example("I don\'t want Indians on my street", "Hate Speech"), Example("Immigrants have a culture of rape", "Hate Speech"), Example("mornin all! have to go to nans for her birthday  boringgggg", "Random"), Example("But I was so busy with the growing line I couldn\'t ask his name.  &lt;/3 He talked about  backpacking through europe!", "Random"), Example("I haven\'t forgotten about sending the Maxwell single to you guys - my internet isn\'t active til tomorrow  g\'night tweeps!", "Random"), Example("Tummy all better. I think I should be working on my English SAC plan. arrggg. and wishing I had more pokemon ", "Random"), Example("@nickyy123  ooooo no Nicky  who\'s gonna make me laugh in English!", "Random"), Example("I like Bagels", "Random"), Example("@POTUS Y'all should really stop with the propaganda. Seems Americans aren't buying it anymore.","Random"),Example("Black democrat  Americans are the most racist people in the world next to white democrats.","Hate Speech")])
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
