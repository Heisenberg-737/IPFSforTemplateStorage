# upload
import requests
import json

files = {
    'fileOne': ('Congrats! This is the first sentence'),
}

response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
p = response.json()
hash = p['Hash']
print(hash)

# retreive
params = (
    ('arg', hash),
)
response_two = requests.post('https://ipfs.infura.io:5001/api/v0/block/get', params=params)
print(response_two.text)