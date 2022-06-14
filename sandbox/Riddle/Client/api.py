import requests

def get_raadsel():
    url = 'http://127.0.0.1:5000/raadsel'
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f'Invalid response. Status code: {r.status_code}')


# ----------------------------------------------------------

if __name__ == '__main__':

    print( get_raadsel() )