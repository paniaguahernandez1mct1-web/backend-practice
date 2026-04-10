## GET SOLICITAR DATOS
# import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# #url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.get(url)

# print(response.status_code)
# #print(response.json())
# data = response.json()
# #print(data[1]) #solo el primer post

# # for post in data[:5]:
# #     print(post["title"])

# # for i, post in enumerate(data[:5], start=1):
# #     print(f"{i}. {post['title']}")

# print(data["title"])

## POST CREAR DATOS
# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# nuevo_post = {
#     "title": "Mi post",
#     "body": "Contenido",
#     "userId": 1
# }

# response = requests.post(url, json = nuevo_post)

# print(response.status_code)
# print(response.json())

##MANEJO DE ERRORES
# import requests

# url = "https://jsonplaceholder.typicode.com/posts/9"

# response = requests.get(url)

# if response.status_code == 200:
#     print("OK")
#     print(response.json())
# elif response.status_code == 404:
#     print("No encontrado")
# else:
#     print("Error:", response.status_code)

##PARSEO DE JSON
# import requests

# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts")
#     response.raise_for_status() #lanza error si falla

#     data = response.json()
#     #print(len(data))

#     for post in data:
#         print(post["id"], post["title"])

# except requests.exceptions.RequestException as e:
#     print("Error:", e)

import requests

url = "https://jsonplaceholder.typicode.com/posts"
#url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

print("Total de posts:", len(data))

#for post in data[:5]:
    #print(f'{post["id"]} - {post["title"]}')
    #print(f'{post["name"]} - {post["email"]} - {post["address"]["city"]}')

for post in data:
    if post["userId"] == 1:
        print(post["title"])
