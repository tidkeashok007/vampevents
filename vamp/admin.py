from django.contrib import admin

# Register your models here.

from vamp.models import contactPost,Index_About_Images,Index_Service_Images,Index_Gallery_Images,Index_FAQ_Questions

admin.site.register(contactPost)
admin.site.register(Index_About_Images)
admin.site.register(Index_Service_Images)
admin.site.register(Index_Gallery_Images)
admin.site.register(Index_FAQ_Questions)