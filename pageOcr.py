from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection.segformer import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from surya.postprocessing.text import sort_text_lines, draw_text_on_image
import json

image = Image.open("11.Bharatiya-Sahityashastra_djvu/images/383.jpg")
langs = ["hi"] # Replace with your languages
det_processor, det_model = load_det_processor(), load_det_model()
rec_model, rec_processor = load_rec_model(), load_rec_processor()

predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)


tolerance_for_vertical_grouping = 1.25
result_dict = sort_text_lines(predictions[0].text_lines,tolerance_for_vertical_grouping)
result_str = ""


bboxes = []
texts = []
for textline in result_dict:
    bboxes.append(textline.bbox)
    texts.append(textline.text)
    result_str = result_str + textline.text
    result_str = result_str + "\n"

tolerance_for_vertical_grouping = str(tolerance_for_vertical_grouping).replace(".","-")
with open(f"surya_outputText_tolerance_{tolerance_for_vertical_grouping}.txt", 'w', encoding="utf-8") as file:
    file.write(result_str)

image = draw_text_on_image(bboxes, texts, (image.width, image.height))

image = image.save("Output_Surya.jpg")