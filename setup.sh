
#!/bin/bash
# setup.sh

# Create virual environment in current workspace
python -m venv .venv

# Use the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Initialize database
python manage.py makemigrations guacamole
python manage.py migrate

# Install database fixtures
python manage.py loaddata guacamole/fixtures/posts.json