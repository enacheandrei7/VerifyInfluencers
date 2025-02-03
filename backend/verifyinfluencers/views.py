import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import HealthClaim
from .services.twitter_service import fetch_tweets
from .services.perplexity_service import extract_and_categorize_health_claims, verify_health_claims, extract_user_twitter_handle

# Create your views here.
class FetchTweetsAndGetVerifiedClaims(APIView):
    def get(self, request, name):
        """Fetch tweets, extract health claims, categorize, verify, and return results."""

        username = extract_user_twitter_handle(name)
        if not username:
            return Response({"error": "No Twitter handle found for that user"}, status=404)

        tweets = fetch_tweets(username)
        if not tweets:
            return Response({"error": "No tweets found for the specified user."}, status=404)
        if type(tweets) != list:
            if tweets.status_code == 429:
                return Response({"error": "Too many Twitter/X requests."}, status=429)
            if tweets.status_code == 404:
                return Response({"error": "The provided name does not exist."}, status=404)

        # Get a list of dictionaries, each containing the claim and category
        categorized_claims = extract_and_categorize_health_claims(tweets)

        # Get a list of dictionaries containing the claims, categories, studies, trust scores and verification statuses
        verified_claims = verify_health_claims(categorized_claims)

        results = []
        for verified_claim_object in verified_claims:
            claim = verified_claim_object.get("claim", "")
            category = verified_claim_object.get("category", "Other")
            studies = verified_claim_object.get("studies", [])
            trust_score = verified_claim_object.get("trust_score", 50)
            verification_status = verified_claim_object.get("verification_status", "Questionable")

            # Save to database
            hc = HealthClaim.objects.create(
                claim=claim,
                category=category,
                verification_status=verification_status,
                trust_score=trust_score,
                sources=studies
            )

            results.append({
                "claim": hc.claim,
                "category": hc.category,
                "verification_status": hc.verification_status,
                "trust_score": hc.trust_score,
                "sources": hc.sources,
            })

        return Response(results)