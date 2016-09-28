#Django Login Tutorial

##Requirement
```
Python 3.5
MySQL
```
##Environment
There are two choice for you.

1. Install this following Requirement on your environment.

...```
...Django==1.10.1
...mysqlclient==1.3.7
...```

2. Use our Virtual Environment by do following step
...
```
$cd env/Scripts
env/Scripts$activate
(env) env/Scripts cd ../..
```
...
##Step by step
1. Start Django Project

...
```
$django-admin startproject djangologin
$cd djangologin
```
...
2. Initialize App
...
```
djangologin$python manage.py startapp login
```
...
3. Edit Django to use MySQL Database
...In `djangologin\settings.py` edit this part  
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
...Migrate database
...```
djangologin$python manage.py migrate
```

4. Connect your app with your project
...In `djangologin\settings.py` add this
...```
INSTALLED_APPS = [
    'login.apps.LoginConfig', #Connect your login app
```

5.
