from django.contrib import admin
from myapp.models import Contact,customer,Driver,Delivery
from myapp.models import Shop
from myapp.models import product
from myapp.models import ordermodel
# Register your models here.

admin.site.register(Contact)
admin.site.register(Shop)
admin.site.register(product)
admin.site.register(ordermodel)
admin.site.register(customer)
admin.site.register(Driver)
admin.site.register(Delivery)