import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweet_ids = tweets[tweets['content'].str.len() > 15]['tweet_id']
    result=pd.DataFrame()
    result['tweet_id']=invalid_tweet_ids
    return result