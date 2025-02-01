import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import HealthClaim
from .services.twitter_service import fetch_tweets
from .services.perplexity_service import extract_and_categorize_health_claims, verify_health_claim

# Create your views here.
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



class FetchClaims(APIView):
    def get(self, request, username):
        """Fetch tweets, extract health claims, categorize, verify, and return results."""
        # TODO: Add function to extract and user's handle of Twitter (we can do that with Perplexity)
        tweets = fetch_tweets(username)
        categorized_claims = extract_and_categorize_health_claims(tweets)

        results = []
        for claim in categorized_claims:
            verification = verify_health_claim(claim)
            trust_score = verification.get("trust_score", 50)
            status = verification.get("status", "Questionable")

            # Save to database
            hc = HealthClaim(
                text=claim,
                category=categorized_claims[claim],
                verification_status=status,
                trust_score=trust_score,
                source=verification.get("source", "")
            )

            results.append({
                "claim": hc.text,
                "category": hc.category,
                "verification_status": hc.verification_status,
                "trust_score": hc.trust_score,
                "sources": hc.sources,
            })

        return Response(results)