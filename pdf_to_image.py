from pdf2image import convert_from_path
 
def convert_to_images(pdf_path, image_path, book_name):
    images = convert_from_path(pdf_path, poppler_path="poppler-23.11.0/Library/bin")
    
    for i in range(len(images)):
        images[i].save(f"{image_path}/{book_name}/images/" + str(i) +'.jpg', 'JPEG')


if __name__ == "__main__":
    print("Pdf_to_image")