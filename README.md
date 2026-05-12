# Web Services and Applications

Student: Sophia Godoy

This repository contains my coursework for the Web Services and Applications module.

## Repository structure

- assignments: assignment work
- labs: weekly lab work and practice exercises

## Assignments completed

### Assignment 03 - CSO dataset

Files:
- assignments/assignment03-cso.py
- assignments/cso.json

This assignment retrieves the CSO exchequer account historical series dataset and stores the result in a JSON file called cso.json.

### Assignment 04 - GitHub API

File:
- assignments/assignment04-github.py

This assignment uses the GitHub API to read a file from a repository, replace the text Andrew with my name, and commit the change back to GitHub.

For security, the GitHub token is not stored directly in the file. The program asks for the token when it runs.

## Labs completed

### Lab 02 - Data representation and CSV work

Files:
- labs/lab02_representing_data.py
- labs/lab02_trains.py
- lab02_train.csv
- lab02_train_full.csv

### Lab 03 - Requests

File:
- labs/lab03_1_requests.py

This lab covers making HTTP requests with Python.

### Lab 04 - GitHub API

Files:
- labs/lab04_github.py
- labs/lab04_03_githubmodule.py

These labs cover using the GitHub API from Python.

### Lab 05 - REST server

File:
- labs/lab05.01_rest_server.py

This lab covers basic REST server functionality.

### Lab 06 - SQL and CRUD

Files:
- labs/lab06_1.sql
- labs/lab06_2_create_db.py
- labs/lab06_2_create_table.py
- labs/lab06_2_insert.py
- labs/lab06_2_view.py
- labs/lab06_2_update.py
- labs/lab06_2_delete.py

These labs cover database creation and Create, Read, Update and Delete operations.

### Lab 09.1 - Car Viewer

File:
- labs/lab09_1_carviewer.html

This lab displays car data in a browser-based viewer.

### Lab 09.4 - AJAX Calls to REST

File:
- labs/lab09_4_ajax.html

This lab uses AJAX calls to perform Create, Update and Delete operations.

Due to CORS restrictions with the external API, the lab includes local fallback behaviour so that the page can still demonstrate the required functionality.

To test locally:

python3 -m http.server 8000

Then open in Chrome:

http://localhost:8000/labs/lab09_4_ajax.html

Chrome is recommended because Safari may block some requests more strictly.

## Notes

Some external API requests may be affected by browser CORS restrictions. Where needed, local fallback behaviour was used to demonstrate the required functionality.

## Author

Sophia Godoy
