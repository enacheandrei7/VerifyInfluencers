import requests
import os
import json
import re
from django.conf import settings
from pydantic import BaseModel
from typing import Literal

from rest_framework.response import Response

PERPLEXITY_API_KEY = settings.PERPLEXITY_API_KEY

# class CategoryAndClaimAnswerFormat(BaseModel): # This doesn't work for normal users,o nly tier-3
#     tweet: str
#     claim: str
#     category: str


# class VerifiedClaimAnswerFormat(BaseModel):
#     claim: str
#     category: str
#     studies_names: list
#     studies_links: list
#     trust_score: str
#     verification_status: Literal["Verified", "Debunked", "Questionable"]
#     # TODO: Do a response model for the answer here. Result from Perplexity now:


def extract_and_categorize_health_claims(tweets):
    """Use Perplexity API to extract and categorize health claims from tweets."""

    categories = ["Medicine", "Nutrition", "Mental Health", "Neuroscience", "Longevity", "Sleep", "Performance", "Stress Managemenr", "Endocrinology", "General Health", "Other"]
    system_query = "Please return the result in the following JSON Format, without any other text: {\"health_related_claims\": [{\"claim\": \"Some claim here\", \"category\": \"Some category\"}]}"
    user_query = (
        f"From the following tweets, identify any health-related claims and remove the duplicates. "
        f"For each claim, categorize it as one of the following: {categories}. The tweets list is: {tweets}.")

    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}
    payload = {
        "model": "sonar",
        "messages": [
                        {
                            "role": "system",
                            "content": system_query
                        },
                        {
                            "role": "user",
                            "content": user_query
                        }
                    ],
                }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        results = response.json()
        perplexity_response_string_in_json_format = results.get("choices", [])[0].get("message", {}).get("content")
        perplexity_response_json = json.loads(perplexity_response_string_in_json_format)
        claim_and_category = perplexity_response_json.get("health_related_claims", [])
        return claim_and_category  # Extract structured health claims and categories
    else:
        return []  # Return empty list if request fails


def verify_health_claims(claims_and_categories):
    """Verify a health claim against scientific journals using Perplexity API."""
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}

    system_query =  "Return the result in the following JSON format: {\"claims\": [{\"claim\": \"Some claim here\", \"category\": \"Some category\", \"studies\": [{\"study_name\": \"Study name 1\", \"study_link\": \"Study Link 1\"}], \"trust_score\": \"Some number\", \"verification_status\": \"Some verification status\"}]}"
    user_query = f"Taking the following list of claims and categories: {claims_and_categories}, find referencing journals that affirm or debunk those claims. Return the claims together with the referencing articles, generate a trust score between 0-100 for each claim and give it one of the following statuses:  Verified, Debunked, Questionable"

    data = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": system_query
            },
            {
                "role": "user",
                "content": user_query
            }
                    ]
        }

    perplexity_response = requests.post(url, headers=headers, json=data)

    if perplexity_response.status_code == 200:
        results = perplexity_response.json()
        perplexity_response = results.get("choices", [])[0].get("message", {}).get("content")

        perplexity_response_json_string = extract_json(perplexity_response)
        perplexity_response_json = json.loads(perplexity_response_json_string)
        verified_claims = perplexity_response_json.get("claims", [])
        return verified_claims  # Extract structured health claims and categories
    else:
        return []  # Return empty list if request fails


def extract_user_twitter_handle(name):
    """Use Perplexity API to extract and categorize health claims from tweets."""

    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}

    system_query = "Return only the Twitter username of the user in the format 'username' by removing the leading '@'."
    user_query = f"Taking the following name: {name}, return the health influencer with that name on Twitter/X. " \
                 f"If the provided username is a Twitter hanlde just return it back. " \
                 f"If no user is found, return 'can't find an user'"

    data = {
        "model": "sonar-pro",
        "messages": [
            {
                "role": "system",
                "content": system_query
            },
            {
                "role": "user",
                "content": user_query
            }
                    ]
    }

    print("Preparing to extract the user...")
    response = requests.post(url, headers=headers, json=data)
    print("Checking if the perplexity has found a proper response...")

    if response.status_code == 200:
        results = response.json()
        twitter_handle = results.get("choices", [])[0].get("message", {}).get("content")
        if len(twitter_handle.replace(" ", "")) != len(twitter_handle):
            print(f"No twitter handle found for the specified user.")
            return ""
        print(f"The found user is: {twitter_handle}")
        return twitter_handle
    else:
        print("No name found for the specified user.")
        return ""  # Return empty value if user not found


def extract_json(text):
    """
    Method used to get the JSON object from the perplexity API response.
    """
    pattern = r'\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}'  # Handles nested {}
    match = re.search(pattern, text, re.DOTALL)
    return match.group(0) if match else None