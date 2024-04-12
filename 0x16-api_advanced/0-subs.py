#!/usr/bin/python3
"""Module for task 0."""


def number_of_subscribers(subreddit):
    """Query the Reddit API,
    and return the number of subscribers to the subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if the subreddit
        does not exist or cannot be reached.
    """
    import requests

    sub_info = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )
    if sub_info.status_code >= 300:
        return 0
