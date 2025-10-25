#!/usr/bin/python3
"""
This module queries the Reddit API and retrieves the number
of subscribers for a given subreddit. If the subreddit is
invalid, it returns 0.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Python:subscribers:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
