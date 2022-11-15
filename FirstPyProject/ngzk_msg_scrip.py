import http.client
import json
from json.decoder import JSONDecodeError
import gzip
from urllib.parse import urlencode
import os
import re


def get_accsee_token():
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
    # print(responseObject)
    access_token = responseObject['access_token']
    print(f'access_token: {access_token}')
    return access_token


# access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Njc2NDczNjksInN1YiI6IjEzODk2In0.cSoXvIeDMekuU4h2xsvyHipiPczMfkSnEryIpcBemqg"


def get_batch_msg(access_token, updated_from, member):
    conn = http.client.HTTPSConnection("api.n46.glastonr.net")
    payload = ''
    headers = {
        'Host': 'api.n46.glastonr.net',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Talk-App-ID': 'jp.co.sonymusic.communication.nogizaka 2.2',
        'User-Agent': 'Hot/1.4.01 (jp.co.sonymusic.communication.nogizaka; build:140; iOS 16.0.0) Alamofire/5.6.2',
        'Accept-Language': 'zh-Hans-CN;q=1.0, en-CN;q=0.9, ja-CN;q=0.8',
        'Authorization': 'Bearer ' + access_token,
        'Accept-Encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
        'Content-Type': 'application/json'
    }
    params = {
        "count": "200",  # 获取msg的数量
        "created_from": "2022-02-21T16:24:39Z",  # msg 最开始的时间. 2022-02-21T16:24:39Z
        "order": "asc",  # asc正序；desc逆序；
        "updated_from": updated_from  # msg的时间点，采用的是格林尼治时间，与显示时间相差（-8）小时。2022-02-21T16:00:00Z
    }
    members = {
        "asuka": "3",
        "renka": "18"
    }
    print(f"GET /v2/groups/{members[member]}/timeline?{urlencode(params)}")
    conn.request(
        "GET",
        "/v2/groups/" + members[member] + "/timeline?" + urlencode(params),
        payload,
        headers
    )
    res = conn.getresponse()
    # 头部信息
    res_headers = res.headers
    print(res_headers)
    if res.getheader("Content-Encoding") is None:
        # 单获取一条数据时，不会压缩，不需要解压
        # bytes
        data = res.read().decode("UTF-8")
    else:
        # bytes
        data = gzip.decompress(res.read()).decode("UTF-8")
    # 变成字典
    # dict
    msg = json.loads(data)
    # print(list(msg))

    if 'letters' in msg:
        print(msg["letters"])
        del msg['letters']
    if 'comments' in msg:
        print(msg["comments"])
        del msg['comments']
    if 'continuation' in msg:
        print(msg["continuation"])
        del msg['continuation']
        continuation = True
    else:
        continuation = False

    # 顺序输出: sort_keys=True;格式化输出: indent=4; 紧凑输出: separators=(',', ':'); 字符不转义输出: ensure_ascii=False;
    # print(json.dumps(msg, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False))

    # 写入文件
    # file = open("renka_msg.json", "a", encoding="UTF-8")
    # json.dump(obj=msg, fp=file, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
    # file.write("\n")
    # file.close()

    file_names = {
        'renka': 'renka_msg.json',
        'asuka': 'asuka_msg.json'
    }

    file_name = file_names[member]

    if os.path.getsize(file_name) == 0:
        with open(file_name, "w", encoding="UTF-8") as f:
            json.dump(obj=msg, fp=f, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
    else:
        with open(file_name, "r", encoding="UTF-8") as fr:
            json_data = json.load(fr)

        if 'messages' in json_data:
            json_data['messages'] += msg['messages']
        else:
            json_data = msg

        with open(file_name, "w", encoding="UTF-8") as fw:
            json.dump(obj=json_data, fp=fw, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)

    if continuation:
        return msg['messages'][-1]['updated_at']
    else:
        return None


# def get_one_msg():
#     access_token = get_accsee_token()
#     conn = http.client.HTTPSConnection("api.n46.glastonr.net")
#     payload = ''
#     headers = {
#         'Host': 'api.n46.glastonr.net',
#         'Connection': 'keep-alive',
#         'Accept': '*/*',
#         'X-Talk-App-ID': 'jp.co.sonymusic.communication.nogizaka 2.2',
#         'User-Agent': 'Hot/1.4.01 (jp.co.sonymusic.communication.nogizaka; build:140; iOS 16.0.0) Alamofire/5.6.2',
#         'Accept-Language': 'zh-Hans-CN;q=1.0, en-CN;q=0.9, ja-CN;q=0.8',
#         'Authorization': 'Bearer ' + access_token,
#         'Accept-Encoding': 'br;q=1.0, gzip;q=0.9, deflate;q=0.8',
#         'Content-Type': 'application/json'
#     }
#     conn.request("GET", "/v2/messages/5171", payload, headers)
#     res = conn.getresponse()
#     # 头部信息
#     res_headers = res.headers
#     print(res_headers)
#     if res.getheader("Content-Encoding") is None:
#         # 单获取一条数据时，不会压缩，不需要解压
#         # bytes
#         data = res.read().decode("UTF-8")
#     else:
#         # bytes
#         data = gzip.decompress(res.read()).decode("UTF-8")
#     # 变成字典
#     # dict
#     msg = json.loads(data)

#     # 顺序输出: sort_keys=True;格式化输出: indent=4; 紧凑输出: separators=(',', ':'); 字符不转义输出: ensure_ascii=False;
#     print(json.dumps(msg, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False))


def change_time(time):
    updated_time = str(int(time.group(2)) + 1).zfill(2)
    return '{}:{}Z'.format(time.group(1), updated_time)


if __name__ == '__main__':
    member = 'renka'
    # 运行前需要把文件清空。（文件链接携带过期参数，所以每次需要重新生成文件。）
    with open(f'{member}_msg.json', "w", encoding="UTF-8") as f:
        f.truncate(0)

    rec = re.compile(r'(.*):(.*)Z')
    start_time = '2022-02-21T16:24:39Z'
    access_token = get_accsee_token()
    while True:
        updated_from = get_batch_msg(access_token, start_time, member)
        if updated_from is None:
            break
        print(updated_from)
        start_time = rec.sub(change_time, updated_from)
