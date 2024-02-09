import requests
import json

url = "http://bhasha.iiit.ac.in/pageocr/api"
payload = {'language': 'hindi',
'version': 'v4_robust',
'modality': 'printed',
'layout_model': 'v2_doctr'}

files=[
 ('image',(
 '1.jpg',
 open('1.png','rb'),
 'image/jpeg')
 )
]
resp = requests.post(url, headers={}, data=payload, files=files)

# print(resp.text)
req_json = json.loads(resp.text)
print(req_json["text"])

with open("file.txt", "w", encoding="utf-8") as f:
    f.write(req_json["text"])