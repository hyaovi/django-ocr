
from functools import partial
from contextlib import suppress

import pytesseract
from PIL import ImageFilter, Image
from pdf2image import convert_from_bytes


def text_extract(lang, image_file):
    return pytesseract.image_to_string(image_file, lang=lang)


def handle_input(fileobj, multi=False):
    if multi:
        yield from convert_from_bytes(fileobj.read(), 500)

    with suppress(IOError):
        img = Image.open(fileobj)
        img = img.convert('RGB')
        img = img.filter(ImageFilter.SHARPEN)
        # text = text_extract(lang, img)
        yield img


def get_text(fileobj, lang, multi):
    extract = partial(text_extract, lang)
    results = map(extract, handle_input(fileobj, multi))
    return ''.join(results)
