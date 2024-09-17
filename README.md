
# Django Project

## Overview

This is a Django application designed to demonstrate Django functionality and basic project structure.

## Project Structure

- `DjangoProject/`: Contains project settings and configurations.
- `djangoApp/`: Placeholder for Django app code.
- `media/`: User-uploaded media files.
- `static/`: Static files (CSS, JavaScript).
- `templates/`: HTML templates.
- `theme/`: Additional styling themes.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django management script.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/omkarkhoche3448/Django.git
   cd Django
   ```

2. **Create and Activate a Virtual Environment:**

   - On macOS/Linux:

     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Optional):**

   If you need an admin user, create one by running:

   ```bash
   python manage.py createsuperuser
   ```

6. **Collect Static Files:**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000/` to see the running application.

## Notion Notes

For additional details, visit the Notion page: [Django Project Notes](https://www.notion.so/Django-f006a1f86a944887ad4bd758b2c10fe8)
```

