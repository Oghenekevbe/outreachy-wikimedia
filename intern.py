from urllib import request
import urllib

r = open("Task2-Intern.csv", "r")

while r :


    for url in r:
        url.strip()
        try:
            f = request.urlopen(url)
            print(f'{f.status} {f.url} ')

        except Exception as e:
            print(f'Error for url: {url} , {e}')