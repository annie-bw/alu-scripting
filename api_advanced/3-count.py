#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses titles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively fetches all hot titles from a subreddit and
    counts occurrences of keywords.

    Args:
        subreddit (str): Subreddit name
        word_list (list): List of keywords to count
        word_count (dict): Accumulated word counts
        after (str): ID of last post from previous page
    """
    if word_count is None:
        # Initialize count dictionary (case-insensitive)
        word_count = {}
        for w in word_list:
            w_lower = w.lower()
            if w_lower in word_count:
                word_count[w_lower] += 0
            else:
                word_count[w_lower] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python:count_words:v1.0 (by /u/yourusername)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        # Count words in titles
        for post in children:
            title = post.get("data", {}).get("title", "")
            title_words = title.lower().split()
            for word in word_count:
                word_count[word] += title_words.count(word)

        # Recursive call for next page if available
        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, word_count, after)

        # End of recursion: sort and print
        # Only include words with count > 0
        sorted_items = sorted(
            [(k, v) for k, v in word_count.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_items:
            print("{}: {}".format(word, count))

        return word_count

    except Exception:
        return None


if __name__ == "__main__":
    # Example usage
    subreddit = "python"
    keywords = ["Python", "Java", "Javascript"]
    count_words(subreddit, keywords)
