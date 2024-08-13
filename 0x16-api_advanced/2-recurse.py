#!/usr/bin/python3
"""2-recurse.py"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom'}
    params = {'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    if data['after'] is not None:
        return recurse(subreddit, hot_list, data['after'])
    return hot_list
