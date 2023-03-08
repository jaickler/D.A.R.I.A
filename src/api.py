import requests
import json



class DestinyApi():
    def __init__():
        pass

    url = "https://www.bungie.net/Platform"

    def get_vendors(destiny_key:str)-> dict:
        headers = {"X-API-KEY":destiny_key}
        res = requests.get("https://www.bungie.net/Platform/Destiny2/Vendors/?components=400,401,402", headers=headers)
        return res.json()
    

if __name__ == '__main__':
    with open("configuration.json", "r") as config: 
        data = json.load(config)
        token = data["token"]
        prefix = data["prefix"]
        owner_id = data["owner_id"]
        destiny_key = data["destiny_key"]

    print(DestinyApi.get_vendors(destiny_key=destiny_key))