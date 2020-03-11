from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(required=True, label='ファイル', help_text='拡張子CSVのファイルをアップロードしてください')

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.name.endswith('.csv'):
            return file
        else:
            raise forms.ValidationError('拡張子がCSVではありません')
