import sys
import os

import pytesseract
from PIL import ImageFilter, Image
from pdf2image import convert_from_path


def user_input():
    file_path = ''
    lang = input('langage: eng,fra,rus, ukr: ')
    ext = input('extension')
    sharpened_image = image_processor(file_path)
    text = text_extract(sharpened_image)
    print(text)

# Extract text from picture


def text_extract(image_file, lang='eng'):
    return pytesseract.image_to_string(image_file, lang=lang)

# Sharpen picture for ocr extraction


def image_processor(image_path):
    image = None
    if isinstance(image_path, str):
        image = Image.open(image_path)

    else:
        image = Image.frombytes('RGBA', (128, 128), image_path, 'raw')

    return image.filter(ImageFilter.SHARPEN)


def convert_pdf(pdf_path):
    images_from_pdf = convert_from_path(pdf_path)
    return images_from_pdf


def handle_extraction(filepath, lang='eng'):
    try:
        print(filepath)
        im = Image.open(filepath)
        im = im.convert('RGB')
        im = im.filter(ImageFilter.SHARPEN)
        text = text_extract(im, lang=lang)
        return text
    except IOError as err:
        return 'err'


if __name__ == "__main__":
    pass
    # file_path = sys.argv[1]
    # print(file_path)

    # pdf = image_processor(file_path)
    # with open('res.txt', 'w') as f:
    #     f.write(pdf)
