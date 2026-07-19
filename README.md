# product-service

Python microservice for the Chetan DevOps learning path.

## API

| Method | Path | Response |
|--------|------|----------|
| GET | `/products` | `application/json` — hardcoded list of products |
| GET | `/health` | `application/json` — health check |

## Run locally

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000/products

## Tests

```bash
pytest -q
```

## CI

`Jenkinsfile` runs on Jenkins (AWS EC2): prints who/what/when for the commit, runs unit tests, runs a basic dependency security scan.
