import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin


if os.path.exists('books') == False:
    os.mkdir('books')

if os.path.exists('images') == False:
    os.mkdir('images')


comments_list = []


def check_for_redirect(response):    
    if response.history:
        raise requests.HTTPError
    

def download_txt(response, filename, folder='books/'):
    file_path = os.path.join(folder, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def download_image(book_image_url, filename, folder='images/'):
    img_response = requests.get(book_image_url)
    file_path = os.path.join(folder, filename)
    with open(file_path, 'wb') as file:
        file.write(img_response.content)


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
        print(f'\n{title_name}')

        # comments = soup.find_all("div", class_='texts')
        # for comment in comments:
        #     comments_list.append(comment.find(class_='black').text)
        #     if i == 10:
        #         for com_from_list in comments_list:
        #             print(com_from_list)


        genres = soup.find_all('span', class_='d_book')
        for genre in genres:
            genre = genre.find('a').text
            print(genre)
        
        # response = requests.get(download_url)
        # response.raise_for_status()
        # check_for_redirect(response)
        # download_txt(response, f'{title_name}.txt')

        # book_titles_image = soup.find('table', class_='d_book').find('img')['src']
        # book_image_url = urljoin(book_url, book_titles_image)
        # download_image(book_image_url, f'{i}.jpg')
        
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
