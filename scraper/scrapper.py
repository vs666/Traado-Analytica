import twint
import sys
path = "./tweets/"
try:
    c = twint.Config()
    topic = sys.argv[1]
    print("Searching for",topic,".....")
    c.Search = [topic]       # topic
    c.Limit = int(sys.argv[2])      # number of Tweets to scrape
    c.Store_csv = True       # store tweets in a csv file
    c.Profile_full = True
    c.lang = "en"            # language
    c.Output = path+topic+"_tweets.csv"     # path to csv file
    twint.run.Search(c)
except:
    print("Exception happened")