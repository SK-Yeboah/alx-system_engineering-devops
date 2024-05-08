#!/usr/bin/python3
"""
A metthod that queries reddit api and returns number
subscribers for a given subreddit
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'YourBotName'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            print(f"Top 10 hot posts in r/{subreddit}:")
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    else:
        print("None")
