from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from myapp.models import Contact,Driver,ordermodel,customer,product,Delivery,Shop
from .forms import OrderForm,PlaceOrderForm

# Create your views here.
def index(request):
    #return HttpResponse("this is a homepage!")
    return render(request,'index.html')
def about(request):
    #return HttpResponse("this is aboutpage")
    return render(request,'about.html')
def order(request):
    #return HttpResponse("Place your order here")
    customers = customer.objects.all()

    if request.method == 'POST':
        # Get form data from the request
        customer_id = request.POST.get('customer')
        selected_products = request.POST.getlist('products')

        # Create a new order based on the form data
        customer_instance = customer.objects.get(pk=customer_id)
        order = ordermodel(customer=customer_instance)
        order.save()

        # Add selected products to the order
        order.product.add(*selected_products)

    else:
        # Render the form and pass the customers to the template
        context = {
            'customers': customers,
        }
        return render(request, 'youractions.html', context)
    #return render(request,'youractions.html')
def delivery(request):
    return render(request,'deliveryguy.html')
def viewassigned(request):
    deliv = Delivery.objects.all()
    #datafromCustomer = customer.objects.values('firstname','lastname','customermobile1','customeraddress').all()
    #datafromOrder = Delivery.objects.values('deliverystatus','paymentstatus','paymentmethod')
    context={
        'deliv' : deliv,
        #'Address': customeraddress
    }
    return render(request,'viewassigned.html',context)
def myorders(request):
    deliv = Delivery.objects.all()
    context={
        'deliv' : deliv,
    
    }
    return render(request,'myorders.html',context)
def vieworder(request):
    prod = Delivery.objects.all()
    context={
        'prod' : prod,
    }
    return render(request,'vieworder.html',context)
def updatestatus(request, id):
    delivery=Delivery.objects.get(id = id)
    if request.method == "POST":
        #delivery.order.id = request.POST.get('Order.id')
        delivery.deliverystatus = request.POST.get('DeliveryStatus')
        delivery.paymentstatus = request.POST.get('paymentstatus')
        delivery.save()
    return render(request,'updatestatus.html',{'delivery':delivery})

'''def assigndriver(request, id):
    delivery=Delivery.objects.get(id = id)
    if request.method == "POST":
        #delivery.order.id = request.POST.get('Order.id')
        delivery.deliverystatus = request.POST.get('DeliveryStatus')
        delivery.paymentstatus = request.POST.get('paymentstatus')
        delivery.billamount = request.POST.get('billamount')
        #delivery.deliveryagent = request.POST.get('deliveryagent')
        #driver_id = request.POST.get('Driver')  # Get the selected driver's ID
        #driver = Driver.objects.get(id=driver_id)  # Retrieve the selected driver object
        driver=Driver.objects.all
        delivery.deliveryagent = driver  # Assign the selected driver to the delivery
        delivery.save()
    drivers = Driver.objects.all()
    return render(request,'assigndriver.html',{'delivery':delivery,'drivers': driver})'''

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            selected_order = form.cleaned_data['order']
            new_delivery = form.save(commit=False)
            new_delivery.order = selected_order
            new_delivery.save()
            return HttpResponse("Order Created successfully.")
    else:
        form = OrderForm()
    
    return render(request, 'order_form.html', {'form': form})
def place_order(request):
    if request.method == 'POST':
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            selected_shop = form.cleaned_data['shop']
            selected_products = form.cleaned_data['product']

            # Filter products based on the selected shop
            products = selected_shop.product_set.all()

            new_order = ordermodel(customer=customer)
            new_order.save()

            # Set only the selected products that belong to the selected shop
            new_order.product.set(products.filter(id__in=selected_products))

            return HttpResponse("Order Placed successfully.")
    else:
        form = PlaceOrderForm()

    return render(request, 'place_order.html', {'form': form})

    
def contact(request):
    #return HttpResponse("Contact Us.")
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(Name=name,Email=email,phone=phone,desc=desc,date= datetime.today())
        contact.save()
    return render(request,'contact.html')
def register(request):
    #return HttpResponse("Contact Us.")
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        middlename=request.POST.get('middlename')
        lastname=request.POST.get('lastname')
        customermobile1=request.POST.get('customermobile1')
        alternatenumber=request.POST.get('alternatenumber')
        customeraddress=request.POST.get('customeraddress')
        register = customer(firstname=firstname,middlename=middlename,lastname=lastname,customermobile1=customermobile1,alternatenumber=alternatenumber,customeraddress=customeraddress)
        register.save()
    return render(request,'register.html')
