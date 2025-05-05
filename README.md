# Solidity Contract Generator API

This API provides an endpoint to generate Solidity smart contracts by sending text prompts to an external cloud server. It uses FastAPI for the endpoint implementation and handles communication with the cloud-based model server.

## Features

- REST API endpoint for generating Solidity smart contracts
- Configurable parameters for contract generation
- Error handling and request validation
- Environment-based configuration
- Automatic API documentation

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-directory>
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory:
```env
CLOUD_SERVER_URL=https://your-cloud-server-url/endpoint
```

## Usage

1. Start the server:
```bash
python InferenceEndPoint.py
```

The server will start on `http://localhost:8000`

2. Access the API documentation:
- Open your browser and navigate to `http://localhost:8000/docs`
- This provides an interactive Swagger UI to test the API endpoints

3. Make API requests:

Using curl:
```bash
curl -X POST "http://localhost:8000/generate-contract" \
     -H "Content-Type: application/json" \
     -d '{
           "prompt": "Create a simple ERC20 token contract",
           "max_tokens": 1000,
           "temperature": 0.7
         }'
```

Using Python requests:
```python
import requests

response = requests.post(
    "http://localhost:8000/generate-contract",
    json={
        "prompt": "Create a simple ERC20 token contract",
        "max_tokens": 1000,
        "temperature": 0.7
    }
)
print(response.json())
```

## API Endpoints

### POST /generate-contract

Generates a Solidity smart contract based on the provided prompt.

**Request Body:**
```json
{
    "prompt": "string",
    "max_tokens": integer,  // optional, default: 1000
    "temperature": float    // optional, default: 0.7
}
```

**Response:**
```json
{
    "generated_contract": "string",
    "status": "string"
}
```

## Error Handling

The API includes comprehensive error handling for:
- Connection issues with the cloud server
- Invalid responses
- General server errors

Error responses will include appropriate HTTP status codes and error messages.

## Environment Variables

- `CLOUD_SERVER_URL`: The URL of the cloud server where the model is deployed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your chosen license]

## Support

For support, please [contact information or create an issue in the repository]
