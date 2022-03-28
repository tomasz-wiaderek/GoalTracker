# GoalTracker
GoalTracker is a web app that allows you to track your progress in fighting your bad habits.

Add habit that you want to quit with and the app will track your progress and duration of abstinence. 
Milestones will be set automatically to keep you motivated.

## Set Up locally
Clone repository into desired location.
```
https://github.com/tomasz-wiaderek/GoalTracker.git
```
Enter location of cloned repository.
```bash
pip install virtualenv
virtualenv venv 
venv source .bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Usage
Enter below and register using email and password.
``` 
http://127.0.0.1:8000/register/
```
Enter below to log in using email nad password
``` 
http://127.0.0.1:8000/login/
```
Enter below to login using email nad password
``` 
http://127.0.0.1:8000/login/
```
###Functionalities
When logged out you can reset your password using your email.

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
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.