import requests
import time
import random
from tqdm import tqdm

# headers
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'referer': ''
}

# Target video url
url = ''    
for i in tqdm(range(1, 622)):
    if len(str(i)) < 2:
        id = "00" + str(i)
    elif len(str(i)) == 2:
        id = "0" + str(i)
    else:
        id = str(i)
    file_name = "{id}.ts".format(id=id)
    with open("./deview/" + file_name, "wb") as f:
        try:
            res = requests.get(url.format(id=id), headers=headers)
            f.write(res.content)
        except:
            continue
    time.sleep(random.uniform(1, 3))


