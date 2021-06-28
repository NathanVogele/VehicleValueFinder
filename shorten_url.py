# We are running this program through an API from TinyURL.com
# This feature lets us shorten the URl so that we can generate
# A QR Code later.

import api_keys
import requests
import logging

tiny_url_key = api_keys.tinyurl_key
logging.basicConfig(level=logging.DEBUG)


# Tags has to be an array of tags.
# Group can be anything, but is a custom domain to t
def shorten_url_bitly(url, tags, campaign):

    headers = {
        'Authorization': 'Bearer ' + api_keys.BIT_API_KEY,
        'Content-Type': 'application/json',
    }

    # Formats the Post Request -- BELOW IS THE DEFAULT PROVIDED BY BitLy
    # data = '{ "long_url": "https://dev.bitly.com", "domain": "bit.ly", "group_guid": "Ba1bc23dE4F" }'

    data = '{ "long_url": "' + url + '", "domain": "bit.ly", "group_guid": "Bk7ofsao0js" }'

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
    res = response.json()

    logging.debug(res)

    # Check to make sure the response is a string

    bitly_link = (res["link"])
    logging.debug(bitly_link)

    return bitly_link


# def shorten_url_tiny(url, campaign, tags):
#     longURL = url
#
#     # Tags can be comma sperated
#     urlTags = tags
#     urlCampaign = campaign
#     headers = {
#         'accept': 'application/json',
#         'Authorization': 'Bearer {' + tiny_url_key + '}',
#         'Content-Type': 'application/json',
#     }
#
#     # Formats the Post Request
#     data = '{ "url": "' + longURL + '", "domain": "tiny.one", "alias": "' + str(
#         urlCampaign) + '", "tags":  ' + urlTags + ' }'
#
#     response = requests.post('https://api.tinyurl.com/create', headers=headers, data=data)
#     logging.debug(response)
#
#     # Check to make sure the response is a string
#     shortURL = str(response.tiny_url)
#     logging.debug(shortURL)
#
#     return shortURL


campaign = "Test_Mailer"

tags = "Martin_City"

shortURL = shorten_url_bitly("https://www.MartinCityMarketing.com/thisisatest", tags, campaign)

print("The Short URL IS " + shortURL)
