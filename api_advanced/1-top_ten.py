#!/usr/bin/python3
"""
This script queries the Reddit API and prints the titles of
the first 10 hot posts of a given subreddit. At the end,
prints 'OK'. If the subreddit is invalid, only prints 'OK'.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.
    Prints 'OK' at the end.

    Args:
        subreddit (str): Name of the subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("OK")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        pass

    print("OK")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
