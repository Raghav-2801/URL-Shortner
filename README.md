# URL Shortener API

A simple and efficient URL shortener service built with Flask and SQLite.

## Features

- Shorten long URLs to short, memorable links
- Generate random alphanumeric short IDs
- Collision detection to ensure unique short URLs
- Persistent storage using SQLite database
- RESTful API design
- Proper error handling and validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Raghav-2801/URL-Shortner.git
cd URL-Shortner
```

2. Install dependencies:
```bash
pip install flask
```

## Usage

1. Start the server:
```bash
python3 server.py
```

2. The server will run on `http://127.0.0.1:5000`

## API Endpoints

### Shorten a URL
**POST** `/shorten`

Request body:
```json
{
  "url": "https://example.com/very/long/url"
}
```

Response:
```json
{
  "short_url": "http://127.0.0.1:5000/s/abc123x",
  "short_id": "abc123x"
}
```

### Redirect to Original URL
**GET** `/s/<short_id>`

Redirects to the original long URL.

## Technical Details

- **Framework**: Flask
- **Database**: SQLite
- **Short ID Length**: 7 characters
- **Character Set**: a-z, 0-9 (36 possible characters per position)
- **Possible Combinations**: ~78 billion unique URLs

## License

MIT
