from pydantic import BaseModel, Field


class TweetAnalysis(BaseModel):
    id: int = Field(description="The id of the tweet")
    text: str = Field(description="The content of the tweet")
    isPolitical: bool = Field(
        description="indicates if the tweet is political")
    isOffensive: bool = Field(
        description="indicates if the tweet is offensive")
    isNeutral: bool = Field(description="indicates if the tweet is neutral")

    class config:
        orm_mode = True
