Django is a high-level, open-source web framework for building web applications, written in Python. It follows the Model-View-Controller (MVC) architectural pattern, although in Django, it's often referred to as Model-View-Template (MVT).

Key Features:
Rapid Development: Django encourages fast development by providing a lot of built-in features such as an admin panel, authentication system, and URL routing.
DRY Principle: "Don’t Repeat Yourself" — Django promotes reusability and efficiency, helping developers write less code.
Security: It helps developers avoid common security pitfalls like SQL injection, cross-site scripting, and clickjacking.
Scalability: Django can be used for small projects as well as large-scale applications.
ORM (Object-Relational Mapping): Django includes an ORM that allows developers to interact with databases using Python code instead of raw SQL.

Common Uses:
Building web applications like social media sites, e-commerce platforms, and content management systems.
Projects like Instagram, Pinterest, and Mozilla are known to use Django due to its scalability and efficiency.
Django's philosophy is to make it easier to build complex, database-driven websites quickly with less code.




Creating A Django Project
Open cmd
```sh
  django-admin startproject mysite
   ```
 create a first Django app inside the mysite .
```sh
django-admin startapp myapp
```
Running Django Project On Localhost
```sh
python manage.py runserver
```
the process of creating tables out of a Django model is called as making migrations.
```sh
python manage.py makemigrations
```
create those tables, you need to type in another command.
```sh
python manage.py migrate
```
