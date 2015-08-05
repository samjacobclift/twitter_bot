import twitter
import json

with open('creds.json') as data_file:
    creds = json.loads(data_file.read())

api = twitter.Api(consumer_key=creds['consumer_key'],
                  consumer_secret=creds['consumer_secret'],
                  access_token_key=creds['access_token_key'],
                  access_token_secret=creds['access_token_secret'])

search_results = api.GetSearch('retweet to win! -follow -tune', count=100)

for result in search_results:
    try:
        api.PostRetweet(result.GetId())
        print 'retweeted ', result.text
    except twitter.error.TwitterError:
        print 'already retweeted ', result.text
