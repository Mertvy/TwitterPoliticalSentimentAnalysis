import csv
import os

def calculateCommonHashtags():

    os.chdir("/TrainingData")
    with open('DemVsRep.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            row[2]
        csv_file.close()






def get_trends(lat, long):
    trendy = tweepy.closest_trends(lat, long)
    print(trendy)

get_trends(40.4173N, 82.9071W)