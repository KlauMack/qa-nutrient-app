# Nutrient Application

A web application built with the Django framework. Tracks food nutrients and user set targets.

---

## Prerequisites
Before you begin, ensure you have the following installed:

- **Python** ≥ 3.10  
- **pip** (Python package manager)  
- **virtualenv** (recommended)  
- **Git** (optional)  
- **PostgreSQL** or **SQLite** (depending on your settings)

---

## Setup Instructions

### 1. Clone the Repository
```bash
[git clone https://github.com/yourusername/your-django-app.git](https://github.com/KlauMack/qa-nutrient-app.git)
cd nutrient-app
```

### 2. Create and Activate a Virtual Environment

Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a .env file in the project root directory and add the following variables:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

(Adjust for PostgreSQL if needed, e.g. postgres://user:password@localhost:5432/dbname)

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Then open your browser and go to:
```bash
http://127.0.0.1:8000/
```
