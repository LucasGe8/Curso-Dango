from django import forms

class CommentForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre: ', help_text='100 caracteres maximos')
    comentario = forms.CharField(max_length=1000, label='Comentario:', help_text='1000 caracteres maximos')
    url = forms.URLField(label='URL: ', required=False, min_length=10, initial='https://', help_text='URL valida')
    
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre: ', widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Ingrese su nombre'}))
    email = forms.EmailField(label='Correo: ', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}))
    mensaje = forms.CharField(max_length=1000, label='Mensaje:', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje'}))

    def clean_nombre(self):
        name = self.cleaned_data['nombre']
        if name != 'Open':
            raise forms.ValidationError("El nombre debe contener la palabra Open")
        return name