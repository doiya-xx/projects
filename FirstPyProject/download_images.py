import json
import re
import requests  # request img from web
import shutil  # save img locally
import os

members = ['asuka', 'renka']
file_types = {'picture': '.jpg', 'video': '.mp4', 'voice': '.m4a'}

for member in members:
    with open(member + "_msg.json", "r", encoding="UTF-8") as fr:
        json_data = json.load(fr)
    # print(json.dumps(json_data['messages'], sort_keys=False, indent=4, ensure_ascii=False))

    for file_type in file_types:
        print(f"Start download {member}'s {file_type}s")
        dir_path = f'./msg/{member}_msg_{file_type}s/'
        files = os.listdir(dir_path)
        files.sort(key=lambda x: int(x[:-20]))
        if len(files) == 0:
            file_id = 0
        else:
            file_id = int(re.search(r'(.*)-(.*)-(.*)', files[-1]).group(1))

        for item in json_data['messages']:
            if item['type'] == file_type:
                if item['id'] <= file_id:
                    print(f"id: {item['id']} has downloaded")
                    continue
                print(f'id: {item["id"]}; file: {item["file"]}')
                url = item['file']
                file_name = re.search('(.*)/(.*)\\.jpg?(.*)', url).group(2)
                file_path = f"{dir_path}{file_name}{file_types[file_type]}"
                #
                res = requests.get(url, stream=True)
                if res.status_code == 200:
                    with open(file_path, 'wb') as f:
                        shutil.copyfileobj(res.raw, f)
                    print('Image successfully Downloaded: ', file_path)
                else:
                    print('Image Couldn\'t be retrieved')

        print(f"{member}'s {file_type}s has completed downloading")
