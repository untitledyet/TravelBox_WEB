import requests


def smsoffice_send(number, code):
    api_key = '399699a18ba645eb8d2c420d44f0930f'
    destination = number
    sender = 'Auto Finder'
    text = 'დაადასტურეთ კოდით : ' + str(code)

    url = f'http://smsoffice.ge/api/v2/send?key={api_key}&destination={destination}&sender={sender}&content={text}'
    print(url)

    response = requests.get(url)

    print(response.content)
