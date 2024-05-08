#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    if not word_list:
        return

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    
    headers = {'User-Agent': 'YourBotName'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data'] and len(data['data']['children']) > 0:
            children = data['data']['children']
            for child in children:
                title = child['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title:
                        counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())
            after = data['data']['after']
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit.")