# Readme

## TODO

[The big spreadsheet](https://docs.google.com/spreadsheets/d/1TuYWxL2T_N-pSu8TwCEgKb5vM3JAp8re7imdczCbWqE/edit?usp=sharing)

- Tests did this work?
  - I get to 404 when posts/<id> does not exist in DB
  - I get 404 when I go to some/route/that/does/not/exist
- Can create post (ie. client availability)
- Can update post
- Can delete post

## Development

### Setup

Clone this repository into a Python virtual environment.

To create a new virtual environment:

```bash
# Create a virtual environment
python -m venv my_virtual_env
cd my_virtual_env
# Then clone this repo
```

Then, run the setup:

```bash
cd burrito
bash setup.sh
```

### Useful commands

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
python manage.py test guacamole/tests
```

To dump fixtures:

```bash
python manage.py dumpdata guacamole.Post --indent 2  > guacamole/fixtures/posts.json
```

To load fixtures:

```bash
python manage.py loaddata guacamole/fixtures/posts
```
