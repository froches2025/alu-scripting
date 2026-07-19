#!/usr/bin/python3
"""Function to query hot posts for a given Reddit subreddit."""
import requests
from xml.etree import ElementTree


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts listed for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot/.rss".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    root = ElementTree.fromstring(response.content)
    entries = root.findall("{http://www.w3.org/2005/Atom}entry")

    for entry in entries[:10]:
        title = entry.find("{http://www.w3.org/2005/Atom}title")
        if title is not None and title.text is not None:
            print(title.text)
