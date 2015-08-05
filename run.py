import twitter
import json

with open('creds.json') as data_file:
    creds = json.loads(data_file.read())

api = twitter.Api(consumer_key=creds['consumer_key'],
                  consumer_secret=creds['consumer_secret'],
                  access_token_key=creds['access_token_key'],
                  access_token_secret=creds['access_token_secret'])


def page_and_retweet(page=None):
    search_results = api.GetSearch('retweet win -follow -tune -email -link -fav -vote',
                                   count=100,
                                   since_id=page)

    for result in search_results:
        try:
            api.PostRetweet(result.GetId())
            print 'retweeted ', result.text
        except twitter.error.TwitterError:
            print 'duplicate retweets'
            pass

    # return the last id
    return search_results[-1].id

last_id = page_and_retweet()
last_id = page_and_retweet(last_id)
last_id = page_and_retweet(last_id)
last_id = page_and_retweet(last_id)
last_id = page_and_retweet(last_id)
last_id = page_and_retweet(last_id)
