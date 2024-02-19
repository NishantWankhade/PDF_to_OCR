from pdf2image import convert_from_path
import requests
import json
import os
from file_paths import retrive_file_paths
from pdf_to_image import convert_to_images
import time


def pdf_to_text(output_path):

    os.makedirs(f"{output_path}/text", exist_ok=True)
    print("Performing OCR on images...")
    url = "http://bhasha.iiit.ac.in/pageocr/api"
    payload = {'language': 'hindi',
               'version': 'v4_robust',
               'modality': 'printed',
               'layout_model': 'v2_doctr'}
    
    images = os.listdir(f"{output_path}/images")
    file_paths = []
    for i in range(1, len(images)):
        files = [('image', ('1.jpg', open(f'{output_path}/images/{i + 1}.jpg', 'rb'), 'image/jpeg'))]
        resp = requests.post(url, headers={}, data=payload, files=files)
        req_json = json.loads(resp.text)

        text_file_path = f"{output_path}/text/{i+1}.txt"
        file_paths.append(text_file_path)

        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(req_json["text"])

        print(f"Text file {i + 1} created.")


    print("Combining text files into a single text file...")
    file_paths.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    with open(output_path+"/ocr_by_Bhashini.txt", 'w', encoding='utf-8') as outfile:
        for page_number, file_path in enumerate(file_paths, start=1):
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n')  # add a newline between files if needed
        print("Combined text file created.")

    # # Optionally to delete the text files and imagess
    # # Commented out for now
    for file_path in file_paths:
        os.remove(file_path)
    
    for i in range(1,len(images)):
        os.remove(f'{output_path}/images/{i}.jpg')


if __name__ == "__main__" :
    
    # Path to the pdf
    pdf_path = "" 
    output_path = pdf_path.replace(".pdf", "")

    start = time.perf_counter()
    
    convert_to_images(pdf_path, output_path)
    
    pdf_to_text(output_path)

    end = time.perf_counter()

    print(round(end - start, 2))
