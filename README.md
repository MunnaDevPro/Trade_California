# Trade California International

A full-stack, dynamic trade platform designed to connect American products and services with international markets.

## Technology Stack

- **Backend:** Django 5.x, PostgreSQL
- **Frontend:** Tailwind CSS (via `django-tailwind`), HTML, Vanilla JS
- **Admin:** Django Unfold for a modern, sophisticated dashboard
- **Forms:** Django Crispy Forms with Tailwind integration
- **Media:** Pillow & Django ImageKit for optimized images
- **Configuration:** `django-environ`

## Setup & Installation Instructions

Follow these instructions to set up the project locally.

### 1. Prerequisites
- Python 3.10+
- Node.js (v18+) for building Tailwind CSS
- [uv](https://github.com/astral-sh/uv) (Extremely fast Python package manager written in Rust)
- PostgreSQL (optional for local dev, SQLite is configured as a fallback)

### 2. Clone the Repository
```bash
git clone <repository_url>
cd Trade_California
```

### 3. Setup Environment and Dependencies
Use `uv` to create a virtual environment and install dependencies:

```bash
uv venv
# Activate the virtual environment
# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install requirements
uv pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file from the example template:

```bash
# On Windows
copy .env.example .env
# On macOS/Linux
cp .env.example .env
```
Ensure that `DEBUG=True` for local development. By default, it will use SQLite. If you wish to use PostgreSQL, update the `DATABASE_URL` in `.env`.

### 5. Database Setup & Migrations
Run the migrations. This will automatically seed the database with default settings, navigation links, and placeholder content.

```bash
python manage.py migrate
```

### 6. Create Superuser
Create an admin user to access the backend dashboard:

```bash
python manage.py createsuperuser
```

### 7. Install Tailwind Dependencies
Install the Node.js packages required by the Tailwind pipeline:

```bash
python manage.py tailwind install
```

### 8. Run the Development Server
You will need two terminal windows to run both the Django server and the Tailwind CSS watcher.

**Terminal 1 (Django Server):**
```bash
# Ensure your virtual environment is activated
python manage.py runserver
```

**Terminal 2 (Tailwind Watcher):**
```bash
# Ensure your virtual environment is activated
python manage.py tailwind start
```

### 9. Access the Application
- **Frontend:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Dashboard:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Production Deployment Notes
- Use `collectstatic` to gather static files.
- Set `DEBUG=False` in `.env`.
- Provide a secure `SECRET_KEY` and the production `DATABASE_URL`.
- Use a production WSGI server like Gunicorn behind Nginx.
- Configure media file storage (e.g., AWS S3) using `django-storages` as needed.
