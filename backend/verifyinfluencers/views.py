import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Influencer, HealthClaim
from .serializers import InfluencerSerializer, HealthClaimSerializer
from .services.twitter_service import fetch_tweets
from .services.listennotes_service import search_podcast_episodes

# Create your views here.
class ClaimVerificationView(APIView):
    """
    View used to ...
    """
    def post(self, request):
        claim_text = request.data.get("text")

        # Call Perplexity API (mocked response)
        result = {"status": "Debunked", "trust_score": 2.5, "sources": ["Journal of Medicine 2023"]}

        return Response({
            "text": claim_text,
            "status": result["status"],
            "trust_score": result["trust_score"],
            "sources": result["sources"]
        })

class FetchTweetsView(APIView):
    """
    API Endpoint to fetch recent tweets from an influencer.
    """
    def get(self, request, username):
        print(JsonResponse({"message": f"Fetching tweets for {username}"}))
        tweets = fetch_tweets(username, max_results=30)
        print(tweets)
        if not tweets:
            return Response({"error": "No tweets found or API error"}, status=404)

        return Response({"username": username, "tweets": tweets})



class FetchPodcastsView(APIView):
    """
    API Endpoint to fetch recent tweets from an influencer.
    """
    def get(self, request, name):
        print(JsonResponse({"message": f"Fetching tweets for {name}"}))
        podcasts = search_podcast_episodes(name, max_results=10)
        print(podcasts)
        if not podcasts:
            return Response({"error": "No podcasts found or API error"}, status=404)

        return Response({"name": name, "podcasts": podcasts})