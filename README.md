# speakify_Task
Submission for speakify task by Sanskar Shrivastava

# Speakify


## Features

- User registration and login
- Update user status (online/offline)
- Real-time WebSocket Connection based on Matching Interests
- Uses ASGI server instead of WSGI

## Technologies Used

- Django: Python web framework
- Django Channels: WebSocket framework for Django
- Redis
- HTML, CSS, and JavaScript: Front-end development

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/speakify.git
   ```
   
2. Create a virtual environment and activate it
    ```
    python -m venv myenv
    source myenv/bin/activate
    ```
    
3.Install the dependencies:
   ```
    pip install -r requirements.txt
   ```
    
4. Start the Redis server by
    * Go into redis-windows-master and open redis-server.exe
    * and then opening redis-cli.exe and typing PING in that so it returns PONG and the setup is complete
    
5. Make Migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
 6. Run server:
    ```
    python manage.py runserver
    ```
    
    
## Configuration
The Django Channels settings are configured in the settings.py file. Make sure you have the correct configuration for the Channels layer and Redis backend.
Update the ASGI_APPLICATION setting in settings.py to point to your ASGI application.
