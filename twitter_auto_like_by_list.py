from my_twitter import MyTwitter
import random
import time


class TwitterAutoLikeByList:

    def run(self):
        twitter = MyTwitter()
        # LIKE は 15 分以内で 50 回まで。それ以上実行すると 429 Too Many Requests がしばらく発生するので注意
        # NOTE: https://developer.twitter.com/en/docs/twitter-api/rate-limits
        api_limit = 50
        max_results = random.choice([12, 11, 10, 9, 8])

        tweets = twitter.get_list_tweets(twitter.config.auto_like_list_id, max_results)

        if len(tweets) <= api_limit:
            time.sleep(random.choice([1, 2, 3]))
            twitter.like(tweets)
        else:
            time.sleep(random.choice([1, 2, 3]))
            twitter.like(tweets[0:api_limit])

        print('Auto Like By List Done')


twitter_auto_like_by_list = TwitterAutoLikeByList()
twitter_auto_like_by_list.run()
