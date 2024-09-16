from django.db import models

# Create your models here.

#585. Creating Models In Django
class Book(models.Model):
    #So here inside the model, you can actually go ahead and add a string representation of that model.
    #So a string representation is nothing, but it's the way your object is going to be displayed when yougo ahead and try to get a particular object.
    #So here, in order to add the string representation, you would do def.
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
    book_image = models.ImageField(default='default.jpg', upload_to='book_images/')

#587. Adding Objects To Database
#So in case if you actually wanted to go ahead and if you wanted to add some data to the database, normally
#you would need to use something which is called as SQL or structured query language.
#So you would have to go ahead and write in some SQL queries to insert data into the database.
#However, as now we are using Django, we don't actually have to go ahead and write SQL.
#Instead we can use Django ORM So this lecture is exactly going to be about that.
#, how exactly can we go ahead and use the Django ORM?
#