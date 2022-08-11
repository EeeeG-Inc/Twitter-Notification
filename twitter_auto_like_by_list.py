from my_twitter import MyTwitter
import datetime
from datetime import timedelta


class TwitterAutoLikeByList:

    def run(self):
        twitter = MyTwitter()
        # LIKE は 15 分以内で 50 回まで。それ以上実行すると 429 Too Many Requests がしばらく発生するので注意
        # NOTE: https://developer.twitter.com/en/docs/twitter-api/rate-limits
        api_limit = 50
        max_results = 10

        tweets = twitter.get_list_tweets(twitter.config.auto_like_list_id, max_results)

        if len(tweets) <= api_limit:
            twitter.like(tweets)
        else:
            twitter.like(tweets[0:api_limit])

        print('Auto Like By List Done')


twitter_auto_like_by_list = TwitterAutoLikeByList()
twitter_auto_like_by_list.run()
