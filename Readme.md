#Django Login Tutorial

##Requirement
```
Python 3.5
MySQL
```
##Environment
There are two choice for you.

1. Install this following Requirement on your environment.
  ```
  Django==1.10.1
  mysqlclient==1.3.7
  ```

2. Use our Virtual Environment by do following step
  ```
  $ cd env/Scripts
  env/Scripts$ activate
  (env) env/Scripts$ cd ../..
  ```

##Step by step
1. Start Django Project
  ```
  $django-admin startproject djangologin
  $cd djangologin
  ```

2. Initialize App
  ```
  djangologin$ python manage.py startapp login
  ```

3. Edit Django to use MySQL Database
  In `djangologin\settings.py` edit this part  
  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'HOST' : 'localhost',  #You can fill this with your DATABASE Host
          'NAME': 'login-tutorial',   #You can fill this with your DATABASE name
          'USER' : 'root', #You can fill this with your user in database
          'PASSWORD' : '', #You can fill this with your password
          'PORT' : '3306' #You can fill this with your database port
      }
  }
  ```
  Migrate database
  ```
  djangologin$ python manage.py migrate
  ```

4. Connect your app with your project
  In `djangologin\settings.py` add this
  ```
  INSTALLED_APPS = [
      'login.apps.LoginConfig', #Connect your login app
  ```

5. Route urls to app urls
  ```
  from django.conf.urls import url,include
  from django.contrib import admin

  urlpatterns = [
      url(r'^login/',include('login.urls')),
      url(r'^admin/', admin.site.urls),
  ]
  ```

6. Create Simple html
  Create Directory `login\templates\login` then create file `index.html`
  ```
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <title>Login</title>
  </header>
  <body>
    <h1>Login</h1>
  </body>
  </html>
  ```

  Edit `login\views.py` to render from our `index.html`
  ```
  from django.shortcuts import render

  # Create your views here.
  def index(request) :
      return render(request,'login/index.html')
  ```

  Create `login\urls.py` to route url to our views
  ```
  from django.conf.urls import url

  from . import views

  app_name = 'login'

  urlpatterns = [
      url(r'^$', views.index, name='index'),
  ]
  ```

  Let run!
  ```
  djangologin$ python manage.py runserver
  ```

  Go to <http://localhost:8000/login/> and see what happen!
