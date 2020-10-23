from bs4 import BeautifulSoup
import requests as req

resp = req.get('http://etender.uzex.uz/lots/1/0')

soup = BeautifulSoup(resp.text, 'lxml')


app = soup.find('app-root')

print(app, type(app), sep='\n')
