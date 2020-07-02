# Udacity Full Stack Nanodegree Capstone

## Casting agency

* Base url: The API is currently hosted on [heroku](heroku.com).
 ```bash
  https://alessacapstone.herokuapp.com/
  ```

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the Casting_Agency.psql file provided.in terminal run:
```bash
psql Casting_Agency < Casting_Agency.psql
```

## Running the server

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app          
flask run --reload
```





## Testing
To run the tests, run
Make sure to change the Database path in the test_app.py
```
dropdb capstone_test (if there is a database with the same name you must drop it and create)
createdb capstone_test (if there is no database with the same name you need to create it)
python test_app.py
```
