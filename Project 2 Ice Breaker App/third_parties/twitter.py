import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()

#twitter_client = tweepy.Client(
    #bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    #consumer_key=os.environ["TWITTER_API_KEY"],
    #consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    #access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    #access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
#)

def scrape_user_tweets_mock(username="EdenEmarco177", num_tweets=5):
    """
    Scrapes pre made Edens's Github Gist file of tweets and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text", and "url".
    https://twitter.com/EdenEmarco177
    """
    EDEN_TWITTER_GIST = "https://gist.githubusercontent.com/emarco177/827323bb599553d0f0e662da07b9ff68/raw/57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"
    tweets = requests.get(EDEN_TWITTER_GIST, timeout=5).json()

    tweet_list = []
    for tweet in tweets:

        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list


if __name__ == "__main__":

    tweets = scrape_user_tweets_mock(username="EdenEmarco177")
    print(tweets)