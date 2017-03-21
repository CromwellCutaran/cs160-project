from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #image = SM_produce.objects.get(id=1)
    #img = image.image_path
    #return render(request, 'lesson': img)
    return render(request, 'store/index0.html')

