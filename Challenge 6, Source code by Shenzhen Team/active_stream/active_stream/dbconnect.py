
import tweepy
import time

# Replace the "None"s by your own credentials
access_token = "1169326422520786945-lkGEI45ix849t0DcB4oCChb21IaWgd"
access_token_secret = "uPyUh8rtWdLd1v7PhOUhZV21UOmFguh41K2rI2n0suDhG"
api_key = "ap42GG7UV12inZFPynuARHEen"
api_secret = "WVUZk7dqFSv4U6lr0slUsGckgJIlgEOb6snaiELd0Z4NG7vkgZ"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAC3SewEAAAAAORHRvjQKzbQvuUStnWECGG4MxOQ%3DuMj2DRJoHYXMSHiJT72eFPgJKIzaEyUrikr6f0byUpg98DeEO7"


# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

search_terms = ["python", "programming", "coding"]

# Bot searches for tweets containing certain keywords


class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):

        print("Connected")

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            print(tweet.text)
            client.like(tweet.id)

            # Delay between tweets
            time.sleep(0.5)


# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
# It's important to know that these rules don't get deleted when you stop the
# program, so you'd need to use stream.get_rules() and stream.delete_rules()
# to change them, or you can use the optional parameter to stream.add_rules()
# called dry_run (set it to True, and the rules will get deleted after the bot
# stopped running).
for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

# Starting stream
stream.filter(tweet_fields=["referenced_tweets"])
