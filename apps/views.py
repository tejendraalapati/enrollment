from django.shortcuts import render
from .models import profile,contact
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone')
        message=request.POST.get('message')
        con=contact(name=name,email=email,phone_number=phone_number,message=message)
        con.save()
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        address = request.POST.get('address')
        course = request.POST.get('choose')
        percentage = request.POST.get('percent')
        photo = request.FILES.get('photo')
        en = profile(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                phone_number=phone_number,
                address=address,
                Course=course,
                Percentage=percentage,
                Photo=photo
            )
        en.save()

    return render(request, 'register.html')

def enroll(request):
    allenroll=profile.objects.all()
    if request.method == 'GET':
        st=request.GET.get('search')
        if st!=None:
            allenroll=profile.objects.filter(first_name=st)
    
    context={'task':allenroll}
    return render(request,'enrollment.html',context)


        
