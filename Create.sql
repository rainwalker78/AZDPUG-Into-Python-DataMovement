use Demo
go

drop table if exists dbo.jokes

Create Table dbo.jokes
(
	JokeKey int Identity constraint pk_Jokes_jokekey primary key clustered
  , JokeId int not null --constraint ak_Jokes_JokeId unique
  , JokeType varchar(50)
  , Setup varchar(255)
  , Punchline varchar(255)

)