import requests
import os

# url = "https://tululu.org/txt.php?id=32168"
# response = requests.get(url)
# response.raise_for_status() 

# filename = 'books/peski_marsa.txt'

# with open(filename, 'wb') as file:
#     file.write(response.content)

if os.path.exists('books') == False:
    os.mkdir('books')


def check_for_redirect(response):    
    if response.history:
        raise requests.HTTPError


for i in range(1, 11):

    url = f"https://tululu.org/txt.php?id={i}"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        check_for_redirect(response)

        filename = f'books/id{i}.txt'
        with open(filename, 'wb') as file:
            file.write(response.content)
    except requests.HTTPError:
        print("Встречена ошибка requests.HTTPError")