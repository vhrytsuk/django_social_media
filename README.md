# Social Media Application

This is a simple social media application built using Django. The application allows users to create profiles, post updates (called "Meeps"), and interact with other users by following/unfollowing them and liking their posts.

## Features

- User authentication (login, logout, register)
- Profile management
- Posting updates (Meeps)
- Viewing and liking posts
- Following and unfollowing users
- Searching for users and posts

## Project Structure

- `mysite/`: Main project directory
  - `manage.py`: Django's command-line utility
  - `mysite/`: Project settings and configuration
    - `settings.py`: Project settings
    - `urls.py`: URL routing
    - `wsgi.py`: WSGI configuration
    - `asgi.py`: ASGI configuration
- `musker/`: Main application directory
  - `models.py`: Database models
  - `views.py`: Application views
  - `urls.py`: Application URL routing
  - `forms.py`: Forms for user input
  - `templates/`: HTML templates
  - `static/`: Static files (CSS, JavaScript, images)
- `media/`: Uploaded media files
- `requirements.txt`: Project dependencies

## Getting Started

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd mysite
   ```
   
2. **Create and activate a virtual environment**:
   ```sh
   python3 -m venv venv
    source venv/bin/activate
   ```

3. **Install dependencies**:
    ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations**:
    ```sh
   python manage.py migrate
   ```
5. **Run the development server**:
    ```sh
   python manage.py runserver
   ```

Navigate to http://127.0.0.1:8000/
   
