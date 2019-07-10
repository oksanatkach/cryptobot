import tweepy

consumer_key = 'wwK6NYzsDyZOthwXVk1QDPK4j'
consumer_secret = 'kznZ25E0eoRzRLrWfLbDJz59ep0EjmQMtNmvUQAXS6btBNjLEq'
access_token = '180070452-YDdkH2pTlAoojTDipWDHEqya7fzlju1gOGPs9gWC'
access_secret = 'xIPFZVTwNKpaEm1FyCmYbESCVviyEO8VUOVF9AuW4WqMy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(follow=['15754281'])
