# Group Anagrams API

A REST API implementation of the Group Anagrams algorithm, built with Flask and served with Gunicorn. Containerized with Docker and deployed to Railway, with a GitHub Actions CI/CD pipeline for automated testing and deployment.

## Tech Stack

- **Python 3.12**
- **Flask** — web framework
- **Gunicorn** — production WSGI server
- **Docker** — containerization
- **Railway** — cloud deployment
- **GitHub Actions** — CI/CD pipeline
- **pytest** — unit testing

## Endpoints

### `POST /group-anagrams`

Groups a list of strings into anagram groups.

**Request body:**
```json
{
  "words": ["eat", "tea", "tan", "ate", "nat", "bat"]
}
```

**Response:**
```json
{
  "metadata": {
    "length": 3,
    "input_size": 6
  },
  "groups": [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
  ]
}
```

**Error responses:**
| Status | Reason |
|--------|--------|
| `400` | Missing or invalid `words` field |
| `413` | Request body exceeds 1MB |
| `500` | Unexpected server error |

## How to Run

### With Docker
```bash
docker build -t group-anagrams-api .
docker run -p 8080:8080 group-anagrams-api
```

### Without Docker
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

## Examples
```bash
# Valid request
curl -X POST https://flask-group-anagrams-api-production.up.railway.app/group-anagrams \
  -H "Content-Type: application/json" \
  -d '{"words": ["eat", "tea", "tan", "ate", "nat", "bat"]}'

# Invalid request
curl -X POST https://flask-group-anagrams-api-production.up.railway.app/group-anagrams \
  -H "Content-Type: application/json" \
  -d '{"words": "not a list"}'
```