<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2020/04/django-python-logo.png?w=500&ssl=1" alt="Django logo"></a>
</p>

<h3 align="center">Understanding Context Processors In Djnago</h3>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [What it is and How it works](#working)
- [Other UseCases](#usage)
- [End](#end)


## 🏁 Getting Started <a name = "getting_started"></a>
- Clone the repo
- cd into the project directory
- Create a virtual environment by running `python3 -m venv env` or `virtualenv env`
- Activate the virtual environment by running `source env/bin/activate` or `env/bin/activate`
- Install the requirements by running `pip install -r requirements.txt`
- Generate a secret key by running `python3 secret_key_generator.py` and copy the generated key
- For MacOS and Linux use `export SECRET_KEY=THESECRETKEYYOUJUSTCOPIED` for Windows 10 and lower `Set SECRET_KEY=THESECRETKEYYOUJUSTCOPIED` and for Windows 11 `$ENV:SECRET_KEY = 'THESECRETKEYYOUJUSTCOPIED'`
- Run the make migrations by running `python3 manage.py makemigrations` and then `python3 manage.py migrate`
- Run the server by running `python3 manage.py runserver`
- There be nothing in the database so you can create a superuser by running `python3 manage.py createsuperuser` and follow the instructions to create a superuser then login to the admin panel `http\\:localhost:8000\admin\` and add some categories and posts.

## 💭 What is it and  How it works <a name = "working"></a>
According to the django documentation, context_processors is a list of dotted Python paths to callables that are used to populate the context when a template is rendered with a request. These callables take a request object as their argument and return a dict of items to be merged into the context. in other words, it is a function that takes the request object as its only argument and returns a dictionary of items to be merged into the template context.

Now why is it important? It is important because it allows you to add data to the context of every template rendered in a request. This is useful for adding data that is used in every template, such as the current user, site-wide settings, or anything else you might want to add to every page.

So do you need to use it? No, you don't need to use it. But it is a very useful tool that can be used to add data to the context of every template rendered in a request.



Here's how it works:
- Create a file called context_processors.py in the root directory of your app which in my case is `blog`
- I added the following code to the file
```python
from .models import Category

def category(request):
    return {'categories': Category.objects.all()}
``` 
this code gets all the categories from the database and returns them as a dictionary with the key `categories`
- I then added the following code to the `settings.py` file
```python
TEMPLATES = [
    {
        ...
            'context_processors': [
                ...
                # line below is the one I added
                'blog.context_processors.category',
            ],
        },
    },
]
```
with this, django now knows that the function `category` in the `context_processors.py` file is a context processor and should be used to add data to the context of every template rendered in a request.

- Now I can use the categories in any template by using the following code
```html
{% for category in categories %}
    <li><a href="#">{{ category.name }}</a></li>
{% endfor %}
```
Instead of using the `Category.objects.all()` in every view, making the code look messy. this is a much cleaner way of doing it. that's why context processors can be very useful.


## 🎈 Other UseCases <a name = "usage"></a>
You can find the use of context processors in a wide range of django projects both big and small. Some of the use cases include:

- [My Django eCommerce Project](https://github.com/Digitalguyco/django-ebook/blob/master/cart/context_processors.py)
- [Django Documentation](https://docs.djangoproject.com/en/3.2/ref/templates/api/#writing-your-own-context-processors)
and many more. you can find more use cases by searching for `django context processors` on google or any other search engine.


## 🎉 End <a name = "end"></a>
I'm writing all this to  help myself and whoever finds if useful to udnerstand djnago core concepts. I hope you find it useful. If you have any questions, feel free to reach out to me on [Twitter](https://twitter.com/khitoTM) or [LinkedIn](https://www.linkedin.com/in/daniel-ikekwem-361658238/)