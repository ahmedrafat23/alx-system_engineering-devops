import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return 0
    
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)

