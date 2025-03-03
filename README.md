# Web Application with FastAPI, MySQL, and SQLAlchemy

## Overview

This web application is built using the **FastAPI** framework and follows the **Model-View-Controller (MVC)** design pattern, ensuring separation of concerns between routing, business logic, and database calls. The application interfaces with a **MySQL database** using **SQLAlchemy** for ORM functionality, with **Pydantic** models providing extensive type validation for the data.

## Application Features

The web application exposes several RESTful endpoints to handle user authentication and post management. It also implements robust validation and dependency injection for managing user authentication and data integrity.

### Core Features:

1. **Signup Endpoint**:

   - Accepts `email` and `password`.
   - Returns a token (JWT or randomly generated string) on successful signup.

2. **Login Endpoint**:

   - Accepts `email` and `password`.
   - Returns a token upon successful login or an error response if login fails.

3. **AddPost Endpoint**:

   - Accepts `text` and `token` for authentication.
   - Validates payload size (limit to 1 MB) and saves the post in memory.
   - Returns the `postID` upon successful post creation.
   - Returns an error if the token is invalid or missing.
   - Implements dependency injection for token-based authentication.

4. **GetPosts Endpoint**:

   - Requires a token for authentication.
   - Returns all posts for the authenticated user.
   - Implements response caching for up to 5 minutes to optimize performance.
   - Returns an error if the token is invalid or missing.
   - Implements dependency injection for token-based authentication.

5. **DeletePost Endpoint**:
   - Accepts `postID` and `token` for authentication.
   - Deletes the corresponding post from memory.
   - Returns an error if the token is invalid or missing.
   - Implements dependency injection for token-based authentication.

### Additional Requirements:

- Token-based authentication for `AddPost` and `GetPosts` endpoints (obtained from the `Login` endpoint).
- Payload size validation (limit to 1 MB) for the `AddPost` endpoint.
- In-memory caching for `GetPosts` for up to 5 minutes.
- Extensive **SQLAlchemy** and **Pydantic** model validation for accuracy and integrity of data.
- Optimized functions with no redundant database calls or logic.
- Comprehensive documentation for all functions.

## Technology Stack

- **Backend**: Python, FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Authentication**: JWT or Randomly Generated Token
- **Caching**: In-memory caching for up to 5 minutes for `GetPosts` endpoint.

## Project Structure

The project follows the MVC design pattern with three distinct levels:

1. **Model Layer**: SQLAlchemy models for interacting with the database.
2. **View Layer**: FastAPI routes to handle HTTP requests and responses.
3. **Controller Layer**: Business logic and validation, using dependency injection and service layers.

### Example Directory Structure:
