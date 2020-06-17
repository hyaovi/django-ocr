from django.shortcuts import render, redirect

from .forms import UserFileForm, FileModelForm
from .models import FileModel
from .ocr_engine import get_text


def homepage(request):
    context = {'form': UserFileForm()}
    if request.method == 'POST':
        user_input = UserFileForm(request.POST, request.FILES)
        if user_input.is_valid():
            fileobj = request.FILES['user_file']
            lang = user_input.cleaned_data['lang']
            is_image = fileobj.name.endswith(('jpg', 'png', 'jpeg', 'tiff'))
            if is_image:
                multi = False
            else:
                multi = True
            text = get_text(fileobj, lang, multi)
            context['text'] = text
            return render(request, 'ocr/index.html', context)

    return render(request, 'ocr/index.html', context)
