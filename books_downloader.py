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


def parse_book_page(soup, title, image):

    comments = soup.find_all("div", class_='texts')
    coms = []
    for comment in comments:
        comment = comment.find_all(class_='black')
        for com in comment:
            coms.append(com.text)
    
    rating = soup.find(id=f'unit_long{i}').find('span').find('strong').text

    genres = soup.find_all('span', class_='d_book')
    genre_list = []
    for genre in genres:
        genre = genre.find_all('a')
        for gen in genre:  
            genre_list.append(gen.text)
            


    book_title = sanitize_filename(title[0].strip())
    book_author = sanitize_filename(title[1].strip())
    
    book_info = {
        'Название': book_title,
        'Автор': book_author,
        'Жанр(ы)': genre_list,
        'Ссылка на изображение': image,
        'Рейтинг': f'{rating}/5'
        'Коментарии': coms
    }

    # print(book_info)
    



for i in range(1, 11):

    download_url = f"https://tululu.org/txt.php?id={i}"
    book_url = f"https://tululu.org/b{i}/"
    try:
        response = requests.get(book_url)
        response.raise_for_status() 
        check_for_redirect(response)
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find(id='content').find('h1').text
        title = title.split(' :: ')
        title_name = sanitize_filename(title[0].strip()) 
        
        response = requests.get(download_url)
        response.raise_for_status()
        check_for_redirect(response)
        download_txt(response, f'{title_name}.txt')

        book_titles_image = soup.find('table', class_='d_book').find('img')['src']
        book_image_url = urljoin(book_url, book_titles_image)
        download_image(book_image_url, f'{i}.jpg')

        

        parse_book_page(soup, title, book_image_url)
        
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
