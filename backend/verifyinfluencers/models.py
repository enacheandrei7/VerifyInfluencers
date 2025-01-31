from django.db import models

# Create your models here.
class Influencer(models.Model):
    """
    Class used to create the Influencer object.
    """
    username = models.CharField(max_length=255, unique=True)
    followers = models.IntegerField()
    topics = models.JSONField()
    trust_score = models.FloatField(default=0)

class HealthClaim(models.Model):
    """
    Class used to create the Health Claim object.
    """
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    text = models.TextField()
    category = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('Verified', 'Verified'), ('Debunked', 'Debunked'), ('Questionable', 'Questionable')])
    trust_score = models.FloatField(default=0)
    sources = models.JSONField()
