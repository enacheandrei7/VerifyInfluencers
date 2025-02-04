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

#     dummy_response = """
#  Here is the response in the requested JSON format, with claims, categories, referencing studies, trust scores, and verification statuses:
#
# ```json
# {
#   "claims": [
#     {
#       "claim": "Certain foods are designed to make you ingest more via gut-to-brain dopamine signaling, contributing to obesity.",
#       "category": "Nutrition",
#       "studies": [
#         {
#           "study_name": "Neuromicrobiology, an emerging neurometabolic facet of the gut",
#           "study_link": "https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1098412/full"
#         }
#       ],
#       "trust_score": 70,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Foods labeled as 'heart healthy' may not be due to their ingredients and effects on consumption.",
#       "category": "Nutrition",
#       "studies": [
#         {
#           "study_name": "Promoting a Healthy Microbiome with Food and Probiotics",
#           "study_link": "https://www.va.gov/WHOLEHEALTHLIBRARY/tools/promoting-healthy-microbiome-with-food-probiotics.asp"
#         }
#       ],
#       "trust_score": 60,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Improving decision making can enhance performance.",
#       "category": "Performance",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Dopamine regulation impacts motivation and drive.",
#       "category": "Mental Health",
#       "studies": [
#         {
#           "study_name": "Dopamine regulates the motivation to act",
#           "study_link": "https://www.sciencedaily.com/releases/2013/01/130110094415.htm"
#         },
#         {
#           "study_name": "How does dopamine regulate both learning and motivation?",
#           "study_link": "https://www.sciencedaily.com/releases/2023/06/230606111734.htm"
#         }
#       ],
#       "trust_score": 90,
#       "verification_status": "Verified"
#     },
#     {
#       "claim": "Sleep is a critical health topic.",
#       "category": "Sleep",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Food impacts mood through macro and micronutrients.",
#       "category": "Nutrition",
#       "studies": [
#         {
#           "study_name": "Neuromicrobiology, an emerging neurometabolic facet of the gut",
#           "study_link": "https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1098412/full"
#         }
#       ],
#       "trust_score": 80,
#       "verification_status": "Verified"
#     },
#     {
#       "claim": "Awareness and tools can aid in stress mitigation and overall health.",
#       "category": "Stress Management",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Cardiovascular and muscular strength are important health topics.",
#       "category": "General Health",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     }
#   ]
# }
# ```"""
#     return dummy_response
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

#     perplexity_response = """ Here is the response in the requested JSON format, with claims, categories, referencing studies, trust scores, and verification statuses:
# 
# ```json
# {
#   "claims": [
#     {
#       "claim": "Certain foods are designed to make you ingest more via gut-to-brain dopamine signaling, contributing to obesity.",
#       "category": "Nutrition",
#       "studies": [
#         {
#           "study_name": "Neuromicrobiology, an emerging neurometabolic facet of the gut",
#           "study_link": "https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1098412/full"
#         }
#       ],
#       "trust_score": 70,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Foods labeled as 'heart healthy' may not be due to their ingredients and effects on consumption.",
#       "category": "Nutrition",
#       "studies": [
#         {
#           "study_name": "Promoting a Healthy Microbiome with Food and Probiotics",
#           "study_link": "https://www.va.gov/WHOLEHEALTHLIBRARY/tools/promoting-healthy-microbiome-with-food-probiotics.asp"
#         }
#       ],
#       "trust_score": 60,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Improving decision making can enhance performance.",
#       "category": "Performance",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Dopamine regulation impacts motivation and drive.",
#       "category": "Mental Health",
#       "studies": [
#         {
#           "study_name": "Dopamine regulates the motivation to act",
#           "study_link": "https://www.sciencedaily.com/releases/2013/01/130110094415.htm"
#         },
#         {
#           "study_name": "How does dopamine regulate both learning and motivation?",
#           "study_link": "https://www.sciencedaily.com/releases/2023/06/230606111734.htm"
#         }
#       ],
#       "trust_score": 90,
#       "verification_status": "Verified"
#     },
#     {
#       "claim": "Sleep is a critical health topic.",
#       "category": "Sleep",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Food impacts mood through macro and micronutrients.",
#       "category": "Nutrition",
#       "studies": [
#         {
#           "study_name": "Neuromicrobiology, an emerging neurometabolic facet of the gut",
#           "study_link": "https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1098412/full"
#         }
#       ],
#       "trust_score": 80,
#       "verification_status": "Verified"
#     },
#     {
#       "claim": "Awareness and tools can aid in stress mitigation and overall health.",
#       "category": "Stress Management",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     },
#     {
#       "claim": "Cardiovascular and muscular strength are important health topics.",
#       "category": "General Health",
#       "studies": [],
#       "trust_score": 50,
#       "verification_status": "Questionable"
#     }
#   ]
# }
# ```
# """
#     perplexity_response_json_string = extract_json(perplexity_response)
#     perplexity_response_json = json.loads(perplexity_response_json_string)
#     verified_claims = perplexity_response_json.get("claims", [])
#     return verified_claims  # Extract structured health claims and categories

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
    #TODO: Delete this
    # return 'ChrissyChris'
    url = "https://api.perplexity.ai/chat/completions"
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}

    system_query =  "Return only the username of the user in the format 'username'. Remove the leading '@'."
    user_query = f"Taking the following name: {name}, return the health influencer with that name on Twitter/X. If no user is found, return 'can't find an user'"

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

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        results = response.json()
        twitter_handle = results.get("choices", [])[0].get("message", {}).get("content")
        if len(twitter_handle.replace(" ", "")) != len(twitter_handle):
            print(f"No twitter handle found for the specified user.")
            return ""
        print(f"The found user is: {twitter_handle}")
        return twitter_handle
    else:
        return ""  # Return empty value if user not found


def extract_json(text):
    """
    Method used to get the JSON object from the perplexity API response.
    """
    pattern = r'\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}'  # Handles nested {}
    match = re.search(pattern, text, re.DOTALL)
    return match.group(0) if match else None