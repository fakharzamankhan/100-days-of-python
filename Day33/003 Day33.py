import requests
response=requests.get(url="https://api.artic.edu/api/v1/artworks/search?q=cats")
response.raise_for_status()
print(response.json())
print(response.json()["pagination"])
print(response.json()["pagination"]["total"])
