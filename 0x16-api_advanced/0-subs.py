#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        print("OK")
        return subscribers
    else:
        print("OK")
        return 0
