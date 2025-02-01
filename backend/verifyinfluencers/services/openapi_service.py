from openai import OpenAI
from django.conf import settings

OPENAI_API_KEY = settings.OPENAI_API_KEY


# Even though  OpenAI is better to summarize + put in categories, it costs
def extract_health_claims(texts):
    """Identify health-related claims from tweets using OpenAI."""
    prompt = f"Extract and list health-related claims from the following tweets and remove duplicates if there are any:\n{texts}"

    client = OpenAI(api_key=OPENAI_API_KEY)
    completion  = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"The completion from EXTRACT_HEALTH_CLAIMS is: \n =============================================================== \n {completion}")
    return completion["choices"][0]["message"]["content"].split("\n")


def categorize_claims(claims):
    """Categorize each health claim into predefined categories."""
    categories = ["Medicine", "Nutrition", "Mental Health", "Neuroscience", "Longevity", "Sleep", "Performance", "Stress Managemenr", "Endocrinology", "General Health"]

    prompt = f"Categorize these claims into {categories}:\n{claims}"

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"The completion from CATEGORIZE_CLAIMS is: \n =============================================================== \n {completion}")
    return completion["choices"][0]["message"]["content"]