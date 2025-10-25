#!/usr/bin/python3
"""
Recursive function to fetch all hot article titles
from a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API recursively and returns a list
    containing the titles of all hot articles for a given
    subreddit. Returns None if the subreddit is invalid.

    Args:
        subreddit (str): Subreddit name
        hot_list (list): List of titles collected so far
        after (str): ID of the last post from previous page
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python:hot_recurse:v1.0 (by /u/yourusername)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title = post.get("data", {}).get("title")
            if title:
                hot_list.append(title)

        # Check if there is a next page
        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except Exception:
        return None


if __name__ == "__main__":
    # Example usage:
    subreddit = "python"
    titles = recurse(subreddit)
    if titles is not None:
        for t in titles:
            print(t)
    else:
        print("Invalid subreddit")
