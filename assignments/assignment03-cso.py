import requests
import json

url = "https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%22C02568V03113%22%5D,%22dimension%22:%7B%22C02568V03113%22:%7B%22category%22:%7B%22index%22:%5B%2205%22%5D%7D%7D%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22JSON-stat%22,%22version%22:%222.0%22%7D,%22matrix%22:%22FIQ02%22%7D,%22version%22:%222.0%22%7D%7D"

response = requests.get(url)
response.raise_for_status()

data = response.json()

with open("cso.json", "w") as f:
    json.dump(data, f, indent=4)

print("Saved dataset to cso.json")
