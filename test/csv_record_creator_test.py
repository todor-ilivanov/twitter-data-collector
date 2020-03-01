import pytest
from unittest.mock import MagicMock
from test.tweet_stub import Tweet
from src.csv_record_creator import CsvRecordCreator

def test_csv_record_creator():
  record_creator = CsvRecordCreator()
  record_creator.tweet_api_request = MagicMock(return_value=3)
  assert record_creator.tweet_api_request() == 3