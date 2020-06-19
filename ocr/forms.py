from django import forms
from . import models


class FileModelForm(forms.ModelForm):
    class Meta:
        model = models.FileModel
        fields = ('user_file', 'rec_lang')

        widgets = {
            'user_file': forms.FileInput(
                attrs={
                    'class': 'form-control-file custom-file'
                }
            ),
            'rec_lang': forms.Select(
                attrs={
                    'class': 'form-control custom-select',
                }
            )
        }
        labels = {
            'rec_lang': 'File language'
        }


class UserFileForm (forms.Form):
    userfile = forms.FileField(label='Select a file')
    lang = forms.ChoiceField(label='Select a language', choices=models.LANG_LIST,  widget=forms.Select(
        attrs={'class': 'form-control custom-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userfile'].widget.attrs.update(
            {'class': 'form-control custom-file'})

    def clean_userfile(self):
        fileobj = self.cleaned_data['userfile']
        print(fileobj)
        if not fileobj.__str__().endswith(('pdf', 'jpg', 'png', 'jpeg', 'tiff')):
            raise forms.ValidationError('unsupported file type')

        return fileobj
