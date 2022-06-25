from django.shortcuts import render
import string,random
from .models import UploadDB
from django.http import FileResponse, HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        filename  = request.FILES['filename']
        n = 7
        res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = n))
        urlname = str(res)
        dbobj = UploadDB(file = filename,ulrfile = urlname)
        dbobj.save()
        print(filename)
        url =  urlname
        return render(request,"index.html",{'url':url})
    return render(request,"index.html")


def downloadfile(request,slug):
    dbobj = UploadDB.objects.get(ulrfile= slug)
    url = dbobj.file.url
    return render(request,"lastpage.html",{'url':url})
    



