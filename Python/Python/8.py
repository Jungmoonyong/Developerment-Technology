import urllib.request

url = input('분석 url : ')

http_req = urllib.request.urlopen(url)
if http_req.code == 200:
    print(http_req.headers)