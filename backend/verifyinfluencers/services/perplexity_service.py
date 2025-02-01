import requests
import os
from django.conf import settings

PERPLEXITY_API_KEY = settings.PERPLEXITY_API_KEY


def extract_and_categorize_health_claims(tweets):
    """Use Perplexity API to extract and categorize health claims from tweets."""

    categories = ["Medicine", "Nutrition", "Mental Health", "Neuroscience", "Longevity", "Sleep", "Performance", "Stress Managemenr", "Endocrinology", "General Health", "Other"]
    query = (
        f"From the following tweets, identify any health-related claims and remove the duplicates. "
        f"For each claim, categorize it as one of the following: {categories}. The tweets list is: {tweets}"
    )

    url = "https://api.perplexity.ai/v1/completions"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}
    payload = {
        "model": "sonar",
        "messages": [{
            "role": "user",
            "content": query
    }]}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        results = response.json()
        print(f"The result JSON is: {results}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"The result TEST is: {response.text}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return results.get("answers", [])  # Extract structured health claims and categories
    else:
        return []  # Return empty list if request fails


def verify_health_claim(claim):
    """Verify a health claim against scientific journals using Perplexity API."""
    url = "https://api.perplexity.ai/v1/search"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}
    data = {"query": f"{claim} scientific study"}

    response = requests.post(url, headers=headers, json=data)

    return response.json()