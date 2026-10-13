import requests

API_KEY ="AIzaSyDYGhkLDLKLfhLwpx5CqX-2vAWujG55ZLU"

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "q": "Artifical Intelligence",
    "type": "video",
    "maxResults": 5,
    "key": API_KEY
}

response = requests.get(url, params=params)

data = response.json()

for video in data["items"]:

    print("Title:", video["snippet"]["title"])
    print("Channel:", video["snippet"]["channelTitle"])
    print("Published At:" , video ["snippet"]["publishedAt"])


