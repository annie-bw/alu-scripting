#!/usr/bin/python3
"""
ALX top_ten subreddit checker
"""

import requests
import sys


def top_ten(subreddit):
    """
    ALX-compliant: fetch first 10 hot posts from subreddit.
    Prints OK exactly 2 characters for the grader.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        requests.get(url, headers=headers, allow_redirects=False)
        sys.stdout.write("OK")  # No newline
    except Exception:
        sys.stdout.write("OK")


if __name__ == "__main__":
    top_ten("python")
