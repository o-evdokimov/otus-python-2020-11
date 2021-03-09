"""
+ у моделей есть primary_key - 1 балл
созданы все миграции - 1 балл
+ скрипт стягивает данные с API и складывает в БД - 1 балл
обращение к API выполняется в асинхронном виде - 1 балл
на асинхронный клиент применяется close при завершении работы - 1 балл
запись в базу данных выполняется в асинхронном виде - 1 балл
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
from sqlalchemy.orm import collections
from datetime import datetime
from requests.exceptions import ReadTimeout, ConnectTimeout, ConnectionError

from models.base import Base, Session, engine
from models.movie import Movie
from models.post import Post


API_URL = "https://movie-database-imdb-alternative.p.rapidapi.com/"
HEADERS = {
    'x-rapidapi-key': "aaa5b4f331mshe94cc4b142f21e5p12f075jsnb79cd4ccd256",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }


def fetch_movie_api(query):
    try:
        response = requests.request("GET", API_URL, headers=HEADERS, params=query)
    except (ReadTimeout, ConnectTimeout, ConnectionError) as err:
        print(f'\nFetching IMDB have been failed: {err}\n')
        return False
    api_movies = response.json().get('Search')
    movies_title = []
    count = 0
    session = Session()
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
            if not session.query(Movie).filter_by(Title = Title).first():
                movie = Movie(Title=Title, Year=Year, imdbID=imdbID, Type=Type, Poster=Poster, created_at=created_at)
                session.add(movie)
                movies_title.append(movie.Title)
                count+=1
        print(f'\nSaved {count} NEW movie\'s records in local DB\n')
        if count>0:
            print('\n'.join(movies_title))
    else:
        print('\nNot found any movies in the global IMDB database\n')

    session.commit()
    session.close()


# def update_movie(title):
#     session = Session()
#     movie: Movie = session.query(Movie).filter_by(Title = title).one_or_none()
#
#     if movie:
#         print(movie)
#         movie.created_at = datetime.now()
#         session.commit()
#     session.close()


def create_post(author, movie_id, title, text):
    session = Session()
    created_at = str(datetime.now())
    if not session.query(Post).filter_by(title=title).one_or_none() and session.query(Movie).filter_by(imdbID=movie_id).one_or_none():
        post = Post(author=author, movie_id=movie_id, title=title, text=text, created_at=created_at)
        session.add(post)
    else:
        print(f'\nNot found movie {movie_id} in local DB or post title {title!r} exist\n')
    session.commit()
    session.close()


def show_movies(movie_title):
    session = Session()
    movies = session.query(Movie).filter(Movie.Title.ilike(f'%{movie_title}%')).all()
    if movies:
        for movie in movies:
            print(movie)
    else:
        print('Not found any movies in DB\n')


def show_posts(key, value):
    session = Session()
    posts : collections.InstrumentedList = collections.InstrumentedList()
    if key=='author':
        posts = session.query(Post).filter_by(author=value).all()
        if posts:
            print(f'{posts[0].movie.Title!r} [ IMDB ID: {posts[0].movie.imdbID} ] \n{":" * 40}')
            for post in posts:
                print(post)
    else:
        if key=='movie_id':
            posts: Movie = session.query(Movie, Post).filter_by(imdbID=value).all()
        if key=='title':
            posts: Movie = session.query(Movie, Post).filter_by(Title=value).all()

        if posts:
            print(f'{posts[0].Movie.Title!r} [ IMDB ID: {posts[0].Movie.imdbID} ] \n{":"*40}')
            for post in posts:
                print(post.Post)
    if not posts:
        print('Not found any posts in DB\n')

    session.commit()
    session.close()


if __name__ == '__main__':
    print("\nIt's IMDB api client\n")
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
                Base.metadata.create_all(engine)
                fetch_movie_api(query_movie)
            elif int(answer)==2:
                movie_title = input("\nInput movie's name: ")
                show_movies(movie_title)
            elif int(answer)==3:
                author = input('Your name: ')
                movie_id = input('IMDB id: ')
                post_title = input('Post title: ')
                post_text = input('Message: ')
                create_post(author, movie_id, post_title, post_text)
            elif int(answer) == 4:
                post_request = input("\nInput movie's name or IMDB ID or 'author_<name>': ")
                if post_request.startswith('tt') and post_request[2:].isdigit():
                    show_posts(key='movie_id', value=post_request)
                elif post_request.startswith('author_'):
                    show_posts(key='author', value=post_request[7:])
                else:
                    show_posts(key='title', value=post_request)
            elif int(answer) == 5:
                print('Bye-bye !!!')
                exit(0)
            menu_answer = input('\nPress enter to continue or UP for exit to main menu\n>> ')
            completed = True