from django import forms
from django.core import validators
#from first_app.models import Album,Musician   #direct access kora jaito
from first_app import models    #eivabe import korle models.Album diye access kora lagbe
# alternate of html form

def even_or_odd(value):
    if value%2==1:
        raise forms.ValidationError("Please insert  a even number! ")

class user_form(forms.Form):
    # <label for="user_name">Full Name: </label>
    # <input type="text" name="user_name" value="" required>
    #initial like value in html  ,initial="Saju"
    #placeholder Enter your fill name
    # attrs dictionary te shob hTML attribute use korte parbo ja dorker
    #style = "width:300px"
    # user_name= forms.CharField(required=True,label="Full Name",widget=forms.TextInput(attrs={'placeholder':'Enter your full name','style':'width:200px'}))
    # user_email=forms.EmailField(label="Email", widget =forms.TextInput(attrs={'placeholder':'Enter your mail'}) )
    #<input type="date"> TextInput means html r input tag r attribute gula
    # user_dob=forms.DateField(label="Date of Birth",widget=forms.TextInput(attrs={'type':'date'}))

    # boolean_field=forms.BooleanField(required=False)
    # char_field=forms.CharField(max_length=10,min_length=5)

    # drop_field=forms.ChoiceField(choices=(('','--Select Option--'),('1','First'),('2','Second'),('3','Third')),required=False)

    # choices=(('A','A'),('B','B'),('C','C'))
    # radio_field=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)

    # choices=(('','--Select Option--'),('1','First'),('2','Second'),('3','Third'))
    # multiple_choice_field=forms.MultipleChoiceField(choices=choices,required=False)

    # choices=(('A','A'),('B','B'),('C','C'))
    # field=forms.MultipleChoiceField(choices=choices,widget=forms.CheckboxSelectMultiple)
    #multiple Radio Field
    # name=forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    # number_field=forms.IntegerField(validators=[validators.MaxValueValidator(15),validators.MinValueValidator(5)])
    # number_field=forms.IntegerField(validators=[even_or_odd])
    user_email=forms.EmailField()
    user_vmail=forms.EmailField()

    def clean(self):
        all_cleaned_data=super().clean()    #siper ei form er shob data variable a ene rakhbe
        user_email=all_cleaned_data.get('user_email')
        user_vmail=all_cleaned_data.get('user_vmail')

        if user_email!=user_vmail :
            raise forms.ValidationError("Field's don't match!!")


class MusicianForm(forms.ModelForm):
    class Meta:
        model= models.Musician
        fields= "__all__"
        # exclude=['first_name']  #first_name bad
        # fields=('first_name','last_name',) # egula thakbe just
        
