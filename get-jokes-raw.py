import requests

r = requests.get('https://api.sampleapis.com/jokes/goodJokes')

print()

print (r._content)




