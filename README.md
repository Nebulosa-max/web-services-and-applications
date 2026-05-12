# Web Services and Applications

**Student:** Sophia Godoy  
**Repository:** `web-services-and-applications`  
**Module:** Web Services and Applications

This repository contains my coursework, practical lab work, assignment work, and project development for the Web Services and Applications module.

The work is organised to show my progress through the main areas of the module: data representation, HTTP requests, REST APIs, authentication, database interaction, Flask, AJAX, deployment preparation, and the final project / assessment work.

---

## Repository Structure

The repository is organised into the following main sections:

- `labs/` - weekly practical lab work and exercises
- `assignments/` - assignment tasks completed during the semester
- project-related work - files connected to the larger assessed project / final assessment work
- supporting files - datasets, configuration examples, and documentation

---

## Assessment Context

The work in this repository is organised around three main areas:

### 1. Labs

The lab work demonstrates practical engagement with the weekly material. These labs were used to practise the technical concepts introduced in lectures and to build the skills required for the larger project.

### 2. Assignments

The assignments were technically not the main marked assessment, but they still support evidence of engagement, progress, and applied understanding. They demonstrate that I completed the requested weekly tasks and used the module material in practice.

### 3. Big Project / Assessment

The larger project is the main assessed component of the module. The weekly labs and assignments helped build the required foundation for this work, including API design, database interaction, client-side interaction, and deployment considerations.

---

## Topics Covered During the Semester

The module covered the following areas:

### Introduction and Environment Setup

The course began with setting up the working environment, including Python, VS Code, GitHub, and the basic repository structure used throughout the semester.

Key areas:
- Python development environment
- VS Code workflow
- Git and GitHub
- Repository organisation
- Use of folders for labs and assignments

### Data Representation

The early part of the module reviewed different ways of representing and transferring data.

Topics included:
- CSV
- XML
- JSON
- Reading and processing structured data
- Understanding how external systems provide data

Related files include:
- `lab02_train.csv`
- `lab02_train_full.csv`
- `trainsxml.xml`
- `labs/lab02_representing_data.py`
- `labs/lab02_trains.py`

### HTTP, URLs and REST

The module then moved into HTTP communication and RESTful APIs.

Topics included:
- HTTP requests and responses
- URLs
- HTTP methods
- Status codes
- RESTful API concepts
- Using curl and Postman for testing
- Using Python to make requests

Related files include:
- `labs/lab03_1_requests.py`

### APIs in the Wild

This section focused on retrieving data from external APIs and public data sources.

Topics included:
- Consuming JSON from APIs
- Reading data from CSO.ie
- Retrieving government datasets
- Understanding API responses
- Saving API data locally

Related assignment:
- `assignments/assignment03-cso.py`
- `assignments/cso.json`

Assignment 03 retrieves the CSO exchequer account historical series dataset and stores the result in a JSON file called `cso.json`.

### Authentication and GitHub API

The module introduced API authentication and the use of API keys / tokens.

Topics included:
- API keys
- OAuth concepts
- GitHub API
- Using PyGithub
- Reading files from a GitHub repository
- Updating files through the GitHub API
- Avoiding hard-coded secrets in source code

Related files include:
- `labs/lab04_github.py`
- `labs/lab04_03_githubmodule.py`
- `assignments/assignment04-github.py`

Assignment 04 uses the GitHub API to read a file from a repository, replace the text `Andrew` with my name, and commit the change back to GitHub.

For security, the GitHub token is not stored directly in the file. The program asks for the token at runtime.

### Flask and Creating an API

The module then moved into creating our own API using Flask.

Topics included:
- Flask applications
- Routes
- Mapping URLs to functions
- Returning data from an API
- Creating a basic REST server
- Separating application logic from the data layer

Related file:
- `labs/lab05.01_rest_server.py`

### Databases and CRUD Operations

The module covered linking applications to databases and performing basic database operations.

Topics included:
- SQL
- MySQL
- Creating a database
- Creating tables
- Insert, view, update and delete operations
- DAO / data access layer concepts
- Connecting Python code to a database

Related files include:
- `labs/lab06_1.sql`
- `labs/lab06_2_create_db.py`
- `labs/lab06_2_create_table.py`
- `labs/lab06_2_insert.py`
- `labs/lab06_2_view.py`
- `labs/lab06_2_update.py`
- `labs/lab06_2_delete.py`

### HTML, JavaScript and AJAX

The later part of the module focused on client-side interaction and connecting a web page to an API.

Topics included:
- HTML
- CSS
- JavaScript
- jQuery
- AJAX
- Client-side requests to a REST API
- Displaying API data in the browser
- Create, update and delete operations from a web interface

Related files include:
- `labs/lab09_1_carviewer.html`
- `labs/lab09_4_ajax.html`

Lab 09.4 uses AJAX calls to perform Create, Update and Delete operations. Due to CORS restrictions with the external API, local fallback behaviour was included so the page can still demonstrate the required functionality.

To test the AJAX lab locally:

    python3 -m http.server 8000

Then open:

    http://localhost:8000/labs/lab09_4_ajax.html

Chrome is recommended for testing because Safari may block some requests more strictly.

### Pulling the Project Together

