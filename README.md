# BIONIC-READER

A FastAPI application for bionic reading text processing.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Local Setup

1. Clone the repository

bash
git clone <repository-url>
cd BIONIC-READER
)
bash
On Windows
python -m venv venv

.\venv\Scripts\activate
On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
make install
:
Run the application with auto-relo

### Production Mode
Run the application without auto-reload:

he server will start at `http://127.0.0.1:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://127.0.0.1:8000/docs`
- Alternative API documentation (ReDoc): `http://127.0.0.1:8000/redoc`

## Project Structure

BIONIC-READER/
├── main.py # FastAPI application entry point
├── src/ # Application source code
│ ├── parsers/ # Text parsing modules
│ └── processing/ # Text processing modules
├── requirements.txt # Project dependencies
└── Makefile # Command shortcuts


## Available Make Commands

- `make install`: Install project dependencies
- `make dev`: Run development server with auto-reload
- `make run`: Run production server
- `make test`: Run tests (when implemented)

## License

[Your chosen license]