import requests, base64, hmac, hashlib, time, json

def get_headers(request_path, apikey, secret, method='GET'):

    # nonce값 생성
    nonce = str(time.time())
    method = method
    request_path = request_path

    #필수 정보를 연결하여 prehash 문자열을 생성함
    what = nonce + method + request_path
    #base64로 secret을 디코딩함
    key = base64.b64decode(secret)
    #hmac으로 필수 메시지에 서명하고
    signature = hmac.new(key, str(what).encode('utf-8'), hashlib.sha512)
    #그 결과물을 base64로 인코딩함
    signature_b64 = base64.b64encode(signature.digest())
    
    custom_headers = {
        'API-Key': apikey,
        'Signature': signature_b64,
        'Nonce': nonce
    }
    
    return custom_headers

def get_order_headers(request_path, apikey, secret, method, request_body):

    # nonce값 생성
    nonce = str(time.time())
    method = method
    request_path = request_path
    

    #필수 정보를 연결하여 prehash 문자열을 생성함
    what = nonce + method + request_path + json.dumps(request_body)#, sort_keys=True)
    print("what : ", what)
    #base64로 secret을 디코딩함
    key = base64.b64decode(secret)
    #hmac으로 필수 메시지에 서명하고
    signature = hmac.new(key, str(what).encode('utf-8'), hashlib.sha512)
    #그 결과물을 base64로 인코딩함
    signature_b64 = base64.b64encode(signature.digest())
    
    custom_headers = {
        'API-Key': apikey,
        'Signature': signature_b64,
        'Nonce': nonce
    }
    
    return custom_headers

def get_balances(apikey, secret, asset_name=None):
    ## 잔액 조회하기
    print("get_balances!")
    if asset_name:
        request_path = f'/balances/{asset_name}'
    else:
        request_path = '/balances'
    method = "GET"
    headers = get_headers(request_path, apikey, secret, method)
    req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = headers)
    
    if req.ok:
        return req
    else:
        print ('요청 에러')
        print(req)
        return req

def make_orders(apikey, secret, trading_pair):
    ## 주문 하기
    print("make_orders!")
    request_path = '/orders'
    method = "POST"
    request_body = {
        "type": "limit", #limit 또는 market	
        "side": "buy", #buy 또는 sell
        "price": 6.45,
        "amount": 1000.0,
        "tradingPairName": trading_pair,
    }
    
    headers = get_order_headers(request_path, apikey, secret, method, request_body)
    req = requests.post(url = 'https://api.gopax.co.kr' + request_path, headers = headers, json=request_body)
    
    if req.ok:
        return req
    else:
        print ('요청 에러')
        print(req)
        return req

def get_orders(apikey, secret, order_id=None):
    ## 주문 조회하기
    if order_id:
        request_path = f'/orders/{order_id}'
    else:
        request_path = '/orders'
    method = "GET"
    headers = get_headers(request_path, apikey, secret, method)
    req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = headers)
    
    if req.ok:
        return req
    else:
        print ('요청 에러')
        print(req)
        return req

def cancel_order_id(apikey, secret, order_id):
    ## 주문 id로 주문 취소하기
    
    request_path = f'/orders/{order_id}'
    method = "DELETE"
    headers = get_headers(request_path, apikey, secret, method)
    req = requests.delete(url = 'https://api.gopax.co.kr' + request_path, headers = headers)
    
    if req.ok:
        return req
    else:
        print ('요청 에러')
        print(req)
        return req

def get_order_book(apikey, secret, trading_pair):
    # orderbook 조회하기
    print("get_order_book!")
    request_path = f'/trading-pairs/{trading_pair}/book?level=1'
    method = "GET"
    headers = get_headers(request_path, apikey, secret, method)
    req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = headers)
    
    if req.ok:
        return req
    else:
        print ('요청 에러')
        print(req)
        return req

def get_order_book_recently(apikey, secret, trading_pair):
    # orderbook 조회하기
    
    request_path = f'/trading-pairs/{trading_pair}/trades'
    method = "GET"
    headers = get_headers(request_path, apikey, secret, method)
    req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = headers)
    
    if req.ok:
        return req
    else:
        print ('요청 에러')
        print(req)
        return req

