#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            results = response.json().get("data", {}).get("children", [])
            if not results:
                print("None")
            else:
                for post in results:
                    print(post.get("data", {}).get("title"))
        else:
            print("None")
    except requests.exceptions.JSONDecodeError:
        print("None")
    except requests.exceptions.RequestException as e:
        print("None")
