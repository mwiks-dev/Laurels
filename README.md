# LAURELS
### 13th Dec. 2021
## Author 
[Maryann Mwikali](https://github.com/Maryan23)
# Description 
Laurels is a platform that allows project developers to post their projects for rating based on design, usability and content. They are also able to see other  profiles and projects.
##  Live Link
https://laurels.herokuapp.com/

## Screenshots
<img src="static/images/Screenshot from 2021-12-14 14-07-22.png">
<img src="static/images/Screenshot from 2021-12-14 14-07-30.png">
<img src="static/images/Screenshot from 2021-12-14 14-08-05.png">

## User Story 
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects 
5. View projects overall score
6. View my profile page


## Setup and Installation 
##### Clone the repository: 
 ```bash
git@github.com:Maryan23/Laurels.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd Laurels
 - pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual
- source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations photos
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
* [Python3.8](https://www.python.org/)
* [Django==3.2.9](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)
## Known Bugs 
* There are no known bugs
## Support and Contact Information
Incase of any contributions fork the repo and make any substantial changes.
Incase of any ideas,suggestions or complaints feel free to connect with me on mwikali119@gmail.com 

## License
MIT
Copyright (c) 2021 **Laurels**