# Requirement
## back-end 
- [Python 3.x.y](https://www.python.org/downloads/)
- [django](https://www.djangoproject.com/download/)
```
pip install Django==2.1.2

```
- modules
```pip
pip install django-cors-headers
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

```


## front-end 
- [Angular 4+](https://angular.io/guide/quickstart) ( in case you want to run the source code for the front-end)

# Steps
- navigate to **back-end** directory and run the following commands:
```
python manage.py runserver 

```
- Change into the outer front-end_deployed directory, if you haven’t already, and run the following commands:
```
php -S localhost:1000 
```

or open the file index.html  and change [the base tag](https://angular.io/guide/deployment#the-base-tag)

# Informations

- **back-end :**
    > containe an interface  for the admin ( login : **admin**, password: **admin**)  to manage the app, and *API RESTful*  for creating web services. [link](http://localhost:8000/admin/)
    > I used that password just to make the login easy for you.

+ links :
	*[admin](http://localhost:8000/admin/)

	*[items list](http://localhost:8000/shops/items/)

	*[item Instance](http://localhost:8000/shops/items/1/)
	