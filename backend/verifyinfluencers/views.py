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
        # TODO: Add function to extract and user's handle of Twitter (we can do that with Perplexity)
        username = extract_user_twitter_handle(name)
        tweets = fetch_tweets(username)
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
            hc = HealthClaim(
                claim=claim,
                category=categorized_claims[claim],
                verification_status=verification_status,
                trust_score=trust_score,
                sources=verification.get("source", "")
            )

            results.append({
                "claim": hc.text,
                "category": hc.category,
                "verification_status": hc.verification_status,
                "trust_score": hc.trust_score,
                "sources": hc.sources,
            })

        return Response(results)