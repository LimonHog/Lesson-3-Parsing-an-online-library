# Парсер книг с сайта tululu.org

Данный проект может скачивать книги, их обложки и названия с сайта [tululu.org](https://tululu.org). А так же он выводит словарь с информацией о книге (название, ссылка на изображение, автор, комментарии, жанр(ы), рейтинг).

# Как установить

Прежде чем запускать код необходимо установить некоторые библиотеки. Их всех с нужными версиями можно найти в файле `requirements.txt`, а для установки используйте команду:
```
pip install -r requirements.txt
```

Чтобы проект выполнял свою работу необходимо написать команду:
```
python books_downloader.py
```


# Аргументы

В коде присутствует два необязательных аргумента: `--start_id`, `--end_id`. Они нужны для установления рамок ID книг для скачивания.
`--start_id` отвечает за ID первой из скачиваемых книг, а `--end_id` за последнюю. Эти аргументы необязательны и имеют базовые значения. Для `--start_id` это 1, а для `--end_id` это 10.

Чтобы аргументы заработали, их нужно написать сразу после команды запуска. За ними необходимое ID книги. Например:
```
python books_downloader.py --start_id 10 --end_id 20
```
Представленный выше код скачает все книги с ID от 10 до 20.
Код будет работать и при написании только одного из аргументов или без них вовсе.


# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).