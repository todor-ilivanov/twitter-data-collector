import pytest
from unittest.mock import MagicMock, Mock
from test.tweet_stub import *
from src.csv_record import CsvRecord
from src.csv_record_creator import CsvRecordCreator
from src.input_arguments_error import InputArgumentsError
from twitter import TwitterError

def mock_api_response():
  user = User(id_str="1234", 
              description="I am a twitter user.",
              followers_count=100,
              friends_count=50,
              created_at="Sat Jan 01 23:33:24 +0000 2018",
              lang="bg")

  tweet1 = Tweet(text="Hi", 
                hashtags=[Hashtag("hi"), Hashtag("sup")], 
                user_mentions=[Mention("jack"), Mention("todor"), Mention("elon")], 
                urls=[Url("jack.com"), Url("todor.com"), Url("elon.org")], 
                created_at="Sun Feb 29 23:33:24 +0000 2020",
                retweeted_status=True, 
                user=user)

  tweet2 = Tweet(text="My name is", 
                hashtags=[Hashtag("hi"), Hashtag("sup"), Hashtag("test"), Hashtag("test2")],  
                urls=[Url("jack.com"), Url("todor.com"), Url("elon.org")], 
                created_at="Sun Feb 29 23:33:24 +0000 2020", 
                user=user)

  tweet3 = Tweet(text="Who? My name is", 
                created_at="Sun Feb 21 23:33:24 +0000 2020", 
                user=user)   

  tweet4 = Tweet(text="Chicka Chicka Slim Shady", 
                hashtags=[Hashtag("hi")], 
                user_mentions=[Mention("jack"), Mention("todor"), Mention("elon")], 
                urls=[Url("jack.com")], 
                created_at="Sun Feb 20 23:33:24 +0000 2020", 
                user=user)
                
  tweet5 = Tweet(text="Chicka Chicka Slim Shady", 
                hashtags=[Hashtag("hi"), Hashtag("sup")], 
                user_mentions=[Mention("jack")],
                created_at="Sun Feb 20 23:33:24 +0000 2020",
                retweeted_status=True, 
                user=user)

  return [tweet1, tweet2, tweet3, tweet4, tweet5]


def mock_expected_csv_record():
  expected_record = CsvRecord()
  expected_record.userid = "1234"
  expected_record.user_profile_description = "I am a twitter user."	
  expected_record.follower_count = 100	
  expected_record.following_count = 50	
  expected_record.account_creation_date = "01/01/2018"	
  expected_record.account_language = "bg"	
  expected_record.ratio_follower_to_following = 2.0
  expected_record.descr_len = 20	
  expected_record.days_since_creation = 365	
  expected_record.avg_tweet_len = 15.0
  expected_record.avg_hashtag_num = 1.8	
  expected_record.avg_hashtag_char_num = 2.88889	
  expected_record.avg_mentions_num = 1.4	
  expected_record.avg_urls_num = 1.4	
  expected_record.tweet_url_ratio = 0.6
  expected_record.retweet_rate = 0.4
  expected_record.retweet_url_ratio = 0.2	
  expected_record.tweet_std = 0.4714
  expected_record.avg_tweets_per_day = 1.66667
  return expected_record

def test_csv_record_creator_empty_tweets_list():
  record_creator = CsvRecordCreator()
  record_creator.tweet_api_request = MagicMock(return_value=[])
  with pytest.raises(TwitterError) as e:
    record_creator.create_csv_record(1234, 'twittername')
  assert e.value.message == 'Empty tweets object.'

def test_csv_record_creator_success():
  record_creator = CsvRecordCreator()
  record_creator.tweet_api_request = MagicMock(return_value=mock_api_response())
  record = record_creator.create_csv_record(1234, 'twittername')
  expected_record = mock_expected_csv_record()
  assert str(record) == str(expected_record)

def test_csv_record_creator_invalid_id_fall_back_to_screen_name():
  record_creator = CsvRecordCreator()
  record_creator.api.GetUserTimeline = MagicMock(return_value=123)
  result = record_creator.tweet_api_request(0, 'tweetname', 200)
  assert result == 123

def test_csv_record_creator_invalid_id_and_screen_name():
  record_creator = CsvRecordCreator()
  record_creator.api.GetUserTimeline = MagicMock(return_value=mock_api_response())
  
  with pytest.raises(InputArgumentsError) as e:
    record_creator.tweet_api_request(0, '', 200)

  assert e.value.code == 1232
  assert e.value.message == 'User id <= 0. Screen name is blank.'

def test_csv_record_creator_acc_not_found_fall_back():
  record_creator = CsvRecordCreator()
  record_creator.api.GetUserTimeline = Mock(side_effect=[TwitterError('Account not found.'), 123])
  result = record_creator.tweet_api_request(4567, 'tweet', 200)
  assert result == 123

def test_csv_record_creator_acc_not_found_fall_back_empty_screen_name():
  record_creator = CsvRecordCreator()
  record_creator.api.GetUserTimeline = Mock(side_effect=TwitterError('Account not found.'))
  
  with pytest.raises(InputArgumentsError) as e:
    record_creator.tweet_api_request(4567, '', 200)

  assert e.value.code == 32
  assert e.value.message == 'Account not found. Screen name is blank.'
  assert record_creator.api.GetUserTimeline.call_count == 1