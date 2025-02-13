import requests
import json

r = json.loads(requests.get('https://api.sampleapis.com/jokes/goodJokes').content)

print()
print(type(r))
print()

for joke in r:
    print()
    print(joke['id'])
    print(joke['type'])
    print(joke['setup'])
    print(joke['punchline'])
