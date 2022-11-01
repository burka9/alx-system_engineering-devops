#!/usr/bin/python3
# API Advanced
import requests
import sys


def number_of_subscribers(subreddit):
    """send request to reddit api"""
    header = {
        'User-Agent': 'xica369'
    }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=false)

    if response.status_code == 200:
        return (response.json().get('data')).get('subscribers')

    return (0)
