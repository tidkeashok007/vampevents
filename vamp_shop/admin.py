from django.contrib import admin

from vamp_shop.models import Product, Contact, Orders, orderupdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(orderupdate)
