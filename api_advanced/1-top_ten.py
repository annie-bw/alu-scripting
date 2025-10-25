#!/usr/bin/python3
"""
This script queries the Reddit API and prints the titles of
the first 10 hot posts of a given subreddit. If the subreddit
is invalid, it prints None.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)


if __name__ == "__main__":
    # Subreddit name provided as first CLI argument
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
