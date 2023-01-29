from cohere.classify import Example
from cohere import Client
from APIKeys import *
import random


def AnalyzeLeftVSRight(messages):
    co = Client(CohereKeys.key)

    examples = []

    with open("../TrainingData/UpdatedDemVsRep.csv") as demVsRep:
        i = 0
        while True:
            line = random.choice(demVsRep.readlines())
            if i == 500:
                break
            line = line.split(",", 2)
            try:
                phrase = line[2].strip("\"").strip()
            except:
                continue
            examples.append(Example(phrase, line[0]))
            i += 1

    response = co.classify(
        model='large',
        inputs=messages,
        examples=examples,
    )

    return response


def DetectHateSpeech(messages):
    co = Client(CohereKeys.key)

    examples = []

    with open("../TrainingData/UpdatedHateSpeechExamples.csv") as hse:
        i = 0
        for line in hse.readlines():
            if i == 200:
                break
            line = line.split("\"", 6)
            try:
                phrase = line[-2]
            except:
                phrase = line[-1]
            examples.append(Example(phrase, "Hate speech"))
            i += 1

    with open("TrainingData/RandomTweets.csv") as randomTweets:
        for line in randomTweets.readlines():
            if i == 1000:
                break
            line = line.strip().split(",", 5)
            try:
                phrase = line[-1]
            except:
                pass
            examples.append(Example(phrase, "Not hate speech"))
            i += 1

    response = co.classify(
        model='large',
        inputs=messages,
        examples=examples,
    )

    return response

