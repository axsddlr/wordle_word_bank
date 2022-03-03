import requests

url = "https://www.nytimes.com/games/wordle/main.bfba912f.js"

response = requests.get(url)


if __name__ == '__main__':
    print(response.text.split("Ma=")[1].split(",Ra=")[0])