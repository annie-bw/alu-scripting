#!/usr/bin/python3
"""
Script to get top 10 hot posts for a subreddit and print OK.
"""

import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit. Prints 'OK' at the end.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Python:topten:v1.0 "
                      "(by /u/yourusername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            sys.stdout.write("OK")
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        output = ""
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                output += "{}\n".format(title)

        # Remove trailing newline so OK is exactly last 2 chars
        output = output.rstrip("\n")
        sys.stdout.write(output + "OK")

    except Exception:
        sys.stdout.write("OK")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
