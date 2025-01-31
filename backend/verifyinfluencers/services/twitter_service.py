import requests
import tweepy
from django.conf import settings

TWITTER_BEARER_TOKEN = settings.TWITTER_BEARER_TOKEN


def fetch_tweets(username, max_results=10):
    """
    Fetch recent tweets from a given influencer.
    :param username: Twitter handle of the influencer
    :param limit: Number of tweets to fetch (default 10)
    :return: List of tweet texts
    """
    # TODO: Put a try catch here (for 404 and 429)
    print(f"THE TWITTER BEARER TOKEN IS: {TWITTER_BEARER_TOKEN}")

    client = tweepy.Client(TWITTER_BEARER_TOKEN)
    # Use the handle of the user to retrieve their ID
    user = client.get_user(username=username, user_auth=False)
    print(f'The user is: {user}')

    user_id = ''
    if user.data:
        # Get user ID
        user_id = user.data.id
        name = user.data.name
    else:
        print(f"User '{username}' not found.")
        return []

    # Fetch latest tweets, excluding the retweets and replies because we're intereted only in the person's opinions
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "text"],
        exclude=["retweets", "replies"]
    )
    print([tweet.text for tweet in tweets.data])
    return [tweet.text for tweet in tweets.data] if tweets.data else []
