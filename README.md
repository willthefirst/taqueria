# Readme

## TODO

https://docs.google.com/spreadsheets/d/1TuYWxL2T_N-pSu8TwCEgKb5vM3JAp8re7imdczCbWqE/edit?usp=sharing

- Can read all posts
- Can read single post
- Can create post (ie. client availability)
- Can update post
- Can delete post

## Development

Clone this repository into a Python virtual environment.

To create a new virtual environment:

```bash
# Create a virtual environment
python -m venv my_virtual_env
cd my_virtual_env
# Then clone this repo
```

To run Django:

```bash
cd burrito
python manage.py runserver
```

Then navigate to http://127.0.0.1:8000/ in a browser.

To create and run a migration:

```bash
python manage.py makemigrations mymigration
python manage.py migrate
```

To open a shell:

```bash
python manage.py shell
```

To run tests:

```bash
python manage.py test
```
