import tweepy

consumer_key = 'pVP7lAeNB2cxk2yDYMS1TD6JS'
consumer_secret = 'jnrlslX7DLz5oihRfzCCb5S0FZbbbcH7ORCeTC2ggrlVN7xoJ4'
access_token = '1115469043484561408-pJ9N3VFuNuYrZ459VADEX97MznRTLm'
access_token_secret = 'JbmMAXJ9YzeV8YjhcDeWEtSmnRPetVC76zVDB4D1ar6wM'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_word = "Washington Football Team"
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_word).items(numbersOfTweets):
    try:
        tweet.favorite()
        print("This means the code liked the tweet.")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
