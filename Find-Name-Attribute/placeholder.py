import requests
import bs4

user_val = input("Enter placeholder of user : ")
password_val = input("Enter placeholder of password : ")
url = input('Enter your URL : ')

response = requests.get(url)
bs = bs4.BeautifulSoup(response.text, "html.parser")
bss = bs.find_all("input")
liss = []
for att in bss:
    place = att.get('placeholder')
    # print(place)
    if user_val == place:
        if user_val not in liss:
            liss.append(att.get('placeholder'))
            liss.append(att.get('name'))
    if password_val == place:
        if password_val not in liss:
            liss.append(att.get('placeholder'))
            liss.append(att.get('name'))

print(liss)
