# upload
from moralis import evm_api
import base64
import requests

api_key = "7hstobdqT97qzSbNkW6Spq227cMCBXEPsKBAM7yk70Wqhiygi3uHD7snLqupcL46"

def store_on_ipfs(knn_template, user_key):

    encoded_content = base64.b64encode(knn_template).decode('utf-8')

    body = [{
        "path": f'{user_key}_tem.json',
        "content": encoded_content,
    }]

    cid = evm_api.ipfs.upload_folder(
        api_key=api_key,
        body=body,
    )

    print(cid)
    return cid

def retrieve_from_ipfs(cid):
    ipfs_gateway = 'https://ipfs.moralis.io'

    # Concatenate the IPFS gateway URL with the CID
    url = f'{ipfs_gateway}/ipfs/{cid}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content
            # Process the retrieved data as needed
            print(data)
            return data
        else:
            print('Error:', response.status_code)
            return 0
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return 0
