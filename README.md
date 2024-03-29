# GoalTracker
GoalTracker is a web app that allows you to track your progress in fighting your bad habits.

Please, visit https://goalstracker.pl/ to check its content.

Add habit that you want to quit with and the app will track your progress and duration of abstinence. 
Milestones will be set automatically to keep you motivated.

## Frameworks and services used
```
#django
#docker
#postgres
#nginx
#bootstrap 
#letsencrypt 
#mailtrap.io
```

## Set Up locally
Clone repository into desired location.
```
https://github.com/tomasz-wiaderek/GoalTracker.git
```
Enter location of cloned repository.
Run below command with Docker:
```
docker compose -f docker-compose.dev.yml up --build -d
```

## Usage
In your web browser enter:
```
http://localhost:8000/
```
Enter below and register using email and password.
``` 
http://localhost:8000/register/
```
Enter below to log in using email nad password
``` 
http://localhost:8000/login/
```

## Functionalities
When logged out you can reset your password using your email. Email sender served by mailtrap.io.<br>

Chose link <u>My profile</u> to view and/or update your Username and Email.

Chose link <u>My habits</u> to view list of all habits added by you and time of abstynence.

From this view you can also:  
Add new habit,  
Update existing habit,  
Chagen name and description of your habit,  
Reset you habit - change the time of the last occurrance,  
See achieved and current milestone,  
Delete habit.


## Contributing
Additional features and improvements are under development. Any suggestions are most welcome.
