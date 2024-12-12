import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin
import argparse
import time


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


def parse_book_page(response):
    soup = BeautifulSoup(response.text, 'lxml')

    comments = soup.find_all("div", class_='texts')
    coms = [comment.find(class_="black").text for comment in comments]

    all_genres = soup.find_all('span', class_='d_book')[0].find_all('a')
    genres = [genre.text for genre in all_genres]
    
    title = soup.find(id='content').find('h1').text
    title = title.split(' :: ')

    book_titles_image = soup.find('table', class_='d_book').find('img')['src']

    book_title = sanitize_filename(title[0].strip())
    book_author = sanitize_filename(title[1].strip())
    
    book_params = {
        'Title': book_title,
        'Author': book_author,
        'Genres': genres,
        'Image_url': book_titles_image,
        'Comments': coms
    }
    
    return(book_params)
    

def main():

    os.makedirs('books', exist_ok='False')
    os.makedirs('images', exist_ok='False')

    parser = argparse.ArgumentParser(description='Скачивает книги и изображения их обложек; а также получает другую информацию о книгах')
    parser.add_argument('--start_id', type=int, default=1, help='ID первой книги')
    parser.add_argument('--end_id', type=int, default=10, help='ID второй книги')
    args = parser.parse_args()

    for id_number in range(args.start_id, args.end_id+1):

        params = {'id': id_number}

        download_url = f"https://tululu.org/txt.php"
        book_url = f"https://tululu.org/b{id_number}/"
        try:
            response = requests.get(book_url,  params=params)
            response.raise_for_status() 
            check_for_redirect(response)
            book_params = parse_book_page(response)

            book_image_url = urljoin(book_url, book_params['Image_url'])
            download_image(book_image_url, f'{id_number}.jpg')

            response = requests.get(download_url,  params=params)
            response.raise_for_status()
            check_for_redirect(response)
            download_txt(response, f'{book_params['Title']}.txt')
            
        except requests.HTTPError:
            print("Такой книги нет")

        except requests.ConnectionError:
            print('Разорвано соединение')
            time.sleep(5)


if __name__ == "__main__":
    main()
