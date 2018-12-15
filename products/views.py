from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home(request):
    product = Product.objects
    return render(request,'products/home.html',{'product':product})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon'] and request.POST['url'] :
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://'+request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/'+ str(product.id))
        else:
            return render(request,'products/create.html',{'error':'All fields must be filled!'})
    else:
        return render(request,'products/create.html')

def detail(request,product_id):
    dproduct=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':dproduct})

@login_required(login_url="/accounts/signup")
def upvote(request,product_id):
    if request.method == 'POST':
        dproduct=get_object_or_404(Product,pk=product_id)
        dproduct.votes_total = dproduct.votes_total + 1
        dproduct.save()
    return redirect('/products/'+ str(dproduct.id))
    #return render(request,'products/detail.html',{'product':dproduct})
