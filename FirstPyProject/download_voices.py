import json
import os
import re
import requests  # request img from web
import shutil  # save img locally

member = 'asuka'

with open(member + "_msg.json", "r", encoding="UTF-8") as fr:
    json_data = json.load(fr)

# print(json.dumps(json_data, sort_keys=False, indent=4, ensure_ascii=False))

# print(json.dumps(json_data['messages'], sort_keys=False, indent=4, ensure_ascii=False))

for item in json_data['messages']:
    dir_path = f'./msg/{member}_msg_images/'
    files = os.listdir(dir_path)
    files.sort(key=lambda x: int(x[:-20]))
    file_id = int(re.search(r'(.*)-(.*)-(.*)', files[-1]).group(1))
    if item['id'] <= file_id:
        continue
    if item['type'] == 'voice':
        print(f'id: {item["id"]}; file: {item["file"]}')
        url = item['file']
        r = re.search('(.*)/(.*)\\.m4a?(.*)', url)
        file_name = "./msg/" + member + "_msg_voices/" + r.group(2) + ".m4a"
        #
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image successfully Downloaded: ', file_name)
        else:
            print('Image Couldn\'t be retrieved')
