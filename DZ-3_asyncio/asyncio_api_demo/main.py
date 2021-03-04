"""
+ у моделей есть primary_key - 1 балл
+ созданы все миграции - 1 балл
+ скрипт стягивает данные с API и складывает в БД - 1 балл
обращение к API выполняется в асинхронном виде - 1 балл
на асинхронный клиент применяется close при завершении работы - 1 балл
+ запись в базу данных выполняется в асинхронном виде - 1 балл
+ соединение с базой данных закрывается при завершении работы - 1 балл
"""

# =============

# API_ABOUT_URL
# https://rapidapi.com/rapidapi/api/movie-database-imdb-alternative
example_of_response = \
    {"Search":
         [{"Title":"Terminator 2: Judgment Day",
           "Year":"1991","imdbID":"tt0103064",
           "Type":"movie",
           "Poster":"https://m.media-amazon.com/images/M/MV5BMGU2NzRmZjUtOGUxYS00ZjdjLWEwZWItY2NlM2JhNjkxNTFmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg"},],
     "totalResults":"100","Response":"True"}

import requests
from datetime import datetime
from tortoise import run_async
from models.post import Post
from models.movie import Movie
from requests.exceptions import ReadTimeout, ConnectTimeout, ConnectionError
from models.base import Connect_DB
import asyncio
import aiohttp

API_URL = "https://movie-database-imdb-alternative.p.rapidapi.com/"
HEADERS = {
    'x-rapidapi-key': "aaa5b4f331mshe94cc4b142f21e5p12f075jsnb79cd4ccd256",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

async def fetch_api(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, headers=HEADERS, params=query) as response:
            resp = (await response.json()).get('Search')
    return resp


async def fetch_movie_api(query):
    try:
        api_movies = await fetch_api(query)
    except (ReadTimeout, ConnectTimeout, ConnectionError) as err:
        print(f'\nFetching IMDB have been failed: {err}\n')
        return False

    movies_title = []
    count=0
    if api_movies:
        print(f'\nFetching IMDB have been completed. \nFound {len(api_movies)} movies')
        for item in api_movies:
            print(item)
            Title = item.get('Title')
            Year = item.get('Year')
            imdbID = item.get('imdbID')
            Type = item.get('Type')
            Poster = item.get('Poster')
            created_at = str(datetime.now())
            if not await Movie.exists(Title=Title, Type=Type):
                movie = Movie(Title=Title, Year=Year, imdbID=imdbID, Type=Type, Poster=Poster, created_at=created_at)
                await movie.save()
                movies_title.append(movie.Title)
                count+=1
        print(f'\nSaved {count} NEW movie\'s records in local DB\n')
        if count>0:
            print('\n'.join(movies_title))
    else:
        print('Not found any movies in the global IMDB database\n')


async def show_movies(movie_title):
    movies = await Movie.filter(Title__icontains=movie_title).all()
    if movies:
        for movie in movies:
            print(movie)
        print(f'Found {len(movies)} movies in local DB\n')
    else:
        print('Not found any movies in DB\n')


async def create_post(author, movie_id, title, text):
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not await Post.filter(title=title).exists() and await Movie.exists(imdbID=movie_id):
            post = Post(author=author, movie_id=movie_id, title=title, text=text, created_at=created_at)
            await post.save()
    else:
        print(f'\nNot found movie {movie_id} in local DB or post title {title!r} exist\n')


async def show_posts(key, value):
    posts=[]
    if key=='author':
        posts = await Post.filter(author=value).all()
    elif key=='movie_id':
        movie = await Movie.filter(imdbID=value).first()
        posts = await Post.filter(movie=movie).all()
    elif key=='title':
        movie = await Movie.filter(Title=value).first()
        posts = await Post.filter(movie=movie).all()
    if posts:
        for post in posts:
            print(f'{(await posts[0].movie).Title!r} [ IMDB ID: {(await posts[0].movie).imdbID} ] \n{":" * 40}')
            print(post)
    else:
        print('Not found any posts in DB\n')


async def run():
    await Connect_DB()

    answer=''
    menu_answer = 'up'
    while 1:
        completed = False
        if menu_answer.lower() == 'up':
            answer = input("""Select:
            1. request movie's info from IMDB and save in the local DB
            2. show movie's info [from the local DB]
            3. create new post
            4. show posts for the Movie
            5. exit\n
            >> """)
            if not answer.isdigit():
                continue
        while not completed:
            if int(answer)==1:
                movie_title = input("\nInput movie's name: ")
                query_movie = {"s": movie_title, "page": "1", "r": "json"}
                await fetch_movie_api(query_movie)
            elif int(answer)==2:
                movie_title = input("\nInput movie's name: ")
                await show_movies(movie_title)
            elif int(answer)==3:
                author = input('Your name: ')
                movie_id = input('IMDB id: ')
                post_title = input('Post title: ')
                post_text = input('Message: ')
                await create_post(author, movie_id, post_title, post_text)
            elif int(answer) == 4:
                post_request = input("\nSearch posts by movie's name, IMDB ID or author.\n"
                                     "Type 'Indiana Jones and the Temple of Doom' or 'tt0087469' or author's name in format 'author_<name>': ")
                if post_request.startswith('tt') and post_request[2:].isdigit():
                    await show_posts(key='movie_id', value=post_request)
                elif post_request.startswith('author_'):
                    await show_posts(key='author', value=post_request[7:])
                else:
                    await show_posts(key='title', value=post_request)
            elif int(answer) == 5:
                print('Bye-bye !!!')
                exit(0)

            menu_answer = input('\nPress enter to continue or UP for exit to main menu\n>> ')
            completed = True


if __name__ == '__main__':
    print("\nIt's IMDB api client (async mode)\n")
    #run_async(run())
    asyncio.run(run())
