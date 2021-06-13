from django.db import models

# Create your models here.

LANG_LIST = [('eng', 'English'), ('rus', 'Русский'),
             ('fra', 'Francais'), ('ukr', 'Ukrainian'), ('spa', 'Spanish'), ('ita', 'Italian'), ('por', 'Portugese'), ('afr', 'African'), ('chi_tra+chi_sim', 'Chinese')]


class FileModel(models.Model):
    user_file = models.FileField(upload_to='ocr/%Y/%m/%d')
    file_extension = models.CharField(max_length=250, blank=True)
    rec_lang = models.CharField(
        max_length=20, choices=LANG_LIST, default='eng', blank=True)
    ocr_text = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

# contact us model

class ContactUs(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    mail = models.CharField(max_length=50, default="")
    message = models.TextField(default="")
    
    def __str__(self):
        return self.name