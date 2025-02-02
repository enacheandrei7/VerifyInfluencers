import requests
import tweepy
from django.conf import settings

TWITTER_BEARER_TOKEN = settings.TWITTER_BEARER_TOKEN


def fetch_tweets(username, max_results=10):
    """
    Fetch recent tweets from a given influencer.
    :param username: Twitter handle of the influencer
    :param limit: Number of tweets to fetch (default 10)
    :return: List of tweet texts
    """

    andrew_huberman_tweets = [
        "Over the last 20 years, there’s been a progressive move toward funding work that is basically already completed. It’s caused a lot of projects that could’ve made major discoveries to not get funded. Anyone who’s been on a grant study section @NIH knows what I’m referring to.",
        "• Basic research is vital for new biomedical discoveries\n• There is a lot redundant science funded by @NIH \n• They should fund bolder (yet safe) work\n• Newer labs should be prioritized; the new blood brain drain from US science is a real concern",
        "The mechanisms are well known, and not controversial. But we are not taught about these.",
        "Once you realize how certain foods are designed to make you ingest more of them via gut-to-brain (unconscious) dopamine signaling you will see how they literally control you from the inside. We are an obese, not a lazy country. Knowledge on this = power.",
        "Obviously fruit, vegetables, lean meat, chicken &amp; eggs, quality starches with minimal ingredients are the exception.",
        "Most foods labeled “heart  healthy” should be labeled “heart healthy to not consume this”. This is true based on the direct effects of some of the ingredients, and indirect effects of how consumption of those foods makes people eat too much/become obese.",
        "You can find the full episode here @X pinned @hubermanlab &amp; linked to all other platforms, all zero cost &amp; timestamped: https://t.co/nRzbKarViC",
        "Improving decision making markedly by reversing awareness of mistakes. Josh Waitzkin explains how he applied this in chess &amp; it’s applicability to all strategic decision making &amp; to avoid catastrophe. From the Huberman Lab podcast out now zero cost here @X &amp; all other platforms. https://t.co/LIagtzzjyZ",
        "New Huberman Lab Essentials (key, actionable takeaways in 30min format), out now. SCIENCE &amp; PROTOCOLS for MOTIVATION &amp; DRIVE • (incl. Dopamine Regulation by Behaviors &amp; Pharmacology) https://t.co/O2hhgFVIAO",
        "Never thought I would hear the words “Are you supportive of these onsies?!” in a US senate hearing.",
        "To be clear, I think most all reviewers acting in good faith, but there’s a sociology to the process and in the last decade it’s really hurt young investigators. I say this from the perspective of somebody who never really had too much trouble getting my grants. I also had a lot… https://t.co/h01RuacBEo",
        "You might ask who decides what’s derivative. I can comment on this (I held and reviewed NIH grants for &gt;decade). There is too much overlap of topics BUT basic research implications for medicine are hard to predict. A shift towards more gutsy (&amp; safe) research and move away from… https://t.co/umY48nRehI",
        "My phone has been blowing up about this @NIH freeze. Here are my predictions (again):\n1) indirect payments will be cut to a flat rate\n2) overall budget won’t change\n(with #1 that means more grants) \n3) work deemed derivative gets axed \n4) $ resumes once new leadership confirmed",
        "I’d like to state again that I am of the belief that basic research is the bedrock of discovery leading to novel therapeutics. While not all research is created equally- and I do think there’s a lot of derivative nonsense that gets funded, the essential and truly great work is… https://t.co/qL7yvRCMJF",
        "For those that don’t understand number 3, currently the amount of money going to an institution for each grant depends on the overhead rate for that in institution. It varies widely. This has been a point of contention for a number of years.",
        "My Predictions: \n1) @NIH study sections will recommence once the new @HHSGov leadership is approved. \n2) The overall @NIH budget won’t be cut\n3) Overhead/indirects will be a flat rate\n4) Institute (re)structure will change in the next 4 years.",
        "In addition to X, this episode with Josh Waitzkin can be found at the links below:  \n\nHuberman Lab site: https://t.co/INTbL1nqyf\nYouTube: https://t.co/boWoPvKUma\nApple Podcasts: https://t.co/tJb1xagC50\nSpotify: https://t.co/2nQSj2I8sG https://t.co/UKmjbc03zz",
        "The new Huberman Lab episode is out: Josh Waitzkin: The Art of Learning &amp; Living Life\n\nThis episode is available in full on X, YouTube, and all podcast platforms.\n\n(0:00) Josh Waitzkin\n(3:21) Chess, Competition &amp; Performance\n(10:50) Martial Arts, Tai Chi, Jiu-Jitsu, Foiling,… https://t.co/1dsHuoca5v https://t.co/ItMoTfCLjF",
        "The incredible Josh Waitzkin (former chess prodigy, martial artist, author of The Art of Learning &amp; so much more) is my guest on the Huberman Lab podcast out tomorrow. We talk peak performance &amp; how to master deep principles of learning hard things. https://t.co/gW3N7HILDE",
        "I actually give Marc a 7/10 on his health protocol adherance (docked 3 for the light/sleep stuff) because his vigor &amp; processing speed is 11/10 now &amp; it’s scary to think what might happen if it increased. That said, I’m happy to hear I’ve reduced his levels of joy in favor of his… https://t.co/1EDrs4Sbm5",
        "“It’s a test of manhood as to\nwhether you can have a blue screen in your face for 3hrs and then go right to sleep.” \n- @pmarca (on new @lexfridman podcast) https://t.co/qQbytMfSTL",
        "This obviously is just a partial list, microbiome, stress mitigation, and on and on. It all starts with awareness (which sounds so hippy but it’s true) and the new breed of health is to test and use tools that impart agency. And to embrace the reality that tools can be… https://t.co/RNkmCzmj7y",
        "Health topics that people are finally starting to take seriously:\n1) sleep\n2) dopamine &amp; reinforcement \n3) food, water &amp; air “cleanliness”\n4) cardiovascular &amp; muscular strength\n5) alcohol \n6) bio-measurements\nGrateful to all learning &amp; sharing health knowledge &amp; protocols.",
        "Of the face.",
        "Turns out it’s in the cheeks.",
        "I had a guest on Huberman Lab podcast yesterday expert on the neural circuits of human-human interactions &amp; hormones. One thing was made certain: men and women interact very differently when women are ovulating, even if the men are not consciously aware of it. Episode soon.",
        "New Episode of Huberman Lab Essentials episode: How Food Impacts Mood (via macro and micronutrients). 30min. Duration. Essential Protocols &amp; Science only. https://t.co/8pwJAyMxDU",
        "We had a great conversation indeed.  \nSee you soon @bryan_johnson ! https://t.co/bos7DDZDMK",
        "Did you watch the last House Appropriations mtg. with @NIHDirector? I did &amp; I took notes. Key discoveries made in recent years were discussed but the *fundamental mismatch in ideology re what the @NIH should fund* was also raised. The division was stark.\nhttps://t.co/PzPGyhhn8q",
        "I am told that @NIH grant review panel dates (these always are scheduled 3-6mo ahead) are getting cancelled left and right (no pun). Does anyone know what this is about? @DrJBhattacharya @RobertKennedyJr"
    ]
    return andrew_huberman_tweets


    client = tweepy.Client(TWITTER_BEARER_TOKEN)
    try:
        pass
    except:
        pass

    # Use the handle of the user to retrieve their ID
    user = client.get_user(username=username, user_auth=False)
    print(f'The user is: {user}')

    user_id = ''
    if user.data:
        # Get user ID
        user_id = user.data.id
        name = user.data.name
    else:
        print(f"User '{username}' not found.")
        return []

    print("Preparing to get the user's tweets...")
    # Fetch latest tweets, excluding the retweets and replies because we're intereted only in the person's opinions
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=["created_at", "text"],
        exclude=["retweets", "replies"]
    )
    # print([tweet.text for tweet in tweets.data])
    return [tweet.text for tweet in tweets.data] if tweets.data else []
