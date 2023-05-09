#!/usr/bin/python3
"""
a module that queries the Reddit API and returns a list
containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    a function that that queries the Reddit API and returns
    a list containing the titles of all hot article
    """
    if hot_list is None:
        hot_list = []
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    elif response.status_code == 404:
        return None
    else:
        raise ValueError(f"Request failed with status code\
                         {response.status_code}")
