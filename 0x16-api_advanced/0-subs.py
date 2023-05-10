#!/usr/bin/python3

"""a module that queries the Reddit API and returns the
   number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns the
    number of subscribers
    """
    head = {"User-Agent": "Version 1.51.110 Chromium: 113.0.5672.77"}
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(reddit_url, headers=head, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers
    else:
        return 0
