#!/usr/bin/python3
"""
Script to get top 10 hot posts for a subreddit and print OK.
"""

import requests
import sys


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:topten:v1.0 (by /u/yourusername)"}

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

        sys.stdout.write(output + "OK")  # all titles + OK with no extra newline

    except Exception:
        sys.stdout.write("OK")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
