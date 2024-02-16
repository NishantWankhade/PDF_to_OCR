from pdf2image import convert_from_path
import requests
import json
import os
from file_paths import retrive_file_paths
from pdf_to_image import convert_to_images


def pdf_to_text(pdf_path, output_text_file, image_dir, book_name):

    os.makedirs(f"{image_dir}/{book_name}/text", exist_ok=True)

    convert_to_images(pdf_path, image_dir, book_name) # call Convert PDF to images function

    print("Performing OCR on images...")
    url = "http://bhasha.iiit.ac.in/pageocr/api"
    payload = {'language': 'hindi',
               'version': 'v4_robust',
               'modality': 'printed',
               'layout_model': 'v2_doctr'}

    file_paths = []
    for i in range(len(images)):
        files = [('image', (f'{i}.jpg', open(f'{image_dir}/{book_name}/images/{i}.jpg', 'rb'), 'image/jpeg'))]
        resp = requests.post(url, headers={}, data=payload, files=files)
        req_json = json.loads(resp.text)

        text_file_path = f"{image_dir}/{book_name}/text/{i}.txt"
        file_paths.append(text_file_path)

        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(req_json["text"])

        print(f"Text file {i + 1} created.")


    print("Combining text files into a single text file...")
    file_paths.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    with open(output_text_file, 'w', encoding='utf-8') as outfile:
        for page_number, file_path in enumerate(file_paths, start=1):
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n')  # add a newline between files if needed
        print("Combined text file created.")

    # Optionally to delete the text files and imagess
    # Commented out for now
    # for file_path in file_paths:
    #     os.remove(file_path)
    #
    # for i in range(len(images)):
    #     os.remove(f'{image_dir}/{book_name}/images/{i}.jpg')


pdf_path = "" # Path to the PDF file
output_text_file = "" # Path to the output text file
image_dir = "" # Path to the directory where images and text files will be saved
book_name = "" # Name of the book, used to create subdirectories in "image_dir

pdf_to_text(pdf_path, output_text_file, image_dir, book_name)
