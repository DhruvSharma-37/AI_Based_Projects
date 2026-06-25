# AI Notes Summarizer Backend

## Overview

AI Notes Summarizer Backend is a FastAPI-based application that allows users to create, manage, and summarize notes using Large Language Models (LLMs). The application integrates database operations, CRUD functionality, and AI-powered text summarization through REST APIs.

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite / SQL Database
* Large Language Models (LLMs)
* REST APIs

## Features

* Create Notes
* View All Notes
* Delete Notes
* AI-Powered Note Summarization
* Database Storage and Retrieval
* REST API Architecture

## API Endpoints

### Create Note

POST `/notes`

### Get All Notes

GET `/notes`

### Delete Note

POST `/delete/{note_id}`

### Summarize Note

POST `/summarize`

## Project Structure

* `app.py` – Main FastAPI application and API routes
* `database.py` – Database connection setup
* `models.py` – Database models
* `schemas.py` – Request and response schemas
* `crud.py` – CRUD operations for notes
* `llm.py` – AI-powered text summarization logic

## Future Improvements

* User Authentication and Authorization
* Cloud Deployment
* Note Search Functionality
* Advanced AI Summarization Features
* Frontend Integration

## Author

Dhruv Sharma
