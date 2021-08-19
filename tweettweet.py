# This allows us to do most of what we're doing with Twitter.
import tweepy
# This allows us to pause if we get a RateLimitError.
import time

# This code is copied and pasted from Tweepy's documentation at:
# https://docs.tweepy.org/en/stable/getting_started.html
# One should replace the variables in here with values specific to the coder,
# but I'm going to assign the values to these variables instead to show what
# the reasoning is behind this code.
# Consumer key is API key.

consumer_key = 'pVP7lAeNB2cxk2yDYMS1TD6JS'
consumer_secret = 'jnrlslX7DLz5oihRfzCCb5S0FZbbbcH7ORCeTC2ggrlVN7xoJ4'
access_token = '1115469043484561408-pJ9N3VFuNuYrZ459VADEX97MznRTLm'
access_token_secret = 'JbmMAXJ9YzeV8YjhcDeWEtSmnRPetVC76zVDB4D1ar6wM'

# auth is short for authenticate, which is what we're doing here.
# This is to set up the authentication for use as the auth variable in later code.
# .OAuthHandler() is a method that comes from tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# This is the code that actually does the action of authenticating our account
# and getting access to the Twittr API.
api = tweepy.API(auth)

# This grabs public tweets from our profile using the .home_timeline() method.
# .home_timeline() is specifically written to get the 20 most recent tweets.
public_tweets = api.home_timeline()
# This loops through each tweet, printing them one at a time.
for tweet in public_tweets:
    print(tweet.text)

# .me() gives basic profile info on the account that has been authenticated.
user = api.me()
# This will return my Twitter user name.
print(user.name)
# This will return my Twitter handle.
print(user.screen_name)
# This will return the number of how many people are following me.
print(user.followers_count)

# This is a function to help us not exceed Twitter's rate limit.
# cursor here should not be capitalized even though class Cursor is.
# This is using a variable called cursor.


def limit_handler(cursor):
    try:
        # This is saying while everything is fine, just keep going.
        while True:
            yield cursor.next()
    # This is for when we hit Twitter's rate limit bc we're demanding stuff from
    # Twitter's API faster than it wants to let us.
    # Instead of throwing a RateLimitError, it'll now pause and try again soon.
    except tweepy.RateLimitError:
        # .sleep() is a module in the time library that allows us to pause for a
        # given number of milliseconds. 1000 milliseconds is 1 second.
        time.sleep(1000)


# This shows how to follow someone through Python.
# tweepy.Cursor allows us to go through everything on Twitter in specific ways.
# .followers grabs all of our followers.
# .items() helps us loop through all the followers.
# Wrapped limit_handler function around code to handle RateLimitError.
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    # print(follower.name) to print a list of all followers
    # This is the code to follow someone:
    # Could tweak this a bunch of ways:
    # if follower.followers_count > 100:
    # I made it so this wouldn't work bc there's no follower of this name.
    if follower.name == 'lkj;lkj;lk':
        # super simple and obvious
        # could also make it print something to say it worked
        follower.follow()
        # This is so it stops looping once it does what we want.
        break
    # Put this on here so I wouldn't have to comment out the above code.
    # This otherwise wouldn't be here.
    else:
        print("No such follower.")
        break

# This is to search for a specific keyword and then like the tweet automatically.
search_word = "Washington Football Team"
numbersOfTweets = 2

# first arg is using .search method
# second arg is our variable set to the value we gave it
# .items() allows us to loop through the tweets.
# numbersOfTweets variable tells us how many tweets we want to find and like.
# could wrap the tweepy.Cursor() in the limit_handler() function if we wanted
for tweet in tweepy.Cursor(api.search, search_word).items(numbersOfTweets):
    try:
        # .favorite() is a method to like a tweet.
        # could do tweet.retweet() to do the same thing:
        # search for a keyword and retweet based on it
        tweet.favorite()
        print("This means the code liked the tweet.")
    # This is to handle any TweepError.
    except tweepy.TweepError as e:
        print(e.reason)
    # This is to handle any StopIteration.
    except StopIteration:
        break
