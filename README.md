# Social Network Database

## Introduction
- This is a challenge in Makers Module 3 - Databases
- I set up this project using a starter project from Makers, as per the challenge instructions below.
- This project includes a database, containing a `posts` and `users` table.
- The main program `app.py` prints a list of all the recipes in the database to the terminal.
- `recipes_schema_recipe.md` documents my design of the `recipes` table

## Objectives
- [x] Learn to test-drive "Repository" class methods to INSERT, DELETE and UPDATE.
- [x] Design and create tables for the following user stories:
  - [x] As a social network user,   
        So I can have my information registered,  
        I'd like to have a user account with my email address.
  - [x] As a social network user,  
        So I can have my information registered,  
        I'd like to have a user account with my username.
  - [x] As a social network user,  
        So I can write on my timeline,  
        I'd like to create posts associated with my user account.
  - [x] As a social network user,
        So I can write on my timeline,  
        I'd like each of my posts to have a title and a content.
  - [x] As a social network user,  
        So I can know who reads my posts,  
        I'd like each of my posts to have a number of views.
- [x] Create a seeds/social_network.sql.
- [x] Test-drive the application to meet the user stories above.

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...

# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/social-network-database.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell
# NB: you may need to change interpreter path, to import pytest and psycopg
# This will give you the path to use
; pipenv --venv

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py

# To exit the pipenv shell
; exit # or Ctrl-D
