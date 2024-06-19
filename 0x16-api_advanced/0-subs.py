#!/usr/bin/python3
"""
A metthod that queries reddit api and returns number
subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    # URL for Reddit API to get subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Setting custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent": "Custom"}
    # Sending GET request to Reddit API
    response = requests.get(url, headers=headers)

    # Checking if the response is successful (status code 200)
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        # Checking if the subreddit exists
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            # If the subreddit does not exist or data is missing, return 0
            return 0
    else:
        # If the request was not successful, return 0
        return 0
