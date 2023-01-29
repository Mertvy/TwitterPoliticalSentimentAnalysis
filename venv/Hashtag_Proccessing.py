from Levenshtein import distance as lev

#Class to Determine Hashtag trends on twitter 
#Attempts to determine the political leaning of tweets by the hashtags used
class HashtagProccessor:

    #Parses through political tweets file and sorts hastags by party
    def calculate_common_hashtags_political(self, party):
        
        #Dictionary to store hashtags
        hashtag_dict={}
        #Open ExtractedTweets.csv as text
        with open('PoliticalTweets.csv', encoding="utf8") as f:
            #Parse
            lines = f.readlines()
        
            for row in lines:
                try:
                    partynametweet = row.split(',')
                    tweet = partynametweet[2].split()
                
                    if partynametweet[0] == party:
                        for string in tweet:
                            
                            string = string.lower().replace('.', '')
                            #If string is a hashtag add it to dictionary
                            if string[0] == "#":
                                if string in hashtag_dict:
                                    hashtag_dict[string]= hashtag_dict[string]+1
                                else:
                                    hashtag_dict[string]= 1
                except:
                    pass


        return hashtag_dict


    #Method to parse and store hashtags in hate speech examples
    def calculate_common_hashtags_racist(self):

        with open('HateSpeechExamples.csv', encoding="utf8") as f:
            
            lines = f.readlines()
            all_hashtags=[]
            racist_hashtags = {}
            for string in lines:
                hashtag = []
                flag = False
                for char in string:

                    if char=="." or char =="!" or char =="?" or char == " " or char == "," or char ==":" or char ==";" or char =="\"" or char =="\'":
                        flag = False
                        string_hashtag = ''.join(hashtag)
                        if not string_hashtag == "":
                            all_hashtags.append(string_hashtag)

                    if flag:
                        hashtag.append(char)

                    if char == "#":
                        hashtag.append(char)
                        flag = True
            
            for hashtag in all_hashtags:
                hashtag = hashtag.replace('#','')
                hashtag = hashtag.lower()
                hashtag = "#" + hashtag
                racist_hashtags[hashtag] = None

        return racist_hashtags

    #Assigns hashtags to certain political parties
    def get_party_unique_hashtags(self, party):

        #Initialize Refined Dictionaries
        democrat_exclusive_hashtags = {}
        republican_exclusive_hashtags = {}
        #If query is for democrat hashtags
        if party == "Democrat":
            #Go through every democrat hashtag
            for hashtag in self.democrat_hashtags:
                #If that hashtag does not exist in republican hashtags
                if not hashtag in self.republican_hashtags:
                    
                    #Add exclusive hashtag to exclusive dictionary
                    if hashtag in democrat_exclusive_hashtags:
                        #add to counter if hashtag already exists in exclusive dictionary
                        democrat_exclusive_hashtags[hashtag]= democrat_exclusive_hashtags[hashtag]+1
                    else:
                        #Add new exclusive hashtag to exclusive hashtags
                        democrat_exclusive_hashtags[hashtag]= 1
                #If the hashtag does exist in repubican hashtags
                if hashtag in self.republican_hashtags:
                    #Check if this hashtag is used 70 percent or more by democrats
                    if float(self.democrat_hashtags[hashtag])/(self.republican_hashtags[hashtag] +self.democrat_hashtags[hashtag]) > 0.7 :
                        
                        #If so add to exclusive
                        #Add exclusive hashtag to exclusive dictionary
                        if hashtag in democrat_exclusive_hashtags:
                            #add to counter
                            democrat_exclusive_hashtags[hashtag]= democrat_exclusive_hashtags[hashtag]+1
                        else:
                            #Add new exclusive hashtag to exclsive hashtags
                            democrat_exclusive_hashtags[hashtag]= 1

            return democrat_exclusive_hashtags
        
        if party == "Republican":
            for hashtag in self.republican_hashtags:
                if not hashtag in self.democrat_hashtags:
                    
                    #Add exclusive tweet to exclusive dictionary
                    if hashtag in republican_exclusive_hashtags:
                        #add to counter
                        republican_exclusive_hashtags[hashtag]= republican_exclusive_hashtags[hashtag]+1
                    else:
                        #Add new exclusive tweet to exclsive tweets
                        republican_exclusive_hashtags[hashtag]= 1
                if hashtag in self.democrat_hashtags:
                    if float(self.republican_hashtags[hashtag])/(self.democrat_hashtags[hashtag] + self.republican_hashtags[hashtag]) > 0.7 :
                        
                        #Add exclusive tweet to exclusive dictionary
                        if hashtag in republican_exclusive_hashtags:
                            #add to counter
                            republican_exclusive_hashtags[hashtag]= republican_exclusive_hashtags[hashtag]+1
                        else:
                            #Add new exclusive tweet to exclsive tweets
                            republican_exclusive_hashtags[hashtag]= 1

            return republican_exclusive_hashtags
                    
    #Constructor
    def __init__(self):
        self.republican_hashtags = self.calculate_common_hashtags_political("Republican")
        self.democrat_hashtags = self.calculate_common_hashtags_political("Democrat")
        self.refined_dem_hashtags = self.get_party_unique_hashtags("Democrat")
        self.refined_rep_hashtags = self.get_party_unique_hashtags("Republican")
        self.racist_hashtags = self.calculate_common_hashtags_racist()
        self.uniquely_racist_hashtags = self.get_uniquely_racist_hashtags()

    #Getters
    def get_republican_hashtags(self):
        return self.republican_hashtags

    def get_democrat_hashtags(self):
        return self.democrat_hashtags

    def get_democrat_exclusive_hashtags(self):
        return self.refined_dem_hashtags

    def get_republican_exclusive_hashtags(self):
        return self.refined_rep_hashtags

    def get_top_10_dem_hashtags(self):
        copy_dict = self.democrat_hashtags
        return_array = []
        for i in range(10):
            max_key = max(copy_dict, key=copy_dict.get)
            return_array.append(max_key)
            del copy_dict[max_key]
        return return_array
    
    def get_top_10_rep_hashtags(self):
        copy_dict = self.republican_hashtags
        return_array = []
        for i in range(10):
            max_key = max(copy_dict, key=copy_dict.get)
            return_array.append(max_key)
            del copy_dict[max_key]
        return return_array 

    def get_racist_hashtags(self):
        return self.racist_hashtags

    def get_uniquely_racist_hashtags(self):
        uniquely_racist_hashtags = {}

        for racist_tag in self.racist_hashtags:
            if not racist_tag in self.democrat_hashtags and not racist_tag in self.republican_hashtags:
                uniquely_racist_hashtags[racist_tag]= None
        
        return uniquely_racist_hashtags

    #Attempts to guess the politcal sentiment of tweets by the hashtag
    def define_hashtag(self, hashtag):

        #Default status
        status = ["politically neutral","non-extremist"]
        #compare to democrat hashtags with levenshtein distance
        for dem_hash in self.refined_dem_hashtags:
            if lev(hashtag, dem_hash) <= 1:
                status[0]= "Left Leaning"
        #compare to republican hashtags with levenshtein distance
        for rep_hash in self.refined_rep_hashtags:
            if lev(hashtag, rep_hash) <= 1:
                status[0]= "Right Leaning"
        #compare to extremist hashtags with levenshtein distance
        for race_hash in self.uniquely_racist_hashtags:
            if lev(hashtag, race_hash) <= 1:
                status[1]= "Extremist"

        return status

    

