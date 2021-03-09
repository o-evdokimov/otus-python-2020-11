from tortoise import Tortoise

async def Connect_DB():
    await Tortoise.init(
        {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": "localhost",
                        "port": "5432",
                        "user": "postgres",
                        "password": "qwerty",
                        "database": "movies.postgres",
                    },
                }
            },
            "apps": {"models": {"models": ["__main__"], "default_connection": "default"}},
        },
        #_create_db=True,
        _create_db=False,
    )
    await Tortoise.generate_schemas()
    #await Tortoise.close_connections()