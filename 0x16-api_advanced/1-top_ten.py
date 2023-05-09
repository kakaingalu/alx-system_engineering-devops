#!/usr/bin/python3
""" that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """a function that queries the Reddit API and returns the
    number of subscribers
    """
    head = {"User-Agent": "Version 1.51.110 Chromium: 113.0.5672.77"}
    Url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = get(Url, headers=head, allow_redirects=False)
    posts = response.json()
    if response.status_code == 200:
        children = posts.get("data").get("children")
        for post in children:
            print(post["data"]["title"])
    else:
        print("None")
