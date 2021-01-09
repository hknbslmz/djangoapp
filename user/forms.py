from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="kullanıcı adı")
    password=forms.CharField(label="parola", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=20, label="kullanıcı adı")
    name=forms.CharField(max_length=30, label="isim")
    surname=forms.CharField(max_length=30, label="soyisim")
    email=forms.EmailField(max_length=200, label="e-mail")
    date=forms.DateTimeField(widget=forms.DateTimeInput,label="doğum tarihi")
    password=forms.CharField(max_length=15,label="parola",widget=forms.PasswordInput)  
    confirm=forms.CharField(max_length=15,label="parolayı doğrula",widget=forms.PasswordInput)
    def clean(self):
        username= self.cleaned_data.get("username")
        name= self.cleaned_data.get("name")
        surname= self.cleaned_data.get("surname")
        email= self.cleaned_data.get("email")
        date= self.cleaned_data.get("date")
        password= self.cleaned_data.get("password")
        confirm= self.cleaned_data.get("confirm")

        if confirm and password and password != confirm:
            raise forms.ValidationError("parola eşleşmiyor")
    
        values={
            "username":username,
            "password":password,
            "email":email,
            "name":name,
            "surname":surname,
            "date":date,
        }
        return values


class ProfileForm(forms.Form):
    user_img=forms.FileField(label="") 
    def clean(self):
        user_img= self.cleaned_data.get("user_img") 
        values={
            "user_img":user_img,
        }
        return values

