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


## Installation & Setup

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .env file

```
OPENAI_API_KEY=your_api_key
```

### 4. Run the application

```bash
python -m uvicorn app:app --reload
```

### 5. Open Swagger UI

```
http://127.0.0.1:8000/docs
```



## API Endpoints

| Method | Endpoint | Description |
|----------|------------------|-------------------------------------|
| POST | /notes | Create a new note |
| GET | /notes | Retrieve all saved notes |
| POST | /delete/{note_id} | Delete a note |
| POST | /summarize | Generate AI summary |
| POST | /upload | Upload TXT or PDF file and generate summary |
