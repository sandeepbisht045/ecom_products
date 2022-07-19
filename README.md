GUIDE TO RUN THIS PROJECT
# extract zip file of the project in a folder
# create python3.8 virtual environment and then activate it
# move inside the django project
# run the command: pip3 install -r requirements.txt 
# run the command: python3 manage.py makemigrations
# run the command: python3 manage.py migrate
# run the command: python3 manage.py createsuperuser and follow the instructions
# At last , run the command : python3 manage.py runserver
# Now you are good to go run this project on your localhost
# Follow the API documentation file provided for different endpoints

TO SETUP MYSQL DATABASE FOLLOW THE INSTRUCTIONS PROVIDED BELOW:
# install the mysql server on your system
# install mysqlclient python module provided in requirements.txt file
# go to settings.py file of your django project and make below changes under DATABASE

            DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql', 
        'NAME'    : 'database_name',                
        'USER'    : 'username',                    
        'PASSWORD': 'database_password',             
        'HOST'    : 'localhost',               
        'PORT'    : '3306',
    }
}

 
