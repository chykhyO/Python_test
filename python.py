import requests

url = 'https://discord.com/api/webhooks/1430245473955872981/oKKIGGydiJiqTlQrjeaCAkIgJYqp_kxxgSJvUSz8C0URFpn98JCVShq2P1Io7r8I_PkZ'

payload = {
    'content' : 'Hi!',
}

headers = {
    'Authorization' : 'MTQwMjU5MjE5NDUxODU4MTI1OA.GcCnSy.5SvZx8kEXZD76blrs_TXs0gx5tECfJU2KK55b4'
}


while True:
    res = requests.post(url, payload, headers=headers)