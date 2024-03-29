import os
import argparse
import requests
from dotenv import load_dotenv




def shorten_link(long_url,token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
    	'Authorization': f'Bearer {token}'    
    }
    params = {
        'long_url': long_url
    }
    response = requests.post(url = url, json=params, headers=headers)
    response.raise_for_status()
    return response.json()['id']
    



def is_bitlink(bitlink,token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
		'Authorization': f'Bearer {token}'    
	}
    response = requests.get(url=url, headers=headers)
    return response.ok


        
        
def count_clicks(bitlink,token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'    
    }
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


    

def main():
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
    parser = argparse.ArgumentParser(
    description='Описание что делает программа'
)
    parser.add_argument('url', help='ссылка')
    args = parser.parse_args()
    url = args.url
    try:
        if is_bitlink(url,token):
            total_clicks = count_clicks(url,token)
            print(" Счёт :", total_clicks)
        else:
            bitlink = shorten_link(url,token)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print("api ссылка неверна")




if __name__ == '__main__':
    main()



