import json
from json.decoder import JSONDecodeError
from urllib.parse import urlencode

# params = {
#     "count": "100",
#     "created_from": "2022-02-21T16:24:39Z",
#     "order": "asc",
#     "updated_from": "2022-04-14T04:37:30Z"
# }
#
# urlparam = urlencode(params)
#
# print(urlparam)

# file = open("./renka_msg.json", "r+", encoding="UTF-8")
# json_data = json.load(file)
# print(type(json_data))
# print(type(json_data['messages']))
# print(json_data['messages'])
# json_data['messages'].append({"test": 11111111111111111111111})
# json.dump(obj=json_data, fp=file, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
# file.write(json_data)
# file.write("\n")
# file.close()

# with open("./renka_msg.json", "r", encoding="UTF-8") as fr:
#     json_data = json.load(fr)
#
# json_data['messages'].append({"test": 11111111111111111111111})
#
# with open("./renka_msg.json", "w", encoding="UTF-8") as fw:
#     json.dump(obj=json_data, fp=fw, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)

# with open("./renka_msg.json", "a+", encoding="UTF-8") as fr, open("./renka_msg.json", "w", encoding="UTF-8") as fw:
#     try:
#         json_data = json.load(fr)
#         json_data['messages'] = []
#         json.dump(obj=json_data, fp=fw, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)
#     except JSONDecodeError:
#         pass

import requests  # request img from web
import shutil  # save img locally

# res = requests.get("https://djznowbmqickg.cloudfront.net/private/messages/files/273-20220222-040332.jpg?Expires=1667660404&Signature=kSj6JmKEqkKfDzHFWH7YgP6nVhmKQGVU7ZYgmBdt~XC3GdEUmHLWMwYw24rryAXgS1sbrpf6WETfJrLsZHyGvvO0YuEm9FSc7u37vPA7KK5-cRJ2Y80JZt9hxL2jQOxr9ozlyE9vMBbhRjsBJR-ED3dhig-OB2HP0xS6b-nYHEq7mEa-I6CUav3AmjWPSD2ryX-kPyfI~OuCaSmY4V4nM2MVtYSngjwaMlEYaFnUTQDfJ43WwaqFXVOC05Ycx1DDnAWV4h6LoqHYyCBI-0TN00qVnpv1GdLX4S-queA4Ao~baGsZSlHAG~3xiuk6l0JTcITTKqcC9s560UxTDmTi0A__&Key-Pair-Id=K2YPX0KZV2O4IU", stream = True)
#
# if res.status_code == 200:
#     with open("273-20220222-040332.jpg", 'wb') as f:
#         shutil.copyfileobj(res.raw, f)
#     print('Image successfully Downloaded: ', "273-20220222-040332.jpg.jpg")
# else:
#     print('Image Couldn\'t be retrieved')

import re

# url = "https://djznowbmqickg.cloudfront.net/private/messages/files/932-20220227-092834.jpg?Expires=1667660404&Signature=mA1riveoo69r7Z6zHu~kjj2Jbd6u83SJYZAAmKfZA~VjiJa1HZsb24oLqtbppGVBRf1VecOGCypBPOoa1OTC6aWv1UW5zpusIu-5CQrH9Ybwl~L~nFdeimooXf~7rY98fTAwCYij2DFZ0ORIcnbRP3OGaXC05eOw3ictshMS5z8509Ketm8mvMVraQyHG-b44K48XLUzGWZfQKzQLdbLE9LhkbxAAXdzYITBnp81G4oc8-n4gYrTUjp0rjbh~gRRYU4lUWcBmJhOADAUtiuALERBg2BGg644yee6AKyoqDWb9sxBKLnZyrL7JveJW5931yj81zox8~q3t4jZD7GQYQ__&Key-Pair-Id=K2YPX0KZV2O4IU"
#
# r = re.search('(.*)/(.*)\\.jpg?(.*)', url)
#
# print(f'0: {r.group(0)}')
# print(f'1: {r.group(1)}')
# print(f'2: {r.group(2)}')
# print(f'3: {r.group(3)}')

# start_time = '2022-02-21T16:24:39Z'
# updated_from = '2022-04-04T10:53:03Z'
# rec = re.compile(r'(.*):(.*)Z')
#
#
# def change_time(time):
#     updated_time = str(int(time.group(2)) + 1).zfill(2)
#     return '{}:{}Z'.format(time.group(1), updated_time)
#
#
# print(updated_from)
# print(rec.sub(change_time, updated_from))

import os

# dir_path = './msg/renka_msg_images/'
# files = os.listdir(dir_path)
# files.sort(key=lambda x: int(x[:-20]))
# print(files)

# print(int(re.search(r'(.*)-(.*)-(.*)', files[-1]).group(1)))

# f = os.walk(dir_path)
# for root, dirs, files in os.walk(dir_path):
#     print(f'root: {root}, dirs: {dirs}, files: {files}')

file_type = {'images': '.jpg', 'videos': '.mp4', 'voices': '.m4a'}
print(file_type['images'])

for t in file_type:
    print(t)