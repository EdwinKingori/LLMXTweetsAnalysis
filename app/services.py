import instructor
from openai import OpenAI
from .database import SessionLocal
from .models import Tweet
from .schemas import TweetAnalysis
from instructor.exceptions import InstructorRetryException

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
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": f"Classify this tweet as political, offensive or neutral only if confident: '{tweet.x_tweets}'"
                }],
                response_model=TweetAnalysis
            )

        except InstructorRetryException as e:
            error_message = str(e)
            if 'exceed_quota' in error_message:
                print(
                    "Error: You exceeded your quota. Please check your billing details.")
            else:
                print(f"An error occured: {error_message}")
            break
        except Exception as e:
            print(f"An error occured: {str(e)}")

        analysis_result = TweetAnalysis(
            id=tweet.id,
            text=tweet.x_tweets,
            isPolitical=response.get("isPolitical", False),
            isOffensive=response.get("isOffensive", False),
            isNeutral=response.get("isNeutral", False),
        )

        results.append(analysis_result)

    return results
