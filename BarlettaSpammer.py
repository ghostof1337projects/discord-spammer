import requests
import json
import os
import time
def main():
    bot = discord.Client()
    client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
__VERSION__ = "1.7"
os.system(f'cls & mode 85,20 & title [Barletta Spammer] - {__VERSION__} - Made by Ghost Of 1337')
print(f'''\u001b[32m

               ╔╗ ┌─┐┬─┐┬  ┌─┐┌┬┐┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐
               ╠╩╗├─┤├┬┘│  ├┤  │  │ ├─┤  ╚═╗├─┘├─┤││││││├┤ ├┬┘
               ╚═╝┴ ┴┴└─┴─┘└─┘ ┴  ┴ ┴ ┴  ╚═╝┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─

''')
channelID = 123456789 #id canal
headers = {
    "authorization":
    "ABCDEFGHtoken"
}
file = open("file.txt", "r")
lines = file.readlines()
while True:
    for line in lines:
        try:
            requests.post(
                f"https://discord.com/api/v9/channels/{channelID}/messages",
                headers=headers,
                json={"content": line})
        except requests.exceptions.RequestException as e:
            print(e)
            time.sleep(5)
            continue