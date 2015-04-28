# coding: utf-8
from django import forms

SERVICE_TYPES = (
    ("LO", "Limpieza del hogar"),
    ("JA", "Jardinería"),
    ("SN", "Servicios de Niñería"),
    ("MA", "Mascotas"),
    ("CO", "Comida"),
    ("OT", "Otros servicios"),
)

IS_COMPANY = (
    (True, "Compañía"),
    (False, "Freelance")
)
PRICE_DELIMITER = (
    ("H", "hora"),
    ("S", "servicio"),
    ("U", "unidad"),
    ("D", "día"),
)

PRICE_DELIMITER = (
    ("H", "hora"),
    ("S", "servicio"),
    ("U", "unidad"),
    ("D", "día"),
)

STATE = (
    ("JAL", "Jalisco"),
)

CITY = (
    ("GDL", "Guadalajara"),
    ("ZAP", "Zapopan"),
    ("TON", "Tonalá"),
    ("TLAJ", "Tlajomulco"),
)

class RegisterForm(forms.Form):
    user_name = forms.CharField(required=True, label="Nombre", max_length=255, help_text="Nombre del nuevo Gurú", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    user_lname = forms.CharField(required=True, label="Apellido", max_length=255, help_text="Apellido", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    email = forms.EmailField(required=True, label="E-mail", help_text="Email", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    user_password = forms.CharField(required=True, label='Password', max_length=255, help_text='Password', widget=forms.PasswordInput(attrs={'class' : 'password required edd-input form-control'}))
    user_password2 = forms.CharField(required=True, label='Confirmar Password', max_length=255, help_text='Password', widget=forms.PasswordInput(attrs={'class' : 'password required edd-input form-control'}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        user_password = cleaned_data.get("user_password")
        user_password2 = cleaned_data.get("user_password2")
        if not user_password == user_password2:
            self.add_error('user_password2', "El Password y la confirmación no coinciden")


class EditProfile(forms.Form):
    user_name = forms.CharField(label="Nombre", max_length=255, help_text="Nombre del nuevo Gurú", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    user_last_name = forms.CharField(label="Apellido", max_length=255, help_text="Apellido", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    user_password = forms.CharField(label='Password', max_length=255, help_text='Password', widget=forms.PasswordInput(attrs={'class' : 'password required edd-input form-control'}))
    user_password2 = forms.CharField(label='Confirmar Password', max_length=255, help_text='Password', widget=forms.PasswordInput(attrs={'class' : 'password required edd-input form-control'}))

    def clean(self):
        cleaned_data = super(EditProfile, self).clean()
        user_password = cleaned_data.get("user_password")
        user_password2 = cleaned_data.get("user_password2")
        if not user_password == user_password2:
            self.add_error('user_password2', "La contraseña y la confirmación no coinciden")

class AddServiceForm(forms.Form):
    service_title = forms.CharField(required=True, label="Nombre del servicio", max_length=45, help_text="Título del servicio", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    service_type = forms.ChoiceField(required=True, label="Tipo del servicio", choices=SERVICE_TYPES)
    service_is_company = forms.ChoiceField(required=True, label="Tipo de negocio", widget=forms.RadioSelect, choices=IS_COMPANY)
    service_company_name = forms.CharField(required=False, label="Nombre de la compañía", max_length=45, help_text="Nombre de la compañía", widget=forms.TextInput(attrs={'class' : 'edd-input form-control'}))
    service_account = forms.CharField(required=True, label="Número de Cuenta", max_length=16, help_text="Número de cuenta bancario", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    service_price = forms.CharField(required=True, label="Precio", max_length=45, help_text="$", widget=forms.TextInput(attrs={'class' : 'required edd-input form-control'}))
    service_price_delimiter = forms.ChoiceField(required=True, label=" X ", choices=PRICE_DELIMITER)
    service_state = forms.ChoiceField(required=True, label=" Estado ", choices=STATE)
    service_city = forms.ChoiceField(required=True, label=" Ciudad", choices=CITY)
    service_image = forms.ImageField(required=False, label="Imagen");
    service_email = forms.EmailField(label="E-mail de contacto", max_length=70, help_text="e-mail", widget=forms.TextInput(attrs={'class' : 'edd-input form-control'}))
    service_telephone = forms.CharField(label="Teléfono", max_length=15, help_text="# de teléfono", widget=forms.TextInput(attrs={'class' : 'edd-input form-control'}))
    service_brief_desc = forms.CharField(required=True, label="Breve descripción", help_text="Escribe una breve descripción de tu servicio", max_length=140, widget = forms.Textarea)
    service_description = forms.CharField(required=True, label="Descripción", help_text="Escribe una descripción más detallada de tu servicio", widget = forms.Textarea)




