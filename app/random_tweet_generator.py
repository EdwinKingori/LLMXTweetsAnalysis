import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random tweets


def generate_tweet(username):
    political_tweets = [
        f"@{username} Biden is failing us during #HurricaneHelene! We need better leadership!",
        f"@{username} Trump would have handled #HurricaneHelene differently. #MakeAmericaGreatAgain",
        f"@{username} Harris is nowhere to be seen during #HurricaneHelene. What's going on?",
        f"@{username} Pelosi needs to step up and help the victims of #HurricaneHelene!",
        f"@{username} Bill Gates is more focused on his money than helping hurricane victims. #HurricaneHelene",
        f"@{username} Elon Musk should use his wealth to support those affected by #HurricaneHelene!"
    ]

    neutral_tweets = [
        f"@{username} Stay safe everyone during #HurricaneHelene. Make sure to prepare!",
        f"@{username} The weather is really unpredictable. #HurricaneHelene",
        f"@{username} Hope everyone is doing well despite #HurricaneHelene.",
    ]

    profane_tweets = [
        f"@{username} This shitshow of a storm is ruining everything! #HurricaneHelene",
        f"@{username} What a fucked up situation with #HurricaneHelene! Stay safe, folks!",
        f"@{username} I'm so pissed off about the damage from #HurricaneHelene!",
    ]

    # Selecting a type of tweet based on random choice
    tweet_type = random.choice(['political', 'neutral', 'profane'])

    if tweet_type == 'political':
        return random.choice(political_tweets)
    elif tweet_type == 'neutral':
        return random.choice(neutral_tweets)
    else:
        return random.choice(profane_tweets)


# Generate the data
data = []
base_username = "user"
start_date = datetime.now()

for i in range(500):
    username = f"{base_username}{i+1}"
    tweet = generate_tweet(username)
    created_at = (
        start_date - timedelta(days=random.randint(0, 30))).strftime('%b %d')
    data.append([username, tweet, created_at])

# Create DataFrame
df = pd.DataFrame(data, columns=["username", "x-tweets", "created_at"])

# Display the DataFrame
print(df)

# save the DataFrame in a table format
df.to_csv("tweets.csv", index=False)