import csv
from csv_record_creator import CsvRecordCreator

account_names = csv.DictReader(open("user_ids/users.csv")) # [{'account_id': '12314', 'handle': 'frank'}]

file = open('data/control_dataset_BIG.csv', 'w', encoding='utf-8')
file.write('userid,user_profile_description,follower_count,following_count,account_creation_date,account_language,ratio_follower_to_following,descr_len,days_since_creation,avg_tweet_len,avg_hashtag_num,avg_hashtag_char_num,avg_mentions_num,avg_urls_num,tweet_url_ratio,retweet_rate,retweet_url_rate,tweet_std,avg_tweets_per_day\n')
record_creator = CsvRecordCreator()

for acc in account_names:
  print(acc)
  try:
    record = record_creator.create_csv_record(int(acc['account_id']), acc['handle'])
    if record != None:
      file.write(str(record))
      file.write('\n')
  except Exception as e:
    print(e)

file.close()
print('Done.')
