# US States API

A simple Flask-based REST API that provides information about US states.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
python us_states_api.py
```

The API will be available at `http://localhost:5000`

## Endpoints

### Get All States
- **URL:** `/api/states`
- **Method:** GET
- **Response:**
```json
{
  "success": true,
  "count": 50,
  "data": [
    {"code": "AL", "name": "Alabama"},
    {"code": "AK", "name": "Alaska"},
    ...
  ]
}
```

### Get State by Code
- **URL:** `/api/states/<state_code>`
- **Method:** GET
- **Example:** `/api/states/CA`
- **Response:**
```json
{
  "success": true,
  "data": {"code": "CA", "name": "California"}
}
```

### Get State by Name
- **URL:** `/api/states/name/<state_name>`
- **Method:** GET
- **Example:** `/api/states/name/Texas`
- **Response:**
```json
{
  "success": true,
  "data": {"code": "TX", "name": "Texas"}
}
```

### Search States
- **URL:** `/api/states/search?q=<query>`
- **Method:** GET
- **Example:** `/api/states/search?q=new`
- **Response:**
```json
{
  "success": true,
  "count": 4,
  "data": [
    {"code": "NM", "name": "New Mexico"},
    {"code": "NH", "name": "New Hampshire"},
    {"code": "NJ", "name": "New Jersey"},
    {"code": "NY", "name": "New York"}
  ]
}
```

### Health Check
- **URL:** `/api/health`
- **Method:** GET
- **Response:**
```json
{
  "status": "healthy",
  "service": "US States API"
}
```

## Error Responses

When a state is not found:
```json
{
  "success": false,
  "error": "State with code 'XX' not found"
}
```

Status Code: `404`
