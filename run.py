import requests
import json

key = 'https://newsapi.org/v2/everything?q=Apple&from=2022-11-30&sortBy=popularity&apiKey' \
      '=349efcb0503940538e3c073151d726d8 '

response = requests.get(key)

newjson = json.loads(str(response))

