import requests
import os
import json
from APIKeys import *
from url_grabber import get_tweet_from_id

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

bearer_token = TweepyKeys.bearer_token

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {
            "value": "context:88.941041031239237632 OR context:35.950465066800881665 OR context:131.847878884917886977 OR context:131.1070032753834438656 OR context:35.1295853707200835584 AND context:131.847878884917886977 -is:retweet AND -has:links lang:eng",
            "value": "context:35.875006493984149509 OR context:35.10040395078 OR 131.847878884917886977 OR 131.900740740468191232 OR131.1070032753834438656 -has:links AND -is:retweet AND lang:en",
        }
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    i = 0
    for response_line in response.iter_lines():
        if i >= 5:
            break
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
            json_saved = json.dumps(json_response, indent=4, sort_keys=True)
        i += 1
    return json_saved

def single_tweet_stream(set):
    q = []
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    i = 0
    for response_line in response.iter_lines():
        if i >= 2:
            break
        if response_line:
            json_response = json.loads(response_line)
            tweet_data = json_response["data"]
            tweet_id = tweet_data["id"]
            json_saved = json.dumps(json_response, indent=4, sort_keys=True)
        i += 1
    return str(tweet_id)

def clean_slate():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    stream = (single_tweet_stream(set))
    return get_tweet_from_id(stream)

print(clean_slate())