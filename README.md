# Fastapi-HTMX-Quickstart

A quick-start template using Python's FastAPI and HTMX for interactive yet robust web applications.

## Features

* Modern web development utilities such as TailwindCSS, AlpineJS, and Webpack
* FastAPI backend with HTMX for server-rendered HTML
* Database integration with SQLAlchemy and Alembic for migrations
* Convenient local development & testing with `docker-compose`
* Pre-configured `pre-commit` hooks and GitHub Actions to enforce code quality

## Installation

Install `pip` dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

Install `npm` dependencies:

```bash
npm install
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

Run interactive cluster, for real-time development:

```bash
docker compose -f docker-compose.local.yml up --build
```
