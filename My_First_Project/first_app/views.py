from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms
# Create your views here.





def index(request):
    diction={'sample_text':'This is a text'}
    return render(request,'first_app/index.html',context=diction)

#
# def index(request):
#     #return HttpResponse("<h1>Hello World</h1> ")
#     #equivalemt select * from Musician order by first_name
#     musician_list= Musician.objects.order_by('first_name')
#     diction={'text_1':'This is a list of Musicians','musician':musician_list}
#     return render(request,'first_app/index.html',context=diction)
#
# def form(request):
#     new_form=forms.user_form()
#     diction={'test_form':new_form,'heading_1': "This form is created using djnago library"}
#
#     if request.method=='POST':                      #submit hoise form
#         new_form=forms.user_form(request.POST)      #value ta new form ei overload korlam
#         diction.update({'test_form':new_form})
#         if new_form.is_valid():                     #form er value gula valid kina
#
#             # user_name=new_form.cleaned_data['user_name']
#             # user_email=new_form.cleaned_data['user_email']
#             # user_dob=new_form.cleaned_data['user_dob']
#             #
#             # diction.update({'user_name':user_name})
#             # diction.update({'user_email':user_email})
#             # diction.update({'user_dob':user_dob})
#             diction.update({'field':'Fields Match'})
#             diction.update({'form_submitted':"Yes"})
#
#     return render(request,'first_app/form.html',context=diction)


#formModel print
def form(request):
    new_form=forms.MusicianForm()

    if request.method=='POST':
        new_form=forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction={'test_form':new_form,'heading_1':'Add new Musicians'}
    return render(request,'first_app/form.html',context=diction)




def home(request):
    return HttpResponse("<h1>This is home</h1> <a href='contact/'>Contact Page</a> <a href='about/'>About US</a>")

def contact(request):
    # href='/' mane main domain a back korbe
    return HttpResponse("<h1>This is contact page</h1> <a href='/first_app'>Home Page</a> <a href='/first_app/about/'>About US</a>")

def about(request):
    return HttpResponse("<h1>This is about us</h1> <a href='/first_app/contact/'>Contact Page</a> <a href='/first_app/'>Home Page</a>")
