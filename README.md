# Fastapi-HTMX-Quickstart

A quick-start template using Python's FastAPI and HTMX for fast and robust web applications.

## Features

* Modern web development utilities such as TailwindCSS, AlpineJS, and Webpack
* Convenient local development & testing with `docker-compose`
* Pre-configured `pre-commit` hooks to enforce code quality

## Installation

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

Install pre-commit hooks:

```bash
pre-commit install
```

## Local Development

Run cluster with `docker-compose`:

```bash
docker compose up --build
```
