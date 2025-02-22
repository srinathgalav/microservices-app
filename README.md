# Microservices App

## About
This is a simple microservices application that uses Docker. It has three main parts:
1. **Web Service:** A Flask app that handles HTTP requests.
2. **Worker Service:** A background service for processing tasks.
3. **Database Service:** A PostgreSQL database for storing data.

## Technologies
- Python (Flask)
- PostgreSQL
- Docker
- Docker Compose

## Getting Started

### Prerequisites
- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).

### Steps to Run the App
1. Clone the repository:
   ```bash
   git clone https://github.com/srinathgalav/microservices-app.git
   cd microservices-app
2. Build and start the services:
   docker-compose up --build
3. Open your browser and go to http://localhost:8080 to see the web service.
