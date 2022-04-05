import requests
try:

    response = requests.get('https://catfact.ninja/fact')
    print(response.status_code)
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact']
    print(f'A random cat fact{fact}')

except Exception as e:
        print(e)
        print('error making a request')