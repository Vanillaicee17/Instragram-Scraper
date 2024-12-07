from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)

followers_data = []
following_data = []

followers = cl.user_followers(cl.user_id)
for user_id in followers.keys():
    followers_data.append(followers[user_id].username)


following = cl.user_following(cl.user_id)
for user_id in following.keys():
    following_data.append(following[user_id].username)

not_following_back = [
    user for user in following_data if user not in followers_data]

for i in not_following_back:
    print(i)
