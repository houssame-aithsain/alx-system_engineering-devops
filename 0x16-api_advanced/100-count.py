#!/usr/bin/python3
"""100-count.py"""
import collections
import requests


def count_words(subreddit, word_list, counts={}, after=None):
    """
    Queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom'}
    params = {'after': after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()['data']
    for post in data['children']:
        title = post['data']['title'].lower().split()
        for word in word_list:
            counts[word] = counts.get(word, 0) + title.count(word.lower())
    if data['after'] is not None:
        count_words(subreddit, word_list, counts, data['after'])
    elif data['after'] is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
