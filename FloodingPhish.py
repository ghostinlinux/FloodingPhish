import requests
import string
import random

my_banner = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*     ___  _                    _  _                  ___  _      _       _       *
*    / __\| |  ___    ___    __| |(_) _ __    __ _   / _ \| |__  (_) ___ | |__    *
*   / _\  | | / _ \  / _ \  / _` || || '_ \  / _` | / /_)/| '_ \ | |/ __|| '_ \   *
*  / /    | || (_) || (_) || (_| || || | | || (_| |/ ___/ | | | || |\__ \| | | |  *
*  \/     |_| \___/  \___/  \__,_||_||_| |_| \__, |\/     |_| |_||_||___/|_| |_|  *
*                                           |___/                                 *
*                                                                                 *
*          Coded by Pratik Singh                                                  *
*                                                                                 * 
*                    www.ghostinlinux.me                                          *
*                                                                                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *    
"""
print(my_banner)
user_url = input("Enter your URL : ")
range1, range2 = input(
    "Enter your range for flooding with comma seperated : ").split(",")
email_name = input("Enter email name attribute : ")
pass_name = input("Enter password name attribute : ")
session = requests.session()
try:
    while True:
        generate_range = random.randint(int(range1), int(range2))
        emailval = ''.join(random.choices(
            string.ascii_uppercase, k=generate_range))
        passval = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=generate_range))

        payload = {email_name: emailval, pass_name: passval}
        response = session.post(user_url + '/login.php', data=payload)
        print(f"Flooding {response.reason}")
        if response.reason == "Not Found":
            break

except Exception as e:
    print("Disconnected")

except KeyboardInterrupt:
    print("End task")
