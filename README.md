# Refunite.org code challenge

Indeed it's an overkill to build a Flask application just to serve static files, but we're also adding user authentication and role management. As mentioned, the goal was to develop an appropriate solution for a site that's about to get much more complex over time so the first issue to address is the foundation: the file structure should be carefully organized and since Flask is intrinsically modular, our project should take that in mind.

I organized my work in these smaller steps:

1. basic configuration and file structure
2. setup and prepare deployment tools (heroku, in this case)
3. organize development, staging, testing and production environments with Git
4. database structure
5. user authentication
6. role management
7. automate insertion of dummy data for testing
8. ensure secure storage and transmission of passwords
9. users and role administration
10. hierarchical structured and responsive templates
11. bundles and static files

### Next steps to pursue at the end of the challenge
* keep separate branches for development, staging and production;
* follow the **development** > **staging** > **production** flow of integration, to always ensure compability and integrity among all modules of the project;
* any new features or bug fixes should be developed in a new branch forked from development, then proposed as a pull request and reviewed by the peers;
* write tests for new features;
* always (always) run the tests locally before pushing new code;
* have the project integrated with some automated testing platform like [Travis-CI](https://travis-ci.org/) or [Jenkins-CI](https://jenkins.io);
* only add new external modules (packages) if needed - even though they make our life easier, they also add up more maintenance to the project.

---

*Footnote:* I had to change the margin element on the logo class in `left-button.scss` from

```
.logo {
  text-align: center;
  margin: 100px;
  height: 50px;
}
```

to

```
.logo {
  text-align: center;
  margin: 100px 0;
  height: 50px;
}
```

to **ensure mobile responsiveness**. The logo image has `170px` width and most mobile screens have a width smaller than `100px + 170px + 100px`, so that would break the layout.

# Instalation Instructions

### Configuration

Virtual environment:
Create a [virtualenv](http://virtualenvwrapper.readthedocs.org/) to control the dependencies in a sandbox.

Install all the dependencies:
`pip install -r requirements.txt`

In case of failure when installing any of the python packages, you might want to check you Linux packages, probably there is something missing in order to compile one of these dependencies. For my instalation, I used these:

```
python-dev
python3-dev
python-pip
libpq-dev
postgresql
postgresql-contrib
```

### Environment variables

There are two ways you can do this: you can both add the variables manually in the terminal or add them to a `.env` file and run `source .env`. I included a `.env_example` file which can be tweaked for that purpose.

```
workon <VIRTUALENV>
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/<DATABASE_NAME>"
export PGPASSWORD="<DATABASE_PASSWORD>"
```

### Database

Make sure you create a [PostgreSQL database](http://www.postgresql.org/docs/8.4/static/tutorial-createdb.html) and export the environment variable with the correct database url. I used [Alembic](	https://pypi.python.org/pypi/Flask-Alembic), which is part of [Flask-Migrate](https://flask-migrate.readthedocs.org), to manage database migrations to update the database’s schema. This way we ensure that database changes go smoothly on our data - the `manager.py` has that role.

To init the database:
`python manage.py db init`

Migrate models:
`python manage.py db migrate`

After any changes to the models (you won't be needing this):
`python manage.py db upgrade`

### Takeoff

Running the application:
`python manage.py runserver`

All good, ready to open it in the [browser](http://localhost:5000).

### Test user accounts

```
admin@refunite.org : admin
test@refunite.org : test
```

### Deployment

I used Heroku to deploy it just as an example:

http://refunite.herokuapp.com

If it takes longer to load, fear not! It's sonely because the server was [asleep](https://www.heroku.com/pricing).
