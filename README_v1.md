# RecipeBox

Kenzie Academy SEQ4 Intro to Django Assessment

Django is the most popular Python web framework for making user-facing applications, and it's easy to see why. With the famous tagline of "batteries included" and thousands of plugins on PyPI, it makes sense that you can find it in a lot of platforms.

    The entirety of Instagram is a single monolithic Django app; as of 2016, they leveraged over 50k instances of their software on over 12k machines
    The grand majority of the Washington Post
    Most of USA Today and accompanying sites
    All of Mozilla's support / documentation sites (all that Javascript documentation you were reading a few months ago? That was Django talking!)
    Disqus comments; the plug-and-play comment system is the most popular system of its type, and it's one giant Django app
    Most of Atlassian Bitbucket, a competitor to GitHub and Gitlab
    The entirety of Eventbrite
    The question-and-answer site Quora

Most of these won't advertise that they're looking for "django developers" because they want to make sure that people can work with their stack; instead, they'll focus on finding "python developers". It's up to us to learn how to leverage Django and its vast ecosystem to handle different types of applications.
Your Task

For our introduction, we want to get familiar with creating a new Django application. Create a new application that serves recipes from different authors, much like our demo application does for news. Intended layout:

    An index page that lists all titles of the loaded recipes (they don't have to be real recipes; just fill them with lorem ipsum and some numbers.)
    Each title is a link that takes you to a single page with the content of that recipe.
    Each detail view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.
    Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that Author has contributed to.
    Make editing all of the models accessible through the admin panel only.

So we have three types of pages: a simple list view, a recipe detail view, and an author detail view. The admin panel will handle the creation views, so we don't need to worry about that.

Important Info:

    Python 3.8, latest version of Django (3.0.5 as of this writing)
    Start a project with `django-admin startproject {project name} .` -- note the period at the end! (for example, `django-admin startproject recipebox .`)
    Start the server with `python manage.py runserver`
    After you create your models, run `python manage.py makemigrations {foldername}` (where foldername is the top level folder for your project) to create them, then `python manage.py migrate` to push them to the db. If you get stuck, delete the db and run the command again
    If you change your models after running the migrations, run makemigrations and migrate again. If the migrations require the creation of a new table, django will automatically handle it
    Create an admin user by running `python manage.py createsuperuser`
    Don't go crazy on the front end. The goal is to just handle the database interactions and basic view path
    Make sure that every detail page (author and recipe) has its own unique URL. If you reload the URL, the same page should appear -- no modals or manipulating the current information on the page. That's too complicated for what we're trying to achieve.
    REITERATING: There are no extra points for pretty HTML! Don't spend time making everything on the front end look gorgeous; we just want to make sure we're serving the right information.
    Please don't commit any extraneous files! It's best practice to use a .gitignore file to keep a clean repository. See the this link (Links to an external site.)Links to an external site. for what you should include in your .gitignore file.

Author model:

    Name (CharField)
    Bio (TextField)

Recipe Model:

    Title (CharField)
    Author (ForeignKey)
    Description (TextField)
    Time Required (Charfield) (for example, "One hour")
    Instructions (TextField)

Note: Follow PEP8 naming conventions with your models and field names. An easy way to check is by looking at examples of code in Django's docs --> https://docs.djangoproject.com/en/3.0/topics/db/models/#quick-example (Links to an external site.)Links to an external site.

If you have any questions or get stuck at any point, don't hesitate to ask. Welcome to a new side of web development!

Demo Video: https://s3.us-east-2.amazonaws.com/videos.kenzie.academy/Software+Engineering+-+Python/2020-01-29+--+Intro+to+Django.mp4 (Links to an external site.)Links to an external site.
Submission

Push up your code to a repo and submit the link to the repo.

https://github.com/<github_username>/recipebox

Rubric
Follow the HttpResponse Road
Follow the HttpResponse Road
Criteria Ratings Pts
This criterion is linked to a Learning Outcome Uses a models.py file to contain all database models
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning Outcome Uses a views.py file to contain all renderable views
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning Outcome Does not contain any logic in models.py
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning Outcome Uses Django template language to create the three primary html files
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning Outcome Clicking on a recipe title takes you to the recipe detail page, and clicking on the author name takes you to the author detail page
3.0 pts
Full Marks
0.0 pts
No Marks
3.0 pts
This criterion is linked to a Learning Outcome The main page only contains recipe titles
1.0 pts
Full Marks
0.0 pts
No Marks
1.0 pts
This criterion is linked to a Learning Outcome The author detail page contains a list of links to all recipes published by that author
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning Outcome All models are manipulated from the built-in django admin page
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
This criterion is linked to a Learning Outcome Repo contains pyproject.toml that includes all necessary dependencies to run application
2.0 pts
Full Marks
0.0 pts
No Marks
2.0 pts
Total Points: 20.0
