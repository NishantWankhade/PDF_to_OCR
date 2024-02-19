from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection.segformer import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from surya.postprocessing.text import sort_text_lines
import json

image = Image.open("11.Bharatiya-Sahityashastra_djvu/images/110.jpg")
langs = ["hi"] # Replace with your languages
det_processor, det_model = load_det_processor(), load_det_model()
rec_model, rec_processor = load_rec_model(), load_rec_processor()

predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)

result_dict = sort_text_lines(predictions[0].text_lines)
result_str = str(result_dict)

with open("output_text.txt", 'w', encoding="utf-8") as file:
    file.write(result_str)