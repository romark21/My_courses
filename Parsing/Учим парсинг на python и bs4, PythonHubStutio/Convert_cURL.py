import requests

cookies = {
    'ARRAffinity': 'bf9d08a74da8563b0a987c31acd9bcac1fecb888afd7a8be0477fce7f38c9c1a',
    'nshgxbs-jsuysbs': 'A3f4Xy9bJlZYbABt+iRyEA==',
}

headers = {
    'authority': 'my.e-klase.lv',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,lv;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'ARRAffinity=bf9d08a74da8563b0a987c31acd9bcac1fecb888afd7a8be0477fce7f38c9c1a; nshgxbs-jsuysbs=A3f4Xy9bJlZYbABt+iRyEA==',
    'origin': 'https://www.e-klase.lv',
    'referer': 'https://www.e-klase.lv/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = {
    'v': '15',
}

data = 'fake_pass=j*paliek&UserName=211009-21492&Password=j*paliek'

response = requests.post('https://my.e-klase.lv/', params=params, cookies=cookies, headers=headers, data=data)

with open('Convert_cURL.html', 'w', encoding='utf-8') as file:
    file.write(response.text)