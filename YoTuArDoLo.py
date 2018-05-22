import tweepy
import pickle


class YoTuArt:

    last_accessed_date = 0
    auth = None
    tw = None
    acc_handles = ['youtubeartifact']

    def __init__(self):
        if not self.auth:
            consumer_key = input('Consumer key: ')
            consumer_secret = input('Consumer secret: ')
            access_token = input('Access token: ')
            access_token_secret = input('Access token secret: ')

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.auth = auth

            self.tw = tweepy.API(auth)

    def scrape(self):
        for handle in self.acc_handles:
            acc = self.tw.user_timeline(handle)


if __name__ == 'main':
    yta_file = 'finish me'
    y_t_a = YoTuArt()
