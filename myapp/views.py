from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Book
from .forms import BookForm
# Create your views here.
def index(request):
    # 589. Passing Objects
    book_list =Book.objects.all()
    context={
        'book_list':book_list
    }
    return render(request,'myapp/index.html',context)

#583. Creating Another view
def karthik(request):
    return HttpResponse("this is another views")


#589. Passing Objects

#592. DetailView Part 1
'''def detail(request,book_id):
    return HttpResponse("This is Book no %s" % book_id)'''

#594. DetailView Part 3
def detail(request,book_id):
    book= Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html',{'book':book})
def add(request):
    if request.method == "POST":
        name= request.POST.get('name',)
        desc = request.POST.get('desc', )
        price = request.POST.get('price', )
        book_image = request.FILES['book_image']

        book =Book(name=name, desc=desc, price=price, book_image=book_image)
        book.save()
    return render(request,'myapp/add_book.html')
def update(request,id):
    book =Book.objects.get(id=id)
    form =BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'form':form,'book':book})
def delete(request,id):
    if request.method=="POST":
        book=Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')