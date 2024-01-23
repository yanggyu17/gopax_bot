import time, base64, hmac, hashlib, requests, json
from utils import get_balances,make_orders, get_orders, cancel_order_id, get_order_book, get_order_book_recently

file_path = "api_key.txt"

## load api key
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    conkey = lines[0].strip()
    secretkey = lines[1].strip()
    
# 발급받은 api키와 시크릿키를 입력한다
apikey = conkey
secret = secretkey

asset_name = "VELO"
ticker_pair = "VELO-KRW"


# HTML 소스 가져오기
def HTMLsouceGet(p):
    print (p.text)
    return p.json()
	
def main():
    balance = get_balances(apikey, secret, asset_name)
    print(balance.text)
    time.sleep(1)
    order_book = get_order_book(apikey, secret, ticker_pair)
    print(order_book.text)
    time.sleep(1)
    req = make_orders(apikey, secret, ticker_pair)
    print("req done!")
    




if __name__ == '__main__':
	main()