from django.db import models

class Index_About_Images(models.Model):
    product_id = models.AutoField
    headline = models.CharField(max_length=100)
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='index/about', default='')

    def __str__(self):
        return self.headline

class Index_Service_Images(models.Model):
    product_id = models.AutoField
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='index/service', default='')

    def __str__(self):
        return self.title
    
class Index_Gallery_Images(models.Model):
    product_id = models.AutoField
    image = models.ImageField(upload_to='index/gallery', default='')

class Index_FAQ_Questions(models.Model):
    question_id = models.AutoField
    question = models.CharField(max_length=350)
    answers = models.CharField(max_length=550)
    pub_date = models.DateField()

    def __str__(self):
        return self.question

class contactPost(models.Model):
    id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=60,default='')
    subject=models.CharField(max_length=50,default='')
    message=models.TextField()

    def __str__(self):
        return self.fname


