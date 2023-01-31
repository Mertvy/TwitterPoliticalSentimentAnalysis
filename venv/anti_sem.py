from APIKeys import *
import cohere
from cohere.classify import Example
import json
import preprocessor as p
from tweet_harvester import search_tweets_for_username

# example_case = [Example("Israel is an aparthied state", "AS"),
#                       Example("I hate Jews", "AS"),
#                       Example("Jews should go back to Europe", "AS"),
#                       Example("Fuck Jews","AS"),
#                       Example("death to Israel", "AS"),
#                       Example("can i ask that we normalize hating on nations rather than people more accurately these days?", "N"),
#                       Example("""Not what you think
#
#     Propagandist
#     PRO zionist (Amos Oz supporter)
#     Parents —> Hollywood""", "AS"),
#                       Example("Your Holiness, I would like to inform you that the building of the Bishop's Curia has been converted into apartments for Jews - Bishop Franciszek Barda reported in a letter to Pope Pius XII. Bishop Barda also gave false baptismal records to the Igel family, among others.","N"),
#                       Example("The latest proof that trump has managed to simultaneously appeal to those who think US Jews aren’t loyal enough to Israel and those who think US Jews are too loyal to Israel", "N"),
#                       Example("I'm probably blackpilled due to years of zog programming but I can't help but think that he watches other men please his wife.", "N"),
#                       Example("""The Republican Jewish Coalition's Matt Brooks says in a statement that Harris-who has a strong pro-Israel record and is married to a Jew - "does not stand with Israel and the Jewish community."
#
#     Could it be because Harris would not endorse inside trading $KODAK #TrumpCorruption""", "AS"),
#                       Example("I like Bagels", "N"),
#                       Example("""Same poll shows Arab areas around Israel,Almost 60+%peoples agree on the Arab countries surrounding Israel are jungle in which Israeli civilisation has been established
#     This means,they want to destroy and occupy the Arab countries,Now the #politicalwar is begin #TurkeyIsNotAlone""","AS"),
#                       Example("Black democrat  Americans are the most racist people in the world next to white democrats.","N"),
#                     Example("""Don't bother with him, hes indirectly helping Israel.
# The irony is that he's subconsciously working towards the of his own people.
# This is his master right here.
# Benjamin Netanyahu has successfully been able to control and demoralized the white race.""","AS"),
#                 Example("""Today we created our own story of Zog in the form of a story board. Tomorrow we will write our story.""","N"),
#                 Example("""Netanyahu: ‘Rabbi Steinsaltz was an outstanding example of the persistent Jew’ - ""","N"),
#                 Example("""When, in the end, they all feed at the same trough, it Does NOT matter.
# The US Imperialist Zionist System has been captured by a Foreign Agent for decades plus, so it's just a question of which one of these lovely ladies will be their messenger.""","AS"),
#                 Example("""Zionists don't want you to rebel.
# Zionists don't want you to resist.
# Zionists don't want you to #BDS.
# They want you to do one thing:""","AS"),
#                 Example("""A subservient or quiet Palestinian is the only kind of Palestinian Zionists of any stripe will acknowledge or like.""","AS"),
#                 Example("""A lot of Zionists - if not all of them - don’t even think Palestinians actually exist.""","AS"),
#                 Example("""the zionist entity is the most well funded terrorist organization in the world""","AS"),
#                 Example("""This shows the grip zionist have on the western media.""","AS"),
#                 Example("""I’m a Jew
#
# My grandfather knew Theodor Herzl & was an early, ardent Zionist
#
# Israel is now a vicious apartheid State, where the Rule of Law does not operate to protect Palestinian rights or lives
#
# I abhor this Israeli State
#
# Don’t let anyone tell you such criticism is antisemitic""","AS"),
#                 Example("""Supporting Palestinian rights is antisemitic because Israel wants it to be""","AS"),
#                 Example("""Zionism represents the Jewish people’s unbreakable bond and age-old desire to be free in their ancestral home.""","N"),
#                 Example("""Zionism means supporting Israel, which is righteous and good""","N"),
#                 Example("""Israel is the only democracy in the middle east, and is good""", "N"),
#                 Example("""I'm a proud zionist""","N"),
#                 Example("""I support the Jewish Zionist state""","N"),
#                 Example("""I love Jews""","N"),
#                 Example("""Israel’s existence and wellbeing is vital to the Jewish people’s safety, survival, and human rights""","N"),
#                 Example("""for the overwhelming majority of Jews, their connection to Israel is central to their Jewish identity.""","N"),
#                 Example("""The state of Israel is crucial for the survival of the Jews""","N"),
#                 Example("""Am Yisrael Chai""","N"),
#                 Example("""Long live Israel""","N"),
#                 Example("""Jews are indigenous to Israel""","N"),
#                 Example("""Jew's killed arabs""","AS"),
#                 Example("""Yahoudi""","AS"),
#                 Example("""Jews are driving up the prices""","AS"),
#                 Example("""Pro-Palestinian advocates rally in New York to honor the 10 Palestinians who were massacred in Jenin a few days ago and all Palestinians whose lives have been claimed by Israeli apartheid since the start of 2023.""","AS"),
#                 Example("""On Sunday, hundreds marched through the New York City neighborhood of Bay Ridge, Brooklyn to oppose Zionist terror and support the Palestinian struggle for liberation and return.""","AS"),
#                 Example("""Jenin bleeds but resists""","N"),
#                 Example("""Palestine occupée
# Palestine occup
# Palestine occu
# Palestine oc
# Palestine o
# Palestine
# Palestine l
# Palestine li
# Palestine libr
# Palestine libre
# Palestine libre""","AS"),
#                 Example("""How the pro-Israel lobby buys support for war crimes""","AS"),
#                 Example("""Anti-zionist Orthodox Jews will join tomorrow's Mass rally in Bay Ridge Brooklyn, NY, 2:00pm, to protest and condemn the Zionist regime Massacre in Jenin, where the IOF murdered 9 Palestinians, over 30 Palestinians have been murdered since 2023""","AS"),
#                 Example("""Palestine Action comes to spoil the party of “Make UK”""","N"),
#                 Example("""Palestine is getting water""","N"),
#                 Example("""Free Palestine!""","N"),
#                 Example("""From the River to the Sea, Palestine will be free""","AS"),
#                 Example("""The comic strip "Elise and the New Partisans" censored by a German publishing house for the support of its authors for Palestine""","N"),
#                 Example("""Seven killed in attack on Jerusalem settlement""","N"),
#                 Example("""Mobilization for Ahmad Sa'adat: "supporting the prisoners is supporting the Palestinian resistance""","N"),
#                 Example("""Take to the streets to protest the horrific police killing of Tyre Nichols by five Memphis Police Department officers!""","N"),
#                 Example("""glory2ourmartyrs""","AS"),
#                 Example("""Manchester now: Manchester Supports the Palestinian Resistance! Calling on the world to stand against Israel's ongoing mass murder and ethnic cleansing of the Palestinians & latest massacre in Jenin""","AS"),
#                 Example("""New York City’s
# @WOLPalestine
#  is organizing an emergency protest and vigil for Palestine this Sunday, January 29 at 2:00 pm in Bay Ridge, Brooklyn.""","N"),
#                 Example("""honorourmartyrs""","AS"),
#                 Example("""With the mainstream media uncritically echoing Israeli propaganda - equating oppressor with oppressed - here are 3 key points to remember when reporting or when refuting this myth.""","AS"),
#                 Example("""Israel’s entire society is complicit in this unjust reality."
#
# Former AG of Israel confirms apartheid.""","AS"),
#                 Example("""States, institutions, and corporations supporting apartheid Israel are not just complicit, they have Palestinian blood on their hands. Escalate all #BDS campaigns now!""","AS"),
#                 Example("""call for #UNinvestigateApartheid & lawful sanctions on Israel to dismantle its 74-year-old regime of settler-colonialism, apartheid & military occupation""","AS"),
#                 Example("""Standing with Palestine means action to hold Israel accountable. When will Ireland implement the #OccupiedTerritoriesBill on banning trade with Israeli settlements and join the campaign for ""","N"),
#                 Example("""jews are weird""","AS"),
#                 Example("""Elmo funds the media""","N"),
#                 Example(""""matzah ball soup is gross""","N"),
#                 Example("""bill is a kike""","AS"),
#                 Example("""i love kikes""","AS"),
#                 Example("""coco chanel was a nazi""","N"),
#                 Example("""Jewish Canadians are more alligned with Israel than canada""","AS")]

