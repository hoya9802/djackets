# Project Setup Instructions

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Docker
- You have installed Node.js
- You have a working Git installation

## Cloning the Repository

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/hoya9802/djackets.git
    ```

## Backend Setup with Docker

1. Ensure you are in the root directory of the project:
    ```bash
    cd djackets
    ```
2. Build the Docker image for the backend:
    ```bash
    docker build -t djackets-backend .
    ```
3. Run the Docker containers using `docker-compose.yml`:
    ```bash
    docker compose up
    ```

## Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd ../djackets_vue
    ```
2. Install the required Node.js packages:
    ```bash
    npm install
    ```
3. Start the Vue.js development server:
    ```bash
    npm run serve
    ```

## Running the Project

- Open your browser and navigate to `http://localhost:8000` to access the backend.
- Open your browser and navigate to `http://localhost:8080` to access the frontend.

## Additional Notes

- Ensure both the backend and frontend servers are running simultaneously for the project to function correctly.
