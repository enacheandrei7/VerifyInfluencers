import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Influencer, HealthClaim
from .serializers import InfluencerSerializer, HealthClaimSerializer

# Create your views here.
class ClaimVerificationView(APIView):
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