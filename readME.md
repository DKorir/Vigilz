#   
## Author  
  
>[Dominic Korir] 
  
# Description  
This is a django application that allows users to post their projects for others to rate and review
  
##  Live Link  
 Click [View Site](https://prodommy20.herokuapp.com/)  to visit the site

 
## User Story  
  
* Sign in to the application to start using.
* Upload my Project to the application.
* See my profile with all my pictures.
*search api  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```https://github.com/DKorir/Vigilz
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8.10](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [dommykiprono76@gmail.com]  
  
## License 

* Copyright (c) 2022 **Dominic Korir**