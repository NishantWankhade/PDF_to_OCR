import requests
import os
import json

url = "https://ilocr.iiit.ac.in/layout/"
payload = {'model': 'doctr'}

def return_layout(path_to_book_folder):
    print("Parsing Layout ...")

    path_to_images_folder = path_to_book_folder + "/images"
    image_dir = os.listdir(path_to_images_folder)

    path_to_layouts_folder = path_to_book_folder + "/layouts"
    for i in image_dir:
        files = [
        ('images', (
        '1.jpg',
        open(f'{path_to_images_folder}/{i}', 'rb'),
        'image/jpeg'
        )
        )
        ]
        headers = {}
        response = requests.post(url, headers=headers, data=payload, files=files)
        req_json = json.loads(response.text)
        
        pg_no = i.split(".")[0]

        with open(f"{path_to_layouts_folder}/{pg_no}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(req_json))
    

if __name__=="__main__":
    book_name = "11.Bharatiya-Sahityashastra_djvu"
    path = os.getcwd() + "/" + book_name 
    print(path)
    return_layout(path)
