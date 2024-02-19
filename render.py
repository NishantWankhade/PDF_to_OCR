import os

text = ""
with open("output_text.txt", "r", encoding = "utf-8") as fp:
    text = fp.read()

text = text.replace("TextLine", "\nTextLine")

with open("output_ocr_surya.txt", "w", encoding = 'utf-8') as file:
    file.write(text)