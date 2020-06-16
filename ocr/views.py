import io
import os


from django.shortcuts import render, redirect

from .forms import UserFileForm, FileModelForm
from .models import FileModel
from .ocr_engine import handle_extraction, handle_pdf_file


def homepage(request):
    context = {'form': UserFileForm()}
    if request.method == 'POST':
        user_input = UserFileForm(request.POST, request.FILES)
        if user_input.is_valid():

            ext = str(request.FILES['user_file']).split('.')[-1]
            lang = request.POST['lang']

            text = handle_file(
                request.FILES['user_file'], ext, lang)
            context['text'] = text
            return render(request, 'ocr/index.html', context)

    return render(request, 'ocr/index.html', context)


def handle_file(f, ext, lang='eng'):
    filename = 'temp.%s' % ext
    text = ''
    with open(filename, 'wb+') as temp:
        for chunk in f.chunks():
            temp.write(chunk)
    abs_file_path = os.path.abspath(filename)
    if ext.strip().lower() == 'pdf':
        text = handle_pdf_file(abs_file_path, lang)
    else:
        text = handle_extraction(abs_file_path, lang)
    os.remove(abs_file_path)
    return text
