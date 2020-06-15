import io
import os


from django.shortcuts import render, redirect

from .forms import UserFileForm, FileModelForm
from .models import FileModel
from .ocr_engine import handle_extraction


def homepage(request):

    if request.method == 'POST':
        user_input = UserFileForm(request.POST, request.FILES)
        if user_input.is_valid():

            ext = str(request.FILES['user_file']).split('.')[-1]
            lang = request.POST['lang']

            text = handle_file(
                request.FILES['user_file'], ext, lang)
            return render(request, 'ocr/index.html', {'text': text})

    user_form = UserFileForm()
    context = {'form': user_form}
    return render(request, 'ocr/index.html', context)


def handle_file(f, ext, lang='eng'):
    filename = 'temp.%s' % ext
    with open(filename, 'wb+') as temp:
        for chunk in f.chunks():
            temp.write(chunk)
    abs_file_path = os.path.abspath(filename)
    text = handle_extraction(abs_file_path, lang)
    return text
