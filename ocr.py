import requests
import json
import base64 
  
  
with open("2.png", "rb") as image2string: 
    converted_bytes = base64.b64encode(image2string.read()) 
    converted_string = converted_bytes.decode()


url = "https://ilocr.iiit.ac.in/ocr/infer"

payload = json.dumps({
"modality": "printed",
"language": "hi",
"version": "v4_robust",
"imageContent": [
 f"{converted_string}",
]
})

headers = {
'Content-Type': 'application/json',
}
response = requests.post(url, headers=headers, data=payload)
print(response.text)