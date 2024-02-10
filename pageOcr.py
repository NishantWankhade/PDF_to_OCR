import requests
import json

url = "http://bhasha.iiit.ac.in/pageocr/api"
payload = {'language': 'hindi',
'version': 'v4_robust',
'modality': 'printed',
'layout_model': 'v2_doctr'}


count = 0

while count < 516 :
    files=[
    ('image',(
    '1.jpg',
    open(f'Bharatiya-SahityaShastra/{count}.jpg','rb'),
    'image/jpeg')
    )
    ]
    resp = requests.post(url, headers={}, data=payload, files=files)

    req_json = json.loads(resp.text)
    print(req_json["text"])

    with open(f"Ocred Book/{count}.txt", "w", encoding="utf-8") as f:
        f.write(req_json["text"])
    
    print(f"{count} done !")
    count = count + 1