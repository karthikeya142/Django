from django.contrib import admin
from django.urls import path
from myapp import views

app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
     #book/2
    path('book/<int:book_id>/',views.detail, name="detail"),
    # here <int:book_id> treated as integer numbers
    path('add/',views.add, name ='add_book'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
]

#597. Namespacing URLs
#So namespactsking is nothing, but it's actually using app names for your URL patterns.


#598. Adding Staticfiles
