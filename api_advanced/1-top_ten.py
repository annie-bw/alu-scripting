#!/usr/bin/python3
"""
Script to print the titles of the first 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    of a given subreddit. Prints None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if subreddit is valid
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])
        for post in data:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print(None)


if __name__ == "__main__":
    # Example usage
    subreddit = "python"
    top_ten(subreddit)
