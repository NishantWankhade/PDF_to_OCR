# PDF_to_OCR

Project for PDF file to its OCR text output, supporting multilingual detections using Surya Modules.

## Setup and Installation - Surya Pipeline

- Create Virtual Python environment 

```bash 
python -m venv surya_venv 
```

- Activate the venv 

```bash
source surya_venv/Scripts/activate
```

- Install Surya Python module

```bash
pip install surya-ocr
```

- Requires Pytorch to be installed

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
