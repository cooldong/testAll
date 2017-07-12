import urllib.request
import http.cookiejar


url = 'http://weibo.com/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username': '15991685275',  'password': '111111'}
# headers = {'User-Agent': user_agent}
# data = urllib.parse.urlencode(values).encode(encoding='UTF8')
# request = urllib.request.Request(url, data, headers)
# response = urllib.request.urlopen(request)
# page = response.read()

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)

HTTPCookieProcessor = urllib.request.HTTPCookieProcessor(cookie)
response = urllib.request.build_opener(HTTPCookieProcessor).open(url)
for item in cookie:
    print('Name = '+item.name)
    print ('Value = '+item.value)
cookie.save(ignore_discard=True, ignore_expires=True)
# print(page)
