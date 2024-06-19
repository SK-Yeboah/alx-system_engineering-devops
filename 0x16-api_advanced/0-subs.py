#!/usr/bin/python3
"""
A metthod that queries reddit api and returns number
subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    # URL for Reddit API to get subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit),
    # Setting custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Custom"}
    # Sending GET request to Reddit API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
    