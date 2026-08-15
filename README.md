# Django Todo List

A simple and user-based Todo List web application built with Django. Users can create an account, manage their own tasks, set priorities and deadlines, and track task completion.

## Features

* User registration
* User login and logout
* Session-based authentication
* User-specific authorization
* Create tasks
* Edit tasks
* Delete tasks
* Mark tasks as completed
* Filter tasks by:

  * All
  * Active
  * Completed
* Task priorities:

  * Low
  * Medium
  * High
* Optional task deadlines
* Deadline validation to prevent selecting past dates
* Delete confirmation modal
* Logout confirmation modal
* User-specific task access

## Authorization

Each task belongs to a specific user.

Users can only access and manage their own tasks. Task queries are filtered using the authenticated user, and protected views use Django's `@login_required` decorator.

For example:

```python
Task.objects.filter(user=request.user)
```

This prevents users from accessing, editing, completing, or deleting tasks that belong to other users.

## Authentication

The project uses Django's built-in authentication system with session-based authentication.

Users can:

* Register a new account
* Log in using their username and password
* Log out securely
* Access protected pages only after authentication

Passwords are created using Django's `create_user()` method, which hashes passwords before storing them in the database.

## Technologies

* Python
* Django
* SQLite
* HTML
* CSS
* python-dotenv

## Project Structure

```text
django-todo-list/
│
├── Todo_list/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   ├── accounts/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── tasks/
│   │   ├── add_task.html
│   │   ├── edit_task.html
│   │   └── show_tasks.html
│   │
│   └── layout.html
│
├── static/
│   └── css/
│       └── style.css
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/arshia-dev86/django-todo-list.git
```

Move into the project directory:

```bash
cd django-todo-list
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the environment file

Create a `.env` file in the project root.

You can use `.env.example` as a reference:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

Generate your own Django secret key and replace the example value.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Environment Variables

| Variable     | Description                                      |
| ------------ | ------------------------------------------------ |
| `SECRET_KEY` | Django secret key used for cryptographic signing |
| `DEBUG`      | Enables or disables Django debug mode            |

Example:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## Security Notes

The following files are not included in the repository:

* `.env`
* `.venv/`
* `db.sqlite3`
* `__pycache__/`

Sensitive configuration values such as `SECRET_KEY` are stored using environment variables and loaded with `python-dotenv`.

## Current Status

The project has reached its MVP stage.

Possible future improvements include:

* Password change functionality
* Username or profile management
* Task search
* Task categories or tags
* Improved form validation using Django Forms
* Custom error pages
* REST API
* JWT authentication for API-based authentication
* Deployment

## License

This project is licensed under the MIT License.
