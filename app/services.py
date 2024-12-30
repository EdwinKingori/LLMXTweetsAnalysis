import instructor
from openai import OpenAI
from .database import SessionLocal
from .models import Tweet
from .schemas import TweetAnalysis

# initializing the client
client = instructor.from_openai(OpenAI())


def analyze_tweets():
    results = []
    session = SessionLocal()

    # retrieve tweets from db
    tweets = session.query(Tweet).all()


#  creating a for loop that iterates over each tweet in the db
#  And for each tweet, a message should be constructed and sent over to the desired LLM.
#  In this case, the model used is "gpt-4o-mini" using a response prompt

    for tweet in tweets:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Classify this tweet as political, offensive or neutral only if confident: '{tweet.text}'"
            }],
        )

        analysis_result = TweetAnalysis(
            id=tweet.id,
            text=tweet.text,
            isPolitical=response.get("isPolitical", False),
            isOffensive=response.get("isOffensive", False),
            isNeutral=response.get("isNeutral", False),
        )

        results.append(analysis_result)

    return results
