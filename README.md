# SE-Sprint01-Team05

# Sprint 1

-   Shronim Tiwari
-   Hannah McDermott

## About the Project

'Corona Archive' is a web application created for the course Software Engineering at Jacobs University of Bremen. This application is meant to help policy-makers in Germany with decisions regarding which corona restrictions to implement and which to disregard as too strict.

## Built With

-   HTML
-   CSS
-   Python3
-   SQLite

## Getting Started

Follow these steps to clone this repository and run the project in your local machine.

-   Flask

```
pip3 install Flask
```

-   Virtual Env

```
sudo pip3 install virtualenv
```

## Installation Guide

```zsh
# Cloning the repo
$ git clone https://github.com/Magrawal17/SE-Sprint01-Team05.git
$ cd SE-Sprint01-Team05

#Create Virtual Environment
$ virtualenv env

#Activate Virtual Environment
$ source env/bin/activate

#Installing Required Dependencies
$ pip3 install -r requirements.txt

#Setup SQLite Database
$ python db.py

#Run Flask server
$ python test01.py
```

## Access Webapp

Open following link in your browser to access webapp

```
http://127.0.0.1:5000
```

## View Documentation

The documentation can be viewed from following url after starting the server.

```
http://127.0.0.1:5000/docs
```

## Run test

Tests should be ran inside the environment with following command:

```zsh
$ python -m pytest
```

There are some UNIQUE elements in the table. So, if you rerun, some test might fail. If you remove coronatest.sqlite, and run 'python db.py', all test cases should pass.

## More information for next sprint (from Sprint 1)

-   inside /login.html, login as hospital is disabled as it couldn't be implemented
-   agents can be registered through /reg_agent.html. However, this should not be accessible to public but just for user. This is mainly implemented to test login.
-   through check-in (/scan_qrcode.html) scanning of qr-code should be performed. Currently, it is not correctly working
-   after agent or hospital logs in, they should be redirected to dashboard_agent.html or dashboard_hospital.html respectively. These are not implemented in this sprint
-   /reg_locale.html is to register the location. Needs to be implemented

# Sprint 2

-   Justin Morris
-   Manish Thapa

## Sprint Progress

✅ Organized sprint1's code and folders (check below at cleaned structure)<br>

-   Deleted unused files
-   Renamed files to descriptive names
-   Moved like files together
    <br>

✅ Added file structure<br>
✅ Added a git ignore <br>
✅ Added python formatter<br>
✅ Fixed create tables script with proper fields and types<br>
✅ Implement working tests (GET and POST)<br>

-   Works with sessions

✅ Cleanup html pages

-   Many pages - Remove unruly font family
-   index page - remove not needed tags<br>
-   login page - cleanup to adhere to database and flask request form names<br>
-   reg_agent page - cleanup, fix typos, and correctly format flask request names
-   reg_local page - add comments, and change names to fit with flask server request
-   reg_visitor page - Alter names of inputs
-   scan_qrcode page - format code
-   users page - Fix names to match with that of the values passed from the flask server
    <br>

✅ Implementation of sessions

-   Able to log out and session closed
-   Hospitals: Allow change of who is positive
    -   To be done in future sprint
-   Agents: Can search all visitors in database
    <br>

✅ Added working visitor and place registration page
<br>
✅ Login implemented with dashboard and appropriate navigation control 

-   Login implmented for Agent
-   Hospitals can now login with the credential provided by agent

✅ New features for Agent 

-   Search visitor by name
-   Search place by name
-   Register Hospitals 

✅ New features for Hospital 

-   Search patient(visitor) by name

✅ New features for Visitor 

-   Visitor can scan QR code of places they visit.
-   Scanning a QR code will lead visitor to time counter

✅ New features for Place 

-   QR code for places is generated
-   QR code can be downloaded

## New Project File Structure

```
\--SE-Sprint01-Team06
        \--static                   # JS, CSS files and any other assets (ex. images)
            \-- CSS
                \-- form_style.css
                \-- style.css
            \-- js
                \-- main.js
        \--templates                # HTML templates (jinja2)
            \-- agent_dash.html
            \-- agent_dashboard_baselayout.html
            \-- agent_login.html
            \-- all_visitors.html
            \-- baselayout.html
            \-- dashboard_agent.html
            \-- dashboard_hopsital.html
            \-- display_camera.html
            \-- hospital_login.html
            \-- hospital_registration.html
            \-- imprint.html
            \-- index.html
            \-- login.html
            \-- place_dashboard.html
            \-- place_registration.html
            \-- reg_locale.html
            \-- scan_qrcode.html
            \-- visitor_registration.html
            \-- visitor_timer.html
        \--SQL                   # SQLite database initialization files
            \-- createTables.py
            \-- db_insert.py
        \--tests                    # Python based tests
            \-- tests.py
        -- Customer_Requirements.pdf    # Project
        -- app.py                   # Main python (flask) app
        -- db.sqlite                # database
        -- README.md                # This file
        -- requirements.txt         # Flask dependency list (see below)
        -- .gitignore               # files to ignore when committing
```

## New Installation and How to Run (changed post organization)

Note, it is assumed as a pre-requisite, that you have [Python](https://www.python.org/downloads/) installed.

1. Install VirtualEnv

```
pip3 install virtualenv
```

2. Setup

-   Clone/Download entire repository
-   Navigate to repository base folder, open bash/command prompt

3. Create your virtual environment

```
python3 -m venv myEnv
```

4.  Source into virtual environment

```
source myEnv/bin/activate
```

5.  Install required project dependencies

```
pip3 install -r requirements.txt
```

6. Create the sql database and insert data

```
python3 sql/createTables.py && python3 sql/dummyValuesInsert.py
```

7.  Run development server

```
python3 app.py
```

8.  Open flask application in the web browser

```
http://localhost:3000/
```

## Testing

Note: The login features of the testing file require certain credentials to be present to login agents and hospitals. Such credentials are inserted into the database upon the run of the `dummyValuesInsert.py`.

0. Source into the environment

1. If no database file exists, from the root folder, run

```
python3 sql/createTables.py && python3 sql/dummyValuesInsert.py
```

2. If the database already exists, check if the values inserted in `dummyValuesInsert.py` are present. If not, from the root folder, run

```
python3 dummyValuesInsert.py
```

3. Ensure the flask server is running
4. Run the test file (Must be run from the root folder)

```
python3 tests/tests.py
```
