from pdf2image import convert_from_path


def convert_to_images(pdf_path, image_dir, book_name):

    os.makedirs(f"{image_dir}/{book_name}/images", exist_ok=True)

    print("Converting PDF to images...")
    images = convert_from_path(pdf_path, poppler_path="poppler-23.11.0/Library/bin")

    print("Saving images...")
    for i, image in enumerate(images):
        image.save(f"{image_dir}/{book_name}/images/{i}.jpg", 'JPEG')
        print(f"Image {i + 1} saved.")

    print("Performing OCR on images...")