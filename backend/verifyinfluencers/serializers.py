from rest_framework import serializers
from .models import Influencer, HealthClaim


class HealthClaimSerializer(serializers.ModelSerializer):
    """
    Class used to serialize the HealthClaim model.
    """
    class Meta:
        model = HealthClaim
        fields = ['claim', 'category', 'verification_status', 'trust_score', 'sources']


class InfluencerSerializer(serializers.ModelSerializer):
    """
    Class used to serialize the Influencer model.
    """
    healthclaims = HealthClaimSerializer(many=True, read_only=True)

    class Meta:
        model = Influencer
        fields = ['username', 'name', 'topics', 'healthclaims']
