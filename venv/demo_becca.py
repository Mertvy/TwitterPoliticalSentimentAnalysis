from APIKeys import *
import cohere
from cohere.classify import Example
import json
import preprocessor as p
from tweet_harvester import search_tweets_for_username
from anti_sem import search_method
from anti_sem import open_sesame

with open("list_of_users.txt", 'r') as f:
    user_list = f.read().split(',')

file_name = 'examplefile.file'

with open('examplefile.file', 'r') as example_case:
    example_case = json.load(example_case)

example_case2 = []

for i in example_case:
    text = i[0]
    lbl = i[1]
    example_case2.append(Example(text,lbl))

test_cases = ["Israel didn't deliberately murder 9 Palestinians in Jenin"]

print(search_method(test_cases))

# if __name__=="__main__":
#     user_list = open_sesame()
#     user_list = user_list[0]
#     example_cases = open_sesame()
#     example_case2 = example_cases[1]
#     print(search_method(test_cases))