import requests


ServiceID = '159721591'
response = requests.get(f'http://10.80.19.114:9194/?0000000090&ServiceID={ServiceID}&QueryCode=GetHalls&DateList=&Theatres=&Encoding=Windows-1251&Version=3')

GetMovies = requests.get(f'http://10.80.19.114:9194/?0000000090&ServiceID={ServiceID}&QueryCode=GetMovies&CardCode=&Theatres=&Halls=&DateList=&PastTime=&ListType=PropertiesShow&Category=&Encoding=Windows-1251&Version=3&Expect=')
GetFistMovieSession = requests.get(f'http://10.80.19.114:9194/?0000000090&ServiceID={ServiceID}&QueryCode=GetFirstMovieSession&FilmID=6&Encoding=Windows-1251')
# ServiceID=159721591&QueryCode=GetFirstMovieSession&FilmID=6&Encoding=Windows-1251
# OK http://10.80.19.114:9194/?0000000090&ServiceID=159721591&QueryCode=GetHalls&DateList=&Theatres=&Encoding=Windows-1251&Version=3


print(response)
print(GetMovies)
print(GetFistMovieSession)