import http.client
import json

conn = http.client.HTTPSConnection("api.n46.glastonr.net")
payload = "{\"refresh_token\":\"6a8994c5-796c-4144-a13d-81e6aba2a645\"}"
headers = {
    'Accept': ' */*',
    'Accept-Encoding': ' br;q=1.0, gzip;q=0.9, deflate;q=0.8',
    'Accept-Language': ' zh-Hans-CN;q=1.0, en-CN;q=0.9, ja-CN;q=0.8',
    'Connection': ' keep-alive',
    'Content-Length': ' 56',
    'Host': ' api.n46.glastonr.net',
    'User-Agent': ' Hot/1.0.03 (jp.co.sonymusic.communication.nogizaka; build:117; iOS 15.3.1) Alamofire/5.5.0',
    'X-Talk-App-ID': ' jp.co.sonymusic.communication.nogizaka 2.2',
    'Content-Type': ' application/json'
}
conn.request("POST", "/v2/update_token", payload, headers)
res = conn.getresponse()
data1 = res.read().decode("UTF-8")
responseObject = json.loads(data1)
print(responseObject)
access_token = responseObject['access_token']
print(access_token)
