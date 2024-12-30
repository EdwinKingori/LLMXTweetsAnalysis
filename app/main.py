from app.services import analyze_tweets

if __name__ == '__main__':
    analyzed_tweets = analyze_tweets()

    for result in analyzed_tweets:
        print(result.json())
