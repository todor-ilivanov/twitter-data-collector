class Tweet:
  text = None
  hashtags = None
  user_mentions = None
  urls = None
  created_at = None
  retweeted_status = None
  user = None

  def __init__(self, text, hashtags=None, user_mentions=None, urls=None, 
              created_at=None, retweeted_status=None, user=None): 
        self.text = text
        self.hashtags = hashtags or []
        self.user_mentions = user_mentions or []
        self.urls = urls or []
        self.created_at = created_at or ''
        self.retweeted_status = retweeted_status
        self.user = user

class Hashtag:
  text = None
  def __init__(self, text): 
        self.text = text

class Mention:
  text = None
  def __init__(self, text): 
        self.text = text

class Url:
  text = None
  def __init__(self, text): 
        self.text = text

class User:
  id_str = None
  description = None
  followers_count = None
  friends_count = None
  created_at = None
  lang = None
  def __init__(self, id_str, description, followers_count, friends_count, created_at, lang): 
        self.id_str = id_str
        self.description = description
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.created_at = created_at
        self.lang = lang

