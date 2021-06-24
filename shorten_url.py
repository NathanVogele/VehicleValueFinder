# We are running this program through an API from TinyURL.com
# This feature lets us shorten the URl so that we can generate
# A QR Code later.

import api_keys
import requests
import logging

# Some Basic Setup
tiny_url_key = api_keys.tinyurl_key
logging.basicConfig(level=logging.DEBUG)


def shorten_url(url, campaign, tags):
    longURL = url

    # Tags can be comma sperated
    urlTags = tags
    urlCampaign = campaign
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer {' + tiny_url_key + '}',
        'Content-Type': 'application/json',
    }

    # Formats the Post Request
    data = '{ "url": "' + longURL + '", "domain": "tiny.one", "alias": "' + str(urlCampaign) + '", "tags":  ' + urlTags + ' }'

    response = requests.post('https://api.tinyurl.com/create', headers=headers, data=data)
    logging.debug(response)

    # Check to make sure the response is a string
    shortURL = str(response.tiny_url)
    logging.debug(shortURL)

    return shortURL
