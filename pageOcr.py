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
    for i in range(len(images)):
        files = [('image', ('1.jpg', open(f'{output_path}/images/{i + 1}.jpg', 'rb'), 'image/jpeg'))]
        resp = requests.post(url, headers={}, data=payload, files=files)
        req_json = json.loads(resp.text)

        text_file_path = f"{output_path}/text/{i+1}.txt"
        file_paths.append(text_file_path)

        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write(req_json["text"])


    print("Combining text files into a single text file...")
    file_paths.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    
    first_page = ""
    second_page = ""
    third_page = ""
    
    each_slice_size = len(images)/3  
    
    with open(output_path+"/ocr_by_Bhashini.txt", 'w', encoding='utf-8') as outfile:
        for page_number, file_path in enumerate(file_paths, start=1):
            with open(file_path, 'r', encoding='utf-8') as infile:
                infile_text = infile.read()
                outfile.write(infile_text + f'\n\n ---{page_number} end--- \n\n')  # add a newline between files if needed

                #First Page Selection
                # 1. Page_number comes under first slice
                # 2. First_page is empty
                # 3. First_page length is above some threshold of 1000 characters 
                if(page_number < each_slice_size and len(first_page) == 0 and len(infile_text) > 1000):
                    first_page = str(page_number)
                    print(page_number,len(infile_text))
                elif(page_number > each_slice_size and page_number < 2 * each_slice_size and len(second_page) == 0 and len(infile_text) > 1000):
                    second_page = str(page_number)
                    print(page_number,len(infile_text))
                elif(len(infile_text) > 1000):
                    third_page = str(page_number)
                    print(page_number,len(infile_text))
                
        print("Combined text file created.")

    print(first_page, second_page, third_page)
    
    # # Optionally to delete the text files and imagess
    # # Commented out for now
    for file_path in file_paths:
        if(file_path.find(first_page + '.txt') == -1 and file_path.find(second_page + '.txt') == -1 and file_path.find(third_page + '.txt') == -1):
            os.remove(file_path)
    
    for i in range(len(images)):
        image_path = f'{output_path}/images/{i+1}.jpg'
        if(image_path.find(first_page + '.jpg') == -1 and image_path.find(second_page + '.jpg') == -1 and image_path.find(third_page + '.jpg') == -1):
            os.remove(image_path)


if __name__ == "__main__" :
    
    # Pdf Path
    pdf_path = "" 
    output_path = pdf_path.replace(".pdf", "")

    start = time.perf_counter()
    
    convert_to_images(pdf_path, output_path)
    
    pdf_to_text(output_path)

    end = time.perf_counter()

    print(round(end - start, 2))
