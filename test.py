from pdf2image import convert_from_path
import requests
import json
import os
from file_paths import retrive_file_paths


def pdf_to_text(pdf_path, output_text_file, image_dir, book_name):

    os.makedirs(f"{image_dir}/{book_name}/images", exist_ok=True)
    os.makedirs(f"{image_dir}/{book_name}/text", exist_ok=True)


    print("Converting PDF to images...")
    images = convert_from_path(pdf_path, poppler_path="poppler-23.11.0/Library/bin")


    print("Saving images...")
    for i, image in enumerate(images):
        image.save(f"{image_dir}/{book_name}/images/{i}.jpg", 'JPEG')
        print(f"Image {i + 1} saved.")


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


pdf_path = r"D:\PDF_to_OCR\2015.307602.Hindhi-pad-piues-Ki.pdf"
output_text_file = "pad_pues_ki.txt"
image_dir = "pad_pues_ki_images"
book_name = "pad_pues_ki"

pdf_to_text(pdf_path, output_text_file, image_dir, book_name)
