## Run the docker
``` bash
cd docker
docker-compose up
```


## Get the PNG via http request
```python
import requests

message = './message.eml'

url = 'http://127.0.0.1:9595/'
headers = {}
data = open(message, 'rb').read()
resp = requests.post(url, headers=headers, files={'file': ('message', data)})

with open('./message.png', 'wb') as f:
    f.write(resp.content)
```
