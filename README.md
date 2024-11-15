## Flask Joke API Application 
This Flask application fetches jokes from an external API (JokeAPI), processes the jokes, and stores them in a SQLite database. It includes two main endpoints: one to fetch and store jokes in the database and another to validate the number of jokes stored in the database.

## Note: 
The JokeAPI supports a maximum of 10 jokes per call.

## Features
Processes the following fields from the fetched jokes:
category
type
joke (for "single" type jokes)
setup and delivery (for "twopart" type jokes)
nsfw, political, sexist flags
safe and lang

## Requirements
Python 3.7+
Flask
SQLAlchemy
Requests library

Create a virtual environment:
python3 -m venv venv 

Activate the Virtual environment:
source venv/bin/activate 

Install the required dependencies:

pip install -r requirements.txt

Running the Application
Start the Flask application:
python jokes_app.py

## Endpoints:
GET /fetch_jokes: Fetches jokes from the JokeAPI and stores them in the SQLite database.
GET /validate_jokes: Validates the number of jokes stored in the database.

## Usage

## Fetch and Store Jokes:
Send a GET request to http://localhost:5000/fetch_jokes to fetch up to 10 jokes from the JokeAPI and store them in the jokes.db database.
Note: JokeAPI currently supports fetching a maximum of 10 jokes at a time. Attempting to fetch more jokes in a single request will not work.

## Validate Stored Jokes:
Send a GET request to http://localhost:5000/validate_jokes to check the number of jokes currently stored in the database.

## Database
The database used is SQLite, and the data is stored in a file named jokes.db. The jokes table contains the following columns:

id (Primary Key)
category
type
joke
setup
delivery
nsfw
political
sexist
safe
lang

## Example Responses
Fetch Jokes (GET /fetch_jokes):
{
    "message": "Jokes fetched and stored successfully!"
}

Validate Jokes (GET /validate_jokes):
{
    "message": "Number of jokes in the database: 10"
}