import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin


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
    

def download_txt(response, filename, folder='books/'):
    file_path = os.path.join(folder, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)


for i in range(1, 11):

    download_url = f"https://tululu.org/txt.php?id={i}"
    book_url = f"https://tululu.org/b{i}/"
    try:
        response = requests.get(book_url)
        response.raise_for_status() 
        check_for_redirect(response)
        soup = BeautifulSoup(response.text, 'lxml')
        title_name = soup.find(id='content').find('h1').text
        title_name = title_name.split(' :: ')
        title_name = sanitize_filename(title_name[0].strip())
        book_titles_image = soup.find('table', class_='d_book').find('img')['src']
        book_titles_image_url = urljoin(book_url, book_titles_image)

        print(title_name)
        print(book_titles_image_url)


        # response = requests.get(download_url)
        # response.raise_for_status()
        # check_for_redirect(response)
        # download_txt(response, f'{title_name}.txt')
    except requests.HTTPError:
        print("Встречена ошибка requests.HTTPError")


# url = 'http://tululu.org/b1/'
# response = requests.get(url)
# response.raise_for_status()

# soup = BeautifulSoup(response.text, 'lxml')
# id1_title = soup.find(id='content').find('h1').text
# id1_title = id1_title.split('::')
# print("Название:", id1_title[0],  "\\\nАвтор:", id1_title[1])




# url = 'http://tululu.org/txt.php?id=1'
# response = requests.get(url)
# response.raise_for_status() 

# download_txt(response, 'Алиби.txt')
# url = "https://tululu.org/b3/"
# response = requests.get(url)
# response.raise_for_status() 
# check_for_redirect(response)
# soup = BeautifulSoup(response.text, 'lxml')
# title_name = soup.find('div', id='content').find('h1')
# print(title_name)
