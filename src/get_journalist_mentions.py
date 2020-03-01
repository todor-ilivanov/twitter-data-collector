import twitter

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='',
                      sleep_on_rate_limit=True)

file = open('../data/journ_mention_ids.csv', 'w', encoding='utf-8')
file.write('userid,name\n')

JOURNALIST_LIST_ID = 15084461
list_members = api.GetListMembersPaged(list_id=JOURNALIST_LIST_ID, count=410, skip_status=True, include_entities=False)
journalist_ids = [x.id for x in list_members[2]]
journalist_screen_names = ['@' + x.screen_name for x in list_members[2]]

# get users who tweeted mentions/replies? of journ accounts
for journ_name in journalist_screen_names:
  print(journ_name)
  test = api.GetSearch(term=journ_name, count=100)
  user_list = [x.user for x in test if journ_name in x.text]

  for user in user_list:
      file.write(str(user.id) + ',' + user.screen_name)
      file.write('\n')

file.close()
print('Done')