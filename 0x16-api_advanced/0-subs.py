#!/usr/bin/python3
"""
A metthod that queries reddit api and returns number 
subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """A method that queries  the Reddit API 
    -If not  a valid  subreddit, return 0.
    """
    req = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit), headers={"User -Agent": "Custom"}, )
    
    if req.status_code == 200:
        return req.json().get('data').get('subscribers')
    else:
        return 0