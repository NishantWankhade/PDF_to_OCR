import concurrent.futures
import shutil
import requests
import json
import os
import time
from pdf2image import convert_from_path
from file_paths import retrive_file_paths
from pdf_to_image import convert_to_images


def pdf_to_text(output_path):

    os.makedirs(f"{output_path}/text", exist_ok=True)
    # print("Performing OCR on images...")
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


    # print("Combining text files into a single text file...")
    file_paths.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    
    first_page = ""
    second_page = ""
    third_page = ""
    
    each_slice_size = len(images)/3  
    
    with open(output_path+"/ocr_by_Bhashini.txt", 'w', encoding='utf-8') as outfile:
        for page_number, file_path in enumerate(file_paths, start=1):
            with open(file_path, 'r', encoding='utf-8') as infile:
                infile_text = infile.read()
                outfile.write(infile_text + f'\n\n --- {page_number} end--- \n\n')  # add a newline between files if needed

                #First Page Selection
                # 1. Page_number comes under first slice
                # 2. First_page is empty
                # 3. First_page length is above some threshold of 1000 characters 
                if(page_number < each_slice_size and len(first_page) == 0 and len(infile_text) > 1000):
                    first_page = str(page_number)
                elif(page_number > each_slice_size and page_number < 2 * each_slice_size and len(second_page) == 0 and len(infile_text) > 1000):
                    second_page = str(page_number)
                elif(len(infile_text) > 1000):
                    third_page = str(page_number)
                
        # print("Combined text file created.")

    print(first_page, second_page, third_page)
    
    # # Optionally to delete the text files and imagess
    # # Commented out for now
    for file_path in file_paths:
        first_page_path = f"{output_path}/text/{first_page}.txt"
        second_page_path = f"{output_path}/text/{second_page}.txt"
        third_page_path = f"{output_path}/text/{third_page}.txt"
        
        if(file_path != first_page_path or file_path != second_page_path or file_path != third_page_path):
            os.remove(file_path)
    
    for i in range(len(images)):
        image_path = f'{output_path}/images/{i+1}.jpg'
        
        first_image_path = f"{output_path}/images/{first_page}.jpg"
        second_image_path = f"{output_path}/images/{second_page}.jpg"
        third_image_path = f"{output_path}/images/{third_page}.jpg"
        
        if(image_path != first_image_path or image_path != second_image_path or image_path != third_image_path):
            os.remove(image_path)


# Invoking the subsequent functions
def super_function(pdf_path):
    
    output_path = pdf_path.replace(".pdf", "")
    try :
        convert_to_images(pdf_path, output_path)
        pdf_to_text(output_path)
    except :
        shutil.rmtree(output_path)
    return pdf_path


if __name__ == "__main__" :
    
    pdf_file_paths = retrive_file_paths(2,"hindi_pdfs/pdfs")
    print(pdf_file_paths)
    
    start = time.perf_counter()
    
    # Use ThreadPoolExecutor for parallel downloading
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        # Submit tasks to the executor
        future_to_item = {executor.submit(super_function, ele): ele for ele in pdf_file_paths[0:5]}
        
        # Process as tasks complete
        for future in concurrent.futures.as_completed(future_to_item):
            item = future_to_item[future]
            try:
                data = future.result()
            except Exception as exc:
                # print(f'{item} generated an exception: {exc}')
                with open("exception_files.txt", 'a', encoding='utf-8') as f:
                    f.write(f'{item} generated an exception: {exc} \n') 
            else:
                # print(f'{item} downloaded successfully')
                with open("ocred_files.txt", 'a', encoding='utf-8') as f:
                    f.write(f'{item} \n') 
    
    
    end = time.perf_counter()

    print(round(end - start, 2))
