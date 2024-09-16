from django.contrib import admin
from .models import Book
#588. Creating Superuser
#A super user is some user which actually has access to all of your website and he can control and manipulate
#therefore he must actually have all the privileges to add data, remove data, modify data or view data.

# Register your models here.
admin.site.register(Book)