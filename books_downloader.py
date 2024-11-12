import requests
import os
from bs4 import BeautifulSoup

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


# for i in range(1, 11):

#     url = f"https://tululu.org/txt.php?id={i}"
#     try:
#         response = requests.get(url)
#         response.raise_for_status() 
#         check_for_redirect(response)

#         filename = f'books/id{i}.txt'
#         with open(filename, 'wb') as file:
#             file.write(response.content)
#     except requests.HTTPError:
#         print("Встречена ошибка requests.HTTPError")


url = 'http://tululu.org/b1/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')
id1_title = soup.find(id='content').find('h1').text
id1_title = id1_title.split('::')
print("Название:", id1_title[0],  "\\\nАвтор:", id1_title[1])