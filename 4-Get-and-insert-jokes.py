import requests
import json
import pyodbc

r = json.loads(requests.get('https://api.sampleapis.com/jokes/goodJokes').content)

print()
print('Inserting Jokes...')
print()

conn = pyodbc.connect(r'Driver=SQL Server;Server=(local);Database=Demo;Trusted_Connection=yes;')

for joke in r:

    cursor = conn.cursor()

    cursor.execute("Insert into dbo.jokes (JokeId , JokeType, Setup, Punchline) Values (?, ?, ?, ?)"
                , (joke['id'], joke['type'], joke['setup'], joke['punchline'])
            )

    conn.commit()

print()
print('...Jokes Inserted.')
print()    
