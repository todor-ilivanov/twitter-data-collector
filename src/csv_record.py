import datetime as dt
from collections import Counter 
from statistics import pstdev 

class CsvRecord:
  userid = None
  user_profile_description = None	
  follower_count = None	
  following_count = None	
  account_creation_date = None	
  account_language = None	
  ratio_follower_to_following = None	
  descr_len = None	
  days_since_creation = None	
  avg_tweet_len = None	
  avg_hashtag_num = None	
  avg_hashtag_char_num = None	
  avg_mentions_num = None	
  avg_urls_num = None	
  tweet_url_ratio = None
  retweet_rate = None
  retweet_url_ratio = None	
  tweet_std = None
  avg_tweets_per_day = None	

  def __str__(self):
    record_string = f'{self.userid},{self.user_profile_description},{self.follower_count}, \
        {self.following_count},{self.account_creation_date},{self.account_language}, \
        {self.ratio_follower_to_following},{self.descr_len},{self.days_since_creation}, \
        {self.avg_tweet_len},{self.avg_hashtag_num},{self.avg_hashtag_char_num}, \
        {self.avg_mentions_num},{self.avg_urls_num},{self.tweet_url_ratio}, \
        {self.retweet_rate},{self.retweet_url_ratio},{self.tweet_std},{self.avg_tweets_per_day}'

    return ' '.join(record_string.split())

def average(lst):
  return sum(lst) / len(lst) if len(lst) > 0 else 0

def reformat_date(date_str):
  date_format_old = '%a %b %d %H:%M:%S %z %Y'
  date_format_new = '%d/%m/%Y'
  return dt.datetime.strptime(date_str, date_format_old).strftime(date_format_new)

def follower_following_ratio(follower_count, following_count):
  return follower_count / following_count if following_count > 0 else 0

def days_since_creation(date_str):
  baseline = dt.date(2019, 1, 1)
  date = dt.datetime.strptime(date_str, '%d/%m/%Y').date()
  return (baseline - date).days

def avg_tweet_len(tweets):
  tweets_len = [len(t.text) for t in tweets]
  return average(tweets_len)

def avg_hashtag_num(tweets):
  hashtags = [len(t.hashtags) for t in tweets]
  return average(hashtags)

def avg_hashtag_char_num(tweets):
  hashtags_len = [len(h.text) for t in tweets for h in t.hashtags]
  return average(hashtags_len)

def avg_mentions_num(tweets):
  mentions = [len(t.user_mentions) for t in tweets]
  return average(mentions)

def avg_urls_num(tweets):
  urls = [len(t.urls) for t in tweets]
  return average(urls)

def avg_tweets_per_day(tweets):
  tweet_dates = [reformat_date(t.created_at) for t in tweets]
  num_occurrences_per_day = Counter(tweet_dates).values()
  return average(num_occurrences_per_day)

def tweet_url_ratio(tweets):
  tweets_with_url = [t for t in tweets if len(t.urls) > 0]
  return len(tweets_with_url) / len(tweets)

def retweet_rate(tweets):
  # From Twitter API Docs:
  # Retweets can be distinguished from typical Tweets
  # by the existence of a retweeted_status attribute
  retweets = [t for t in tweets if t.retweeted_status != None]
  return len(retweets) / len(tweets)

def retweet_url_ratio(tweets):
  retweets = [t for t in tweets if t.retweeted_status != None]
  retweets_with_url = [r for r in retweets if len(r.urls) > 0]
  return len(retweets_with_url) / len(tweets)

def tweet_std(tweets):
  tweet_dates = [reformat_date(t.created_at) for t in tweets]
  num_occurrences_per_day = Counter(tweet_dates).values()
  return pstdev(num_occurrences_per_day) #ddof=0