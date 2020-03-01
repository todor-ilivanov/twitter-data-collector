import csv
from csv_record_creator import CsvRecordCreator

account_names = csv.DictReader(open("user_ids/user_ids_20000.csv")) 
print(account_names)

file = open('data/control_dataset_20k.csv', 'w', encoding='utf-8')
file.write('userid,user_profile_description,follower_count,following_count,account_creation_date,account_language,ratio_follower_to_following,descr_len,days_since_creation,avg_tweet_len,avg_hashtag_num,avg_hashtag_char_num,avg_mentions_num,avg_urls_num,tweet_url_ratio,retweet_rate,retweet_url_rate,tweet_std,avg_tweets_per_day\n')
record_creator = CsvRecordCreator()

for acc in account_names:
  print(acc['name'])
  try:
    record = record_creator.create_csv_record(1, acc['name'])
    if record != None:
      file.write(str(record))
      file.write('\n')
  except Exception as e:
    print(e)

file.close()
print('Done.')
