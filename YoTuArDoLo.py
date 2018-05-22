import tweepy
import os.path
import pickle


class YoTuArt:

    last_accessed_date = 0
    auth = None
    tw = None
    acc_handles = ['youtubeartifact']

    def __init__(self):
        if not self.auth:
            print("Welcome to YoTuArt. I need yr dataz.")
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
    yta_filepath = 'y_t_a_config.P'
    if os.path.exists(yta_filepath):
        with open(yta_filepath, 'wb') as yta_file:
            y_t_a = pickle.load(yta_file)
    else:
        y_t_a = YoTuArt()

