#!/usr/bin/python
import oauth2 as oauth
import urllib2 as urllib
import time

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "your access_token_key"
access_token_secret = "your access_token_secret"

consumer_key = "your consumer_key"
consumer_secret = "your consumer_secret"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response


def fetchsamples():

  for i in range(310,10000):
   # Passing the Query string for search     
   url = "https://api.twitter.com/1.1/search/tweets.json?q=bjp&result_type=recent&count=400"
   parameters = []
   response = twitterreq(url, "GET", parameters)
   #Change file name to what you want it to be .
   filename='ntr'+str(i)+'.txt' 
   z = open(filename,'w')
   for line in response:
    z.write(line.strip())
   z.close()
   #Sleep for some time otherwise your script will be banned 
   time.sleep(180)

     
if __name__ == '__main__':
  fetchsamples()
