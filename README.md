# backend-python-LMP

A lightweight FastAPI backend for managing students (`alumnos`) with Firebase authentication and JWT-protected endpoints.

## Features

- FastAPI-based REST API
- Firebase service account initialization with Firestore
- JWT authentication middleware for protected routes
- Student CRUD endpoints under `/api/alumnos`
- Login endpoint under `/api/auth/login`
- Health check endpoint `/api/health`

## Requirements

- Python 3.10+ (recommended)
- `pip install -r requirements.txt`
- `.env` file with required environment variables

## Environment Variables

Create a `.env` file with the following values:

```env
PORT=3050
CORS_ORIGIN=http://localhost:3000
JWT_SECRET=secret

FIREBASE_PROJECT_ID=your-firebase-project-id
FIREBASE_CLIENT_EMAIL=your-firebase-client-email
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
```

> Note: The repository loads environment variables with `python-dotenv`. The Firebase private key is expected to include `\n` escapes for newlines.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Start the server locally with:

```bash
python run.py
```

Or with Uvicorn directly:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 3050
```

## API Endpoints

- `GET /api/health`
  - Returns the application health status.

- `POST /api/auth/login`
  - Request body: `{ "usuario": "<username>", "password": "<password>" }`
  - Returns an authentication response from the auth service.

- `GET /api/alumnos/`
  - Returns all students. Requires `Authorization: Bearer <token>`.

- `POST /api/alumnos/`
  - Creates a new student. Requires `Authorization: Bearer <token>`.

- `PATCH /api/alumnos/{id}`
  - Updates an existing student. Requires `Authorization: Bearer <token>`.

- `DELETE /api/alumnos/{id}`
  - Deletes a student. Requires `Authorization: Bearer <token>`.

## Project Structure

- `run.py` - application entry point
- `app/main.py` - FastAPI app initialization
- `app/core/` - environment and Firebase client setup
- `app/modules/auth/` - authentication routes, schema, and service
- `app/modules/alumnos/` - student repository, routes, schema, and service
- `app/shared/middleware/` - auth middleware and error handling
- `app/shared/utils/api_error.py` - custom API error response helper

## Notes

- Make sure Firebase credentials are valid and the environment variables are set correctly.
- `CORS_ORIGIN` should be a comma-separated list of allowed origins.
- The auth middleware verifies JWT tokens using the `Authorization` header.
