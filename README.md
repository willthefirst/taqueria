# Readme

## TODO

[The big spreadsheet](https://docs.google.com/spreadsheets/d/1TuYWxL2T_N-pSu8TwCEgKb5vM3JAp8re7imdczCbWqE/edit?usp=sharing)

- Clean up
  - Test all auth/registration routes
  - Organize routes
- Posts needs pagination and filtering

## Development

### Setup

Run the setup:

```bash
cd taqueria
bash setup.sh
```

This will install and activate a Python virtual environment inside the project directory.

### Useful commands

To run Django:

```bash
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
