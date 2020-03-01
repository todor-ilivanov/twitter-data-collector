import pytest
from src.csv_record import *
from test.tweet_stub import *

def test_average():
    num_list = [1, 2, 3, 4]
    expected_avg = 2.5
    assert average(num_list) == expected_avg 

def test_average_empty():
    num_list = []
    expected_avg = 0
    assert average(num_list) == 0 

def test_reformat_date():
    date_to_reformat = "Sat Feb 29 23:33:24 +0000 2020"
    expected_date = "29/02/2020"
    assert reformat_date(date_to_reformat) == expected_date

def test_follower_following_ratio():
    assert follower_following_ratio(6, 3) == 2

def test_date_since_creation_success():
    assert days_since_creation("01/01/2018") == 365

def test_date_since_creation_wrong_format():
    with pytest.raises(ValueError):
        assert days_since_creation("01-01-2018")

def test_avg_tweet_len():
    tweet1 = Tweet(text="Hi")
    tweet2 = Tweet(text="Test")
    assert avg_tweet_len([tweet1, tweet2]) == 3

def test_avg_hashtag_num():
    hashtags1 = [Hashtag("hi"), Hashtag("sup")]
    tweet1 = Tweet(text="Hey #sup #hi", hashtags = hashtags1)
    hashtags2 = [Hashtag("hi")]
    tweet2 = Tweet(text="Hello #hi", hashtags = hashtags2)
    assert avg_hashtag_num([tweet1, tweet2]) == 1.5

def test_avg_hashtag_char_num():
    hashtags1 = [Hashtag("hi"), Hashtag("sup")]
    tweet1 = Tweet(text="Hey #sup #hi", hashtags = hashtags1)
    hashtags2 = [Hashtag("heya")]
    tweet2 = Tweet(text="Hello #heya", hashtags = hashtags2)
    assert avg_hashtag_char_num([tweet1, tweet2]) == 3

def test_avg_mentions_num():
    mentions1 = [Mention("jack"), Mention("todor"), Mention("elon")]
    tweet1 = Tweet(text="Hey @jack @todor @elon", user_mentions = mentions1)
    mentions2 = [Mention("billgates")]
    tweet2 = Tweet(text="Hello @billgates", user_mentions = mentions2)
    assert avg_mentions_num([tweet1, tweet2]) == 2

def test_avg_urls_num():
    urls1 = [Url("jack.com"), Url("todor.com"), Url("elon.org")]
    tweet1 = Tweet(text="Hey jack.com todor.com elon.org", urls = urls1)
    urls2 = [Url("billgates.com"), Url("elon.org")]
    tweet2 = Tweet(text="Hello billgates.com elon.org", urls = urls2)
    assert avg_urls_num([tweet1, tweet2]) == 2.5

def test_avg_tweets_per_day():
    tweet1 = Tweet(text="Hi", created_at="Sun Feb 29 23:33:24 +0000 2020")
    tweet2 = Tweet(text="Test", created_at="Sat Feb 28 23:33:24 +0000 2020")
    tweet3 = Tweet(text="Test", created_at="Sat Feb 28 23:33:24 +0000 2020")
    tweet4 = Tweet(text="Hi", created_at="Fri Feb 27 23:33:24 +0000 2020")
    tweet5 = Tweet(text="Test", created_at="Fri Feb 27 23:33:24 +0000 2020")
    tweet6 = Tweet(text="Hi", created_at="Fri Feb 27 23:33:24 +0000 2020")
    tweet7 = Tweet(text="Test", created_at="Sun Feb 22 23:33:24 +0000 2020")
    assert avg_tweets_per_day([tweet1, tweet2, tweet3, tweet4, tweet5, tweet6, tweet7]) == 1.75

def test_tweet_url_ratio():
    urls1 = [Url("jack.com"), Url("todor.com"), Url("elon.org")]
    tweet1 = Tweet(text="Hey jack.com todor.com elon.org", urls = urls1)
    urls2 = [Url("billgates.com"), Url("elon.org")]
    tweet2 = Tweet(text="Hello billgates.com elon.org", urls = urls2)
    urls2 = [Url("billgates.com"), Url("elon.org")]
    tweet3 = Tweet(text="No url tweet.")
    tweet4 = Tweet(text="No url tweet 2.")
    assert tweet_url_ratio([tweet1, tweet2, tweet3, tweet4]) == 0.5

def test_retweet_rate():
    tweet1 = Tweet(text="Hi retweet", retweeted_status=True)
    tweet2 = Tweet(text="Hiya retweet", retweeted_status=True)
    tweet3 = Tweet(text="Hiya retweet3", retweeted_status=True)
    tweet4 = Tweet(text="Test no retweet")
    assert retweet_rate([tweet1, tweet2, tweet3, tweet4]) == 0.75

def test_retweet_url_ratio():
    urls1 = [Url("jack.com"), Url("todor.com"), Url("elon.org")]
    tweet1 = Tweet(text="Hi retweet", urls=urls1, retweeted_status=True)
    tweet2 = Tweet(text="Hiya retweet", retweeted_status=True)
    tweet3 = Tweet(text="Hiya retweet3", retweeted_status=True)
    tweet4 = Tweet(text="Test no retweet")
    assert retweet_url_ratio([tweet1, tweet2, tweet3, tweet4]) == 0.25

def test_tweet_std():
    tweet1 = Tweet(text="Hi", created_at="Sun Feb 29 23:33:24 +0000 2020")
    tweet2 = Tweet(text="Test", created_at="Sat Feb 28 23:33:24 +0000 2020")
    tweet3 = Tweet(text="Test", created_at="Sat Feb 28 23:33:24 +0000 2020")
    tweet4 = Tweet(text="Hi", created_at="Fri Feb 27 23:33:24 +0000 2020")
    tweet5 = Tweet(text="Test", created_at="Fri Feb 27 23:33:24 +0000 2020")
    tweet6 = Tweet(text="Hi", created_at="Fri Feb 27 23:33:24 +0000 2020")
    tweet7 = Tweet(text="Test", created_at="Sun Feb 22 23:33:24 +0000 2020")
    tweets = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6, tweet7]
    assert round(tweet_std(tweets), 5) == 0.82916
