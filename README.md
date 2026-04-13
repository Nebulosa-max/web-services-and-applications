# WSAA-Courseware
Courseware for the Web services and Applications module, part of the HDip in Data Analytics
# Web Services and Applications (WSAA)

This repository contains my work for the **Web Services and Applications** module (ATU), including **assignments** and **labs**.

## Repository structure

- `assignments/` — Weekly assignments and submissions
- `labs/` — Lab work and practice tasks
- `WSAA-Courseware/` — Courseware cloned from the lecturer’s repository (reference material)

> Note: `WSAA-Courseware/` is included for learning/reference and is not where my submissions are kept.

## Setup

### Courseware (reference)
The courseware repository was cloned from:

- `https://github.com/andrewbeattycourseware/WSAA-Courseware`

### Tools
- VS Code
- Git / GitHub
- Python (via Anaconda)

## Progress log

### 2026-02-09
- Created the module repository: `web-services-and-applications`
- Created folder structure: `assignments/` and `labs/`
- Cloned courseware repository: `WSAA-Courseware`
- Completed the “Quick Assignment HTTP and URLs” quiz (submission completed)

## Notes
This README will be updated throughout the semester with new work, links, and progress updates.

## Assignment: Deal Cards (Deck of Cards API)

This assignment demonstrates how to consume a REST API using Python.

Features implemented:

- Create and shuffle a deck
- Draw cards
- Add cards to piles
- List pile contents
- Shuffle piles
- Draw from piles (top/random)
- Return cards to deck
- Reshuffle remaining cards
- Create brand new deck (with jokers)
- Create partial deck
- Access back-of-card image

File: `assignments/deal_cards.py`

# Lab 06.01 Databases

This lab demonstrates basic MySQL operations.

## Tasks completed
- Created database `wsaa`
- Created table `student`
- Inserted, selected, updated and deleted data in `student`
- Created table `book`
- Inserted sample data into `book`

## Files
- `lab06_01.sql`

# Lab 06.2 – Python and Databases

## Overview
This lab demonstrates how to connect Python to a MySQL database and perform basic CRUD operations.

CRUD stands for:
- **Create**
- **Read**
- **Update**
- **Delete**

The lab also includes a simple `StudentDAO` class to organise the database operations in a reusable way.

## Files included
- `lab06_2_create_db.py` – creates the `wsaa` database
- `lab06_2_create_table.py` – creates the `student` table
- `lab06_2_insert.py` – inserts a record into the table
- `lab06_2_view.py` – reads and displays a record
- `lab06_2_update.py` – updates a record
- `lab06_2_delete.py` – deletes a record
- `studentDAO.py` – contains the `StudentDAO` class
- `lab06_2_testdao.py` – tests the DAO methods

## Database details
This lab uses:
- **MySQL**
- host: `localhost`
- user: `root`
- password: `root`
- database: `wsaa`

## Table structure
The `student` table contains:
- `id` – integer, primary key, auto increment
- `name` – varchar
- `age` – integer

## How to run
Run the files in this order:

```bash
python lab06_2_create_db.py
python lab06_2_create_table.py
python lab06_2_insert.py
python lab06_2_view.py
python lab06_2_update.py
python lab06_2_view.py
python lab06_2_delete.py
python lab06_2_view.py
python lab06_2_testdao.py