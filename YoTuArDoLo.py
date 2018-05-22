import tweepy
import pickle

# so now I just need to use Tweepy
tw = tweepy.api()
YoTuArt_handle = 'youtubeartifact'
YoTuArt = tw.user_timeline(YoTuArt_handle)


class YoTuArt:

    last_accessed_date = 0

    def __init__(self):
        pass

