from pdf2image import convert_from_path
 
images = convert_from_path('book.pdf', poppler_path="poppler-23.11.0/Library/bin")
 
for i in range(len(images)):
    images[i].save('Bharatiya-SahityaShastra/'+ str(i) +'.jpg', 'JPEG')