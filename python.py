import requests

url = 'https://discord.com/api/v9/channels/1465749994589130797/messages'

payload = {
    'content' : 'FAH!',
}

headers = {
    'Authorization' : 'MTQwMjU5MjE5NDUxODU4MTI1OA.GcCnSy.5SvZx8kEXZD76blrs_TXs0gx5tECfJU2KK55b4'
}


while True:
    res = requests.post(url, payload, headers=headers)
