МЕССЕНДЖЕР НА ПИТОНЕ


## Описание
Студенческий проект за третий курс по созданию мессенджера на языке Python
## Запуск
Для запуска нужно скачать **fastapi** и **uvicorn** в _Python Packages_ и использовать команду:

 `./venv/Scripts/python.exe -m  uvicorn main:app --reload`
 ## Запуск Swagger
 Для запуска сваггера нужно ввести в адресную строку
 `http://127.0.0.1:8000/docs`
 ## Миграция в базу
 Миграция происходит по команде в терминале:
`.\venv\Scripts\python.exe -m alembic upgrade head`
