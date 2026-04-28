from django import forms

class CommentForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre: ', help_text='100 caracteres maximos')
    comentario = forms.CharField(max_length=1000, label='Comentario:', help_text='1000 caracteres maximos')
    url = forms.URLField(label='URL: ', required=False, min_length=10, initial='https://', help_text='URL valida')
    
