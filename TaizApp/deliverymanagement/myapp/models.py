from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=122)
    Email= models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.Name

class Shop(models.Model):
    shopname = models.CharField(max_length=150)
    shopdescription = models.CharField(max_length = 122)
    shopaddress = models.CharField(max_length=150)
    shopphone = models.IntegerField()
    def __str__(self):
        return self.shopname

class customer(models.Model):
    firstname = models.CharField(max_length=122)
    middlename = models.CharField(max_length=122,blank=True)
    lastname = models.CharField(max_length=122)
    customermobile1 = models.IntegerField()
    alternatenumber = models.IntegerField(default=0,null=False)
    customeraddress = models.CharField(max_length=150)
    def __str__(self):
        return "%s,%s" %(self.firstname,self.lastname)

class product(models.Model):
    productname = models.CharField(max_length=122)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    productdescription = models.CharField(max_length=122)
    #quantity = models.IntegerField()
    shop= models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __str__(self):
        return self.productname
class ordermodel(models.Model):
    createdon = models.DateTimeField(auto_now_add=True)
    customer=models.ForeignKey(customer, on_delete=models.CASCADE)
    #price=models.DecimalField(max_digits=7,decimal_places=2)
    #product = models.ManyToManyField('product',related_name='order',blank=True)
    #product=models.ForeignKey(product,on_delete=models.CASCADE,default=0)
    product=models.ManyToManyField(product)
    #quantity= models.IntegerField()
    def add_products(self,product):
        #return f'Order: {self.createdon.strftime("%b %d %I:%M %p")}'
        #return(self.createdon.strftime)
        return self.product.add(*product)
    def __str__(self):
        return f'Order for {self.customer}'
class Driver(models.Model):
    drivername = models.CharField(max_length=150)
    drivercontact = models.CharField(max_length = 122)
    def __str__(self):
        return self.drivername
class Delivery(models.Model):
    order = models.ForeignKey(ordermodel, on_delete=models.CASCADE,default=2,null=True)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE,null=True)
    deliverystatus = models.CharField(max_length=122,null=True)
    paymentstatus = models.CharField(max_length=122,null=True)
    paymentmethod = models.CharField(max_length=122,null=True)
    billamount = models.DecimalField(max_digits=9,decimal_places=2,default=0,null=True)
    deliveryagent = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.deliverystatus