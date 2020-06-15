from django.db import models

# Create your models here.

LANG_LIST = [('eng', 'English'), ('rus', 'Русский'),
             ('fra', 'Francais'), ('ukr', 'Ukrainian')]


class FileModel(models.Model):
    user_file = models.FileField(upload_to='ocr/%Y/%m/%d')
    file_extension = models.CharField(max_length=250, blank=True)
    rec_lang = models.CharField(
        max_length=3, choices=LANG_LIST, default='eng', blank=True)
    ocr_text = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
