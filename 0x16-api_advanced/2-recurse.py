#!/usr/bin/python3
"""
a module that queries the Reddit API and returns a list
containing the titles of all hot articles
"""
from requests import get
after = None 


def recurse(subreddit, hot_list=[]):
    """
    a function that that queries the Reddit API and returns
    a list containing the titles of all hot article
    """
    global after
    head = {"User-Agent": "Version 1.51.110 Chromium: 113.0.5672.77"}
    Url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    afta = {'limit': 100 'after': after}
    response = get(Url, headers=head, params=afta, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json()
        after = posts.get("data").get("after")
        (After := after) and recurse(subreddit, hot_list)
        children = posts.get("data").get("children")
        return [title.get("data").get("title") for title in children]
    else:
        return None
