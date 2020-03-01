import twitter
import time
from src.csv_record import *

class CsvRecordCreator:
  
  api = None

  def __init__(self):
    self.api = twitter.Api(consumer_key='WyIVvrJqu6qVC3zhi0RiZRwEY',
                      consumer_secret='6pcdAv3OwskVnWhWvzsaFDfohWw3OtyUT1jAzdjvAkGSdj62Lp',
                      access_token_key='321185042-a6KcC4MGwHwOc5OGm6J6LNeV5qqIE4omI5tJqCH9',
                      access_token_secret='I3H6fqciOVeGaRHKfoRRITx8OJx1qsLheLPok7wiraBO4',
                      sleep_on_rate_limit=True) # sleeps for 15 min if rate limit is reached

  def tweet_api_request(self, user_id, screen_name, count):
    try:
      if user_id <= 0:
        raise ValueError('User id <= 0.')
      return self.api.GetUserTimeline(user_id=user_id, count=count)
    except twitter.error.TwitterError:
      if screen_name == '':
        raise ValueError('Screen name is blank.')
      return self.api.GetUserTimeline(screen_name=screen_name, count=count)

  def create_csv_record(self, user_id, screen_name):
    try:
      tweets = self.tweet_api_request(user_id, screen_name, count=200)
      if tweets == []:
        raise twitter.error.TwitterError('Empty tweets object.')

      user = tweets[0].user
      record = CsvRecord()
      record.userid = user.id_str
      record.user_profile_description = user.description.replace(',', '')
      record.follower_count = user.followers_count
      record.following_count = user.friends_count
      record.account_creation_date = reformat_date(user.created_at)
      record.account_language = user.lang or 'en'
      record.ratio_follower_to_following = round(
        follower_following_ratio(record.follower_count, record.following_count), 5 
      )
      record.descr_len = len(user.description)
      record.days_since_creation = days_since_creation(record.account_creation_date)
      
      record.avg_tweet_len = round(avg_tweet_len(tweets), 5)
      record.avg_hashtag_num = round(avg_hashtag_num(tweets), 5)
      record.avg_hashtag_char_num = round(avg_hashtag_char_num(tweets), 5)
      record.avg_mentions_num = round(avg_mentions_num(tweets), 5)
      record.avg_urls_num = round(avg_urls_num(tweets), 5)
      record.avg_tweets_per_day = round(avg_tweets_per_day(tweets), 5)
      record.tweet_url_ratio = round(tweet_url_ratio(tweets), 5)
      record.retweet_rate = round(retweet_rate(tweets), 5)
      record.retweet_url_ratio = round(retweet_url_ratio(tweets), 5)
      record.tweet_std = round(tweet_std(tweets), 5)
      
      #print(str(record))
      return record
    except twitter.error.TwitterError as error:
      print(error)
    except ValueError as error:
      print(str(error))

# creator = CsvRecordCreator()
# r = creator.create_csv_record(1, 'frankarr')
# print(r)