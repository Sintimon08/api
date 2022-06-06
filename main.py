import requests

data = requests.get('https://yandex.ru/images/?utm_source=main_stripe_big')

print(data)