with open("list_of_users.txt", 'r') as f:
    user_list = f.read().split(',')

file_name = 'examplefile.file'

with open('examplefile.file', 'r') as example_case:
    example_case = json.load(example_case)

example_case2 = []

users = ['@PalestineHouse','@samidounPP','@palyouthmvmt', '@cd4_hr', '@mbueckert']

for i in example_case:
    text = i[0]
    lbl = i[1]
    example_case2.append(Example(text,lbl))


def search_method(tweet):
    '''Calls the Cohere API to test the given tweet against the model'''
    co = cohere.Client(CohereKeys.mk)  # This is your trial API key
    response = co.classify(
        model='large',
        inputs= tweet,
        examples= example_case2)
    return response.classifications

def dodek_trainer(tweet):
    '''Asks the user if the tweet is Anti-Semetic, assuming the user told the program that it's evaluation was incorrect'''
    acceptable_responses = ["y", "n"]
    results = search_method(tweet)
    reformatted = get_classification(results)
    user_fb = test_user(reformatted,tweet)
    if user_fb == "n":
        i = 0
        print(f'is this tweet antisemitic?"\n{tweet}\n')
        while i ==0:
            new_fb = str.lower(input("Input Y/N: "))
            if new_fb not in acceptable_responses:
                print(user_fb)
                print("invalid value, please try again")
            else:
                i= i + 1
        if new_fb == "n":
                entered = 'N'
        else:
            entered = 'AS'
        print("thank you for your help training the model!")
        return entered
    else:
        print("thank you for your help training the model!")

    return reformatted[0]

