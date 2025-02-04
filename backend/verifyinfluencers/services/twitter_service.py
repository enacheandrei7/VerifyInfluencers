import requests
import tweepy
from django.conf import settings
from rest_framework.response import Response
from .utility_service import get_or_create_influencer

TWITTER_BEARER_TOKEN = settings.TWITTER_BEARER_TOKEN


def fetch_tweets(username, api_key: str = "", max_results=5):
    """
    Fetch recent tweets from a given influencer.
    :param username: Twitter handle of the influencer
    :param api_key: Optional API key from the user
    :param max_results: Max tweets
    :return: List of tweet texts
    """

    if api_key:
        client = tweepy.Client(api_key)
    else:
        client = tweepy.Client(TWITTER_BEARER_TOKEN)
    try:
        # Use the handle of the user to retrieve their ID
        user = client.get_user(username=username, user_auth=False)
        print(f'The user is: {user}')
    except tweepy.TooManyRequests as exc:
        print(exc)
        return Response({"error": "Too many requests."}, status=429)
    except tweepy.NotFound as exc:
        print(exc)
        return Response({"error": "The provided name does not exist."}, status=404)
    except tweepy.BadRequest as exc:
        print(exc)
        return Response({"error": "The provided name does not exist."}, status=404)
    except tweepy.errors.Unauthorized as exc:
        print(exc)
        return Response({"error": "Unauthorized."}, status=401)

    if user.data:
        # Get user ID
        user_id = user.data.id
        name = user.data.name
    else:
        print(f"User '{username}' not found.")
        return []

    print("Preparing to get the user's tweets...")
    # Fetch latest tweets, excluding the retweets and replies because we're intereted only in the person's opinions
    try:
        tweets = client.get_users_tweets(
            id=user_id,
            max_results=max_results,
            tweet_fields=["created_at", "text"],
            exclude=["retweets", "replies"]
        )
        print("Tweets obtained successfully.")
    except tweepy.TooManyRequests:
        return Response({"error": "Too many requests."}, status=429)
    except tweepy.NotFound:
        return Response({"error": "No tweets found for the specified user."}, status=404)

    influencer = get_or_create_influencer(
        username=username,
        name=name,
        topics=[]
    )
    return [tweet.text for tweet in tweets.data] if tweets.data else []
