from django.shortcuts import render, redirect,HttpResponse
from vamp.models import contactPost,Index_Gallery_Images,Index_FAQ_Questions,Index_About_Images


# Create your views here.
def index(request):
    pics = Index_Gallery_Images.objects.all()
    faq = Index_FAQ_Questions.objects.all()
    about = Index_About_Images.objects.all()
    contact = contactPost.objects.filter()
    context = {
        'pics': pics,
        'faq':faq,
        'about':about,
        'contact':contact
    }
    return render(request, 'vampapp/home.html',context)
    

def insert(request):
    if request.method=="POST":
        contact=contactPost()
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.fname=fname
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1>Thank you</h2>")
    else:
        return render(request, 'vampapp/home.html')






