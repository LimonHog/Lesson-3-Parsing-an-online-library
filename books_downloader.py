import requests
import os

# url = "https://tululu.org/txt.php?id=32168"
# response = requests.get(url)
# response.raise_for_status() 

# filename = 'books/peski_marsa.txt'

# with open(filename, 'wb') as file:
#     file.write(response.content)



    


for i in range(10):
    i += 1

    url = f"https://tululu.org/txt.php?id={i}"
    response = requests.get(url)
    response.raise_for_status() 

    filename = f'books/id{i}.txt'
    with open(filename, 'wb') as file:
        file.write(response.content)
    
    