def test_user(model_guess,tweet):
    '''Asks the user if the bot correctly classified the tweet'''
    i = 0
    acceptable_responses = ["y","n"]
    print(f'Does this look correct for this tweet? \n\n {tweet} \n\n {model_guess}')
    while i == 0:
        user_fb = str.lower(input("Type Y/N: "))
        if user_fb not in acceptable_responses:
            print(user_fb)
            print("invalid value, please try again")
        else:
            i = i + 1
    return user_fb

def get_classification(class_value):
    """Pulls just the classification (AS or N) and the confidence level from the Cohere response"""
    strung_up = str(class_value)
    formatted = strung_up.split(':')
    reformat_class = formatted[1].split(',')
    reformat_conf = formatted[2].split(',')
    result = (reformat_class[0], reformat_conf[0])
    return result

def bringing_it_together(tweet):
    """Is the main function of the code, calls remove ATS to clean the text, then runs it through the various trainer prompts and then appends the results to the example file"""
    result = dodek_trainer(tweet)
    tweet2 = str(tweet)
    tweet2 = tweet2.strip("'[]")
    result = result.strip(" \"")
    result = result.lstrip(' \"')
    new_case = (tweet2,result)
    example_case2.append(new_case)


def remove_ats(tweet):
    tweet = str(tweet)
    twit = []
    listed = tweet.replace('@','')
    # tweet = [p.clean(tweet)]
    twit.append(listed)
    return twit

def hamster_wheel(users):
    with open("list_of_tweets.txt", 'r') as tweets:
        tweets = json.load(tweets)
    tweetles = search_tweets_for_username(users)
    for a in tweetles:
        tweet = []
        tweet.append(a)
        print(tweet)
        bringing_it_together(tweet)
        input2 = input('type c and hit enter to continue (enter any other letter else to stop):')
        if input2 != "c":
            quit()
            
def fetch_all(users):
    '''Fetches all tweets from the users listed (since deprecatd)'''
    list_of_tweets = search_tweets_for_username(users)
    list_of_tweets = list_of_tweets[0:95]
    with open("list_of_tweets.txt", 'w') as tweets:
        json.dump(list_of_tweets, tweets)

    return list_of_tweets


# with open(file_name, 'w') as file_object:
#     json.dump(example_case2, file_object)

hamster_wheel(user_list)