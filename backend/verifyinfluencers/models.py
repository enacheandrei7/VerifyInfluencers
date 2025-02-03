from django.db import models

# Create your models here.
class Influencer(models.Model):
    """
    Class used to create the Influencer object.
    """
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    topics = models.JSONField()

    def __str__(self):
        return str(self.username)

class HealthClaim(models.Model):
    """
    Class used to create the Health Claim object.
    """
    influencer = models.ForeignKey(Influencer, related_name="healthclaims", on_delete=models.CASCADE)
    claim = models.TextField()
    category = models.CharField(max_length=255)
    verification_status = models.CharField(max_length=50, choices=[('Verified', 'Verified'), ('Debunked', 'Debunked'), ('Questionable', 'Questionable')])
    trust_score = models.IntegerField(default=0)
    sources = models.JSONField(default=list, blank=True) # Stores list of dictionaries with link & name

    def __str__(self):
        return self.claim
