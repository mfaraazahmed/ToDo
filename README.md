
# ToDo Application

This is a simple todo application built using Flask. It allows you to add, update, and delete tasks in a todo list.


## Installation

For MacOS

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask db upgrade
```

For Windows 
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask db upgrade
```

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/mfaraazahmed/ToDo
```

Go to the project directory

```bash
  cd ToDo
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```


## Features

- Add Tasks: You can easily add new tasks to your todo list by providing a title and description.

- Update Tasks: If you need to modify any task, you can update its title and description with ease.

- Delete Tasks: Completed or no longer relevant tasks can be removed from your todo list with a single click.

- View Tasks: The application provides a clean and organized view of all your tasks, displaying their titles, descriptions, and creation times.

- Responsive Design: The user interface is designed to be responsive, adapting to different screen sizes and devices, ensuring a seamless experience across desktop and mobile.

- Persistent Storage: All tasks are stored in a SQLite database, allowing you to access your tasks even after restarting the application.

- Validation and Error Handling: The application includes form validation to ensure that all required fields are filled correctly, providing meaningful error messages when necessary.
## Deployment

To deploy your Flask todo application using Railways and Gunicorn, you can follow these steps:

1. Install Railways and Gunicorn:
```bash
pip install railways
pip install gunicorn
```

2. Create a wsgi.py file in your project directory with the following content:
```bash
from app import app

if __name__ == '__main__':
    app.run()

```

3. Create a Procfile in your project directory (without any file extension) with the following content:
```bash
web: gunicorn wsgi:app
```

4. Open a terminal or command prompt and navigate to your project directory.

5. Log in to Railways by running:
```bash
railways login
```
and follow the authentication process.

6. Deploy your application to Railways by running:
```bash 
railways up
``` 
Railways will automatically detect your Python project and deploy it using the configuration specified in the **Procfile**.

7. Railways will provide you with a unique URL where your application is deployed. You can access your Flask todo application using that URL.


*Note: Make sure that your **app.py** file is in the root directory of your project and contains the Flask application instance named **app**.*
