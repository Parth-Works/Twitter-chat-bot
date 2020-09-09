#Section 1: complete code
import tweepy
import os # Operating System library
def create_api():

  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  
#we can play with only once in a minute, so it checks and notify for rate to get replenished
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 
  api.verify_credentials()
  print("API is created")
  return api
  
  
#Section 2: complete code
import time
def follower_count(user):

  emoji_numbers = {0 : '0️⃣',1 : '1️⃣',2 : '2️⃣',3 : '3️⃣',4 : '4️⃣',
                  5 : '5️⃣',6 : '6️⃣',7 : '7️⃣',8 : '8️⃣',9 : '9️⃣'}

  emoji_numbers.keys()

  uf_split = [int(j) for j in str(user.followers_count)]
  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()])
                        
  return emoji_followers

api= create_api()

while True:
  user = api.get_user('beats_humour')
  api.update_profile(name= f'BEATS_humour|{follower_count(user)} Followers')
  print(f'Updating Twitter Name : BEATS_humour|{follower_count(user)} Followers')
  print('Waiting to Refresh')
  time.sleep(60)
    
