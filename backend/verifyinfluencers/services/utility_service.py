from verifyinfluencers.models import Influencer, HealthClaim


def get_or_create_influencer(username, name, topics):
    influencer, created = Influencer.objects.get_or_create(
        username=username,
        defaults={"name": name},
    )
    for topic in topics:
        influencer.topics.append(topic)
    influencer.save()

    return influencer


def add_health_claim(influencer, claim_text, category, verification_status, trust_score, sources):
    health_claim = HealthClaim.objects.get_or_create(
        influencer=influencer,
        claim=claim_text,
        category=category,
        verification_status=verification_status,
        trust_score=trust_score,
        sources=sources
    )
    return health_claim