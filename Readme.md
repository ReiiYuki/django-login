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
  ```python
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
  ```python
  INSTALLED_APPS = [
      'login.apps.LoginConfig', #Connect your login app
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

5. Route urls to app urls
  ```python
  from django.conf.urls import url,include
  from django.contrib import admin

  urlpatterns = [
      url(r'^login/',include('login.urls')),
      url(r'^admin/', admin.site.urls),
  ]
  ```

6. Create Simple html
  Create Directory `login\templates\login` then create file `index.html`
  ```html
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
  ```python
  from django.shortcuts import render

  # Create your views here.
  def index(request) :
      return render(request,'login/index.html')
  ```

  Create `login\urls.py` to route url to our views
  ```python
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

  Go to http://localhost:8000/login/ and see what happen!

7. Create Register form & Login form
  Edit `login\templates\login\index.html`
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <title>Login</title>
  </header>
  <body>
    <h1>Login</h1>
    <form>
      Username:<br>
      <input type="text" name="username"><br>
      Password:<br>
      <input type="text" name="password"><br>
      <input type="submit" value="Login">
    </form>
  </body>
  </html>
  ```

  Create `login\templates\login\register.html`
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <title>Register</title>
  </header>
  <body>
    <h1>Register</h1>
    <form>
      Username:<br>
      <input type="text" name="username"><br>
      Password:<br>
      <input type="text" name="password"><br>
      Email:<br>
      <input type="text" name="email"><br>
      <input type="submit" value="Register">
    </form>
  </body>
  </html>
  ```

  Edit `login\views.py` to render our register page
  ```python
  from django.shortcuts import render

  # Create your views here.

  def index(request) :
      return render(request,'login/index.html')

  def register_view(request) :
      return render(request,'login/register.html')
  ```

  Edit `login\urls.py` to route to our register page
  ```python
  from django.conf.urls import url

  from . import views

  app_name = 'login'

  urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^register/$',views.register_view, name='register_view'),
  ]
  ```
  Let run!
  ```
  djangologin$ python manage.py runserver
  ```

  Go to http://localhost:8000/login/ and see what happen!

  Go to http://localhost:8000/login/register/ and see what happen!

  Wow! we got the form!

8. Make the form active
  First, we modify our `login\templates\login\register.html`
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <title>Register</title>
  </header>
  <body>
    <h1>Register</h1>
    <form action="{% url 'login:register' %}" method="post">
      {% csrf_token %}
      Username:<br>
      <input type="text" name="username"><br>
      Password:<br>
      <input type="password" name="password"><br>
      Email:<br>
      <input type="email" name="email"><br>
      <input type="submit" value="Register">
    </form>
  </body>
  </html>
  ```

  Then modify `login\templates\login\index.html`
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <title>Login</title>
  </header>
  <body>
    <h1>Login</h1>
    <form action="{% url 'login:login' %}" method="post">
      {% csrf_token %}
      Username:<br>
      <input type="text" name="username"><br>
      Password:<br>
      <input type="password" name="password"><br>
      <input type="submit" value="Login">
    </form>
  </body>
  </html>
  ```

  Then I modify `login\views.py` to have method which receive data from form
  ```python
  from django.shortcuts import render
  from django.http import HttpResponseRedirect,HttpResponse
  from django.urls import reverse
  from django.contrib.auth.models import User
  import django.contrib.auth  as auth

  # Create your views here.

  def index(request) :
      print(request.user)
      return render(request,'login/index.html')

  def register_view(request) :
      print(request.POST)
      return render(request,'login/register.html')

  def success(request) :
      print (request.user)
      user = request.user
      return HttpResponse("Welcome %s"%user.username)

  def register(request) :
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      user = User.objects.create_user(username,email,password)
      user.save()
      return HttpResponseRedirect(reverse('login:index'))

  def login(request) :
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None :
          auth.login(request,user)
          return HttpResponseRedirect(reverse('login:success'))
      else :
          return HttpResponseRedirect(reverse('login:index'))
```

  After that we modify `login\urls.py` to create route to each views
  ```python
  from django.conf.urls import url

  from . import views

  app_name = 'login'

  urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^register/$',views.register_view, name='register_view'),
      url(r'^register/register/$',views.register,name='register'),
      url(r'^login/$',views.login,name='login'),
      url(r'^success/$',views.success,name='success')
  ]
  ```

  Now let's try to create our user `<http://localhost:8000/login/register/>` and try to login it!

  Wow! it work!
