import pyodbc

conn = pyodbc.connect('Driver=SQL Server;Server=(local);Database=Demo;Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute("Insert into dbo.jokes (JokeId , JokeType, Setup, Punchline) Values (?, ?, ?, ?)"
            , (-1, 'Test', 'How many hipsters does it take to change a lightbulb?', 'That number is very obscure, you have pobably never heard of it.')
        )

conn.commit()