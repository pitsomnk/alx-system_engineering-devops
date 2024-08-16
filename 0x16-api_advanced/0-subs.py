#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Reddit Subscriber Counter'}

    # Construct the API URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send a GET request to the API, don't follow redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid, Reddit will return a 302 status code
    if response.status_code == 302:
        return 0

    # If the request was successful, parse the JSON response
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']

    # If the request failed for any other reason, return 0
    return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 reddit_subscribers.py <subreddit>")
        sys.exit(1)
    subreddit = sys.argv[1]
    print(number_of_subscribers(subreddit))
