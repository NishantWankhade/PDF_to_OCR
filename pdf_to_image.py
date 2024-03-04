from pdf2image import convert_from_path
import os

def convert_to_images(pdf_path,output_path):

    os.makedirs(f"{output_path}/images", exist_ok=True)

    print("Converting PDF to images...")
    images = convert_from_path(pdf_path, poppler_path="poppler-23.11.0/Library/bin")

    print("Saving images...")
    for i, image in enumerate(images):
        image.save(f"{output_path}/images/{i + 1}.jpg", 'JPEG')
