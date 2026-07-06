from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

# Самая грязная часть приложения, здест у вас точка входа, здесь устанавливайте дишку, ипортируйте лайфспан и все такое

def create_app() -> FastAPI:

    #container = make_async_container(AppProvider()) создаем Di контейнер
    app = FastAPI() #Cоздаем наше приложение
    #setup_dishka(container=container, app=app) #устанваливаем все завиимост внутри дишки
    return app

app = create_app()