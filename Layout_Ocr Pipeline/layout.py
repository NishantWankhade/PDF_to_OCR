import requests
url = "https://ilocr.iiit.ac.in/layout/"
payload = {'model': 'doctr'}
files = [
('images', (
 '1.jpg',
 open(r'D:\PDF_to_OCR\example\1.png', 'rb'),
 'image/jpeg'
 )
)
]
headers = {}
response = requests.post(url, headers=headers, data=payload,
files=files)
print(response.text)