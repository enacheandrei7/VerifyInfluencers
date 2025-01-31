import requests
import tweepy
from django.conf import settings

# DEPRECATED: THIS DOESN'T WORK  FOR FREE TO USE APIS
LISTEN_NOTES_API_KEY  = settings.LISTEN_NOTES_API_KEY


def search_podcast_episodes(person_name, max_results=10):
    """
    Search for podcast episodes mentioning a person's name.
    :param person_name: Name of the person
    :param max_results: Number of podcasts to fetch.
    :return: List of podcasts transcript
    """

    url = "https://listen-api.listennotes.com/api/v2/search"
    headers = {"X-ListenAPI-Key": LISTEN_NOTES_API_KEY}
    params = {
        "q": "Andrew Huberman",
        "sort_by_date": 0,  # 0 = relevance, 1 = newest first
        "type": "episode", # default: episode
        "language": "English",
        "offset": 0,
        "len_min": 5,  # Minimum length (5 minutes)
        "safe_mode": 0,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        episodes = data.get("results", [])

        # episodes_ids = [episode["id"] for episode in episodes]

        # print(f"The KEYS are: {episodes[0].keys()}")
        return [
            {
                "title": ep.get("title_original", ""),
                "id": ep.get("id", ""),
                "podcast": ep.get("podcast_title_original", ""),
                "audio": ep.get("audio", ""),
                "transcript_url": ep.get("transcripts", "None"),
                "description": ep.get("description_original", ""),
                "transcript": fetch_podcast_transcript(ep.get("id", "")),
                "transctipr_ok": ep.get("transcript", "")
            }
            for ep in episodes[:max_results]
        ]

    print(f"Error: {response.status_code} - {response.json()}")
    return []


def fetch_podcast_transcript(episode_id):
    """Fetch the transcript text from the episode id."""
    url = f"https://listen-api.listennotes.com/api/v2/episodes/{episode_id}"
    headers = {"X-ListenAPI-Key": LISTEN_NOTES_API_KEY}
    params = {
        "show_transcript": 1,
    }

    response = requests.get(url, headers=headers, params=params)
    print(response.json())

    if response.status_code == 200:
        data = response.json()
        transcript = data.get("transcript", "")
        return transcript

    return "Failed to fetch transcript."