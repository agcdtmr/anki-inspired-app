# anki-inspired-app

Created with Django, Python and SQLite3

This is inspired by Anki app, a free and open-source flashcard program using spaced repetition, a technique from cognitive science for memorization. A tool I keep using to retain what I am learning.

## To Do / To Fix:
- To connect the boxes cards in loop

## In this step-by-step project, I am learning how to:

- Set up a Django project
- Work with a SQLite database and the Django shell
- Create models and class-based views
- Structure and nest templates
- Create custom template tags
- A database connection that replicates the Leitner system


## How to run

1. Go to our GitHub [repo](https://github.com/agcdtmr/flashcard-django-app)
2. Fork or clone our project to your local directory.
3. Install the python libraries below if necessary:
- python 3.9
- pip
4. Open the repo using pycharm or any IDE.
5. Or open your terminal `cd flashcard-django-app
6. `python manage.py runserver`
7. Open / click the given port

Home page: http://127.0.0.1:8000

## Steps made building this project

1. Create a Virtual Environment
``python3 -m venv venv``
``source venv/bin/activate``
2. Add Dependencies
``python -m pip install django==4.0.4``
3. Initiate Django Project
``django-admin startproject flashcards .``
``python manage.py runserver``
4. Set Up Flashcards App
5. Create Django Flashcards App
``python manage.py startapp cards``
6. Connect the cards app to the flashcards project
- add the line below to INSTALLED_APPS in flashcards/settings.py
``"cards.apps.CardsConfig",``
- Create a path in urls.py in flashcards/ folder and include in the cards URL
7. Add a template directory - base.html
8. Sprinkle in Some Style
``<link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">``
9. Add Card Model. Define how the tables of SQLite database should look.
10. Create migrations and migrate the changes to apply the database
``python manage.py makemigrations``
``python manage.py migrate``
11. Use the Django shell to put some cards into the database.
``python manage.py shell``
12. Create a view for the Card
13. Create a New Card view
14. Create an Update an Existing Card view
15. Connect The Pages - button for Create New Card and The Boxes
16. Backend logic of the cards
17. Create .env file for Django secret key
``pip install python-dotenv``


## Here are some ideas for additional features:

- Archive: Add the option to archive cards that you don’t want to check anymore.
- Success Messages: Show success messages when you create a new card or when a card moves to a new box.
- Spaced Repetition: Enhance the Card model to keep track of the last time when a card was checked, or create reminders to the boxes to schedule the next learning session.
- Flashcard Sets: Expand the app to deal with different sets of flashcards. For instance, you could have a set for the German class, another for Spanish class, and so on.
