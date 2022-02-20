import os
import requests
import json
from dotenv import load_dotenv


def register_commands():
    load_dotenv()
    APP_ID = os.getenv('APP_ID')
    TOKEN = os.getenv('TOKEN')
    SERVER = os.getenv('SERVER')

    url = f"https://discord.com/api/v8/applications/{APP_ID}/guilds/{SERVER}/commands"
    headers = {
        "Authorization": f"Bot {TOKEN}"
    }

    f = open('commands.json')
    content = json.load(f)

    for cmd in content['commands']:
        r = requests.post(url, headers=headers, json=cmd)
        if(r.status_code != 200):
            print(f"Something went wrong: {r.content}")

if __name__ == '__main__':
    register_commands()
