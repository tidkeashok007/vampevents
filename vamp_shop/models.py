from django.db import models
import os

# Define a function to determine the upload path for the image
def get_image_upload_path(instance, filename):
    # Construct the upload path based on the category
    upload_path = 'service_product/'

    # Append the category folder based on the 'category' field of the instance
    if instance.category == 'Make Me Glam':
        if instance.subcategory == 'Groom':
            upload_path += 'Make Me Glam/Groom/'
        elif instance.subcategory == 'Bride':
            upload_path += 'Make Me Glam/Bride/'
    
    elif instance.category == 'Costumes':
        if instance.subcategory == 'Groom':
            upload_path += 'Costumes/Groom/'
        elif instance.subcategory == 'Bride':
            upload_path += 'Costumes/Bride/'

    elif instance.category == 'Decorations':
        if instance.subcategory == 'Indoor':
            upload_path += 'Decorations/Indoor/'
        elif instance.subcategory == 'Outdoor':
            upload_path += 'Decorations/Outdoor/'

    elif instance.category == 'Mehendi':
        upload_path += 'Mehendi/'

    elif instance.category == 'Party-Space':
        upload_path += 'Party-Space/'

    elif instance.category == 'Capture the moment':
        upload_path += 'Capture the moment/'
    

    # Append the filename to the upload path
    return os.path.join(upload_path, filename)

CATEGORY_CHOICES = (
    ('Make Me Glam','Make Me Glam'),
    ('Costumes','Costumes'),
    ('Decorations','Decorations'),
    ('Mehendi','Mehendi'),
    ('Party-Space','Party-Space'),
    ('Capture the moment','Capture the moment'),
)

SUBCATEGORY_CHOICES = (
    ('Groom','Groom'),
    ('Bride','Bride'),
    ('Indoor','Indoor'),
    ('Outdoor','Outdoor'),
    ('Mehendi','Mehendi'),
    ('Party-Space','Party-Space'),
    ('Capture the moment','Capture the moment'),
)

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to=get_image_upload_path, default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=50, default='')
    subcategory = models.CharField(choices=SUBCATEGORY_CHOICES,max_length=80, default='')

    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    subject = models.CharField(max_length=250, default='')
    message = models.CharField(max_length=500, default='')
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=10, default=0)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class orderupdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=100)
    timestamp = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[:10] + '...'
