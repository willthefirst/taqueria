
#!/bin/bash
# setup.sh

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Initialize database
python manage.py makemigrations guacamole
python manage.py migrate

# Install database fixtures
python manage.py loaddata guacamole/fixtures/posts.json