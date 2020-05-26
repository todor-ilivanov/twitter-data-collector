import csv
import twitter
from csv_record_creator import CsvRecordCreator

account_names = csv.DictReader(open("../user_ids/validation_journ_mention_ids.csv"))

file = open('../data/validation_dataset_journ_mention.csv', 'w', encoding='utf-8')
file.write('userid,user_profile_description,follower_count,following_count,account_creation_date,account_language,ratio_follower_to_following,descr_len,days_since_creation,avg_tweet_len,avg_hashtag_num,avg_hashtag_char_num,avg_mentions_num,avg_urls_num,tweet_url_ratio,retweet_rate,retweet_url_rate,tweet_std,avg_tweets_per_day\n')

api = twitter.Api(consumer_key='WyIVvrJqu6qVC3zhi0RiZRwEY',
                      consumer_secret='6pcdAv3OwskVnWhWvzsaFDfohWw3OtyUT1jAzdjvAkGSdj62Lp',
                      access_token_key='321185042-a6KcC4MGwHwOc5OGm6J6LNeV5qqIE4omI5tJqCH9',
                      access_token_secret='I3H6fqciOVeGaRHKfoRRITx8OJx1qsLheLPok7wiraBO4',
                      sleep_on_rate_limit=True)

record_creator = CsvRecordCreator(api)

for acc in account_names:
  print(f'{acc["userid"]}: {acc["name"]}')
  try:
    record = record_creator.create_csv_record(int(acc['userid']), acc['name'])
    if record != None:
      file.write(str(record))
      file.write('\n')
  except Exception as e:
    print(e)

file.close()
print('Done.')
