#!/usr/bin/python3
"""
A metthod that queries reddit api and returns number
subscribers for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    if not hot_list:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    
    headers = {'User-Agent': 'YourBotName'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)  # Prevent following redirects

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data'] and len(data['data']['children']) > 0:
            children = data['data']['children']
            for child in children:
                hot_list.append(child['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
