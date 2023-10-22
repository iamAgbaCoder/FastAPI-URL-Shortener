
# FastAPI URL Shortener

FastAPI URL Shortener is a simple URL shortening service built using the FastAPI web framework in Python. It allows you to create shortened versions of long URLs, making them more convenient for sharing.

## Key Features

- Shorten long URLs for easy sharing.
- Redirect to the original URL with the short URL.
- Built with FastAPI for high performance and minimal code.
- Basic security measures implemented with CORS (Cross-Origin Resource Sharing).
- Error handling for cases where short URLs are not found or when URLs are already shortened.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Requests (for the client program)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/iamAgbaCoder/fastapi-url-shortener.git
   cd fastapi-url-shortener
   ```

2. Install the required dependencies:

   ```bash
   pip install fastapi uvicorn requests
   ```

### Usage

1. Start the FastAPI application:

   ```bash
   uvicorn url_shortener_fastapi:app --host 0.0.0.0 --port 8000
   ```

2. Open the client program, update the `BASE_URL` to point to your FastAPI application, and run it to shorten and redirect URLs.

   ```bash
   python client.py
   ```

3. Access the URL shortener at [http://localhost:8000](http://localhost:8000).

### API Endpoints

- `POST /shorten/`: Shorten a long URL. Send a JSON payload with a `long_url` field.
- `GET /{short_url}`: Redirect to the original URL by providing the short URL as a path parameter.

### Security Measures

- CORS (Cross-Origin Resource Sharing) is implemented in the FastAPI application to allow requests from any origin. In a production environment, you should restrict this to trusted domains for added security.

- Basic error handling is implemented to handle cases where short URLs are not found or when a URL is already shortened.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Requests: [https://docs.python-requests.org/en/master/](https://docs.python-requests.org/en/master/)