The project section linked the main parts of the module together:

- DAO / data layer
- Flask server
- REST API endpoints
- AJAX calls to endpoints
- HTML and JavaScript user interface
- Deployment considerations

This section helped connect the weekly labs to the larger assessed project.

### Hosting and Deployment

The module also introduced deployment concepts, including PythonAnywhere.

Topics included:
- Creating a PythonAnywhere account
- Creating a virtual environment
- Deploying a Flask server
- Using a GitHub repository for deployment
- Setting up a database on PythonAnywhere
- Debugging deployment issues
- Using relative URLs for AJAX calls

### SQLite and PythonAnywhere

Later material also covered using SQLite as an alternative where MySQL was not available in the free PythonAnywhere tier.

Topics included:
- SQLite database setup
- Updating the DAO for SQLite
- Adjusting database paths
- Deployment limitations and practical workarounds

---

## Completed Assignments

### Assignment 03 - CSO Dataset

Files:
- `assignments/assignment03-cso.py`
- `assignments/cso.json`

Description:
This assignment retrieves the CSO exchequer account historical series dataset and stores it in a JSON file.

Skills demonstrated:
- Finding a dataset from CSO.ie
- Reading JSON data from an API
- Saving retrieved data locally
- Using Python for API interaction

### Assignment 04 - GitHub API

File:
- `assignments/assignment04-github.py`

Description:
This assignment uses the GitHub API to read a file from a repository, replace the text `Andrew` with my name, and commit the updated file back to GitHub.

Skills demonstrated:
- API authentication
- GitHub API usage
- PyGithub
- Reading repository contents
- Updating files programmatically
- Avoiding hard-coded secrets

---

## Completed Labs

### Lab 02 - Data Representation

Files:
- `labs/lab02_representing_data.py`
- `labs/lab02_trains.py`
- `lab02_train.csv`
- `lab02_train_full.csv`

Focus:
- CSV data
- Basic data representation
- Reading structured data with Python

### Lab 03 - Requests

File:
- `labs/lab03_1_requests.py`

Focus:
- HTTP requests
- Using Python to retrieve external data
- Understanding responses from web services

### Lab 04 - GitHub API

Files:
- `labs/lab04_github.py`
- `labs/lab04_03_githubmodule.py`

Focus:
- API keys
- GitHub authentication
- GitHub API interaction
- Using PyGithub

### Lab 05 - REST Server

File:
- `labs/lab05.01_rest_server.py`

Focus:
- Flask
- REST server basics
- Creating server routes

### Lab 06 - SQL and CRUD

Files:
- `labs/lab06_1.sql`
- `labs/lab06_2_create_db.py`
- `labs/lab06_2_create_table.py`
- `labs/lab06_2_insert.py`
- `labs/lab06_2_view.py`
- `labs/lab06_2_update.py`
- `labs/lab06_2_delete.py`

Focus:
- SQL database setup
- Creating tables
- Insert, view, update and delete operations
- Connecting Python to a database

### Lab 09.1 - Car Viewer

File:
- `labs/lab09_1_carviewer.html`

Focus:
- Browser-based data display
- HTML and JavaScript interaction

### Lab 09.4 - AJAX Calls to REST

File:
- `labs/lab09_4_ajax.html`

Focus:
- AJAX
- REST API interaction from the browser
- Create, update and delete functionality
- CORS issues and local fallback behaviour

---

## Use of Artificial Intelligence

Artificial Intelligence tools were used as a learning and support aid during this module.

AI support was used for:
- Explaining programming concepts in simpler terms
- Helping debug Python, Git, GitHub, JavaScript, and AJAX errors
- Improving understanding of error messages
- Structuring README documentation
- Reviewing code organisation
- Supporting English wording and academic presentation

AI was not used as a replacement for the module learning outcomes. I used it as a support tool while still working through the code, testing files, running commands, checking errors, and adapting the work to my own repository and coursework requirements.

Where AI assistance was used, I reviewed and tested the work myself before including it in the repository.

---

## Security Notes

No API keys or personal access tokens should be committed to this repository.

For GitHub authentication tasks, the token is requested at runtime rather than being stored directly in the source code.

The following files should not contain secrets:
- `README.md`
- `assignments/assignment04-github.py`
- lab files
- public repository files

---

## References

The following resources supported the work completed in this repository:

- ATU Web Services and Applications module materials
- Lecturer-provided courseware and lab sheets
- GitHub documentation
- PyGithub documentation
- Python documentation
- Flask documentation
- W3Schools HTML, CSS and JavaScript references
- CSO.ie data resources
- PythonAnywhere documentation
- MDN Web Docs for HTTP, JavaScript and web APIs

---

## Reflection

This module helped me understand how web applications connect different layers together: data sources, APIs, servers, databases, and client-side interfaces.

The most important learning outcomes for me were:
- understanding how data is retrieved from external services
- using Python to work with APIs
- understanding authentication and API keys
- creating REST-style server functionality
- connecting Python applications to databases
- using AJAX to connect a browser interface to a web service
- organising coursework and project files in GitHub

The labs and assignments gave me practical experience with the same concepts needed for the larger project / assessment work.

---

## Author

Sophia Godoy
