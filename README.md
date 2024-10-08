Shawty - Backend

Shawty is a URL shortening service similar to TinyURL. This repository contains the backend code that powers the URL shortening and redirection functionality.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Shorten long URLs into short, easy-to-share links.
- Redirect shortened URLs to their original destination.
- RESTful API for interacting with the service programmatically.
- Caching mechanism for improved performance.

## Tech Stack

- **Programming Language**: [Python 3](https://www.python.org/)
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [MongoDB](https://www.postgresql.org/)
- **Cache**: [Redis](https://redis.io/)
- **ORM**: [Beanie](https://www.sqlalchemy.org/) 
- **Environment Variables**: [python-dotenv](https://pypi.org/project/python-dotenv/)

## Project Structure

```bash
├── app
│   ├── api                # API routes
│   ├── core               # Core settings and configuration
│   ├── db                 # Database models and migrations
│   ├── services           # Business logic and interactions
│   ├── utils              # Utility functions
│   ├── main.py            # Entry point of the application
├── alembic                # Alembic migration scripts
├── tests                  # Test cases
├── .env.example           # Example environment variables file
├── .gitignore             # Files to be ignored by Git
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Getting Started

### Prerequisites

- [Python 3.11+](https://www.python.org/) installed on your machine.
- A running instance of MongoDB.
- A running instance of Redis.

### Installation


1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/shawty-backend.git
   cd shawty-backend
   ```


2. **Set up environment variables:**

   - Copy `.env.example` to `.env` and update the variables accordingly:

   ```bash
   cp .env.example .env
   ```
   - Add mongodb connection strings.
3. **Install it with Docker!**

   ```bash
   docker-compose up --build
   ```


3b. **Or install it regularly, Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  
   ```

3. **Install dependencies:**

   ```bash
    pip install poetry
    poetry install
   ```

   
6. **Start the server:**

   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

   The server will be running at `http://127.0.0.1:8000`.

## Environment Variables

The application requires the following environment variables:

- The connection string for the MongoDB database.
- The connection string for the Redis instance.

Refer to `.env.example` for a full list of required variables.

## API Endpoints

- **POST /shorten**: Create a new short URL.
- **GET /{short_url}**: Retrieve information of the original URL.

Detailed API documentation is available via Swagger at `http://127.0.0.1:8000/docs` after running the server.

## Testing

To run the tests:
1. **Run tests:**

   ```bash
   python3 -m unittest discover -s app -p '*_tests.py'
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```