import requests
import bs4

url = input('Enter your URL : ')

response = requests.get(url)
bs = bs4.BeautifulSoup(response.text, "html.parser")
bss = bs.find_all("input")
for att in bss:
    print(f"{att.get('placeholder')} : {att.get('type')}  :  {att.get('name')}")