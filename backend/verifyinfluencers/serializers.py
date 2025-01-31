from rest_framework import serializers
from .models import Influencer, HealthClaim

class InfluencerSerializer(serializers.ModelSerializer):
    """
    Class used to serialize the Influencer model.
    """
    class Meta:
        model = Influencer
        fields = '__all__'

class HealthClaimSerializer(serializers.ModelSerializer):
    """
    Class used to serialize the HealthClaim model.
    """
    class Meta:
        model = HealthClaim
        fields = '__all__'