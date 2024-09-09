# Build JS artefacts
FROM node:latest AS builder

WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install

COPY tailwind.config.js tailwind.config.js
COPY webpack.config.js webpack.config.js

COPY templates templates
COPY js js

RUN npx tailwindcss build -o static/dist/tailwind.css
RUN npx webpack --mode production

# Python web server
FROM python:3.12

WORKDIR /app

COPY --from=builder /app/static static

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY templates templates

CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port $PORT"]
