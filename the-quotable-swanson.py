import configparser
import praw
import random
import re
from quotes import quotable_ron

config = configparser.ConfigParser()
config.read('config.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddit = config['REDDIT']['reddit_target_subreddit']
reddit_user_agent = config['REDDIT']['reddit_user_agent']

reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent
)


def main():
    quotes = quotable_ron.ron_quotes
    for comment in reddit.subreddit(reddit_target_subreddit).stream.comments(skip_existing=True):
        if re.search('!wisewords', comment.body, re.IGNORECASE):
            comment.reply(random.choice(quotes))


if __name__ == '__main__':
    main()
