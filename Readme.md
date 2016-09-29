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

  Go to `http://localhost:8000/login/` and see what happen!

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

  Go to `http://localhost:8000/login/` and see what happen!

  Go to `http://localhost:8000/login/register/` and see what happen!

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

  Now let's try to create our user `http://localhost:8000/login/register/` and try to login it!

  Wow! it work!

9. Last Step we will make it beautiful and the page after login

  First Let modify out `login/templates/login/index.html` to have some button to connect to register page and we apply bootstrap css to it.
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <title>Login</title>
  </header>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-12 col-xs-12 col-sm-12 col-lg-12">
          <h1>Login</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 col-xs-12 col-sm-8 col-lg-6">
          <form class="form-group" action="{% url 'login:login' %}" method="post">
            {% csrf_token %}
            Username:<br>
            <input class="form-control" type="text" name="username"><br>
            Password:<br>
            <input class="form-control" type="password" name="password"><br>
            <input class="btn btn-primary" type="submit" name="action" value="Login">
            <input class="btn btn-primary" type="submit" name="action" value="Register">
          </form>
        </div>
      </div>
    </div>
  </body>
  </html>
  ```

  Let's modify our `login/templates/login/register.html` to use bootstrap css too
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <title>Register</title>
  </header>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-12 col-xs-12 col-sm-12 col-lg-12">
          <h1>Register</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 col-xs-12 col-sm-8 col-lg-6">
          <form class="form-group" action="{% url 'login:register' %}" method="post">
            {% csrf_token %}
            Username:<br>
            <input class="form-control" type="text" name="username"><br>
            Password:<br>
            <input class="form-control" type="password" name="password"><br>
            Firstname:<br>
            <input class="form-control" type="text" name="firstname"><br>
            Lastname:<br>
            <input class="form-control" type="text" name="lastname"><br>
            Email:<br>
            <input class="form-control" type="email" name="email"><br>
            <input class="btn btn-primary" type="submit" value="Register">
          </form>
        </div>
      </div>
    </div>
  </body>
  </html>
  ```

  Now we create new html file call `login/templates/login/user.html`
  ```html
  <!Doctype html>
  <html>
  <header>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <title>Login</title>
  </header>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-md-12 col-xs-12 col-sm-12 col-lg-12">
          <h1>Welcome {{user.username}}</h1>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 col-xs-12 col-sm-8 col-lg-6">
          <form class="form-group" action="{% url 'login:logout' %}" method="post">
            {% csrf_token %}
            <input class="btn btn-danger" type="submit" value="Logout">
          </form>
        </div>
      </div>
    </div>
  </body>
  </html>
  ```

  So we have to modify `login\views.py` to work with that.
  ```python
  from django.shortcuts import render
  from django.http import HttpResponseRedirect,HttpResponse
  from django.urls import reverse
  from django.contrib.auth.models import User
  import django.contrib.auth  as auth
  from django.contrib.auth.decorators import login_required

  # Create your views here.

  def index(request) :
      return render(request,'login/index.html')

  def register_view(request) :
      return render(request,'login/register.html')

  @login_required
  def success(request) :
      user = request.user
      return render(request,'login/user.html',{'user':user})

  def register(request) :
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      user = User.objects.create_user(username,email,password,first_name=firstname,last_name=lastname)
      user.save()
      return HttpResponseRedirect(reverse('login:index'))

  def login(request) :
      if request.POST['action'] == 'Register' :
          return HttpResponseRedirect(reverse('login:register_view'))
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None :
          auth.login(request,user)
          return HttpResponseRedirect(reverse('login:success'))
      else :
          return HttpResponseRedirect(reverse('login:index'))

  def logout(request) :
      auth.logout(request)
      return HttpResponseRedirect(reverse('login:index'))
  ```

  The edit our `login/urls.py`
  ```python
  from django.conf.urls import url

  from . import views

  app_name = 'login'

  urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^register/$',views.register_view, name='register_view'),
      url(r'^register/register/$',views.register,name='register'),
      url(r'^login/$',views.login,name='login'),
      url(r'^success/$',views.success,name='success'),
      url(r'^logout/$',views.logout,name='logout'),
  ]
  ```
