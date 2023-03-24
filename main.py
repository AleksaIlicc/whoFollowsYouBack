import json

with open("followers_1.json") as file1:
    followers_json = json.load(file1)

with open("following.json") as file2:
    following_json = json.load(file2)

whoFollowsYouBack = []

for following in following_json["relationships_following"]:
    whoFollowsYouBack.append(following["string_list_data"][0]["value"])

for follower in followers_json:
    username = follower["string_list_data"][0]["value"]
    if username in whoFollowsYouBack:
        whoFollowsYouBack.remove(username)


for user in whoFollowsYouBack:
    print(user)
