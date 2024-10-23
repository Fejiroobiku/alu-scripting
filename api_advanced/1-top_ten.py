#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    If the subreddit is invalid or not found, it prints 'None'.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except requests.RequestException:
        print(None)
        return

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        
        if not data:
            print(None)
            return

        # Print the titles of the first 10 posts
        for i, post in enumerate(data[:10]):
            print(post['data']['title'])
    else:
        print(None)


