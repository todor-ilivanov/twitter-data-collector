class Tweet:
  text = None
  hashtags = None
  user_mentions = None
  urls = None
  created_at = None
  retweeted_status = None

  def __init__(self, text, hashtags=None, user_mentions=None, urls=None, 
              created_at=None, retweeted_status=None): 
        self.text = text
        self.hashtags = hashtags or []
        self.user_mentions = user_mentions or []
        self.urls = urls or []
        self.created_at = created_at or ''
        self.retweeted_status = retweeted_status

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
