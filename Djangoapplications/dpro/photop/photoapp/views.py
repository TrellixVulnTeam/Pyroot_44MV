from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo                 # for getting the table access
from django.template import loader        # template module 
from django.shortcuts import render       # render module 
from django.http import Http404

# Create your views here.

# Without templates 

# def index(request):
#     all_photos = Photo.objects.all()       # for displaying the table values 
#     html = ''

#     for photo in all_photos: 
#         url = '/photos/'+ str(photo.id)                
#         html+= '<a href="' + url + '">' + str(photo.name)+ '</a href><br>'   # the url gets stored as a photonamed hyperlink which is http://127.0.0.1:8000/photos/1/
#                                                                              # then the above url link has the detail view which displays This is the page for photo 1
#     return HttpResponse(html) 

# def detail(request, Photo_id):
    # photo = Photo.objects.get(id=Photo_id)
    # return HttpResponse("<h1>This is the page for Photo"+ str(photo.creator)+ "</h1>")


# using Templates - orgainised code - separate file for the html code 

def index(request):
    all_photos = Photo.objects.all()
    # template = loader.get_template('photoapp/index.html')    # loads the index.html file # using template 
    context = {
        'all_photos' : all_photos
    }
    # return HttpResponse(template.render(context, request))   # using template 
    return render(request, 'photoapp/index.html', context)     # using render 


# View for the detail page and also 404 error 

def detail(request, Photo_id):
    try:
        photo= Photo.objects.get(id=Photo_id)
    except Photo.DoesNotExist:
        raise Http404('Photo page not found')
    context = {
        'photo': photo
    }
    return render(request, 'photoapp/detail.html', context)





